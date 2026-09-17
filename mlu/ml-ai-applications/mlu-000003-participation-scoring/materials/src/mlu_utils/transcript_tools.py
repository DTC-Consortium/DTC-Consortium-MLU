"""Zoom-transcript participation scoring for the Participation Scoring Lab.

Keeps the transcript parsing, per-speaker aggregation, roster reconciliation,
the scoring prompt + model, and report rendering OUT of the notebook so the
notebook stays use-led rather than a wall of code (same convention as
mlu_utils/embeddings.py and mlu_utils/study_tools.py).

The notebook does:

    from mlu_utils.transcript_tools import (
        parse_transcript, aggregate_by_speaker, reconcile_roster,
        ParticipationScorer, build_report,
    )

    utterances = parse_transcript("data/sample_class_transcript.vtt")
    stats      = aggregate_by_speaker(utterances)
    matched, silent, off_roster = reconcile_roster(stats, roster_names)

    scorer = ParticipationScorer(retriever, bedrock_runtime)
    scored = scorer.score_all(matched, silent)
    report_md, csv_rows = build_report(scored)

WHAT THIS IS: a DRAFT participation score the instructor reviews. The
"on topic" judgment is grounded ONLY in the day's lesson material via the
retriever — the same RAG stack the curriculum lab uses. The score never
reaches a gradebook without a human looking at it. See Parts 0 and 7 of the
notebook.
"""
import csv
import json
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from langchain_aws import ChatBedrockConverse
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate


# --------------------------------------------------------------------------- #
# Transcript parsing  (Zoom .vtt and plain .txt — Python stdlib only)         #
# --------------------------------------------------------------------------- #

@dataclass
class Utterance:
    speaker: str
    start: float          # seconds from start of recording
    end: float
    text: str

    @property
    def duration(self) -> float:
        return max(0.0, self.end - self.start)


_TS = re.compile(
    r"(?:(\d+):)?(\d{1,2}):(\d{2})(?:[.,](\d{1,3}))?"  # [H:]MM:SS[.mmm]
)
_VOICE_TAG = re.compile(r"<v\s+([^>]+)>(.*?)(?:</v>)?$", re.IGNORECASE | re.DOTALL)
_SPEAKER_PREFIX = re.compile(r"^([^:]{1,60}?):\s+(.*)$", re.DOTALL)


def _to_seconds(ts: str) -> float:
    m = _TS.search(ts)
    if not m:
        return 0.0
    hours = int(m.group(1) or 0)
    minutes = int(m.group(2))
    seconds = int(m.group(3))
    millis = int((m.group(4) or "0").ljust(3, "0"))
    return hours * 3600 + minutes * 60 + seconds + millis / 1000.0


def _extract_speaker(text: str) -> Tuple[Optional[str], str]:
    """Pull a speaker name off a cue's text. Handles both the WebVTT voice tag
    `<v Name>text</v>` and Zoom's plain `Name: text` prefix. Returns
    (speaker_or_None, remaining_text)."""
    text = text.strip()
    vt = _VOICE_TAG.match(text)
    if vt:
        return vt.group(1).strip(), vt.group(2).strip()
    sp = _SPEAKER_PREFIX.match(text)
    if sp:
        name = sp.group(1).strip()
        # A real Zoom speaker label is a short name, not a sentence. Reject a
        # prefix that looks like prose mis-split on a colon (contains sentence
        # punctuation, or is implausibly long). A bare single word can't be told
        # apart from a first name, so we accept it — fine for real transcripts,
        # which are always speaker-prefixed by Zoom.
        if not re.search(r"[.?!]", name) and 1 <= len(name.split()) <= 5:
            return name, sp.group(2).strip()
    return None, text


