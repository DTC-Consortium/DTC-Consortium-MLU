#!/usr/bin/env python3
"""Build the branded PDFs for The Assignment Lifecycle — two editions, one builder.

Renders the project's Markdown through the DTCC Faculty Handbook's own print stylesheet, then
appends the legal-approved session deck, so each audience receives one file instead of a folder.

    participant  -> dist/assessment-lifecycle-take-home-pack.pdf
                    What an attendee needs to redo the work on their own course.
    facilitator  -> dist/assessment-lifecycle-facilitator-guide.pdf
                    What another instructor needs to deliver the session: the apps they must
                    build first, the talk track, the sample pack, and the deck.

    python3 build_pack.py                          # both
    python3 build_pack.py --edition facilitator    # just one
    python3 build_pack.py --no-deck                # prose only, much faster while iterating
    python3 build_pack.py --keep-html              # keep the intermediate HTML to debug layout

Three things worth knowing before changing it:

**It needs Chrome.** The branding has to match dtcconsortium.org, which means rendering the
handbook's real CSS. Same reason, same renderer, same trade-off documented in
`DTC-Consortium-MLU/scripts/README.md`. Set CHROME if the binary is somewhere unusual.

**The appended deck is never touched.** Its pages are copied in at native size with no overlay,
no scaling and no running furniture. The words on the deck's approved slides may be removed but
never added to — see DECK-APPROVAL.md — so this build treats every deck page as read-only cargo
and verifies it with verify_deck.py first. Furniture is stamped only on the pages this script
generates.

**Unfilled placeholders are surfaced, not hidden.** Any «FILL IN: …» left in the Markdown marks
the PDF as a draft: a banner on the cover, a highlight at each site, and a checklist page listing
every one. Fill them all and the document builds clean, with no draft furniture at all.
"""

import argparse
import html as html_mod
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

import markdown as md_lib
from jinja2 import Template
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as rl_canvas

HERE = Path(__file__).resolve().parent
BRAND = HERE / "brand"

GOLD = "#EBB000"
CHARCOAL = "#181616"
LIGHT_GRAY = "#9C9C9C"
ORANGE = "#C83F04"

