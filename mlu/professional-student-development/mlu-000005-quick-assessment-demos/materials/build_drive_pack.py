#!/usr/bin/env python3
"""Stage the shared Google Drive folder — attendee editions, plain names, ready to upload.

    python3 build_drive_pack.py            # writes dist/drive/
    python3 build_drive_pack.py --check    # verify the staged copy leaks no spoilers

The tree it produces is the one specified in prompts/DRIVE-FOLDER.md. Everything readable is
written as Markdown for conversion to a Google Doc; see that file for the conversion steps and
the smart-quotes trap.

**Why this is a script and not a copy.** The prompt files in prompts/ are facilitator documents.
Each one ends with a "Before you deliver: prove it works" section stating the outputs the build
must produce — Marcus scoring ≈88 on the weak rubric and F on the generated one, and Triage
returning Present for his running-time section. Those are the reveals on slides 11, 12 and 23.
Uploading the files as they stand puts the end of the session in a folder the room opens in the
first five minutes.

So the attendee edition of each prompt is everything up to that section, and the facilitator
sections are dropped by name. --check greps the staged output for the specific strings that
would give the session away, because "I remembered to trim it" is not a guarantee.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / "dist" / "drive"
# Staged separately and NOT uploaded when the folder goes live. See HOLD_REASON.
HOLD = HERE / "dist" / "drive-hold"
HOLD_REASON = """The reference rubric is the answer to the first hands-on AND a spoiler for
slide 12. Its running-time descriptors name Marcus's three errors outright: constant-time access
to the i-th element of a linked list, constant-time insertion into the middle of an array, and
O(1) amortized appends. That is slide 12's table, in a file anyone can open at 0:05.