def parse_transcript(path: str) -> List[Utterance]:
    """Parse a Zoom transcript into a list of Utterances.

    Supports Zoom's WebVTT export (`.vtt`) and a plain-text fallback. A cue with
    no speaker label is attributed to the previous speaker (a continued turn),
    which is how Zoom splits long monologues across cues."""
    with open(path, "r", encoding="utf-8-sig") as f:
        raw = f.read()

    is_vtt = raw.lstrip().upper().startswith("WEBVTT") or path.lower().endswith(".vtt")
    utterances: List[Utterance] = []
    last_speaker: Optional[str] = None

    if is_vtt:
        blocks = re.split(r"\n\s*\n", raw.strip())
        for block in blocks:
            lines = [ln for ln in block.splitlines() if ln.strip()]
            if not lines or lines[0].strip().upper() == "WEBVTT":
                continue
            ts_idx = next((i for i, ln in enumerate(lines) if "-->" in ln), None)
            if ts_idx is None:
                continue
            start_s, _, end_s = lines[ts_idx].partition("-->")
            start, end = _to_seconds(start_s), _to_seconds(end_s)
            text = " ".join(lines[ts_idx + 1:]).strip()
            if not text:
                continue
            speaker, body = _extract_speaker(text)
            if speaker is None:
                speaker = last_speaker or "Unknown speaker"
            last_speaker = speaker
            utterances.append(Utterance(speaker=speaker, start=start, end=end, text=body))
    else:
        # Plain text: one utterance per "Name: text" line; bare timestamp/number
        # lines are skipped. Continuation lines attach to the previous speaker.
        for line in raw.splitlines():
            line = line.strip()
            if not line or re.fullmatch(r"[\d:.,\s\-]+", line):
                continue
            speaker, body = _extract_speaker(line)
            if speaker is None:
                if last_speaker and utterances:
                    utterances[-1] = Utterance(
                        last_speaker, utterances[-1].start, utterances[-1].end,
                        (utterances[-1].text + " " + body).strip(),
                    )
                continue
            last_speaker = speaker
            utterances.append(Utterance(speaker=speaker, start=0.0, end=0.0, text=body))

    return utterances


# --------------------------------------------------------------------------- #
# Aggregation by speaker                                                      #
# --------------------------------------------------------------------------- #

@dataclass
class SpeakerStats:
    name: str
    turns: int = 0           # contiguous runs of speech, not raw cue count
    words: int = 0
    talk_seconds: float = 0.0
    text: str = ""           # all of this speaker's words, concatenated


def aggregate_by_speaker(utterances: List[Utterance]) -> Dict[str, SpeakerStats]:
    """Collapse utterances into per-speaker stats. A 'turn' is a maximal
    contiguous run by the same speaker, so a monologue Zoom split across three
    cues counts as one turn, not three."""
    stats: Dict[str, SpeakerStats] = {}
    prev_speaker: Optional[str] = None
    for u in utterances:
        s = stats.setdefault(u.speaker, SpeakerStats(name=u.speaker))
        if u.speaker != prev_speaker:
            s.turns += 1
        s.words += len(u.text.split())
        s.talk_seconds += u.duration
        s.text = (s.text + " " + u.text).strip()
        prev_speaker = u.speaker
    return stats


# --------------------------------------------------------------------------- #
# Roster reconciliation                                                       #
# --------------------------------------------------------------------------- #

def load_roster(path: str) -> List[str]:
    """Read a roster CSV and return the list of student names. Looks for a
    `student_name`/`name` column; falls back to the first column."""
    names: List[str] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        cols = reader.fieldnames or []
        key = next((c for c in cols if c and c.strip().lower() in ("student_name", "name", "student")), None)
        if key is None and cols:
            key = cols[0]
        for row in reader:
            val = (row.get(key) or "").strip() if key else ""
            if val:
                names.append(val)
    return names


def _norm(name: str) -> str:
    return re.sub(r"\s+", " ", name.strip().lower())


def _tokens(name: str) -> List[str]:
    return [t for t in re.split(r"\s+", _norm(name)) if t]


def _names_match(a: str, b: str) -> bool:
    """Lenient match: exact normalized equality, or same last name AND first
    names agree on at least an initial. Handles 'Aisha Rahman' vs 'Rahman,
    Aisha' and 'J. Chen' vs 'James Chen' without matching unrelated people."""
    if _norm(a) == _norm(b):
        return True
    ta, tb = _tokens(a.replace(",", " ")), _tokens(b.replace(",", " "))
    if len(ta) >= 2 and len(tb) >= 2:
        # last token = surname; require surname match + first-initial agreement
        if ta[-1] == tb[-1] and ta[0][:1] == tb[0][:1]:
            return True
        # handle "Rahman Aisha" reversed order
        if ta[0] == tb[-1] and ta[-1][:1] == tb[0][:1]:
            return True
    return False