CHROME_CANDIDATES = [
    os.environ.get("CHROME", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome-stable",
    "google-chrome",
    "chromium",
]

MD_EXTENSIONS = ["tables", "fenced_code", "attr_list", "sane_lists", "def_list"]

# The talk track cues a facilitator reads while presenting. In Markdown they sit on their own
# lines but fold into one dense paragraph, which is the opposite of what someone scanning from
# a lectern needs. Each gets its own paragraph.
CUE_RE = re.compile(
    r"(?<=\S)\n(\*\*(?:Before|Say|Do|Don.t|Expect|Collect|Fallback|Note|"
    r"What this slide is for|\u2192 Next)\b[^*]*\*\*)",
    re.M,
)

TITLE = "The Assignment Lifecycle"
TAGLINE = "Distributed Teaching Collaboratives Consortium"
BYLINE = "Tariq Hook · Delaware State University"

DECK = HERE / "assessment-lifecycle-deck.pdf"

# Two audiences, one builder. Participants get what they need to redo the work alone;
# facilitators get everything required to deliver the session, in the order they need it.
EDITIONS = {
    "participant": {
        "subtitle": "Take-Home Pack",
        "running": "The Assignment Lifecycle — Take-Home Pack",
        "out": "assessment-lifecycle-take-home-pack.pdf",
        "blurb": ("Four AI tools, one assignment — from building the rubric to letting students "
                  "check their own drafts. Everything you need to do it again on your own course."),
        "deck_note": ("All {n} slides, exactly as presented. The hands-on segments are slides "
                      "13, 15, 21, 24 and 25; the ground rules are on slide 27. Every slide "
                      "carries the QR code for the shared folder \u2014 scan it from any of them."),
        "sections": [
            ("participant-resources/00-START-HERE.md", "Start here"),
            ("participant-resources/hook-handout.md", "The opening exercise"),
        ],
    },
    # What attendees work from. The same source as the Google Doc they follow on screen, so
    # the two never drift — but branded, paginated, and with every prompt in a real callout.
    # No deck appended: this is the thing open beside the laptop, and it stays short enough
    # to stay useful.
    "followalong": {
        "subtitle": "Follow-along guide",
        "running": "The Assignment Lifecycle — Follow along",
        "out": "assessment-lifecycle-follow-along.pdf",
        "deck": False,
        "blurb": ("Everything the session runs on, in the order it runs: the paper to grade, "
                  "the rubric that came with it, the assignment, and the three prompts that "
                  "build the three tools."),
        "deck_note": "",
        "sections": [("prompts/MASTER-FOLLOW-ALONG.md", "Follow along")],
    },
    "facilitator": {
        "subtitle": "Facilitator Guide",
        "running": "The Assignment Lifecycle — Facilitator Guide",
        "out": "assessment-lifecycle-facilitator-guide.pdf",
        "blurb": ("Everything needed to deliver the 90-minute session: what you must build first, "
                  "the talk track slide by slide, the sample pack, and the deck you present from."),
        "deck_note": ("All {n} slides, reproduced in full so you can read the session and the "
                      "deck side by side. Slide 0 is the shared folder; the 28 after it are "
                      "legal-approved \u2014 see Deck approval status."),
        "sections": [
            ("facilitator-guide/00-READ-ME-FIRST.md", "Read me first"),
            ("DECK-APPROVAL.md", "Deck approval status"),
            ("prompts/README.md", "The prompt pack"),
            ("prompts/PROMPT-1-rubric-builder.md", "Prompt 1 — the Rubric Builder"),
            ("prompts/PROMPT-2-ai-proofing.md", "Prompt 2 — the AI-Proofing Assistant"),
            ("prompts/PROMPT-3-triage.md", "Prompt 3 — Pre-Assessment Triage"),
            ("prompts/facilitator/PROMPT-F1-grading-app.md",
             "Prompt F1 — the Grading Assistant, in Quick"),
            ("prompts/facilitator/PROMPT-F2-kiro-grader.md",
             "Prompt F2 — the Grading Assistant, in Kiro"),
            ("prompts/facilitator/RUN-KIRO.md", "Running the Kiro segment — presenter runbook"),
            ("prompts/DRIVE-FOLDER.md", "The shared folder"),
            ("prompts/MASTER-FOLLOW-ALONG.md", "The one document attendees follow"),
            ("facilitator-guide/TALK_TRACK.md", "Talk track"),
            ("activities/sample-pack/README.md", "The sample pack"),
            ("activities/sample-pack/assignment.md", "The assignment"),
            ("activities/sample-pack/rubric-weak.md", "The weak rubric"),
            ("activities/sample-pack/rubric-golden.md", "The reference rubric"),
            ("activities/rubric-format.md", "The rubric format"),
            ("participant-resources/hook-handout.md", "The handout — print one per attendee"),
        ],
    },
}


def sections_for(edition: dict) -> list[dict]:
    return [{"key": f"S{i:03d}", "file": f, "title": t, "outline": t}
            for i, (f, t) in enumerate(edition["sections"], start=1)]

# Section markers are planted in the HTML so each section can be located in the rendered PDF.
# Short and fixed-width on purpose: a long key breaks across text runs and cannot be matched back.
MARK_RE = re.compile("§§(S[0-9]{3})§§")
PLACEHOLDER_RE = re.compile("«\\s*FILL IN:\\s*(.+?)»", re.S)

# ----------------------------------------------------------------- helpers

def chrome_binary() -> str:
    for cand in CHROME_CANDIDATES:
        if not cand:
            continue
        if Path(cand).exists():
            return cand
        found = shutil.which(cand)
        if found:
            return found
    sys.exit("error: could not find Google Chrome.\n"
             "       Install it, or set CHROME to the binary path.")


# The follow-along document delimits each prompt with marker lines rather than a fenced code
# block, because Google Docs' Markdown import drops fences and there would be no box on screen
# to point at. On paper we can do better: the same markers become a real callout.
PROMPT_BLOCK_RE = re.compile(
    r"^\u2501+[^\S\n]*\*\*START OF (?P<label>[^*]+?)\*\*[^\S\n]*\u2501+[^\S\n]*$"
    r"(?P<body>.*?)"
    r"^\u2501+[^\S\n]*\*\*END OF [^*]+?\*\*[^\S\n]*\u2501+[^\S\n]*$",
    re.M | re.S)


def promptboxes(text: str) -> str:
    """Marker-delimited prompt regions become bordered, monospaced callouts.

    The body is emitted inside <pre>, so the prompt prints exactly as it must be pasted —
    line breaks, indentation and quote characters intact. Anything that reflows a prompt
    changes what the app is told to build.
    """
    def box(m):
        label = " ".join(m.group("label").split())
        body = html_mod.escape(m.group("body").strip("\n"))
        return (f'\n<div class="promptbox">\n'
                f'<div class="promptbox-head"><span class="l">{html_mod.escape(label)}</span>'
                f'<span class="r">copy everything inside this box</span></div>\n'
                f'<pre>{body}</pre>\n</div>\n')
    return PROMPT_BLOCK_RE.sub(box, text)


def preprocess(text: str) -> str:
    """Strip what should not print, and normalize the Markdown this project writes."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)          # assembly notes never print
    if text.startswith("---\n"):                                 # YAML front matter
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4:]
    # A list that starts on the line straight after a paragraph: GitHub renders it as a list,
    # python-markdown folds it into the paragraph.
    text = re.sub(r"^((?!\s*[-*+]\s)(?!\s*\d+[.)]\s)(?!\s*#)(?!\s*>)(?!\s*\|)(?!\s*```)\S.*)\n"
                  r"([-*+]\s|\d+[.)]\s)", r"\1\n\n\2", text, flags=re.M)
    text = CUE_RE.sub(r"\n\n\1", text)
    return promptboxes(text).strip() + "\n"


def mark_placeholders(html: str) -> str:
    """Make every unfilled placeholder impossible to miss on the page."""
    return PLACEHOLDER_RE.sub(
        lambda m: f'<span class="todo">TO FILL IN — {html_mod.escape(" ".join(m.group(1).split()))}</span>',
        html)


def classify_callouts(html: str) -> str:
    """A blockquote whose opening strong text signals a warning gets the orange edge."""
    def swap(m):
        body = m.group(1)
        head = re.sub(r"<[^>]+>", "", body[:200]).lower()
        warn = any(w in head for w in ("don't", "do not", "warning", "never", "⚠", "refus"))
        return f'<blockquote class="{"warn" if warn else ""}">{body}</blockquote>'
    return re.sub(r"<blockquote>(.*?)</blockquote>", swap, html, flags=re.S)


def render_tasklists(html: str) -> str:
    """`- [ ]` is meant to be ticked on paper, so the box has to be a real box."""
    if "[ ]" not in html and "[x]" not in html:
        return html
    def fix(m):
        inner = m.group(1)
        if not re.match(r"\s*\[[ xX]\]", inner):
            return m.group(0)
        done = bool(re.match(r"\s*\[[xX]\]", inner))
        inner = re.sub(r"^\s*\[[ xX]\]\s*", "", inner)
        return f'<li class="{"done" if done else ""}">{inner}</li>'
    html = re.sub(r"<li>(.*?)</li>", fix, html, flags=re.S)
    return re.sub(r"<ul>(\s*<li class=\"(?:done)?\">)", r'<ul class="tasklist">\1', html)


A_RE = re.compile(r'<a href="([^"]+)"[^>]*>(.*?)</a>', re.S)


def rewrite_links(html: str, src: Path, sections: list[dict]) -> str:
    """A relative path is navigation in a repository and noise on paper.

    Links to a document that is itself part of this PDF become a named cross-reference; links
    to anything else lose the link and keep their text. External URLs are kept and spelled out,
    so they can be typed from a printed page.
    """
    by_file = {(HERE / x["file"]).resolve(): x["title"] for x in sections}

    def swap(m):
        href, text = m.group(1), m.group(2)
        if href.startswith(("http://", "https://", "mailto:")):
            bare = re.sub(r"<[^>]+>", "", text).strip()
            cls = "" if bare in href else ' class="spelled"'
            return f'<a href="{href}"{cls}>{text}</a>'
        if href.startswith("#"):
            return text
        target = (src.parent / href.split("#")[0]).resolve()
        title = by_file.get(target)
        return f"<em>{html_mod.escape(title)}</em>" if title else text

    return A_RE.sub(swap, html)


# Documents whose own H1s are structure rather than a title. As a section inside a pack the
# section header already carries the title, so the leading H1 is dropped and everything below
# it moves down a level — which puts the Steps at the contents' sub-entry level, where they
# belong, instead of above it.
DEMOTE_HEADINGS = {"prompts/MASTER-FOLLOW-ALONG.md"}


def demote(text: str) -> str:
    # Strip the assembly comment first. These files open with one, so anchoring the title match
    # at \A without removing it means the leading H1 survives — and then shows up in the
    # contents as a sub-entry repeating the section title it was supposed to become.
    text = re.sub(r"\A\s*<!--.*?-->\s*", "", text, flags=re.S)
    text = re.sub(r"\A\s*#\s+.*?\n", "", text, count=1)
    return re.sub(r"^(#{1,5})(\s)", r"#\1\2", text, flags=re.M)


def md_to_html(path: Path, sections: list[dict]) -> str:
    text = path.read_text(encoding="utf-8")
    if str(path.relative_to(HERE)) in DEMOTE_HEADINGS:
        text = demote(text)
    text = preprocess(text)
    html = md_lib.markdown(text, extensions=MD_EXTENSIONS)
    html = rewrite_links(html, path, sections)
    return classify_callouts(render_tasklists(mark_placeholders(html)))


def find_placeholders(sections: list[dict]) -> list[tuple[str, str]]:
    """Every unfilled placeholder, as (source file, what it wants)."""
    out = []
    for sec in sections:
        p = HERE / sec["file"]
        if not p.is_file():
            continue
        body = re.sub(r"<!--.*?-->", "", p.read_text(encoding="utf-8"), flags=re.S)
        for m in PLACEHOLDER_RE.finditer(body):
            out.append((sec["file"], " ".join(m.group(1).split())))
    return out


# ----------------------------------------------------------------- assembly

TEMPLATE = Template("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>{{ title }}</title>
<style>{{ css }}

/* ---- pack-specific additions, layered over the handbook stylesheet ---- */
.todo {
  background: #FFF1E2; border: 0.8px solid {{ orange }}; color: {{ orange }};
  font-weight: 700; font-size: 8.5pt; padding: 0.4mm 1.4mm; border-radius: 0.8mm;
}
.cover .subtitle {
  font-size: 15pt; color: {{ gold }}; font-weight: 700; margin: 0 0 8mm;
}
.cover .byline { font-size: 10.5pt; color: #D4D4D8; margin: 0 0 2mm; }
.draft-flag {
  display: inline-block; background: {{ orange }}; color: #fff; font-weight: 700;
  font-size: 9pt; letter-spacing: 0.12em; text-transform: uppercase;
  padding: 1.6mm 3.4mm; border-radius: 1mm; margin: 0 0 8mm;
}
.appendix-divider .mark { width: 22mm; margin: 0 0 8mm; }
/* The handbook sizes this to 100vh, which in Chrome's print context is the viewport rather
   than the page box and spills a blank page after it. Content height is enough here. */
.appendix-divider { height: auto; padding: 24mm 20mm 30mm; }

/* The prompt callouts. A prompt is the one thing on the page that has to be copied exactly,
   so it is set apart, set in the mono face, and never reflowed. Long ones run across a page
   break rather than leaving half a page empty — the header names which prompt it is, and the
   box edge continues, so it stays obvious where it ends. */
.promptbox { margin: 6mm 0; page-break-inside: auto; }
.promptbox-head {
  background: {{ charcoal }}; color: #fff; padding: 2.2mm 4mm;
  border-radius: 1.2mm 1.2mm 0 0; font-size: 8.5pt; line-height: 1.3;
  display: flex; justify-content: space-between; align-items: baseline; gap: 6mm;
  /* Never let the header sit alone at the foot of a page above an empty box. */
  page-break-after: avoid; break-after: avoid;
}
.promptbox-head .l { font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; }
.promptbox-head .r { color: {{ gold }}; font-weight: 600; font-size: 8pt; white-space: nowrap; }
/* A LEFT RULE, not a box. A prompt runs over a page break, and Chrome does not redraw the
   sides of a bordered block on the pages it continues onto — the box would appear to end at
   the first break. A left border is painted on every fragment, so the rule runs down each
   page the prompt occupies and it stays obvious where you still are. */
.promptbox pre {
  margin: 0; padding: 3.5mm 4mm 3.5mm 4.5mm; background: #FBFBFC;
  border: 0; border-left: 1.3mm solid {{ gold }};
  font-family: var(--mono); font-size: 7.8pt; line-height: 1.5;
  white-space: pre-wrap; word-wrap: break-word;
}

/* A long reference table should flow across pages rather than leaving a near-empty one
   behind it; its rows still stay whole. */
table.flow { page-break-inside: auto; }
table.flow tr { page-break-inside: avoid; }

/* Sub-section locators. Positioned against the heading itself, not the section, so each one
   is found on its own page. Occupies no space, so dropping it in the final pass cannot move
   anything. */
.doc-section h2 { position: relative; }
.submark {
  position: absolute; top: 0; left: 0; font-size: 6pt; line-height: 1;
  white-space: nowrap; word-break: keep-all; color: #fff; pointer-events: none;
}
</style></head><body>

<section class="cover">
  <div><img class="cover-mark" src="{{ mark }}" alt=""></div>
  <div>
    {% if draft %}<div class="draft-flag">Draft — {{ placeholders|length }} item{{ '' if placeholders|length == 1 else 's' }} to fill in</div>{% endif %}
    <div class="rule"></div>
    <div class="tagline">{{ tagline }}</div>
    <h1>{{ title }}</h1>
    <div class="subtitle">{{ subtitle }}</div>
    <p class="blurb">{{ blurb }}</p>
  </div>
  <div class="meta">
    <div class="byline"><strong>{{ byline }}</strong></div>
    {% if deck %}{{ deck_pages }}-slide session deck included &nbsp;·&nbsp; {% endif %}Generated {{ generated }}
  </div>
</section>

{% if draft %}
<section class="fm">
  <h1>Before you distribute this</h1>
  <blockquote class="warn"><p><strong>This is a draft.</strong> {{ placeholders|length }} placeholder{{ '' if placeholders|length == 1 else 's' }}
  {{ 'is' if placeholders|length == 1 else 'are' }} still unfilled. Each one is highlighted in orange where it appears in the
  text. Fill them in the source Markdown and rebuild — when none remain, this page and the cover
  banner disappear on their own.</p></blockquote>
  {% if one_source %}<p class="small muted">All of them are in
  <code>{{ one_source }}</code>, in the order listed.</p>{% endif %}
  <table class="flow">
    <thead><tr><th style="width:9mm">#</th>{% if not one_source %}<th style="width:50mm">Source file</th>{% endif %}<th>What it needs</th></tr></thead>
    <tbody>
    {% for f, want in placeholders %}
      <tr><td>{{ loop.index }}</td>{% if not one_source %}<td style="font-family:var(--mono);font-size:7.5pt">{{ f }}</td>{% endif %}<td>{{ want }}</td></tr>
    {% endfor %}
    </tbody>
  </table>
  <p class="small muted">Two of these decide whether the pack works at all: whether the Amazon
  Quick accounts survive the event, and whether attendees may publish Triage to their students.
  The rest are cosmetic by comparison.</p>
</section>
{% endif %}

<section class="fm toc">
  <h1>Contents</h1>
  {{ toc_html }}
</section>

{{ body_html }}

{% if deck %}
<section class="appendix-divider">
  <img class="mark part-mark" src="{{ mark_light }}" alt="">
  <div class="kicker">Appendix</div>
  <h2>The session deck</h2>
  <p class="note">{{ deck_note }}</p>
  <p class="note small muted">Reproduced unaltered from the approved deck. These pages carry no
  page numbers or running footer because nothing is overlaid on them.</p>
</section>
{% endif %}

</body></html>""")


