# Instructor Walkthrough — Participation Scoring Lab

This is the faculty-tool sibling of the curriculum lab. Unlike the seminar's timed afternoon lab,
this one is meant to be **used repeatedly by a single faculty member** on their own classes. There
is no run-of-show clock; the notes below are for whoever demos, supports, or maintains it.

## The one-sentence pitch

"Drop in a Zoom transcript and the day's lesson, and it drafts a participation score per student —
grounded in what you taught, with the evidence shown — for you to review."

## How it works (the architecture in 30 seconds)

1. **Part 2** embeds the day's lesson PDF into FAISS — this *is* the definition of "on topic."
2. **Part 3** parses the Zoom transcript (`mlu_utils/transcript_tools.parse_transcript`) into
   per-speaker stats, and reconciles speakers against the roster (silent vs. off-roster).
3. **Part 4** scores each speaking student with one grounded Nova Lite call: it retrieves the slice
   of the lesson the student's words relate to, then applies the 0–4 rubric and returns JSON
   (tier, on-topic fraction, evidence quotes, rationale, confidence). Silent students are set to 0
   in code — never sent to the model.
4. **Part 5** is the human-in-the-loop override + equity check. **Part 6** exports `.md` + `.csv`.

All scoring/parsing logic lives in `mlu_utils/transcript_tools.py`, keeping the notebook readable —
same convention as the curriculum lab's `study_tools.py`.

## The sample is engineered to show every tier

`data/sample_class_transcript.vtt` is a CS Data Structures discussion of Ch. 1 of *Open Data
Structures* (the same `persona2` PDF, used here as the lesson material). Expected outcomes when you
run Part 4 on it:

| Student | What they do in the transcript | Expected tier |
|---|---|:---:|
| **Aisha Rahman** | Drives the discussion — probes amortized analysis, the doubling argument, the geometric series, the shrink-at-quarter-full edge case | **4** |
| **Marcus Bell** | Correctly answers FIFO/LIFO, `get(i)` complexity for array vs. linked list, USet/SSet | **3** |
| **Tyler Okonkwo** | Two short but substantive on-topic points (interface = what not how; fixed-increment growth breaks amortization) — **demonstrates brevity is not penalized** | **2–3** |
| **Sofia Reyes** | Talks a fair amount but it's the due date, the basketball game, coffee, a Netflix show, "is this on the exam?" — **demonstrates volume of off-topic ≠ score** | **1** |
| **Daniel Kim** | "Makes sense", "yeah true", "agreed" — filler only | **1** |
| **Priya Nair** | On the roster, never speaks | **0 (silent)** |
| **Jordan Alvarez** | On the roster, never speaks (effectively absent) | **0 (silent)** |
| **James Chen** | The instructor — on the transcript, *not* on the roster | flagged "not scored" |

The two outcomes to point at when demoing:
- **Sofia (chatty, off-topic) scores below Aisha (chatty, on-topic).** This is the whole thesis of
  the lab — relevance, not volume.
- **Priya and Jordan appear at 0** *because* a roster was supplied. Drop `ROSTER_PATH = None` and
  they vanish — a good way to show why the roster matters.

Tier 2 vs. 3 for Tyler may vary slightly run to run (Nova Lite, temperature 0.2). That's expected
and is exactly why Part 5 exists.

## Common support issues

- **A real student shows as "silent."** Zoom logged their speech under a different display name
  (nickname, "iPhone", a second account). Fix the name in the transcript or roster so they match.
  The matcher (`_names_match`) handles "Last, First" and first-initial cases but not unrelated
  display names.
- **Instructor/TA shows up in the scored list.** They're matching a roster row — make sure they're
  not on the roster CSV. Then they land in the "not on the roster — not scored" line.
- **`⚠️ re-run` in a tier cell.** The model returned unparseable JSON for that student. Re-run
  Part 4; the parser degrades gracefully rather than crashing the whole batch.

## Maintenance notes

- **No new dependencies.** `requirements.txt` is identical to the curriculum lab; VTT/TXT parsing
  is stdlib-only. Don't add `webvtt-py` — it's unnecessary and adds install-drift risk.
- **Model IDs** are pinned in `transcript_tools.py` (`ParticipationScorer.__init__`) and the
  notebook's Part 1, matching the curriculum lab (`amazon.nova-lite-v1:0`,
  `amazon.nova-2-multimodal-embeddings-v1:0`).
- **Sample students are invented.** Safe to ship publicly. Keep it that way — never commit a real
  class transcript or roster.

## Pre-demo checklist

- [ ] Bedrock access for both Nova models in `us-east-1`.
- [ ] `pip install -r requirements.txt` completes clean.
- [ ] Parts 1–6 run top to bottom on the bundled sample with no edits.
- [ ] Sofia < Aisha; Priya & Jordan at 0; James Chen flagged not-scored.
- [ ] Part 6 writes a dated `.md` and `.csv` you can open.