def reconcile_roster(
    stats: Dict[str, SpeakerStats],
    roster_names: Optional[List[str]],
) -> Tuple[List[Tuple[str, SpeakerStats]], List[str], List[SpeakerStats]]:
    """Split speakers against a roster.

    Returns (matched, silent, off_roster):
      - matched      : [(roster_name, SpeakerStats)] for students who spoke
      - silent       : [roster_name] enrolled but never spoke  -> scored tier 0
      - off_roster   : [SpeakerStats] speakers not on the roster (instructor,
                       TA, guest) -> flagged, NOT scored

    With no roster, every speaker is 'matched' under their transcript name and
    the other two lists are empty (a fully silent student is then invisible)."""
    speakers = list(stats.values())
    if not roster_names:
        return [(s.name, s) for s in speakers], [], []

    matched: List[Tuple[str, SpeakerStats]] = []
    silent: List[str] = []
    used_speakers = set()

    for roster_name in roster_names:
        hit = next(
            (s for s in speakers if s.name not in used_speakers and _names_match(roster_name, s.name)),
            None,
        )
        if hit is not None:
            matched.append((roster_name, hit))
            used_speakers.add(hit.name)
        else:
            silent.append(roster_name)

    off_roster = [s for s in speakers if s.name not in used_speakers]
    return matched, silent, off_roster


# --------------------------------------------------------------------------- #
# Scoring                                                                     #
# --------------------------------------------------------------------------- #

RUBRIC_TEMPLATE = """You are helping a faculty member draft a class-participation score for ONE
student, for ONE day's class, from a Zoom transcript. Your output is a DRAFT
the instructor will review and adjust — it is NOT a final grade.

You judge "on topic" ONLY against the day's lesson material below. Do not use
outside knowledge of the subject to decide what counts as on-topic.

DAY'S LESSON MATERIAL (this defines what "on topic" means today):
{lesson_context}

STUDENT: {student_name}
Speaking volume for the day: {num_turns} separate turns, about {num_words} words.

EVERYTHING THIS STUDENT SAID (verbatim, in order):
{student_text}

Score the student on this 0–4 participation rubric for the day:

- 4 — Substantive AND on-topic leadership: multiple on-topic contributions that
      advance the discussion (asks probing questions, reasons through the
      material, builds on or challenges peers, connects ideas in the lesson).
- 3 — Solid on-topic contribution: one or more clear, correct, on-topic
      contributions, but not driving the discussion.
- 2 — Some on-topic participation: at least one genuine on-topic contribution,
      possibly brief or surface-level.
- 1 — Minimal or off-topic: spoke, but contributions are mostly filler
      ("yeah", "agreed"), logistics (due dates, exams), or off-topic/social
      (weekend, jokes, unrelated chat). High volume of off-topic talk still
      scores low.
- 0 — Did not participate. (You will not be asked to score a 0; silence is
      handled before you.)

CRITICAL JUDGING RULES:
- Talking a lot is NOT the same as participating. A student who talks a lot but
  off-topic scores LOWER than a student who talks a lot on-topic. Do not reward
  volume of off-topic or logistical talk.
- Brevity is NOT penalized. One sharp, correct, on-topic point can be a 3. A
  single excellent probing question can be a 4 if it clearly advances the topic.
- Base "on topic" strictly on overlap with the lesson material above.
- If the transcript is ambiguous or thin, say so and set confidence to "low" —
  do not inflate.

Respond with ONLY a JSON object, no prose before or after, in this exact shape:
{{
  "tier": <integer 0-4>,
  "on_topic_fraction": <number 0.0-1.0, share of the student's talk that is on-topic>,
  "substance_note": "<one short phrase: e.g. 'probing questions on amortized cost' or 'mostly logistics/social'>",
  "evidence_quotes": ["<short verbatim quote from the student>", "<another>"],
  "rationale": "<1-2 sentences explaining the tier, referencing on-topic vs off-topic>",
  "confidence": "<high|medium|low>"
}}"""


@dataclass
class StudentScore:
    name: str
    status: str                       # "scored" | "silent" | "parse_error"
    tier: Optional[int] = None
    on_topic_fraction: Optional[float] = None
    substance_note: str = ""
    evidence_quotes: List[str] = field(default_factory=list)
    rationale: str = ""
    confidence: str = ""
    turns: int = 0
    words: int = 0
    talk_seconds: float = 0.0


def _parse_json_object(raw: str) -> Optional[dict]:
    """Tolerant JSON extraction — strip code fences and grab the outermost
    object. Same defensive spirit as study_tools' delimiter handling: never
    trust the model to emit clean output, but degrade gracefully."""
    cleaned = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.MULTILINE).strip()
    start, end = cleaned.find("{"), cleaned.rfind("}")
    if start == -1 or end == -1 or end < start:
        return None
    try:
        return json.loads(cleaned[start:end + 1])
    except json.JSONDecodeError:
        return None


