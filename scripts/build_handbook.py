#!/usr/bin/env python3
"""Build the DTCC-MLU Faculty Handbook: every contribution, in full, as one printable PDF.

For faculty who will not go to GitHub. The handbook carries the complete teaching materials —
assignments, rubrics, facilitator guides, handouts — plus the instructional slide decks and
readings each contribution ships, merged in as appendices.

Pipeline:
  1. Load contribution metadata (reusing build_catalog.load).
  2. Render every Markdown document and notebook to HTML, rewriting cross-contribution links
     into in-document anchors.
  3. Compose one HTML document against the DTCC brand stylesheet.
  4. Render it with headless Chrome.
  5. Splice the appendix PDFs in behind their divider pages.
  6. Stamp running furniture and build the PDF outline.

Run twice internally: the first pass locates each section so the contents page can carry true
page numbers, the second produces the document.

Usage:  python3 scripts/build_handbook.py [--out dist] [--skip-appendices] [--keep-html]

Requires Google Chrome (or set CHROME to a binary path) plus the Python packages in
scripts/requirements.txt. Output is a build artifact; it belongs in dist/, never committed.
"""
from __future__ import annotations

import argparse
import html as htmllib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import date
from pathlib import Path

import markdown
import yaml
from jinja2 import Template
from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as rl_canvas

from build_catalog import CATEGORY_INTROS, load

ROOT = Path(__file__).resolve().parent.parent
HANDBOOK = Path(__file__).resolve().parent / "handbook"
REPO_URL = "https://github.com/DTC-Consortium/DTC-Consortium-MLU"

GOLD = "#EBB000"
CHARCOAL = "#181616"
LIGHT_GRAY = "#9C9C9C"

CHROME_CANDIDATES = [
    os.environ.get("CHROME", ""),
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "google-chrome-stable",
    "google-chrome",
    "chromium",
]

MD_EXTENSIONS = ["tables", "fenced_code", "attr_list", "sane_lists", "def_list"]

# Appendices are the documents a facilitator teaches from. Sample data a notebook loads is
# referenced instead — reprinting a 5MB case report nobody reads on paper helps no one.
APPENDIX_DIRS = ("slides", "syllabus", "lectures", "references")

# Documents whose content is better regenerated or collapsed than converted.
SKIP_DOCS = {"LICENSE.md", "CITATION.cff"}

# Section markers are planted in the HTML so each section can be located in the rendered
# PDF. They are short and fixed-width on purpose: a long key breaks across text runs and
# then cannot be matched back. The final pass omits them so nothing leaks into the text.
MARK_RE = re.compile("\u00a7\u00a7(S[0-9]{4})\u00a7\u00a7")


# ----------------------------------------------------------------- discovery


def chrome_binary() -> str:
    for cand in CHROME_CANDIDATES:
        if not cand:
            continue
        if Path(cand).exists():
            return cand
        found = shutil.which(cand)
        if found:
            return found
    sys.exit(
        "error: could not find Google Chrome.\n"
        "       Install it, or set CHROME to the binary path."
    )


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def doc_key(doc: dict, md: Path) -> str:
    """A unique section key for one document.

    Keyed on the path rather than the filename: several contributions carry a nested
    materials/**/README.md, and keying on the stem alone collapsed those into the
    contribution's own README.
    """
    rel = md.relative_to(ROOT / doc["_dir"]).with_suffix("")
    return f'{doc["id"]}-{slugify(str(rel))}'


# Filenames are lowercased slugs, so a naive title-case turns product names into nonsense
# ("Partyrock", "Oacc"). These are restored on the way back out.
TERMS = {
    "ai": "AI", "genai": "GenAI", "ir": "IR", "oacc": "OACC", "mlu": "MLU",
    "dtcc": "DTCC", "aws": "AWS", "partyrock": "PartyRock", "chatgpt": "ChatGPT",
    "copilot": "Copilot", "swot": "SWOT", "faq": "FAQ", "vtt": "VTT",
    "oracle": "O.R.A.C.L.E.", "pdf": "PDF", "api": "API", "csv": "CSV",
}


def prettify(text: str) -> str:
    words = [TERMS.get(w.lower(), w) for w in text.split()]
    if words:
        words[0] = words[0] if words[0] in TERMS.values() else words[0][:1].upper() + words[0][1:]
    return " ".join(words)


def doc_label(doc: dict, md: Path) -> str:
    """A readable heading. A bare "README" is named for the folder it documents."""
    rel = md.relative_to(ROOT / doc["_dir"])
    stem = rel.stem
    if stem.lower() == "readme" and len(rel.parts) > 1:
        parent = rel.parts[-2].replace("-", " ").replace("_", " ")
        return f"{prettify(parent)} — about these files"
    return prettify(stem.replace("_", " ").replace("-", " ").strip())


