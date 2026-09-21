# The Assignment Lifecycle — Quick Assessment Demo Session

**`mlu-000005`** · Professional and Student Development · v0.2.0 · **pilot**

A 90-minute facilitated session that walks a room through one assignment's full lifecycle: write the
rubric, stress-test it, grade against it, and triage submissions before the deadline.

The whole session hangs on **one student paper** — fluent, confident, and wrong. It earns a high
grade under a vague rubric and an **F** under a rubric that names what "correct" means. The room
grades it themselves before anyone reveals that.

> ## The room builds the tools, from prompts
>
> **Nothing is pre-installed and nothing is pre-shared.** Attendees build three of the four tools
> themselves, in about ninety seconds each, by pasting a prompt into Amazon Quick. The facilitator
> builds the fourth in advance and the room watches it.
>
> That is what attendees take home. An app shared to an account they lose access to is not
> something they keep; a prompt is, and it still works on whatever tool they have in two years.
>
> **[`materials/prompts/`](materials/prompts)** has all five prompts, each with the outputs it must
> produce on the bundled sample before you rehearse.

## At a glance

| | |
|---|---|
| **Audience** | Faculty, workshop facilitators, instructional designers |
| **Duration** | ~90 minutes |
| **Delivery** | In person |
| **Runs on** | Amazon Quick (free tier) for the room; Kiro for one facilitator-led segment |
| **Prerequisites** | None for participants. Everything they grade, paste and build is provided. |
| **Expected cost** | None for the materials. Amazon Quick is free to set up and use. |
| **You end with** | Three working apps, and the prompts that rebuild them |

## Learning outcomes

By the end, a participant can:

1. Diagnose why a rubric that rewards visible surface features misgrades a confidently wrong paper.
2. Write a rubric whose criteria name what correct looks like and map to stated learning objectives.
3. Stress-test a rubric against a paper designed to exploit its weaknesses.
4. Use pre-deadline triage to surface missing criteria while students can still act on it.

## Contents

| Path | What it is |
|---|---|
| [`materials/facilitator-guide/00-READ-ME-FIRST.md`](materials/facilitator-guide/00-READ-ME-FIRST.md) | **Start here.** What to read, in what order, and what will go wrong. |
| [`materials/prompts/`](materials/prompts) | The five prompts. Three the room builds from, two the facilitator prepares. |
| [`materials/prompts/MASTER-FOLLOW-ALONG.md`](materials/prompts/MASTER-FOLLOW-ALONG.md) | **The one document attendees follow.** Every step is self-contained. |
| [`materials/facilitator-guide/TALK_TRACK.md`](materials/facilitator-guide/TALK_TRACK.md) | Per-slide talk track — preconditions, what to say, what to do, and **the one thread to protect if time runs short** |
| [`materials/prompts/facilitator/RUN-KIRO.md`](materials/prompts/facilitator/RUN-KIRO.md) | Presenter runbook for the watched segment |
| [`materials/DECK-APPROVAL.md`](materials/DECK-APPROVAL.md) | What may and may not change on the approved slides, and the check that proves it |
| [`materials/activities/sample-pack/`](materials/activities/sample-pack) | One assignment, one course reading, two rubrics, five students |
| [`materials/activities/rubric-format.md`](materials/activities/rubric-format.md) | The `mlu-rubric/1` format shared by all four tools |
| [`materials/dist/`](materials/dist) | Three built PDFs: the follow-along guide, the facilitator guide, the take-home pack |

### The four tools

| # | Tool | Who builds it | Where |
|---|---|---|---|
| 1 | **Rubric Builder** | The room | Amazon Quick |
| 2 | **AI-Proofing Assistant** | The room | Amazon Quick |
| 3 | **Grading Assistant** | Facilitator, in advance | **Kiro** — the room watches |
| 4 | **Pre-Assessment Triage** | The room | Amazon Quick |

Tool 3 is built in Kiro deliberately. The contrast between describing an app and fixing it
afterwards, versus approving requirements then design then tasks before any code exists, *is* the
teaching content of that segment — and it matters most for the tool that assigns grades.

### The five students

| Student | The paper | Its job in the session |
|---|---|---|
| **Aisha Rahman** | Strong and correct | The control — high on every rubric |
| **Marcus Lee** | **Fluent, confident, and wrong** | The centrepiece. High under the weak rubric, F under the golden one. |
| **Priya Chandra** | A reflection, not an analysis | Triage surfaces the missing criteria before the deadline |
| **Leila Haddad** | An unfinished draft | Shows what **Partial** looks like |
| **Diego Alvarez** | Nothing submitted | Flagged **missing** rather than silently skipped |

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Read [`00-READ-ME-FIRST.md`](materials/facilitator-guide/00-READ-ME-FIRST.md).** It is short and
   it sets the three constraints everything else follows from.
3. **Build the two facilitator tools** — [`PROMPT-F1`](materials/prompts/facilitator/PROMPT-F1-grading-app.md)
   and [`PROMPT-F2`](materials/prompts/facilitator/PROMPT-F2-kiro-grader.md). The room builds the
   other three live; these two are demos, and a demo needs something to demo.
4. **Run each prompt's "prove it works" checks.** The session turns on three specific results. A
   build that misses them looks fine and teaches nothing.
5. **Assemble the shared folder** — [`prompts/DRIVE-FOLDER.md`](materials/prompts/DRIVE-FOLDER.md).
   Attendees reach everything through one link, and the deck carries its QR code on every slide.
6. **Read [`TALK_TRACK.md`](materials/facilitator-guide/TALK_TRACK.md) end to end**, including the
   checklists. The session depends on the room grading Marcus's paper cold, so nothing that reveals
   the reference rubric can reach them before that.

### Rebuilding the artifacts

```sh
cd materials
python3 build_deck.py          # regenerate the .pptx, and the folder QR from session_config.py
python3 verify_deck.py --show  # prove the deck is still subtractive against the approved copy
./export_pdf.sh                # PDF via PowerPoint; gated on the check above
python3 build_pack.py          # the three PDFs in dist/
```

The approved slides may have copy **removed** but never added or reworded.
[`verify_deck.py`](materials/verify_deck.py) proves that mechanically against
[`approved-deck-baseline.txt`](materials/approved-deck-baseline.txt), and `export_pdf.sh` will not
overwrite the PDF until it passes. [`DECK-APPROVAL.md`](materials/DECK-APPROVAL.md) explains why
that replaced a frozen checksum.

### Adapting it to your own event

Session facts — the shared-folder link, the date, the venue — live in
[`session_config.py`](materials/session_config.py), because they are stamped into the deck, the
packs and the handouts. Change them there and rebuild. **The materials as shipped carry the dates,
venue and contacts of the first delivery**; treat those as examples to replace, not as content.

## Related

Rubrics written in the `mlu-rubric/1` format load unchanged into
[`mlu-000004`](../../ml-ai-applications/mlu-000004-paper-autograder), which is the automated
counterpart to the grading demo in this session.

## Reuse and attribution

Documentation is `CC-BY-4.0`; code is `MIT`; bundled data keeps its own per-file licence. See
[`LICENSE.md`](LICENSE.md) and [`CITATION.cff`](CITATION.cff). **No real student appears anywhere in
this contribution** — all five students and their papers are invented.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
