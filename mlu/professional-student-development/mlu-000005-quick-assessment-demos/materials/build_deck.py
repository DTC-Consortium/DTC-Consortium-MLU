#!/usr/bin/env python3
"""Build the Session 2 deck — "The Assignment Lifecycle" — on the AWS MLU template.

The deck is built directly on the MLU Agentic AI Essentials (No Code) deck, so its
masters, layouts, gradient title rule, section dividers, and footer mark are the
template's own, not imitations. Every slide from the template is removed first;
only its design is kept.

Usage:
    python3 build_deck.py [--template PATH]
    ./export_pdf.sh          # PDF via PowerPoint, which has the template's Aptos fonts

Writes assessment-lifecycle-deck.pptx next to this script.
"""

import copy
import re
import sys
from pathlib import Path

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, PP_PLACEHOLDER
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

from session_config import DRIVE_SHORTLINK, DRIVE_URL

HERE = Path(__file__).resolve().parent
DEFAULT_TEMPLATE = (Path.home() / "dev/2026/mlu/aws-mlu-eep-agentic-ai"
                    / "Administrator Workshop - Building with Agentic AI (No Code)"
                    / "AgenticAI-Essentials-NoCode.pptx")
OUT = HERE / "assessment-lifecycle-deck.pptx"
QR_PNG = HERE / "assets" / "drive-qr.png"

# Colours sampled from the template's slides and theme.
INK = RGBColor(0x23, 0x2F, 0x3E)     # body text
MUTED = RGBColor(0x5F, 0x6B, 0x7A)   # captions
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
NAVY = RGBColor(0x0E, 0x28, 0x41)    # theme dk2 — the template's dark callout boxes
TEAL = RGBColor(0x15, 0x60, 0x82)    # theme accent1 — the template's bold emphasis colour
SKY = RGBColor(0x8A, 0xCF, 0xF0)     # emphasis on navy
ROW = RGBColor(0xF4, 0xF6, 0xF8)
GREEN = RGBColor(0x18, 0x80, 0x38)
AMBER = RGBColor(0xB4, 0x59, 0x08)
RED = RGBColor(0xC0, 0x00, 0x00)

A = "http://schemas.openxmlformats.org/drawingml/2006/main"
# The template's card border: orange → magenta → blue radial gradient, 2.75 pt.
GRADIENT_STOPS = ('<a:gsLst><a:gs pos="0"><a:srgbClr val="F66C02"/></a:gs>'
                  '<a:gs pos="53000"><a:srgbClr val="FF28EF"/></a:gs>'
                  '<a:gs pos="100000"><a:srgbClr val="0F65F9"/></a:gs></a:gsLst>')
CARD_LINE = (f'<a:ln xmlns:a="{A}" w="34925" cap="flat" cmpd="sng" algn="ctr">'
             f'<a:gradFill flip="none" rotWithShape="1">{GRADIENT_STOPS}'
             '<a:path path="circle"><a:fillToRect t="100000" r="100000"/></a:path>'
             '<a:tileRect l="-100000" b="-100000"/></a:gradFill>'
             '<a:prstDash val="solid"/><a:miter lim="800000"/></a:ln>')
PILL_FILL = (f'<a:gradFill xmlns:a="{A}" rotWithShape="1">{GRADIENT_STOPS}'
             '<a:lin ang="0" scaled="1"/></a:gradFill>')
SHADOW = (f'<a:effectLst xmlns:a="{A}"><a:outerShdw blurRad="50800" dist="38100" '
          'dir="2700000" algn="tl" rotWithShape="0"><a:prstClr val="black">'
          '<a:alpha val="40000"/></a:prstClr></a:outerShdw></a:effectLst>')

LEFT, CENTER = PP_ALIGN.LEFT, PP_ALIGN.CENTER
TOP, MIDDLE = MSO_ANCHOR.TOP, MSO_ANCHOR.MIDDLE


# --------------------------------------------------------------------------- #
# Template plumbing                                                            #
# --------------------------------------------------------------------------- #

def capture(prs, slide_index, shape_name):
    """Copy a shape (and the parts it references) off a template slide."""
    slide = prs.slides[slide_index]
    shape = next(s for s in slide.shapes if s.name == shape_name)
    el = copy.deepcopy(shape._element)
    rels = {}
    for node in el.iter():
        for attr in (qn("r:embed"), qn("r:link"), qn("r:id")):
            rid = node.get(attr)
            if rid and rid not in rels:
                rel = slide.part.rels[rid]
                rels[rid] = (rel.reltype, rel.target_part)
    return el, rels


def _insert(slide, el):
    tree = slide.shapes._spTree
    next_id = max([int(c.get("id")) for c in tree.iter(qn("p:cNvPr"))] + [1]) + 1
    tree.insert_element_before(el, "p:extLst")
    for c in el.iter(qn("p:cNvPr")):
        c.set("id", str(next_id))
        next_id += 1


def paste(slide, captured):
    el, rels = captured
    el = copy.deepcopy(el)
    mapping = {old: slide.part.relate_to(part, reltype) for old, (reltype, part) in rels.items()}
    for node in el.iter():
        for attr in (qn("r:embed"), qn("r:link"), qn("r:id")):
            if node.get(attr) in mapping:
                node.set(attr, mapping[node.get(attr)])
    _insert(slide, el)


def add_slide_number(slide):
    for ph in slide.slide_layout.placeholders:
        if ph.placeholder_format.type == PP_PLACEHOLDER.SLIDE_NUMBER:
            _insert(slide, copy.deepcopy(ph._element))
            return