def build_html(ed: dict, toc_html: str, body_html: str, placeholders: list, deck: bool,
               deck_pages: int) -> str:
    sources = {f for f, _ in placeholders}
    return TEMPLATE.render(
        one_source=(sources.pop() if len(sources) == 1 else None),
        title=TITLE, subtitle=ed["subtitle"], tagline=TAGLINE, byline=BYLINE,
        blurb=ed["blurb"], deck_note=ed["deck_note"].format(n=deck_pages),
        css=(BRAND / "style.css").read_text(encoding="utf-8"),
        mark=(BRAND / "dtcc-mark-neg.jpg").as_uri(),
        mark_light=(BRAND / "dtcc-mark.png").as_uri(),
        generated=date.today().isoformat(),
        toc_html=toc_html, body_html=body_html,
        placeholders=placeholders, draft=bool(placeholders),
        deck=deck, deck_pages=deck_pages, gold=GOLD, orange=ORANGE, charcoal=CHARCOAL,
    )


H2_RE = re.compile(r"<h2([^>]*)>(.*?)</h2>", re.S)


def sections_html(sections: list[dict], with_marks: bool) -> tuple[str, list[dict]]:
    """Render the pack's documents, planting locators. Returns the HTML and the sub-sections."""
    out, subs = [], []
    counter = [0]                      # global, so sub-keys never collide across sections
    for sec in sections:
        path = HERE / sec["file"]
        if not path.is_file():
            sys.exit(f"error: missing {sec['file']}")
        body = md_to_html(path, sections)

        def tag(m, sec=sec):
            counter[0] += 1
            key = f"S1{counter[0]:02d}"
            title = re.sub(r"<[^>]+>", "", m.group(2)).strip()
            subs.append({"key": key, "title": title, "parent": sec["key"]})
            mark = f'<span class="submark">§§{key}§§</span>' if with_marks else ""
            return f"<h2{m.group(1)}>{mark}{m.group(2)}</h2>"

        body = H2_RE.sub(tag, body)
        mark = (f'<span class="secmark" style="color:#fff">§§{sec["key"]}§§</span>'
                if with_marks else "")
        out.append(f'<section class="doc-section">{mark}\n{body}</section>')
    return "\n".join(out), subs