Upload this folder's contents into "Sample pack/" AFTER the rubric segment ends at 0:36. One
drag. The reference rubric then lands exactly when it is useful — as something to compare your
own generated rubric against, which is what it is for."""

# Sections cut from the attendee editions. Matched on the heading text, so a renamed heading
# fails loudly in --check rather than silently shipping.
FACILITATOR_SECTIONS = [
    "Before you deliver: prove it works",
    "A note for whoever delivers this next",
]

# Strings that must never reach the shared folder. Each is a reveal the session depends on.
SPOILERS = [
    ("88", "Marcus's score on the weak rubric — slide 11"),
    ("≈38", "Marcus's score on the golden rubric — slide 11"),
    ("Marcus passing", "the slide 23 payoff"),
    ("wrong about running times", "slide 12, and the slide 7 clause we deleted"),
    ("is the point, not a defect", "the slide 23 payoff"),
    ("present is not", "the closing line — slide 23"),
    ("Present is not", "the closing line — slide 23"),
    # The reference rubric's own descriptors, which spell out Marcus's errors — slide 12.
    ("min{i, n", "the linked-list error — slide 12"),
    ("1 + n \u2212 i", "the array-insertion error — slide 12"),
    ("O(1) amortized", "the array-append error — slide 12"),
]

# published name -> (source, kind). "doc" is converted to a Google Doc; "raw" is uploaded as-is.
PLAN: list[tuple[str, str, str]] = [
    # (published path, source path, kind)
    #
    # ONE document. Everything attendees read, grade, copy or paste is inside it — the paper,
    # the weak rubric, the assignment, the objectives, all three prompts. Seven documents was
    # coherent on paper and wrong in a room; ninety minutes has no room for navigating between
    # files. See prompts/DRIVE-FOLDER.md.
    ("★ THE ASSIGNMENT LIFECYCLE — follow along here.md",
     "prompts/MASTER-FOLLOW-ALONG.md", "doc"),

    # The student papers stay outside, because they get pasted INTO the tools rather than read.
    ("Sample pack/Student papers/Marcus Lee — the paper you graded.txt",
     "activities/sample-pack/papers/Marcus_Lee.txt", "paper"),
    ("Sample pack/Student papers/Aisha Rahman — a strong paper.txt",
     "activities/sample-pack/papers/Aisha_Rahman.txt", "paper"),
    ("Sample pack/Student papers/Priya Chandra — a reflection, not an analysis.txt",
     "activities/sample-pack/papers/Priya_Chandra.txt", "paper"),
    ("Sample pack/Student papers/Leila Haddad — an unfinished draft.txt",
     "activities/sample-pack/papers/Leila_Haddad.txt", "paper"),

    ("Sample pack/The course reading.pdf",
     "activities/sample-pack/persona2_cs_data_structures.pdf", "raw"),
    ("Sample pack/Class roster.csv", "activities/sample-pack/roster.csv", "raw"),

    ("Sample pack/For the tools (advanced)/rubric-format.md",
     "activities/rubric-format.md", "raw"),
    ("Sample pack/For the tools (advanced)/rubric-golden.json",
     "activities/sample-pack/rubric-golden.json", "hold-raw"),
    ("Sample pack/The reference rubric.md", "activities/sample-pack/rubric-golden.md", "hold"),

    ("Take home/The session deck.pdf", "assessment-lifecycle-deck.pdf", "raw"),
    ("Take home/Take-home pack.pdf", "dist/assessment-lifecycle-take-home-pack.pdf", "raw"),
]

# The attendee doc's title, since the facilitator file's H1 says "PROMPT 1 — ..." and the
# folder calls it something else. A reader should not have to reconcile two names.
RETITLE = {
    "1 — Build the Rubric Builder.md": "1 — Build the Rubric Builder",
    "2 — Build the AI-Proofing app.md": "2 — Build the AI-Proofing app",
    "3 — Build Triage.md": "3 — Build Triage",
    "★ START HERE.md": "★ Start here",
}


# Source filenames, as the repo calls them, mapped to what the shared folder calls them. The
# attendee editions are written from facilitator documents that refer to files by their repo
# names; leaving those in sends people looking for "persona2_cs_data_structures.pdf" in a folder
# that has no such thing. Longest first, so rubric-golden.json is not eaten by rubric-golden.md.
FOLDER_NAMES = {
    "persona2_cs_data_structures.pdf": "**The course reading**",
    "activities/sample-pack/": "the **Sample pack** folder",
    "rubric-golden.json": "**The reference rubric**",
    "rubric-golden.md": "**The reference rubric**",
    "rubric-weak.md": "**The weak rubric**",
    "rubric-format.md": "**rubric-format.md** (in *For the tools*)",
    "assignment.md": "**The assignment**",
    "roster.csv": "**Class roster**",
    "Marcus_Lee.txt": "**Marcus Lee's paper**",
    "Aisha_Rahman.txt": "**Aisha Rahman's paper**",
    "Priya_Chandra.txt": "**Priya Chandra's paper**",
    "Leila_Haddad.txt": "**Leila Haddad's paper**",
    "prompts 2 and 3": "files 2 and 3",
    "prompt 1": "file 1",
    # "below" was true when the prompt was a fenced block in the same document. It is not now.
    "paste the prompt below, send it": "open the next document, copy it all, paste it, send it",
    "from the prompt below": "from the prompt in the next document",
    "the prompt in the grey block below": "the prompt in the next document",
    "**Copy the prompt** in the grey block below — all of it — and paste it into the "
    "*describe your app* box. Send it.":
        "**Copy the prompt** — see the box below — and paste it into the *describe your app* "
        "box. Send it.",
    "Copy the prompt in the grey block below": "Copy the prompt from the next document",
    "the grey block below": "the next document",
    "a block of text from this folder": "one of the PROMPT documents in this folder",
    "**Select the whole grey block** and copy it.":
        "Open the matching **PROMPT to copy** document, press **Ctrl-A** / **Cmd-A**, copy.",
    "Each one has the steps at the top and a grey\nblock of text below them.":
        "Each one has the steps, and points you at the\nprompt to copy.",
}


def use_folder_names(text: str) -> str:
    for src, shown in sorted(FOLDER_NAMES.items(), key=lambda kv: -len(kv[0])):
        # Match the name whether or not it is in backticks, and drop the backticks with it.
        text = re.sub(r"`?" + re.escape(src) + r"`?", shown.replace("\\", "\\\\"), text)
    # A name already inside bold must not end up double-bolded.
    return text.replace("****", "")


def flatten_table_emphasis(text: str) -> str:
    """Remove ** and * inside table rows.

    Google Docs' Markdown import escapes emphasis inside a table cell instead of applying it, so
    `**Content**` arrives in the document as a literal `**Content**`. Stripping the markers keeps
    the table and loses only the bold; leaving them in puts asterisks on a projector.
    """
    def fix(m):
        return re.sub(r"\*{1,2}([^*]+?)\*{1,2}", r"\1", m.group(0))
    return re.sub(r"^\|.*$", fix, text, flags=re.M)


def strip_comments(text: str) -> str:
    """Drop the HTML assembly notes — they are instructions to the facilitator, not content."""
    return re.sub(r"<!--.*?-->\s*", "", text, flags=re.S)


def split_sections(text: str) -> list[tuple[str, str]]:
    """Split on level-2 headings, keeping each heading with its body."""
    parts = re.split(r"^(## .+)$", text, flags=re.M)
    out = [("", parts[0])]
    for i in range(1, len(parts), 2):
        out.append((parts[i][3:].strip(), parts[i] + parts[i + 1]))
    return out


def attendee_edition(src: Path, published: str) -> str:
    text = strip_comments(src.read_text(encoding="utf-8"))
    kept, dropped = [], []
    for heading, body in split_sections(text):
        if heading in FACILITATOR_SECTIONS:
            dropped.append(heading)
            continue
        kept.append(body)
    if published in RETITLE:
        kept[0] = re.sub(r"^# .+$", "# " + RETITLE[published], kept[0], count=1, flags=re.M)
    out = "".join(kept).rstrip() + "\n"
    # Collapse the blank runs left behind where a section was cut out.
    out = re.sub(r"\n{4,}", "\n\n\n", out)
    out = re.sub(r"\n---\s*\n\s*$", "\n", out)
    print(f"    cut: {', '.join(dropped) if dropped else '(nothing)'}")
    return out


FENCE = re.compile(r"```[a-z]*\n(.*?)\n```", re.S)


def split_prompt(text: str) -> tuple[str, str]:
    """Separate the steps from the prompt block, and say where the prompt went.

    Google Docs' Markdown import does not keep fenced code blocks — the fence is dropped and
    every line becomes its own paragraph. So there is no grey block in the document, and
    "select the grey block" is an instruction that cannot be followed. Selecting a long run of
    text by hand, on a phone, under time pressure, is exactly the step that fails in a room.

    Putting the prompt in a document of its own reduces the whole operation to Select All,
    Copy — which everyone can already do, on every device.
    """
    m = FENCE.search(text)
    if not m:
        return text, ""
    pointer = (
        "\n\n> ### The prompt is in the next document\n>\n"
        "> Open the document with the same number as this one, named "
        "**\u201cPROMPT to copy\u201d**.\n"
        "> Press **Ctrl-A** (**Cmd-A** on a Mac) to select all of it, copy it, and paste it\n"
        "> into Amazon Quick.\n>\n"
        "> There is nothing in that document except the prompt, so you cannot select too much.\n"
        "> Then come back here for the rest of the steps.\n\n")
    return text[:m.start()].rstrip() + pointer + text[m.end():].lstrip(), m.group(1).strip() + "\n"


def paper_edition(src: Path, published: str) -> str:
    """A student paper, with the header a faculty reader needs to know what they are holding."""
    name = published.rsplit("/", 1)[-1].removesuffix(".txt")
    return (f"# {name}\n\n"
            f"*Synthetic sample data — this student does not exist and this is not real student "
            f"work.*\n\n---\n\n" + src.read_text(encoding="utf-8").strip() + "\n")


def build() -> int:
    for d in (OUT, HOLD):
        if d.exists():
            shutil.rmtree(d)
    for published, source, kind in PLAN:
        src = HERE / source
        if not src.is_file():
            print(f"  MISSING  {source}", file=sys.stderr)
            return 1
        dst = (HOLD if kind.startswith("hold") else OUT) / published
        dst.parent.mkdir(parents=True, exist_ok=True)
        if kind == "hold-raw":
            print(f"  HOLD  {published}")
            shutil.copy2(src, dst)
        elif kind == "hold":
            print(f"  HOLD  {published}")
            dst.write_text(strip_comments(src.read_text(encoding="utf-8")), encoding="utf-8")
        elif kind == "prompt":
            print(f"  doc   {published}")
            steps, prompt = split_prompt(
                use_folder_names(flatten_table_emphasis(attendee_edition(src, published))))
            dst.write_text(steps, encoding="utf-8")
            if prompt:
                side = dst.with_name(f"{published.split(' ')[0]} — PROMPT to copy.txt")
                side.write_text(prompt, encoding="utf-8")
                print(f"  doc   {side.name}   <- select all, copy")
        elif kind == "doc":
            print(f"  doc   {published}")
            dst.write_text(use_folder_names(flatten_table_emphasis(
                strip_comments(src.read_text(encoding="utf-8")))), encoding="utf-8")
        elif kind == "paper":
            print(f"  doc   {published}")
            dst.write_text(paper_edition(src, published), encoding="utf-8")
        else:
            print(f"  file  {published}")
            shutil.copy2(src, dst)
    if HOLD.exists():
        (HOLD / "WHY THESE ARE HELD BACK.txt").write_text(HOLD_REASON + "\n", encoding="utf-8")
    return 0


def check() -> int:
    """Grep the staged folder for the reveals the session depends on."""
    if not OUT.exists():
        print("Nothing staged — run without --check first.", file=sys.stderr)
        return 1
    hits = []
    # An unfilled placeholder is not a spoiler, but it is worse on a projector: it tells the room
    # the materials were assembled in a hurry. Nothing with one in it goes in the folder.
    for f in sorted(OUT.rglob("*")):
        if f.is_file() and f.suffix.lower() not in {".pdf"} and "FILL IN" in f.read_text(
                encoding="utf-8", errors="replace"):
            print(f"  {f.relative_to(OUT)}  — unfilled «FILL IN» placeholder", file=sys.stderr)
            hits.append((f.relative_to(OUT), 0, "«FILL IN»", "unfilled placeholder", ""))
    for f in sorted(OUT.rglob("*")):
        if not f.is_file() or f.suffix.lower() in {".pdf", ".json"}:
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        for needle, why in SPOILERS:
            for m in re.finditer(re.escape(needle), text):
                line = text.count("\n", 0, m.start()) + 1
                ctx = text[max(0, m.start() - 55):m.start() + 55].replace("\n", " ")
                hits.append((f.relative_to(OUT), line, needle, why, ctx))
    for path, line, needle, why, ctx in hits:
        print(f"  {path}:{line}  {needle!r} — {why}\n      …{ctx}…", file=sys.stderr)
    if hits:
        print(f"\nFAIL  {len(hits)} spoiler(s) staged for the shared folder.", file=sys.stderr)
        return 1
    n = sum(1 for f in OUT.rglob("*") if f.is_file())
    h = sum(1 for f in HOLD.rglob("*") if f.is_file()) if HOLD.exists() else 0
    print(f"OK    {n} files staged for upload, no session reveals among them.")
    if h:
        print(f"      {h} file(s) held back in {HOLD.relative_to(HERE)} \u2014 upload at 0:36.")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    raise SystemExit(check() if args.check else (build() or check()))