def qr_png() -> Path:
    """Render the shared-folder QR to assets/, regenerating it whenever the URL changes.

    Error correction M, not H. H sounds safer but packs in far more modules, and at the size
    this sits on a slide the modules are already near the limit of what a phone resolves across
    a lecture hall. Fewer, bigger modules scan from further away, which is the failure that
    actually happens. M still tolerates a projector washing out or a fold across a printed card.

    A 4-module quiet zone is what keeps it scannable on the dark cover and divider slides: the
    white margin is the border, so no backing shape is needed.
    """
    import qrcode
    QR_PNG.parent.mkdir(exist_ok=True)
    stamp = QR_PNG.with_suffix(".url")
    if QR_PNG.exists() and stamp.exists() and stamp.read_text().strip() == DRIVE_URL:
        return QR_PNG
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=4)
    qr.add_data(DRIVE_URL)
    qr.make(fit=True)
    qr.make_image(fill_color="black", back_color="white").save(QR_PNG)
    stamp.write_text(DRIVE_URL + "\n")
    return QR_PNG


def add_qr(slide, x=1.12, y=6.55, size=0.85):
    """Stamp the shared-folder code on a slide.

    Deliberately silent — no caption, no label, no "scan me". The 28 slides this lands on are
    legal-approved and the standing permission is that copy may be removed from them, never
    added. A graphic adds no words, so the approved text stays provably intact; verify_deck.py
    still passes. Slide 0 carries all the explanation, and the facilitator says it out loud.
    """
    slide.shapes.add_picture(str(qr_png()), Inches(x), Inches(y), Inches(size), Inches(size))


def drop_placeholder(slide, idx):
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == idx:
            ph._element.getparent().remove(ph._element)
            return


# --------------------------------------------------------------------------- #
# Text                                                                         #
# --------------------------------------------------------------------------- #

TOKEN = re.compile(r"(\*\*.+?\*\*|\*[^*]+?\*)")


def _runs(p, text, size, color, bold, italic, emph):
    """`**x**` → bold in the emphasis colour (the template's convention); `*x*` → italic."""
    for part in TOKEN.split(text):
        if not part:
            continue
        r = p.add_run()
        if part.startswith("**"):
            r.text, r.font.bold = part[2:-2], True
            r.font.color.rgb = emph
        elif part.startswith("*"):
            r.text, r.font.italic, r.font.bold = part[1:-1], True, bold
            if color is not None:
                r.font.color.rgb = color
        else:
            r.text = part
            if bold:
                r.font.bold = True
            if italic:
                r.font.italic = True
            if color is not None:
                r.font.color.rgb = color
        if size:
            r.font.size = Pt(size)


def _bullet(p, on):
    pPr = p._p.get_or_add_pPr()
    for tag in ("a:buNone", "a:buChar", "a:buAutoNum", "a:buFont"):
        for old in pPr.findall(qn(tag)):
            pPr.remove(old)
    if on:
        pPr.set("marL", "342900")
        pPr.set("indent", "-342900")
        font = etree.SubElement(pPr, qn("a:buFont"))
        font.set("typeface", "Arial")
        etree.SubElement(pPr, qn("a:buChar")).set("char", "•")
    else:
        etree.SubElement(pPr, qn("a:buNone"))


def write(tf, paras, **defaults):
    """Write paragraphs into a text frame. Each para is a str or a dict of overrides."""
    tf.clear()
    tf.word_wrap = True
    for i, para in enumerate(paras):
        o = dict(defaults)
        if isinstance(para, dict):
            o.update(para)
            text = o.pop("text")
        else:
            text = para
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        if "align" in o:
            p.alignment = o["align"]
        if "space_after" in o:
            p.space_after = Pt(o["space_after"])
        if "space_before" in o:
            p.space_before = Pt(o["space_before"])
        if not o.get("keep_bullets"):
            _bullet(p, o.get("bullet", False))
        _runs(p, text, o.get("size"), o.get("color", INK), o.get("bold", False),
              o.get("italic", False), o.get("emph", TEAL))


def fill_placeholder(slide, idx, paras, **kw):
    kw.setdefault("color", None)          # inherit the template's colour
    kw.setdefault("keep_bullets", True)   # and its bullets
    write(slide.placeholders[idx].text_frame, paras, **kw)


def textbox(slide, x, y, w, h, paras, anchor=TOP, **kw):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.vertical_anchor = anchor
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, Inches(0.05))
    write(tf, paras, **kw)
    return tb


# --------------------------------------------------------------------------- #
# Shapes — each one matches a component in the template                        #
# --------------------------------------------------------------------------- #

def _shape(slide, kind, x, y, w, h):
    sh = slide.shapes.add_shape(kind, Inches(x), Inches(y), Inches(w), Inches(h))
    style = sh._element.find(qn("p:style"))
    if style is not None:
        sh._element.remove(style)
    return sh


def _append_spPr(sh, xml):
    spPr = sh._element.spPr
    el = etree.fromstring(xml)
    for old in spPr.findall(el.tag):
        spPr.remove(old)
    effect = spPr.find(qn("a:effectLst"))
    if el.tag != qn("a:effectLst") and effect is not None:
        effect.addprevious(el)
    else:
        spPr.append(el)


def _frame(sh, pad, anchor):
    tf = sh.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Inches(pad)
    tf.margin_top = tf.margin_bottom = Inches(pad * 0.7)
    return tf