class ParticipationScorer:
    """Scores each speaking student against the day's lesson material. One
    grounded LLM call per student; silence is decided in code, never sent to
    the model."""

    MAX_STUDENT_CHARS = 4000          # cap a very talkative student's text
    RETRIEVAL_QUERY_CHARS = 600       # cap the retrieval query length

    def __init__(self, retriever, bedrock_runtime, model_id: str = "amazon.nova-lite-v1:0"):
        self.retriever = retriever
        self._model = ChatBedrockConverse(model=model_id, temperature=0.2, max_tokens=1200)
        self._chain = PromptTemplate.from_template(RUBRIC_TEMPLATE) | self._model | StrOutputParser()

    def _lesson_context(self, query: str) -> str:
        docs = self.retriever.invoke(query[:self.RETRIEVAL_QUERY_CHARS])
        return "\n\n".join(d.page_content for d in docs)

    def score_student(self, display_name: str, stats: SpeakerStats) -> StudentScore:
        """Score one student who spoke. Retrieves lesson context relevant to
        THIS student's words so the on-topic judgment is grounded in the part of
        the lesson they actually engaged (or failed to engage)."""
        context = self._lesson_context(stats.text or display_name)
        raw = self._chain.invoke({
            "lesson_context": context,
            "student_name": display_name,
            "num_turns": stats.turns,
            "num_words": stats.words,
            "student_text": stats.text[:self.MAX_STUDENT_CHARS],
        })
        data = _parse_json_object(raw)
        if data is None:
            return StudentScore(
                name=display_name, status="parse_error",
                rationale="Could not parse the model output — re-run the scoring cell.",
                confidence="low", turns=stats.turns, words=stats.words,
                talk_seconds=stats.talk_seconds,
            )
        tier = data.get("tier")
        try:
            tier = int(tier)
        except (TypeError, ValueError):
            tier = None
        return StudentScore(
            name=display_name, status="scored", tier=tier,
            on_topic_fraction=data.get("on_topic_fraction"),
            substance_note=str(data.get("substance_note", "")),
            evidence_quotes=list(data.get("evidence_quotes", []) or []),
            rationale=str(data.get("rationale", "")),
            confidence=str(data.get("confidence", "")),
            turns=stats.turns, words=stats.words, talk_seconds=stats.talk_seconds,
        )

    def score_all(
        self,
        matched: List[Tuple[str, SpeakerStats]],
        silent: Optional[List[str]] = None,
    ) -> List[StudentScore]:
        """Score every speaking student, then append silent students at tier 0.
        Sorted highest-tier first, ties broken by words spoken."""
        scores = [self.score_student(name, stats) for name, stats in matched]
        for name in (silent or []):
            scores.append(StudentScore(
                name=name, status="silent", tier=0,
                on_topic_fraction=0.0, substance_note="did not speak",
                rationale="On the roster but never spoke in this class.",
                confidence="high",
            ))
        scores.sort(key=lambda s: (-(s.tier if s.tier is not None else -1), -s.words))
        return scores


# --------------------------------------------------------------------------- #
# Reporting                                                                   #
# --------------------------------------------------------------------------- #

def _fmt_quotes(quotes: List[str], limit: int = 2) -> str:
    shown = [f'"{q.strip()}"' for q in quotes[:limit] if q and q.strip()]
    return "; ".join(shown) if shown else "—"


def build_report(scored: List[StudentScore]) -> Tuple[str, List[dict]]:
    """Render (markdown_table, csv_rows) from scored students. The markdown is
    for reading in the notebook; the csv_rows feed the take-home export."""
    header = (
        "| Student | Tier | On-topic | Substance | Evidence | Confidence |\n"
        "|---|:---:|:---:|---|---|:---:|"
    )
    rows_md = []
    csv_rows = []
    for s in scored:
        tier_disp = "—" if s.tier is None else str(s.tier)
        if s.status == "silent":
            tier_disp = "0 · silent"
        elif s.status == "parse_error":
            tier_disp = "⚠️ re-run"
        otf = "" if s.on_topic_fraction is None else f"{round(100 * s.on_topic_fraction)}%"
        rows_md.append(
            f"| {s.name} | {tier_disp} | {otf or '—'} | {s.substance_note or '—'} | "
            f"{_fmt_quotes(s.evidence_quotes)} | {s.confidence or '—'} |"
        )
        csv_rows.append({
            "student_name": s.name,
            "tier": "" if s.tier is None else s.tier,
            "status": s.status,
            "on_topic_fraction": "" if s.on_topic_fraction is None else round(s.on_topic_fraction, 2),
            "turns": s.turns,
            "words": s.words,
            "talk_seconds": round(s.talk_seconds, 1),
            "confidence": s.confidence,
            "substance_note": s.substance_note,
            "rationale": s.rationale,
        })
    return "\n".join([header, *rows_md]), csv_rows