def toc_html(sections: list[dict], pages: dict[str, int], subs: list[dict], deck: bool,
             deck_page: int | None) -> str:
    rows = []
    for sec in sections:
        pg = pages.get(sec["key"], "")
        rows.append(f'<div class="toc-part"><span>{sec["title"]}</span>'
                    f'<span class="leader"></span><span class="pg">{pg}</span></div>')
        for sub in (s for s in subs if s["parent"] == sec["key"]):
            spg = pages.get(sub["key"], "")
            rows.append(f'<div class="toc-sub"><span>{html_mod.escape(sub["title"])}</span>'
                        f'<span class="leader"></span><span class="pg">{spg}</span></div>')
    if deck:
        pg = deck_page or ""
        rows.append('<div class="toc-part"><span>Appendix — The session deck</span>'
                    f'<span class="leader"></span><span class="pg">{pg}</span></div>')
    return "\n".join(rows)


# ----------------------------------------------------------------- rendering

def render_pdf(html_path: Path, out_pdf: Path, chrome: str, timeout: int = 300) -> None:
    """Render with headless Chrome.

    Chrome writes the PDF and then frequently does not exit — a long-standing headless quirk
    unrelated to whether the render succeeded. So watch for the file to appear and stop
    growing, then stop Chrome ourselves.
    """
    out_pdf.unlink(missing_ok=True)
    with tempfile.TemporaryDirectory() as profile:
        cmd = [chrome, "--headless", "--disable-gpu", "--no-sandbox", "--no-first-run",
               "--no-pdf-header-footer", "--allow-file-access-from-files",
               "--virtual-time-budget=30000", f"--user-data-dir={profile}",
               f"--print-to-pdf={out_pdf}", html_path.as_uri()]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        deadline = time.monotonic() + timeout
        stable, last = 0, -1
        try:
            while time.monotonic() < deadline:
                if proc.poll() is not None:
                    break
                size = out_pdf.stat().st_size if out_pdf.is_file() else -1
                stable = stable + 1 if size == last and size > 0 else 0
                last = size
                if stable >= 2:
                    break
                time.sleep(0.6)
        finally:
            if proc.poll() is None:
                proc.terminate()
                try:
                    proc.wait(timeout=15)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    proc.wait(timeout=15)
    if not out_pdf.is_file() or out_pdf.stat().st_size == 0:
        err = (proc.stderr.read() or b"").decode("utf-8", "replace") if proc.stderr else ""
        sys.exit(f"error: Chrome produced no PDF.\n{err[-2000:]}")