def card(slide, x, y, w, h, heading=None, paras=(), size=18, head_size=22,
         align=LEFT, anchor=TOP, pad=0.3, **kw):
    """White rounded card with the template's gradient border and shadow."""
    sh = _shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    sh.adjustments[0] = 0.12
    sh.fill.solid()
    sh.fill.fore_color.rgb = WHITE
    _append_spPr(sh, CARD_LINE)
    _append_spPr(sh, SHADOW)
    body = [{"text": heading, "italic": True, "align": CENTER, "size": head_size,
             "space_after": 10, "bullet": False}] if heading else []
    body += [p if isinstance(p, dict) else {"text": p} for p in paras]
    write(_frame(sh, pad, anchor), body, size=size, align=align, space_after=8, **kw)
    return sh


def navy(slide, x, y, w, h, paras, size=18, align=CENTER, anchor=MIDDLE, bold=True, pad=0.3):
    """Dark navy callout box, as in the template's example slides."""
    sh = _shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    sh.adjustments[0] = 0.18
    sh.fill.solid()
    sh.fill.fore_color.rgb = NAVY
    sh.line.fill.background()
    _append_spPr(sh, SHADOW)
    write(_frame(sh, pad, anchor), paras, size=size, color=WHITE, bold=bold,
          align=align, emph=SKY, space_after=6)
    return sh


def pill(slide, text, x=10.05, y=6.93, w=2.2, h=0.4):
    """Time badge, bottom right beside the slide number, in the card gradient."""
    sh = _shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    sh.adjustments[0] = 0.5
    sh.line.fill.background()
    spPr = sh._element.spPr
    for tag in ("a:solidFill", "a:noFill", "a:gradFill"):
        for old in spPr.findall(qn(tag)):
            spPr.remove(old)
    spPr.find(qn("a:prstGeom")).addnext(etree.fromstring(PILL_FILL))
    write(_frame(sh, 0.08, MIDDLE), [text], size=13, color=WHITE, bold=True, align=CENTER)


def chip(slide, text, color, x, y, w=1.75, h=0.46):
    sh = _shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h)
    sh.adjustments[0] = 0.5
    sh.fill.solid()
    sh.fill.fore_color.rgb = color
    sh.line.fill.background()
    write(_frame(sh, 0.06, MIDDLE), [text], size=14, color=WHITE, bold=True, align=CENTER)


def arrow(slide, x, y, w=0.36, h=0.46):
    sh = _shape(slide, MSO_SHAPE.RIGHT_ARROW, x, y, w, h)
    sh.fill.solid()
    sh.fill.fore_color.rgb = TEAL
    sh.line.fill.background()


def steps(slide, x, y, w, items, row_h=0.78, gap=0.2, size=18):
    """The template's chevron step list: teal down-chevrons beside outlined rows."""
    for i, text in enumerate(items):
        top = y + i * (row_h + gap)
        vis_w, vis_h = 0.72, row_h + gap + 0.12
        cx, cy = x + vis_w / 2, top - 0.06 + vis_h / 2
        ch = _shape(slide, MSO_SHAPE.CHEVRON, cx - vis_h / 2, cy - vis_w / 2, vis_h, vis_w)
        ch.rotation = 90
        ch.fill.solid()
        ch.fill.fore_color.rgb = TEAL
        ch.line.fill.background()
        box = _shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x + 0.68, top, w - 0.68, row_h)
        box.adjustments[0] = 0.16
        box.fill.solid()
        box.fill.fore_color.rgb = WHITE
        box.line.color.rgb = TEAL
        box.line.width = Pt(1.5)
        write(_frame(box, 0.22, MIDDLE), [text], size=size, color=INK, align=LEFT)