def doc_order(doc: dict) -> list[Path]:
    """Every Markdown document in a contribution, in the order the manifest lists them.

    The manifest is human-ordered and reflects how the author wants the contribution read, so
    it beats alphabetical. Anything in materials/ the manifest misses is appended after, so a
    document can never be silently dropped from the handbook.
    """
    base = ROOT / doc["_dir"]
    seen: list[Path] = []

    for entry in doc.get("materials", []):
        if entry.get("external"):
            continue
        p = base / entry["path"]
        if p.is_file() and p.suffix == ".md":
            if p not in seen:
                seen.append(p)
        elif p.is_dir():
            for md in sorted(p.rglob("*.md")):
                if md not in seen:
                    seen.append(md)

    for md in sorted((base / "materials").rglob("*.md")):
        if md not in seen and md.name not in SKIP_DOCS:
            seen.append(md)

    return [p for p in seen if p.name not in SKIP_DOCS]


def notebooks(doc: dict) -> list[Path]:
    return sorted((ROOT / doc["_dir"]).rglob("*.ipynb"))


def appendices(doc: dict) -> list[Path]:
    base = ROOT / doc["_dir"] / "materials"
    out = []
    for pdf in sorted(base.rglob("*.pdf")):
        rel = pdf.relative_to(base)
        if "data" in rel.parts or rel.name.startswith("persona"):
            continue
        if rel.parts and rel.parts[0] in APPENDIX_DIRS:
            out.append(pdf)
    return out


# ----------------------------------------------------------------- markdown


# A list that starts on the line straight after a paragraph, with no blank line between.
# GitHub renders it as a list; python-markdown's stricter parsing folds it into the paragraph,
# which turns a checklist into a run-on sentence full of literal "[ ]".
TIGHT_LIST_RE = re.compile(
    r"^(?P<prev>(?!\s*[-*+]\s)(?!\s*\d+[.)]\s)(?!\s*#)(?!\s*>)(?!\s*\|)(?!\s*```)\S.*)\n"
    r"(?P<item>[-*+]\s|\d+[.)]\s)",
    re.M,
)

# The same problem one level in: a nested checklist hanging straight off its parent item,
# e.g. "5. Confirm:" followed by indented "- [ ]" lines.
TIGHT_NESTED_RE = re.compile(
    r"^(?P<prev>(?:[-*+]|\d+[.)])\s+\S.*)\n(?P<indent>[ \t]+)(?P<item>[-*+]\s|\d+[.)]\s)",
    re.M,
)