def find_marks(pdf: Path) -> dict[str, int]:
    """Locate each section by the marker planted in the HTML."""
    pages: dict[str, int] = {}
    exe = shutil.which("pdftotext")
    if exe:
        with tempfile.TemporaryDirectory() as td:
            txt = Path(td) / "o.txt"
            subprocess.run([exe, "-layout", str(pdf), str(txt)],
                           check=False, capture_output=True)
            if txt.is_file():
                for n, page in enumerate(txt.read_text("utf-8", "replace").split("\f"), 1):
                    for key in MARK_RE.findall(page):
                        pages.setdefault(key, n)
    if not pages:
        reader = PdfReader(str(pdf))
        for n, page in enumerate(reader.pages, 1):
            try:
                for key in MARK_RE.findall(page.extract_text() or ""):
                    pages.setdefault(key, n)
            except Exception:
                pass
    return pages


def stamp(pdf_in: Path, pdf_out: Path, total: int, skip: set[int], running: str) -> None:
    """Chrome has no CSS margin boxes, so running furniture is overlaid afterwards."""
    reader = PdfReader(str(pdf_in))
    width, height = letter
    overlay_path = pdf_out.parent / ".overlay.pdf"
    c = rl_canvas.Canvas(str(overlay_path), pagesize=(width, height))
    for n in range(1, len(reader.pages) + 1):
        y = 34
        c.setStrokeColor(HexColor(GOLD))
        c.setLineWidth(1.6)
        c.line(52, y + 12, width - 52, y + 12)
        c.setFont("Helvetica", 7.5)
        c.setFillColor(HexColor(LIGHT_GRAY))
        c.drawString(52, y, running)
        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(HexColor(CHARCOAL))
        c.drawRightString(width - 52, y, f"{n} / {total}")
        c.showPage()
    c.save()

    overlay = PdfReader(str(overlay_path))
    writer = PdfWriter(clone_from=str(pdf_in))
    for n, page in enumerate(writer.pages, start=1):
        if n != 1 and n not in skip and n - 1 < len(overlay.pages):
            try:
                page.merge_page(overlay.pages[n - 1])
            except Exception:
                pass
        try:
            page.compress_content_streams()
        except Exception:
            pass
    try:
        writer.compress_identical_objects()
    except Exception:
        pass
    with pdf_out.open("wb") as fh:
        writer.write(fh)
    overlay_path.unlink(missing_ok=True)