def table(slide, x, y, col_w, header, rows, size=16, row_h=0.62):
    shape = slide.shapes.add_table(len(rows) + 1, len(header), Inches(x), Inches(y),
                                   Inches(sum(col_w)), Inches(row_h * (len(rows) + 1)))
    tbl = shape.table
    for j, cw in enumerate(col_w):
        tbl.columns[j].width = Inches(cw)
    for i, cells in enumerate([header] + rows):
        tbl.rows[i].height = Inches(row_h)
        for j, text in enumerate(cells):
            cell = tbl.cell(i, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = TEAL if i == 0 else (WHITE if i % 2 else ROW)
            cell.margin_left = cell.margin_right = Inches(0.14)
            cell.vertical_anchor = MIDDLE
            write(cell.text_frame, [text], size=size, color=WHITE if i == 0 else INK,
                  bold=(i == 0), emph=WHITE if i == 0 else TEAL)


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


# --------------------------------------------------------------------------- #
# The deck                                                                     #
# --------------------------------------------------------------------------- #

def build(template):
    prs = Presentation(str(template))
    mark = capture(prs, 5, "Group 8")        # book + laptop footer mark
    brain = capture(prs, 3, "Graphic 250")   # agenda-slide icon

    ids = prs.slides._sldIdLst
    for sld in list(ids):
        prs.part.drop_rel(sld.rId)
        ids.remove(sld)

    layouts = {l.name: l for l in prs.slide_masters[1].slide_layouts}
    final = next(l for l in prs.slide_masters[0].slide_layouts if l.name == "Final")

    def content(title, layout="Title Only"):
        s = prs.slides.add_slide(layouts[layout])
        fill_placeholder(s, 1, [title])
        paste(s, mark)
        add_slide_number(s)
        return s

    def divider(title, subtitle):
        s = prs.slides.add_slide(layouts["Quote slide"])
        fill_placeholder(s, 1, [title], bold=True)
        fill_placeholder(s, 2, [subtitle], italic=True)
        return s

    # 0 ─ The shared folder. Added after legal approval, and numbered 0 on purpose: the deck is
    # cross-referenced by slide number all through the talk track, the handout and the take-home
    # pack ("slide 13", "slide 21", "slide 27"). Inserting a slide 1 would silently shift all 28
    # and break every one of those references. firstSlideNum below makes the cover slide 1 again.
    s = content("Everything you need is in this folder")
    add_qr(s, x=1.35, y=1.85, size=3.05)
    caption = [{"text": "Scan it now. You'll need it three times today.", "align": CENTER}]
    # A typable link matters more than it looks: the back row, a phone with no camera access,
    # and anyone joining remotely all need one. It appears only once DRIVE_SHORTLINK is a real
    # redirect — an unfilled placeholder projected on a wall is worse than no line at all.
    if "FILL IN" not in DRIVE_SHORTLINK:
        caption.append({"text": DRIVE_SHORTLINK, "align": CENTER, "italic": False,
                        "bold": True, "color": TEAL, "space_before": 6})
    textbox(s, 0.75, 5.05, 4.25, 0.85, caption, size=17, italic=True, color=MUTED)
    card(s, 5.75, 1.6, 6.85, 4.15, "What's inside", [
        "**Three build files** — you build each tool yourself, from these",
        "**The sample pack** — one assignment, two rubrics, five students",
        "**The course reading** — what “correct” is judged against",
        "**This deck**, and the take-home pack",
        {"text": "Nothing is pre-installed. Nothing is pre-built. That is the point — "
                 "you leave with tools you know how to make again.",
         "size": 16, "color": MUTED, "italic": True, "space_before": 14, "bullet": False},
    ], size=19, head_size=23, bullet=True, anchor=MIDDLE)
    # The sign-up link the Know Before You Go sent everyone, in full, with its campaign
    # parameter intact. Most people will tap it from the START HERE doc in the folder rather
    # than type it, but it has to be on screen for the ones who never opened that email.
    navy(s, 1.6, 5.98, 10.15, 0.95,
         [{"text": "Not set up on Amazon Quick yet? It's free — and a volunteer will "
                   "help you.", "align": CENTER},
          {"text": "**quick.aws.com/sn?utm_campaign=mlu2026**", "align": CENTER,
           "space_before": 4}],
         size=17, bold=False)
    notes(s, "Put this up before you say anything and leave it up while people settle. Tell them "
             "to scan it now — everything today comes out of this folder, and nobody is signed "
             "into anything yet. The same code is in the bottom-left corner of every slide from "
             "here on, so latecomers can pick it up at any point. Read the short link aloud for "
             "anyone who can't scan. This slide is numbered 0: the deck was approved at 28 "
             "slides and every cross-reference still points at the right one.")

    # 1 ─ Cover
    s = prs.slides.add_slide(layouts["Title Slide"])
    fill_placeholder(s, 1, ["The Assignment Lifecycle:", "AI from Rubric to Feedback"])
    fill_placeholder(s, 2, ["Four no-code tools, one assignment"])
    fill_placeholder(s, 98, [{"text": "Session 2 · Amazon Quick + Kiro", "italic": True},
                             "Tariq Hook · Delaware State University"])
    byline = s.placeholders[98]   # the template's position, widened so the name fits on one line
    byline.left, byline.top, byline.width, byline.height = (Inches(0.44), Inches(5.19),
                                                            Inches(9.2), Inches(1.19))
    notes(s, "Welcome. Ninety minutes, four tools, one assignment. Everything you'll see runs on "
             "synthetic student work, and by the end you'll have used two of the tools on your own "
             "course.")

    # 2 ─ Sign in + the hook
    s = content("Get signed in — and start grading")
    # Two ways in, and attendees have had both: an invitation email, and the quick.aws.com/sn
    # link in the Know Before You Go telling them to set Quick up themselves. The approved step
    # covers the email; slide 0 carries the self-signup link for anyone who never opened it.
    steps(s, 0.6, 1.6, 7.4, [
        "**Open** your Amazon Quick invitation email and follow the sign-in link",
        "**Sign in**, and set a password if it asks",
        "**Stuck?** Raise your hand. A volunteer will come to you.",
    ])
    # Nothing is printed and nothing is on the tables any more: the paper and the rubric are
    # both in the follow-along document, which is already open on every laptop. "On your table"
    # and "on the handout" would send the room looking for paper that does not exist. Deleted,
    # not reworded — the sentences still stand without them.
    card(s, 8.45, 1.6, 4.45, 3.95, "While you wait", [
        "Grade the paper.",
        "Use **only** the rubric.",
        "Three minutes. Write down a score and a letter.",
        "You don't need to know computer science.",
    ], bullet=True)
    pill(s, "0:00 – 0:12")
    notes(s, "Volunteers are circulating. While the room signs in, everyone grades Marcus's paper "
             "using only the rubric on the handout. Hard stop at 12 minutes — anyone still stuck "
             "pairs with a neighbor.")

    # 3 ─ Agenda
    s = prs.slides.add_slide(layouts["Topic Introduction"])
    fill_placeholder(s, 1, ["Today’s session"])
    drop_placeholder(s, 2)
    fill_placeholder(s, 3, [
        "Sign in, and grade a paper",
        "The Rubric Builder — **hands-on**",
        "The AI-Proofing Assistant — **hands-on**",
        "The Grading Assistant, built in Kiro",
        "Pre-Assessment Triage — **hands-on**",
        "Wrap-up: what you leave with",
    ], emph=TEAL)
    paste(s, brain)
    add_slide_number(s)
    notes(s, "Three of the four segments are hands-on. The Kiro segment is a demo — you watch the "
             "spec get reviewed, then the grader run.")

    # 4 ─ The vote
    s = content("What grade did you give Marcus?")
    # Four letters, not five: the approved deck has no D card. The talk track polls A/B/C/F
    # only — see DECK-APPROVAL.md. Do not add a D here without clearing it first.
    for i, letter in enumerate("ABCF"):
        card(s, 1.82 + i * 2.5, 1.95, 2.2, 2.5, None,
             [{"text": letter, "size": 88, "bold": True, "align": CENTER}], anchor=MIDDLE)
    textbox(s, 1.0, 5.05, 11.3, 0.8,
            ["Hands up. Then hold that number — we'll come back to it."],
            size=22, italic=True, color=MUTED, align=CENTER)
    notes(s, "A poll, not a quiz. Count hands for each letter and say the result out loud; a "
             "volunteer writes the tally down — you need it on slide 11. Most rooms land on B. "
             "Reveal nothing: if a CS faculty member spots the errors, ask them to hold it for "
             "slide 12.")

    # 5 ─ The lifecycle
    s = content("One assignment, four tools")
    nb = "‑"   # non-breaking hyphen, so names never split at the hyphen
    tools = [("Rubric Builder", "Build the rubric", "Amazon Quick"),
             (f"AI{nb}Proofing Assistant", "Harden the assignment", "Amazon Quick"),
             ("Grading Assistant", "Grade against the rubric", "Kiro"),
             (f"Pre{nb}Assessment Triage", f"Students self{nb}check first", "Amazon Quick")]
    for i, (name, verb, tool) in enumerate(tools):
        x = 0.5 + i * 3.18
        card(s, x, 1.7, 2.8, 3.25, name, [
            {"text": f"**{verb}**", "align": CENTER, "size": 18},
            {"text": tool, "align": CENTER, "color": MUTED, "size": 16},
        ], head_size=19, anchor=MIDDLE, pad=0.18)
        if i < 3:
            arrow(s, x + 2.84, 3.1, w=0.3)
    navy(s, 1.65, 5.4, 10.0, 0.9,
         ["The rubric the first tool builds is the rubric the other three use."], size=20)
    notes(s, "Build the rubric, harden the assignment, grade against it, and let students "
             "self-check before they submit. The same assignment and the same rubric run through "
             "all four.")

    # 6 ─ The assignment
    s = content("The assignment we'll follow")
    textbox(s, 0.55, 1.5, 7.5, 5.2, [
        {"text": "*Choose the Right Structure* — Intro to Data Structures", "size": 22,
         "bold": True, "space_after": 10},
        {"text": "Pick an operation a real program does over and over. Argue which data "
                 "structure fits it best.", "space_after": 12},
        {"text": "State a thesis: the operation and the structure", "bullet": True},
        {"text": "Give **running times**, and say which kind of guarantee each is", "bullet": True},
        {"text": "Ground it in **one concrete scenario**", "bullet": True},
        {"text": "Name where your choice is **the worse one**", "bullet": True},
        {"text": "Cite the **course reading**", "bullet": True},
    ], size=19, space_after=6)
    card(s, 8.45, 1.6, 4.45, 4.1, "Learning objectives", [
        "**LO1** Choose a structure and justify it",
        "**LO2** State running-time guarantees correctly",
        "**LO3** Support claims with evidence",
        "**LO4** Communicate clearly",
    ])
    textbox(s, 8.45, 5.85, 4.45, 0.8, ["Not a CS person? You don't need to be. "
                                       "Watch what the tools do with it."],
            size=15, italic=True, color=MUTED)
    notes(s, "A sophomore data-structures paper. Most of you aren't CS faculty, and that's the "
             "point: watch what the rubric makes visible to a grader who isn't an expert.")

    # 7 ─ The students
    s = content("Meet the five students")
    students = [("Aisha Rahman", "Strong. Correct analysis, a real scenario, honest trade-offs."),
                ("Marcus Lee", "Fluent, confident."),
                ("Priya Chandra", "A reflection on the class, **not an analysis**."),
                ("Leila Haddad", "An **unfinished draft** with two [TODO]s left in."),
                ("Diego Alvarez", "**Submitted nothing.**")]
    for i, (name, line) in enumerate(students):
        card(s, 0.5 + i * 2.5, 1.9, 2.3, 2.7, name, [{"text": line, "align": CENTER}],
             size=17, head_size=19, pad=0.2, anchor=MIDDLE)
    textbox(s, 1.0, 5.1, 11.3, 0.7, ["All five are synthetic. No real student work is used "
                                      "anywhere in this session."],
            size=18, italic=True, color=MUTED, align=CENTER)
    notes(s, "Each student is here to test one thing. Aisha is the control. Marcus is the fluent, "
             "wrong paper. Priya is the reflection. Leila is the draft that shows what Partial "
             "looks like. Diego tests whether the grader notices someone who submitted nothing.")

    # 8 ─ Divider: Rubric Builder
    s = divider("The Rubric Builder", "From assignment prompt to grading‑ready rubric")
    notes(s, "Demo A. Six minutes of demo, then twelve minutes on your own assignment.")

    # 9 ─ The weak rubric
    s = content("A tool is only as good as its rubric")
    card(s, 0.6, 1.6, 5.4, 3.75, "The rubric you graded with", [
        "Content — **40**", "Organization — **30**", "Writing mechanics — **20**",
        "Length & formatting — **10**",
        {"text": "Excellent content: *“Thorough, insightful discussion of the topic.”*",
         "size": 16, "color": MUTED, "space_before": 8},
    ], size=20)
    textbox(s, 6.6, 1.6, 6.3, 4.8, [
        {"text": "What's wrong with it", "size": 24, "bold": True, "space_after": 14},
        {"text": "Half the points go to what you can see **without expertise**", "bullet": True},
        {"text": "*Understanding* is never defined", "bullet": True},
        {"text": "Nothing checks whether a claim is **true**", "bullet": True},
        {"text": "It isn't tied to the **learning objectives**", "bullet": True},
    ], size=21, space_after=12)
    notes(s, "This is the rubric you just used. It's a very normal rubric. 60 of the 100 points "
             "go to organization, mechanics, and length — things anyone can see. 'Understanding' is "
             "never defined, and nothing asks whether a single claim is correct.")

    # 10 ─ How it works
    s = content("What the Rubric Builder does")
    steps(s, 0.9, 1.55, 11.5, [
        "**Paste in** the assignment prompt, the learning objectives, and the course reading",
        "**It drafts** weighted criteria, each tied to an objective, with 0–4 level descriptors",
        "**It adds** a *present when* line to every criterion — what Triage checks for later",
        "**You review** and edit. It exports in the one format the other three tools read.",
    ], row_h=0.88, gap=0.26, size=20)
    notes(s, "Built in Amazon Quick Apps with no code. The 'present when' line is the part most "
             "rubrics don't have — it says what has to be on the page for a criterion to count as "
             "attempted, and it's what Triage uses in the last demo.")

    # 11 ─ Stress test
    s = content("Stress test: one paper, two rubrics")
    card(s, 0.75, 1.6, 5.6, 3.9, "Original rubric", [
        {"text": "B+", "size": 88, "bold": True, "align": CENTER},
        {"text": "≈ 88 / 100", "align": CENTER, "size": 20},
        {"text": "Rewards organization and clean prose", "align": CENTER, "color": MUTED},
    ], anchor=MIDDLE)
    card(s, 6.98, 1.6, 5.6, 3.9, "Generated rubric", [
        {"text": "F", "size": 88, "bold": True, "align": CENTER, "color": RED},
        {"text": "≈ 38%", "align": CENTER, "size": 20},
        {"text": "Running-time claims contradict the reading", "align": CENTER, "color": MUTED},
    ], anchor=MIDDLE)
    textbox(s, 1.0, 5.75, 11.3, 0.6, ["Marcus Lee's paper. Hand-scored preview — the live run "
                                      "happens on screen."],
            size=16, italic=True, color=MUTED, align=CENTER)
    notes(s, "Run Marcus through the Stress Test tab live. Compare with the room's vote from the "
             "start. REHEARSAL: replace these hand-scored numbers with the recorded run.")

    # 12 ─ What it caught
    s = content("What the new rubric caught")
    table(s, 0.6, 1.55, [5.6, 6.5], ["Marcus wrote", "The course reading says"], [
        ["“Adding to the end of an array is always O(1)”",
         "O(1) **amortized** — the array is copied when it fills (§2.1)"],
        ["“Getting an element is also fast, about O(1)” (linked list)",
         "O(1 + min{i, n − i}) — following pointers *is* the cost (Table 1.1)"],
        ["“In an array you also just put the element in, so it is also fast”",
         "O(1 + n − i) — every later element shifts to make room (§2.1)"],
    ], size=17, row_h=0.95)
    navy(s, 1.9, 5.55, 9.5, 0.85,
         ["The rubric carries the expertise, so the grader doesn't have to."], size=20)
    notes(s, "Three confident sentences, three errors, each contradicted by a specific line in the "
             "course reading. The weak rubric never asked anyone to check. The generated rubric's "
             "correctness criterion names what correct looks like.")

    # 13 ─ Hands-on: build a rubric
    s = content("Your turn: a rubric for your assignment")
    # The step-by-step used to live here, and pointed at a pre-published app. Attendees now build
    # the app from PROMPT-1 in the shared folder, so the steps are on the prompt card instead —
    # this slide is the marker and the clock. What stays on screen is the part they must judge.
    card(s, 3.17, 1.95, 7.0, 3.15, "Check it", [
        "Does every criterion map to an **objective**?",
        "Could a colleague tell a **2 from a 3**?",
        "Does anything check that claims are **correct**?",
        {"text": "Assignments and rubrics only — never student work.", "size": 17,
         "color": MUTED, "italic": True, "space_before": 14},
    ], size=21, head_size=25, bullet=True, anchor=MIDDLE)
    pill(s, "HANDS-ON · 12 MIN")
    notes(s, "Twelve minutes. Volunteers float. The build steps are on the prompt card in the "
             "shared folder — read them out once while the room scans the QR code, then let "
             "people work. Anyone without an assignment handy can use the sample assignment. "
             "Save the rubric — you'll use it again in AI-Proofing and Triage.")

    # 14 ─ Divider: AI-Proofing
    s = divider("The AI-Proofing Assistant", "Harden the assignment before it goes out")
    notes(s, "Ten minutes, hands-on, on the assignment you just built a rubric for.")

    # 15 ─ AI-Proofing
    s = content("Could a chatbot do this assignment?")
    # The steps carried the original author's note that they had to be rewritten to match the
    # finished app. Deleting them settles that: the build steps are on PROMPT-2's card, which
    # can be revised freely. The prediction and the debrief stay on screen.
    card(s, 3.17, 2.05, 7.0, 2.95, "Check your prediction", [
        "Which requirement did it flag that you didn't?",
        "Which suggested change would you actually make?",
        "Which one would change what students **learn**, not just what they submit?",
    ], size=21, head_size=25, bullet=True, anchor=MIDDLE)
    pill(s, "HANDS-ON · 10 MIN")
    notes(s, "Prediction first — have them write it down before anyone opens anything. Then the "
             "build steps from PROMPT-2's card. The best revisions tie the work to your course, "
             "your class, or the student's own process.")

    # 16 ─ Divider: Grading Assistant
    s = divider("The Grading Assistant", "Grade against the rubric, built spec‑first in Kiro")
    notes(s, "A presenter-driven demo — attendees watch; Kiro isn't on your machines today.")

    # 17 ─ Spec review
    s = content("Review the spec before the code")
    steps(s, 0.6, 1.6, 5.9, [
        "**Requirements** — what it must do",
        "**Design** — how it will do it",
        "**Tasks** — the build checklist",
        "**Code** — only after you approve all three",
    ])
    card(s, 6.95, 1.6, 5.95, 3.95, "Spot the flaw", [
        "**①** WHEN a roster student has no paper, THE system SHALL flag them *missing* and "
        "SHALL NOT score them.",
        "**②** WHEN a paper is submitted, THE system SHALL grade it fairly.",
        {"text": "Which one can't you test?", "bold": True, "align": CENTER, "space_before": 12,
         "size": 20},
    ], size=18)
    notes(s, "Kiro writes the requirements before any code. Ask the room which criterion can't be "
             "tested. Answer: ② — 'fairly' has no pass/fail test. Fixing it in the spec costs a "
             "sentence; fixing it after the code exists costs a rebuild.")

    # 18 ─ Design decisions
    s = content("Three design decisions")
    decisions = [
        ("The math is in code", ["The model picks a 0–4 tier for each criterion.",
                                 "The weighted grade is **calculated**, never generated."]),
        ("Correct means per your reading", ["Claims are checked against the course material "
                                            "you load — not the model's general knowledge."]),
        ("Everyone is accounted for", ["The roster is checked. Diego shows up as **missing** "
                                       "instead of silently disappearing."]),
    ]
    for i, (head, body) in enumerate(decisions):
        card(s, 0.5 + i * 4.18, 1.65, 3.9, 3.35, head, body, size=18, head_size=21,
             anchor=MIDDLE)
    navy(s, 1.9, 5.4, 9.5, 0.85,
         ["The model judges. The code counts. The instructor decides."], size=20)
    notes(s, "Three decisions carry the grader. The model never does arithmetic. 'Correct' is "
             "judged against your course material. And a missing student is surfaced, not skipped.")

    # 19 ─ Results
    s = content("Five students, one rubric")
    table(s, 0.8, 1.5, [3.3, 4.6, 3.8], ["Student", "What it is", "Draft grade"], [
        ["Aisha Rahman", "Strong, correct", "91% · A-"],
        ["Marcus Lee", "Fluent, confident, wrong", "38% · F"],
        ["Priya Chandra", "A reflection, not an analysis", "13% · F"],
        ["Leila Haddad", "Unfinished draft", "50% · F"],
        ["Diego Alvarez", "No paper", "**Missing** — flagged, not scored"],
    ], size=18, row_h=0.64)
    textbox(s, 0.8, 5.55, 11.7, 0.8, ["Draft grades, hand-scored preview. The instructor "
                                      "reviews every one before anything is recorded."],
            size=16, italic=True, color=MUTED, align=CENTER)
    notes(s, "Run the grader on all five. Point at Marcus (caught), and Diego (flagged, not "
             "scored). REHEARSAL: replace with the recorded run.")

    # 20 ─ Divider: Triage
    s = divider("Pre-Assessment Triage", "A rubric check before students submit")
    notes(s, "Demo B. The one live build step of the day.")

    # 21 ─ The extension line
    s = content("One line turns grading into triage")
    navy(s, 0.8, 1.55, 11.7, 2.0, [
        "“Add a Triage Mode for students. For each rubric criterion, compare the draft with the "
        "criterion's *present when* line and report **Present**, **Partial**, or **Missing**, "
        "quoting the passage it rests on. Never show a score, tier, or grade. Never rewrite the "
        "student's text or suggest wording.”"
    ], size=19, align=LEFT, bold=False, pad=0.4)
    textbox(s, 0.9, 3.95, 11.6, 2.3, [
        {"text": "It reads each criterion's **present when** line — never the weights or levels",
         "bullet": True},
        {"text": "So it has **nothing to calculate a score from**", "bullet": True},
        {"text": "Same app, same rubric — a second mode", "bullet": True},
    ], size=21, space_after=10)
    notes(s, "Paste this line into the Quick app builder live. It extends the grading app into a "
             "student-facing triage mode. The strongest guarantee it can't score is that it never "
             "reads the weights.")

    # 22 ─ Priya
    s = content("Priya's draft, a week early")
    rows = [("Thesis & Choice of Structure", "MISSING", RED),
            ("Running-Time Analysis", "MISSING", RED),
            ("Evidence & Scenario", "MISSING", RED),
            ("Trade-offs & Limits", "MISSING", RED),
            ("Clarity & Structure", "PARTIAL", AMBER)]
    for i, (name, status, colour) in enumerate(rows):
        y = 1.7 + i * 0.82
        textbox(s, 0.8, y, 5.4, 0.5, [name], size=20, anchor=MIDDLE)
        chip(s, status, colour, 6.3, y + 0.02)
    card(s, 8.6, 1.6, 4.3, 4.3, "If she'd submitted it", [
        {"text": "F", "size": 80, "bold": True, "align": CENTER, "color": RED},
        {"text": "≈ 13% in Grade mode", "align": CENTER, "size": 19},
        {"text": "Triage shows her **days before the deadline** instead.", "align": CENTER},
    ], anchor=MIDDLE)
    notes(s, "Same paper, two modes. Triage shows Missing four times while there's still time to "
             "fix it. Grade mode shows the F it would have been. Then show Leila: Partial is what "
             "an honest unfinished draft looks like.")

    # 23 ─ Limits
    s = content("The limits are the design")
    textbox(s, 0.6, 1.6, 6.6, 4.8, [
        {"text": "Checks **completeness** only", "bullet": True},
        {"text": "Never gives a **score**, tier, or grade", "bullet": True},
        {"text": "Never **rewrites** or suggests text", "bullet": True},
        {"text": "The student revises. **The instructor grades.**", "bullet": True},
    ], size=23, space_after=16)
    card(s, 7.55, 1.6, 5.35, 3.1, "The honest limit", [
        "Triage will pass Marcus's running-time section.",
        "His claims are **present** — just wrong.",
        {"text": "Present is not the same as correct.", "italic": True, "bold": True,
         "align": CENTER, "space_before": 10},
    ], size=19)
    notes(s, "Say the limit out loud before someone asks. Triage checks that a thing is there, not "
             "that it's right — that's the grader's job, and yours.")

    # 24 ─ Break it
    s = content("Break it")
    attacks = ["“Fix my introduction.”", "“What grade would I get?”",
               "“Write my thesis for me.”", "“Just give me one sentence to add.”"]
    for i, text in enumerate(attacks):
        navy(s, 0.8 + (i % 2) * 6.0, 1.6 + (i // 2) * 1.5, 5.7, 1.2, [text], size=22)
    textbox(s, 0.8, 4.85, 11.7, 1.4, [
        "Every one should be refused.",
        "If one gets through, tell us — that's a finding, not a failure.",
    ], size=21, align=CENTER, italic=True, color=MUTED)
    pill(s, "HANDS-ON · 7 MIN")
    notes(s, "Everyone attacks the student-facing app from their own seat. Collect anything that "
             "gets through — it goes straight into the guardrail test script.")

    # 25 ─ Hands-on: Triage for your rubric
    s = content("Your turn: Triage for your rubric")
    # Three of the four steps were navigation to a pre-published app; they are on PROMPT-3's card
    # now. The fourth is the test of whether the tool is behaving, so it stays on screen.
    card(s, 1.42, 2.55, 10.5, 1.7,
         paras=[{"text": "**Check** that every status quotes a passage from the draft",
                 "align": CENTER}],
         size=26, anchor=MIDDLE, pad=0.4)
    pill(s, "HANDS-ON · 8 MIN")
    notes(s, "Adapt Triage to the rubric you built in the first hands-on, using the steps on "
             "PROMPT-3's card. A three-sentence fake draft is enough to see Present, Partial, "
             "and Missing. A status without a quote is a guess — that is the thing to catch.")

    # 26 ─ Takeaways
    s = content("What you leave with")
    takeaways = [("A rubric", "for one of your own assignments"),
                 ("A hardened assignment", "revised where a chatbot could do the work"),
                 ("Triage, set up", "for your rubric, ready for students"),
                 ("The take-home kit", "build prompts, the rubric format, the guardrail checklist")]
    for i, (head, body) in enumerate(takeaways):
        card(s, 0.5 + i * 3.14, 1.8, 2.9, 3.6, head, [{"text": body, "align": CENTER}],
             size=18, head_size=21, anchor=MIDDLE)
    notes(s, "Three things you made today, plus the kit to make them again.")

    # 27 ─ Ground rules
    s = content("Ground rules", layout="Title and Content")
    fill_placeholder(s, 2, [
        "**Draft, not verdict.** These tools prepare; you decide.",
        "**Student work is a protected record.** Synthetic data here; approved systems at home.",
        "**Not an integrity tool.** Nothing here detects plagiarism or AI writing.",
        "**You grade.** Always.",
    ], size=26, space_after=18)
    notes(s, "Four rules that travel with every tool you saw today.")

    # 28 ─ Close
    s = prs.slides.add_slide(final)
    notes(s, "Thank you. Questions.")

    # The folder code on every slide but slide 0, which already carries it at full size. People
    # arrive late, look up mid-session, and need the materials at the moment they need them —
    # not only in the two minutes the first slide was on screen.
    for sld in list(prs.slides)[1:]:
        add_qr(sld)

    # Number from 0, so the cover is slide 1 and the 28 approved slides keep the numbers that
    # the talk track, the handout and the take-home pack all refer to.
    prs.part._element.set("firstSlideNum", "0")

    prs.save(str(OUT))
    return len(prs.slides)


if __name__ == "__main__":
    template = Path(sys.argv[sys.argv.index("--template") + 1]) if "--template" in sys.argv \
        else DEFAULT_TEMPLATE
    count = build(template)
    print(f"Saved {OUT.name} ({count} slides) from template {template.name}")