def preprocess(text: str) -> str:
    """Strip what should not print, and normalize Markdown this repo writes GitHub-style."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            text = text[end + 4 :]

    # Repeat until stable: one pass only fixes the first list in a run of them.
    for _ in range(6):
        fixed = TIGHT_LIST_RE.sub(r"\g<prev>\n\n\g<item>", text)
        fixed = TIGHT_NESTED_RE.sub(r"\g<prev>\n\n\g<indent>\g<item>", fixed)
        if fixed == text:
            break
        text = fixed

    return text.strip()


def render_tasklists(html: str) -> str:
    """python-markdown has no task-list support; the boxes print as a literal "[ ]".

    Two PREFLIGHT_CHECKLIST files are 57 items each and exist to be ticked on paper, so they
    get a real box.
    """

    # Mark the items first, wherever they sit. An item markdown considers "loose" comes back
    # as <li><p>[ ] …</p></li> rather than <li>[ ] …</li>, and matching only the tight shape
    # left those rendering as literal brackets.
    html = re.sub(r"<li>\s*(<p>\s*)?\[ \]\s*", lambda m: '<li class="todo">' + (m.group(1) or ""), html)
    html = re.sub(r"<li>\s*(<p>\s*)?\[[xX]\]\s*", lambda m: '<li class="done">' + (m.group(1) or ""), html)

    # Then style any list whose first item is one of them. Done this way round rather than by
    # matching whole <ul> blocks, which mis-scopes as soon as a list nests.
    return re.sub(r'<ul>(\s*<li class="(?:todo|done)")', r'<ul class="tasklist">\1', html)


def classify_tables(html: str) -> str:
    """Wide tables need smaller type; very wide ones need their own landscape page.

    BRIDGE_AND_LAB_DECK_SPEC.md alone carries 128 rows, 46 of them over 250 characters.
    """

    def fix(m: re.Match) -> str:
        table = m.group(0)
        header = re.search(r"<tr>.*?</tr>", table, flags=re.S)
        cols = len(re.findall(r"<t[hd][ >]", header.group(0))) if header else 0
        rows = re.findall(r"<tr>.*?</tr>", table, flags=re.S)
        widest = max((len(re.sub(r"<[^>]+>", "", r)) for r in rows), default=0)

        if cols >= 6 or widest > 420:
            table = table.replace("<table>", '<table class="xwide">', 1)
            return f'<div class="table-landscape">{table}</div>'
        if cols == 5 or widest > 260:
            return table.replace("<table>", '<table class="wide">', 1)
        return table

    return re.sub(r"<table>.*?</table>", fix, html, flags=re.S)


def classify_callouts(html: str) -> str:
    """Blockquotes are used as callouts throughout; warnings get the orange edge."""

    def fix(m: re.Match) -> str:
        bq = m.group(0)
        text = re.sub(r"<[^>]+>", "", bq).lower()
        if any(w in text for w in ("⚠", "warn", "before you", "not included", "must be built")):
            return bq.replace("<blockquote>", '<blockquote class="warn">', 1)
        return bq

    return re.sub(r"<blockquote>.*?</blockquote>", fix, html, flags=re.S)


class LinkRewriter:
    """Turns repository links into something that works inside a single PDF.

    About 95 relative links point across contributions. Every one carries an mlu-0000NN id, so
    the rewrite is mechanical. Links to documents included in the handbook become in-document
    anchors; anything else falls back to a full GitHub URL that can be typed from paper.
    """

    def __init__(self, anchors: dict[str, str]) -> None:
        self.anchors = anchors  # repo-relative path -> anchor id

    def rewrite(self, html: str, source: Path) -> str:
        def fix(m: re.Match) -> str:
            href = htmllib.unescape(m.group(1))

            if href.startswith("#"):
                return m.group(0)

            if href.startswith(("http://", "https://", "mailto:")):
                return f'<a class="spelled" href="{htmllib.escape(href)}">'

            path, _, frag = href.partition("#")
            if not path:
                return m.group(0)

            try:
                target = (source.parent / path).resolve()
                rel = str(target.relative_to(ROOT))
            except (ValueError, OSError):
                rel = None

            if rel and rel in self.anchors:
                return f'<a href="#{self.anchors[rel]}">'

            # A directory that is a contribution, or any link naming one.
            hit = re.search(r"(mlu-\d{6})", href)
            if hit and hit.group(1) in self.anchors.values():
                return f'<a href="#{hit.group(1)}">'

            if rel:
                return f'<a class="spelled" href="{REPO_URL}/blob/main/{rel}">'
            return m.group(0)

        return re.sub(r'<a href="([^"]+)">', fix, html)


def md_to_html(path: Path, rewriter: LinkRewriter, images: "ImageCache") -> str:
    text = preprocess(path.read_text(encoding="utf-8"))
    html = markdown.markdown(text, extensions=MD_EXTENSIONS)
    html = render_tasklists(html)
    html = classify_tables(html)
    html = classify_callouts(html)
    html = rewriter.rewrite(html, path)
    html = images.rewrite(html, path)
    return html


# ----------------------------------------------------------------- images


class ImageCache:
    """Resolves image paths to absolute file URLs, downsampling oversized ones.

    One screenshot in mlu-000008 is 1.3MB at a size no printed page can use.
    """

    MAX_PX = 1400

    def __init__(self, workdir: Path) -> None:
        self.dir = workdir / "img"
        self.dir.mkdir(parents=True, exist_ok=True)
        self.n = 0

    def rewrite(self, html: str, source: Path) -> str:
        def fix(m: re.Match) -> str:
            src = htmllib.unescape(m.group(1))
            if src.startswith(("http://", "https://", "data:")):
                # A remote badge cannot render offline and means nothing in print.
                return ""
            target = (source.parent / src).resolve()
            if not target.is_file():
                return ""
            return m.group(0).replace(m.group(1), self._prepare(target))

        return re.sub(r'<img [^>]*src="([^"]+)"[^>]*/?>', fix, html)

    def _prepare(self, path: Path) -> str:
        try:
            from PIL import Image

            with Image.open(path) as im:
                if max(im.size) > self.MAX_PX:
                    self.n += 1
                    out = self.dir / f"img{self.n:03d}{path.suffix}"
                    im.thumbnail((self.MAX_PX, self.MAX_PX))
                    im.convert("RGB").save(out, quality=88)
                    return out.resolve().as_uri()
        except Exception:
            pass
        return path.as_uri()


# ----------------------------------------------------------------- notebooks


def notebook_to_html(path: Path) -> str:
    """Markdown cells carry the teaching; code cells print as reference."""
    nb = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for cell in nb.get("cells", []):
        source = "".join(cell.get("source", [])).rstrip()
        if not source:
            continue
        if cell["cell_type"] == "markdown":
            out.append(markdown.markdown(preprocess(source), extensions=MD_EXTENSIONS))
        elif cell["cell_type"] == "code":
            out.append('<div class="nb-label">Code cell</div>')
            out.append(f'<pre class="nb-code"><code>{htmllib.escape(source)}</code></pre>')
    return "\n".join(out)


# ----------------------------------------------------------------- overview page


def pills(doc: dict) -> str:
    out = [f'<span class="pill gold">{doc["subtype"].replace("-", " ")}</span>']
    maturity = doc.get("maturity", "")
    out.append(f'<span class="pill blue">{maturity.replace("-", " ")}</span>')
    for key in ("difficulty", "language"):
        if doc.get(key):
            out.append(f'<span class="pill">{doc[key]}</span>')
    for tool in doc.get("tools", [])[:5]:
        out.append(f'<span class="pill">{htmllib.escape(tool)}</span>')
    return f'<div class="meta-pills">{"".join(out)}</div>'


def overview_html(doc: dict, marker: str = "") -> str:
    def listify(items) -> str:
        return "".join(f"<li>{htmllib.escape(str(i))}</li>" for i in items)

    authors = ", ".join(
        f"{a['name']}{' (' + a['institution'] + ')' if a.get('institution') else ''}"
        for a in doc["authors"]
    )
    pre = doc.get("prerequisites", {})
    use = doc.get("intended_use", {})

    rows = [
        ("Authors", htmllib.escape(authors)),
        ("Audience", htmllib.escape(", ".join(doc.get("audience", [])))),
        ("Disciplines", htmllib.escape(", ".join(doc.get("disciplines", [])))),
        ("Duration", htmllib.escape(str(doc.get("duration") or "—"))),
        ("Delivery", htmllib.escape(", ".join(doc.get("delivery_format") or []) or "—")),
        ("Tools", htmllib.escape(", ".join(doc.get("tools", [])))),
        ("Expected cost", htmllib.escape(str(pre.get("expected_cost", "—")))),
        ("Version", f"v{doc['version']} · published {doc['published']}"),
        ("Maintainer", htmllib.escape(doc["maintainer"]["name"])),
    ]
    table = "".join(f"<tr><th>{k}</th><td>{v}</td></tr>" for k, v in rows)

    parts = [
        f'<div class="doc-section" id="{doc["id"]}-overview">',
        marker,
        "<h1>Overview</h1>",
        pills(doc),
        f'<p style="font-size:11pt">{htmllib.escape(" ".join(doc["summary"].split()))}</p>',
        f'<table class="glance"><tbody>{table}</tbody></table>',
    ]

    if use.get("description"):
        parts += ["<h2>Intended use</h2>", f'<p>{htmllib.escape(use["description"])}</p>']
    if use.get("learning_outcomes"):
        parts += [
            "<h2>Learning outcomes</h2>",
            f'<ul>{listify(use["learning_outcomes"])}</ul>',
        ]

    if pre.get("knowledge") or pre.get("accounts"):
        parts.append("<h2>Before you run this</h2>")
        if pre.get("knowledge"):
            parts += ["<h3>Assumed knowledge and preparation</h3>", f'<ul>{listify(pre["knowledge"])}</ul>']
        if pre.get("accounts"):
            parts += ["<h3>Accounts needed</h3>", f'<ul>{listify(pre["accounts"])}</ul>']

    mats = [m for m in doc.get("materials", []) if not m.get("external")]
    ext = [m for m in doc.get("materials", []) if m.get("external")]
    if mats:
        rows = "".join(
            f'<tr><td style="font-family:var(--mono);font-size:8pt">{htmllib.escape(m["path"])}</td>'
            f'<td>{htmllib.escape(" ".join(m["description"].split()))}</td></tr>'
            for m in mats
        )
        parts += [
            "<h2>What is included</h2>",
            f'<table class="wide"><thead><tr><th style="width:58mm">File</th><th>What it is</th>'
            f"</tr></thead><tbody>{rows}</tbody></table>",
        ]
    if ext:
        rows = "".join(
            f'<tr><td>{htmllib.escape(" ".join(m["description"].split()))}</td>'
            f'<td style="font-family:var(--mono);font-size:7.5pt;overflow-wrap:anywhere">'
            f'{htmllib.escape(m["path"])}</td></tr>'
            for m in ext
        )
        parts += [
            "<h2>Hosted elsewhere</h2>",
            "<p>These are live or externally hosted and cannot be reproduced here. The URLs are "
            "written out so they can be typed.</p>",
            f'<table><thead><tr><th style="width:62mm">What it is</th><th>Where</th></tr></thead>'
            f"<tbody>{rows}</tbody></table>",
        ]

    dl = doc["github"].get("download_url")
    parts += [
        "<h2>Getting the digital version</h2>",
        f'<p>Browse or download this contribution at:</p>'
        f'<p style="font-family:var(--mono);font-size:9.5pt;overflow-wrap:anywhere">'
        f'{REPO_URL}/tree/main/{doc["github"]["path"]}</p>',
    ]
    if dl:
        parts.append(
            f'<p>Packaged release: <span style="font-family:var(--mono);font-size:9.5pt;'
            f'overflow-wrap:anywhere">{dl}</span></p>'
        )
    parts.append("</div>")
    return "\n".join(parts)


# ----------------------------------------------------------------- assembly


def build_html(
    docs: list[dict],
    workdir: Path,
    page_map: dict[str, int] | None,
    marked: bool = True,
) -> tuple[str, dict[str, str]]:
    """Compose the whole document.

    page_map is None on the measuring pass. marked=False omits the section markers, for
    the final render — they are an internal device and must not reach the reader.

    Returns the HTML and a map of marker tag -> section key.
    """
    images = ImageCache(workdir)
    marks: dict[str, str] = {}

    def mark(key: str, dark: bool = False) -> str:
        """Plant a locator for one section. Coloured to match its background."""
        tag = f"S{len(marks) + 1:04d}"
        marks[tag] = key
        if not marked:
            return ""
        colour = CHARCOAL if dark else "#ffffff"
        return f'<span class="secmark" style="color:{colour}">\u00a7\u00a7{tag}\u00a7\u00a7</span>'

    anchors: dict[str, str] = {}
    for doc in docs:
        anchors[doc["_dir"]] = doc["id"]
        anchors[f'{doc["_dir"]}/README.md'] = doc["id"]
        for md in doc_order(doc):
            anchors[str(md.relative_to(ROOT))] = doc_key(doc, md)
    rewriter = LinkRewriter(anchors)

    by_cat: dict[str, list[dict]] = {}
    for doc in docs:
        by_cat.setdefault(doc["category"], []).append(doc)

    parts: list[str] = []
    toc: list[str] = []
    part_no = 0

    def pg(key: str) -> str:
        if page_map is None:
            return "000"
        return str(page_map.get(key, 0))

    for cat in ("course-elements", "ml-ai-applications", "professional-student-development"):
        if cat not in by_cat:
            continue
        toc.append(f'<div class="toc-cat">{CATEGORY_INTROS[cat][0]}</div>')

        for doc in by_cat[cat]:
            part_no += 1
            did = doc["id"]
            title = htmllib.escape(doc["title"])

            parts.append(
                f'<section class="part-title" id="{did}">'
                f'<div class="kicker">Part {part_no} · {CATEGORY_INTROS[cat][0]}</div>'
                f'<div class="rule"></div>'
                f"<h1>{title}</h1>"
                f'<div class="id">{did} · v{doc["version"]} · {doc.get("maturity", "")}</div>'
                f'<p class="summary">{htmllib.escape(" ".join(doc["summary"].split()))}</p>'
                f'{mark(did, dark=True)}'
                "</section>"
            )
            toc.append(
                f'<div class="toc-part"><span>Part {part_no} &nbsp;{title}</span>'
                f'<span class="leader"></span><span class="pg">{pg(did)}</span></div>'
            )

            parts.append(overview_html(doc, mark(f"{did}-overview")))
            toc.append(
                f'<div class="toc-sub"><span>Overview</span>'
                f'<span class="leader"></span><span class="pg">{pg(did + "-overview")}</span></div>'
            )

            readme = ROOT / doc["_dir"] / "README.md"
            if readme.is_file():
                key = f"{did}-readme"
                parts.append(
                    f'<div class="doc-section" id="{key}">'
                    f'{mark(key)}'
                    f"<h1>About this contribution</h1>"
                    f"{md_to_html(readme, rewriter, images)}</div>"
                )
                toc.append(
                    f'<div class="toc-sub"><span>About this contribution</span>'
                    f'<span class="leader"></span><span class="pg">{pg(key)}</span></div>'
                )

            for md in doc_order(doc):
                key = doc_key(doc, md)
                label = doc_label(doc, md)
                body = md_to_html(md, rewriter, images)
                path_line = (
                    f'<p class="source-path">'
                    f'{htmllib.escape(str(md.relative_to(ROOT / doc["_dir"])))}</p>'
                )
                # Most of these documents open with their own title. Printing a generated
                # heading above it would stutter, so the document's own heading is left to do
                # the job and only the source path is added.
                heading = "" if body.lstrip().startswith("<h1") else f"<h1>{htmllib.escape(label)}</h1>"
                parts.append(
                    f'<div class="doc-section" id="{key}">'
                    f"{mark(key)}{path_line}{heading}{body}</div>"
                )
                toc.append(
                    f'<div class="toc-sub"><span>{htmllib.escape(label)}</span>'
                    f'<span class="leader"></span><span class="pg">{pg(key)}</span></div>'
                )

            for nb in notebooks(doc):
                key = f"{did}-nb-{slugify(nb.stem)}"
                parts.append(
                    f'<div class="doc-section" id="{key}">'
                    f'{mark(key)}'
                    f"<h1>Notebook: {htmllib.escape(nb.stem)}</h1>"
                    f'<blockquote><p><strong>This is a notebook.</strong> It is printed here so you '
                    f"can read what it teaches and see what it does, but it has to be run from the "
                    f'repository &mdash; <span style="font-family:var(--mono);font-size:8.5pt">'
                    f'{htmllib.escape(str(nb.relative_to(ROOT)))}</span></p></blockquote>'
                    f"{notebook_to_html(nb)}</div>"
                )
                toc.append(
                    f'<div class="toc-sub"><span>Notebook: {htmllib.escape(nb.stem)}</span>'
                    f'<span class="leader"></span><span class="pg">{pg(key)}</span></div>'
                )

            for i, pdf in enumerate(appendices(doc), start=1):
                key = f"{did}-app-{i}"
                label = pdf.stem.replace("-", " ").replace("_", " ")
                label = label[:1].upper() + label[1:]
                parts.append(
                    f'<div class="appendix-divider" id="{key}">'
                    f'{mark(key)}'
                    f'<div class="kicker">Part {part_no} · Appendix {i}</div>'
                    f"<h2>{htmllib.escape(label)}</h2>"
                    f'<p class="note">Reproduced from <span style="font-family:var(--mono);'
                    f'font-size:9pt">{htmllib.escape(str(pdf.relative_to(ROOT / doc["_dir"])))}</span>, '
                    f"as supplied by the contribution's authors. The pages that follow are that "
                    f"document.</p></div>"
                )
                toc.append(
                    f'<div class="toc-sub"><span>Appendix {i}: {htmllib.escape(label)}</span>'
                    f'<span class="leader"></span><span class="pg">{pg(key)}</span></div>'
                )

    sequences = load_sequences(docs)
    data_credits = []
    for doc in docs:
        for d in doc.get("licenses", {}).get("data") or []:
            data_credits.append(
                {
                    "id": doc["id"],
                    "path": d["path"],
                    "license": d["license"],
                    "source": " ".join(d["source"].split()),
                }
            )

    tmpl = Template((HANDBOOK / "handbook.html.j2").read_text(encoding="utf-8"))
    rendered = tmpl.render(
        title="AI Teaching and Learning Materials",
        blurb=(
            "Ten teaching contributions from the AWS-MLU Faculty Fellows — courses, assignments, "
            "labs, applications and facilitated sessions — reproduced in full so they can be read, "
            "printed and taught from without going online."
        ),
        css=(HANDBOOK / "style.css").read_text(encoding="utf-8"),
        mark=(HANDBOOK / "assets" / "dtcc-mark.png").as_uri(),
        count=len(docs),
        institutions=sorted({i for d in docs for i in d.get("institutions", [])}),
        cohort=docs[0].get("cohort") or "AWS-MLU Faculty Fellows",
        generated=date.today().isoformat(),
        repo_url=REPO_URL,
        sequences=sequences,
        toc_html="\n".join(toc),
        parts_html="\n".join(parts),
        docs=[
            {
                "id": d["id"],
                "title": d["title"],
                "byline": ", ".join(a["name"] for a in d["authors"]),
                "content_license": d["licenses"]["content"],
                "software_license": d["licenses"].get("software"),
            }
            for d in docs
        ],
        data_credits=data_credits,
    )
    return rendered, marks


def load_sequences(docs: list[dict]) -> list[dict]:
    """Curated collections already carry an ordered reading list with rationales."""
    titles = {d["id"]: d["title"] for d in docs}
    out = []
    for path in sorted((ROOT / "collections").glob("*.yml")):
        coll = yaml.safe_load(path.read_text(encoding="utf-8"))
        members = []
        for m in sorted(coll.get("members", []), key=lambda m: m.get("order", 0)):
            if m["id"] in titles:
                members.append(
                    {
                        "order": m.get("order", 0),
                        "id": m["id"],
                        "title": titles[m["id"]],
                        "note": " ".join((m.get("note") or "").split()),
                    }
                )
        if members:
            out.append(
                {
                    "title": coll.get("title", path.stem),
                    "summary": " ".join(coll.get("summary", "").split()),
                    "members": members,
                }
            )
    return out


# ----------------------------------------------------------------- rendering


def render_pdf(html_path: Path, out_pdf: Path, chrome: str, timeout: int = 600) -> None:
    """Render with headless Chrome.

    Chrome writes the PDF and then frequently does not exit — a long-standing headless quirk
    that has nothing to do with whether the render succeeded. So rather than waiting on the
    process, watch for the output file to appear and stop growing, then stop Chrome ourselves.
    """
    out_pdf.unlink(missing_ok=True)

    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--no-first-run",
            "--no-pdf-header-footer",
            "--allow-file-access-from-files",
            "--virtual-time-budget=60000",
            f"--user-data-dir={profile}",
            f"--print-to-pdf={out_pdf}",
            html_path.as_uri(),
        ]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        deadline = time.monotonic() + timeout
        stable, last_size = 0, -1
        try:
            while time.monotonic() < deadline:
                if proc.poll() is not None:
                    break
                size = out_pdf.stat().st_size if out_pdf.is_file() else -1
                # Two consecutive quiet checks on a non-empty file means the write finished.
                stable = stable + 1 if size == last_size and size > 0 else 0
                last_size = size
                if stable >= 2:
                    break
                time.sleep(1.0)
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
    """Locate each section by the marker planted in the HTML.

    Prefers poppler's pdftotext, which reliably sees small text that pypdf's own extractor
    intermittently misses; falls back to pypdf where poppler is not installed. Both results
    are merged, so a page either tool can read is a page we can locate.
    """
    found: dict[str, int] = {}

    if shutil.which("pdftotext"):
        try:
            proc = subprocess.run(
                ["pdftotext", "-q", str(pdf), "-"],
                capture_output=True,
                text=True,
                timeout=300,
            )
            # pdftotext separates pages with a form feed.
            for n, page_text in enumerate(proc.stdout.split("\f"), start=1):
                for key in MARK_RE.findall(page_text):
                    found.setdefault(key, n)
        except (subprocess.SubprocessError, OSError):
            pass

    reader = PdfReader(str(pdf))
    for n, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            continue
        for key in MARK_RE.findall(text):
            found.setdefault(key, n)

    return found


def splice_appendices(body: Path, docs: list[dict], marks: dict[str, int], out: Path) -> dict[str, int]:
    """Insert each appendix PDF immediately after its divider page.

    Returns the final page number of every marked section, after insertion.
    """
    reader = PdfReader(str(body))
    inserts: dict[int, list[Path]] = {}
    for doc in docs:
        for i, pdf in enumerate(appendices(doc), start=1):
            page = marks.get(f'{doc["id"]}-app-{i}')
            if page:
                inserts.setdefault(page, []).append(pdf)

    # Clone rather than re-add: the body pages share font and image objects, and adding them
    # one at a time copies those into every page.
    writer = PdfWriter(clone_from=str(body))
    shift: dict[int, int] = {}  # original page -> final page
    offset = 0
    for n in range(1, len(reader.pages) + 1):
        shift[n] = n + offset
        for pdf in inserts.get(n, []):
            extra = PdfReader(str(pdf))
            for j, p in enumerate(extra.pages):
                writer.insert_page(p, index=n + offset + j)
            offset += len(extra.pages)

    with out.open("wb") as fh:
        writer.write(fh)

    return {key: shift.get(page, page) for key, page in marks.items()}


def stamp(pdf_in: Path, pdf_out: Path, titles: dict[int, str], total: int,
          skip: set[int] | None = None) -> None:
    """Chrome has no CSS margin boxes, so running furniture is overlaid afterwards.

    The overlay is built as one multi-page document rather than one file per page, so the
    fonts and graphics state are shared instead of re-embedded 500 times. Merging also
    decompresses the page content stream, so each page is recompressed afterwards — without
    that the document comes out roughly six times larger than it needs to be.
    """
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
        c.drawString(52, y, "DTCC-MLU Faculty Handbook")

        running = titles.get(n, "")
        if running:
            c.drawCentredString(width / 2, y, running[:62])

        c.setFont("Helvetica-Bold", 8.5)
        c.setFillColor(HexColor(CHARCOAL))
        c.drawRightString(width - 52, y, f"{n} / {total}")
        c.showPage()
    c.save()

    overlay = PdfReader(str(overlay_path))

    # Clone the whole document rather than re-adding pages one at a time. Chrome's pages share
    # their font and image objects; adding them individually makes pypdf copy those shared
    # resources into every page, which inflates the file about sixfold.
    writer = PdfWriter(clone_from=str(pdf_in))

    for n, page in enumerate(writer.pages, start=1):
        # The cover and the part-title pages are full-bleed charcoal. Dark page numbers on a
        # near-black background would be invisible, so those pages carry no furniture.
        if n != 1 and n not in (skip or set()) and n - 1 < len(overlay.pages):
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


def add_outline(pdf: Path, docs: list[dict], pages: dict[str, int]) -> None:
    """A 500-page document needs real bookmarks more than it needs a contents page."""
    writer = PdfWriter(clone_from=str(pdf))
    last = len(writer.pages)

    def at(key: str) -> int:
        return max(0, min(pages.get(key, 1), last) - 1)

    for doc in docs:
        did = doc["id"]
        parent = writer.add_outline_item(f'{did} · {doc["title"]}', at(did))
        writer.add_outline_item("Overview", at(f"{did}-overview"), parent=parent)
        if f"{did}-readme" in pages:
            writer.add_outline_item("About this contribution", at(f"{did}-readme"), parent=parent)
        for md in doc_order(doc):
            key = doc_key(doc, md)
            if key in pages:
                writer.add_outline_item(doc_label(doc, md), at(key), parent=parent)
        for nb in notebooks(doc):
            key = f"{did}-nb-{slugify(nb.stem)}"
            if key in pages:
                writer.add_outline_item(f"Notebook: {nb.stem}", at(key), parent=parent)
        for i, ap in enumerate(appendices(doc), start=1):
            key = f"{did}-app-{i}"
            if key in pages:
                writer.add_outline_item(f"Appendix {i}: {ap.stem}", at(key), parent=parent)

    try:
        writer.compress_identical_objects()
    except Exception:
        pass

    with pdf.open("wb") as fh:
        writer.write(fh)


def running_titles(docs: list[dict], pages: dict[str, int], total: int) -> dict[int, str]:
    starts = sorted(
        ((pages[d["id"]], d["title"]) for d in docs if d["id"] in pages),
        key=lambda t: t[0],
    )
    out: dict[int, str] = {}
    for i, (start, title) in enumerate(starts):
        end = starts[i + 1][0] - 1 if i + 1 < len(starts) else total
        for n in range(start, end + 1):
            out[n] = title
    return out


# ----------------------------------------------------------------- main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="dist", help="output directory (default: dist)")
    ap.add_argument("--skip-appendices", action="store_true", help="omit merged source PDFs")
    ap.add_argument("--keep-html", action="store_true", help="keep the intermediate HTML")
    args = ap.parse_args()

    chrome = chrome_binary()
    docs = load()
    if not docs:
        sys.exit("error: no contributions found.")

    outdir = ROOT / args.out
    outdir.mkdir(parents=True, exist_ok=True)
    work = outdir / ".handbook-build"
    work.mkdir(exist_ok=True)

    print(f"Building handbook from {len(docs)} contributions…")

    def locate(pdf: Path, index: dict[str, str]) -> dict[str, int]:
        """Marker tag pages -> section key pages."""
        by_tag = find_marks(pdf)
        missing = [k for t, k in index.items() if t not in by_tag]
        if missing:
            print(f"    warning: {len(missing)} section(s) not located, e.g. {missing[:3]}")
        return {index[t]: p for t, p in by_tag.items() if t in index}

    # Pass 1 — measure where everything lands.
    print("  pass 1: measuring…")
    html, index = build_html(docs, work, None)
    (work / "pass1.html").write_text(html, encoding="utf-8")
    render_pdf(work / "pass1.html", work / "pass1.pdf", chrome)
    marks = locate(work / "pass1.pdf", index)
    body_pages = len(PdfReader(str(work / "pass1.pdf")).pages)
    print(f"    {body_pages} body pages, {len(marks)}/{len(index)} sections located")

    if args.skip_appendices:
        final_pages = marks
    else:
        spliced = work / "pass1-merged.pdf"
        final_pages = splice_appendices(work / "pass1.pdf", docs, marks, spliced)
        print(f"    {len(PdfReader(str(spliced)).pages)} pages with appendices merged")

    # Pass 2 — re-render so the contents page carries real page numbers, and re-locate, since
    # setting them can nudge the layout.
    print("  pass 2: paginating…")
    html, index = build_html(docs, work, final_pages)
    (work / "pass2.html").write_text(html, encoding="utf-8")
    render_pdf(work / "pass2.html", work / "pass2.pdf", chrome)
    marks2 = locate(work / "pass2.pdf", index)

    # Pass 3 — the same document with the markers stripped, so none of that internal
    # bookkeeping reaches the reader's text selection or search. Its layout must match pass 2;
    # if it does not, fall back rather than ship a document whose page numbers lie.
    print("  pass 3: final render…")
    html, _ = build_html(docs, work, final_pages, marked=False)
    (work / "pass3.html").write_text(html, encoding="utf-8")
    render_pdf(work / "pass3.html", work / "pass3.pdf", chrome)

    body = work / "pass3.pdf"
    if len(PdfReader(str(body)).pages) != len(PdfReader(str(work / "pass2.pdf")).pages):
        print("    warning: marker-free render changed pagination; keeping the marked render")
        body = work / "pass2.pdf"

    if args.skip_appendices:
        merged, pages = body, marks2
    else:
        merged = work / "merged.pdf"
        pages = splice_appendices(body, docs, marks2, merged)

    total = len(PdfReader(str(merged)).pages)
    stamped = work / "stamped.pdf"
    dark_pages = {pages[d["id"]] for d in docs if d["id"] in pages}
    stamp(merged, stamped, running_titles(docs, pages, total), total, skip=dark_pages)

    version = date.today().strftime("%Y.%m")
    final = outdir / f"dtcc-mlu-handbook-{version}.pdf"
    shutil.copy(stamped, final)
    add_outline(final, docs, pages)

    if not args.keep_html:
        shutil.rmtree(work, ignore_errors=True)

    mb = final.stat().st_size / (1024 * 1024)
    print(f"\n  {final.relative_to(ROOT)}")
    print(f"  {total} pages · {mb:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