def append_deck(body: Path, out: Path) -> int:
    """Copy the approved deck in at native size. Nothing is scaled, overlaid or re-encoded."""
    writer = PdfWriter(clone_from=str(body))
    reader = PdfReader(str(DECK))
    for page in reader.pages:
        writer.add_page(page)
    with out.open("wb") as fh:
        writer.write(fh)
    return len(reader.pages)


def add_outline(pdf: Path, sections: list[dict], pages: dict[str, int], subs: list[dict],
                deck_page: int | None) -> None:
    writer = PdfWriter(clone_from=str(pdf))
    last = len(writer.pages)

    def at(n: int) -> int:
        return max(0, min(n, last) - 1)

    writer.add_outline_item(TITLE, 0)
    for sec in sections:
        if sec["key"] not in pages:
            continue
        parent = writer.add_outline_item(sec["outline"], at(pages[sec["key"]]))
        for sub in (x for x in subs if x["parent"] == sec["key"] and x["key"] in pages):
            writer.add_outline_item(sub["title"], at(pages[sub["key"]]), parent=parent)
    if deck_page:
        writer.add_outline_item("Appendix — The session deck", at(deck_page))
    with pdf.open("wb") as fh:
        writer.write(fh)


# ----------------------------------------------------------------- main

def build_edition(name: str, ed: dict, out_dir: Path, chrome: str,
                  include_deck: bool, deck_pages: int, keep_html: bool) -> Path:
    # An edition can opt out of the appendix entirely; --no-deck still overrides everything.
    include_deck = include_deck and ed.get("deck", True)
    sections = sections_for(ed)
    for sec in sections:
        if not (HERE / sec["file"]).is_file():
            sys.exit(f"error: {name} edition is missing {sec['file']}")

    final = out_dir / ed["out"]
    placeholders = find_placeholders(sections)
    print(f"\n[{name}] {len(sections)} sections"
          + (f", {len(placeholders)} placeholder(s) unfilled — building as DRAFT"
             if placeholders else ""))

    tmp = out_dir / f".build-{name}"
    tmp.mkdir(parents=True, exist_ok=True)

    # Pass 1 — plant markers, empty page numbers, read back where each section landed.
    body1, subs = sections_html(sections, True)
    html1 = tmp / "pass1.html"
    html1.write_text(build_html(ed, toc_html(sections, {}, subs, include_deck, None), body1,
                                placeholders, include_deck, deck_pages), encoding="utf-8")
    pdf1 = tmp / "pass1.pdf"
    print("  pass 1 — locating sections")
    render_pdf(html1, pdf1, chrome)
    pages = find_marks(pdf1)
    body_pages = len(PdfReader(str(pdf1)).pages)
    missing = [x["key"] for x in sections if x["key"] not in pages]
    if missing:
        print(f"  ! could not locate {missing} — contents page numbers may be wrong")

    # Pass 2 — real page numbers, markers gone. They occupy no space, so removing them
    # cannot move anything.
    deck_page = body_pages + 1 if include_deck else None
    body2, _ = sections_html(sections, False)
    html2 = tmp / "pass2.html"
    html2.write_text(build_html(ed, toc_html(sections, pages, subs, include_deck, deck_page),
                                body2, placeholders, include_deck, deck_pages), encoding="utf-8")
    pdf2 = tmp / "pass2.pdf"
    print("  pass 2 — final render")
    render_pdf(html2, pdf2, chrome)

    n2 = len(PdfReader(str(pdf2)).pages)
    if n2 != body_pages:
        print(f"  ! pagination shifted ({body_pages} -> {n2}); contents may be off by one")
        body_pages = n2
        deck_page = body_pages + 1 if include_deck else None

    # Furniture on the generated pages only — never on the appended deck.
    stamped = tmp / "stamped.pdf"
    stamp(pdf2, stamped, body_pages + (deck_pages if include_deck else 0), set(),
          ed["running"])
    print(f"  stamped {body_pages} generated pages (deck pages left untouched)")

    if include_deck:
        append_deck(stamped, final)
    else:
        shutil.copy(stamped, final)
    add_outline(final, sections, pages, subs, deck_page)

    if keep_html:
        for f in (html1, html2):
            shutil.copy(f, out_dir / f"{name}-{f.name}")
    else:
        shutil.rmtree(tmp, ignore_errors=True)

    total = len(PdfReader(str(final)).pages)
    size = final.stat().st_size / 1_048_576
    flag = f"  [DRAFT — {len(placeholders)} to fill]" if placeholders else ""
    print(f"  wrote {final.relative_to(HERE)} — {total} pages, {size:.1f} MB{flag}")
    return final


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--edition", choices=[*EDITIONS, "all"], default="all",
                    help="which edition to build (default: all)")
    ap.add_argument("--out", default="dist", help="output directory (default: dist)")
    ap.add_argument("--no-deck", action="store_true", help="omit the appended session deck")
    ap.add_argument("--keep-html", action="store_true", help="keep the intermediate HTML")
    args = ap.parse_args()

    chrome = chrome_binary()
    out_dir = HERE / args.out
    out_dir.mkdir(parents=True, exist_ok=True)

    include_deck = not args.no_deck
    deck_pages = 0
    if include_deck:
        if not DECK.is_file():
            sys.exit(f"error: {DECK.name} not found — cannot append the deck.")
        deck_pages = len(PdfReader(str(DECK)).pages)
        # The deck used to be checked against a fixed md5. That stopped being the right test
        # once subtractive edits were permitted: a legitimate rebuild changes the md5 every
        # time, so the check cried wolf on every build and said nothing about whether the
        # content was actually allowed. verify_deck.py answers the real question — does this
        # deck contain only approved strings, and fewer of them?
        check = subprocess.run([sys.executable, str(HERE / "verify_deck.py"), "--pdf", str(DECK)],
                               capture_output=True, text=True)
        if check.returncode != 0:
            print(f"! WARNING: {DECK.name} is NOT subtractive against the approved deck:")
            for line in (check.stdout + check.stderr).strip().splitlines():
                print(f"    {line}")
            print("  Building anyway, but do not ship this. See DECK-APPROVAL.md.")
        else:
            print(f"deck verified subtractive against the approved copy ({deck_pages} pages)")

    names = list(EDITIONS) if args.edition == "all" else [args.edition]
    for name in names:
        build_edition(name, EDITIONS[name], out_dir, chrome, include_deck, deck_pages,
                      args.keep_html)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
