# Curriculum Embedding Lab — Embed AI in Your Course

**`mlu-000001`** · Professional and Student Development · v1.0.0 · classroom-tested

A 90-minute faculty lab whose deliverable is a decision, not a demo. Each participant builds a
working, discipline-grounded AI tool from a persona matched to their field, then writes the
curriculum plan for where it belongs in a course they actually teach — and, explicitly, where AI
does **not** belong.

The design idea in one line: **the tool is not the deliverable — the decision is.**

> **Start here if you are running the four-lab sequence.** This contribution establishes *where AI
> fits* before [`mlu-000002`](../mlu-000002-discipline-assistant-seminar) shows *how it works* and
> the two assessment tools put it to work.

> ## Scope: this is the 90-minute lab, not the whole day
>
> `materials/agenda/SEMINAR_PLAN.md` describes a full 9:00–4:00 faculty seminar. **Only the
> 1:30–3:00 PM lab is included here** — and it is fully self-contained, with notebooks, six
> licence-clean discipline documents, and a complete facilitator track.
>
> The rest of that day (the morning PartyRock lab and three lecture blocks) comes from AWS MLU
> material that is **not in this repository**, and whose upstream links currently return HTTP 404.
>
> **To deliver the 90-minute lab — what most people want — you need nothing else.** Go to
> [`INSTRUCTOR_CHEATSHEET.md`](materials/facilitator-guide/INSTRUCTOR_CHEATSHEET.md), which scripts
> it minute by minute, then
> [`PREFLIGHT_CHECKLIST.md`](materials/facilitator-guide/PREFLIGHT_CHECKLIST.md) for setup. The
> seminar plan's opening table shows block by block what is and is not included.

## At a glance

| | |
|---|---|
| **Audience** | Faculty, academic staff, instructional designers. No coding experience required. |
| **Duration** | ~90 minutes (Parts 0–7) |
| **Delivery** | In person or online-synchronous |
| **Runs on** | Amazon SageMaker Studio + Amazon Bedrock (Nova Lite) |
| **Prerequisites** | AWS account with SageMaker Studio and Bedrock Nova Lite model access |
| **Expected cost** | Under USD 1 per participant in inference; shut Studio compute down afterward |
| **Sample data** | Six licence-clean discipline PDFs — runs out of the box, no prep |
| **You end with** | A working tool, a written curriculum plan, an explicit "not here" boundary, and a dated commitment |

## Learning outcomes

By the end, a participant can:

1. Identify where in a specific course an AI tool adds instructional value, and articulate what the
   instructor still does.
2. Build a discipline-grounded AI tool from a persona brief, using retrieval over a real document
   from their field.
3. State an explicit boundary for where AI does not belong in their own teaching, and defend it.
4. Commit to one dated, specific instructional action.

Blank reflection cells are treated as a missing plan, not a skipped exercise.

## Contents

| Path | What it is |
|---|---|
| [`materials/activities/curriculum-embedding-lab/`](materials/activities/curriculum-embedding-lab) | The runnable lab. **Its README is the full usage guide.** |
| ├─ `curriculum-embedding-lab.ipynb` | The faculty lab, Parts 0–7 |
| ├─ `study-mastery-lab.ipynb` | Student-facing companion — Quiz Me, Socratic Hint, Explain-Back |
| ├─ `data/` | Six discipline personas, with per-file provenance in `data/README.md` |
| └─ `mlu_utils/` | `NovaMultimodalEmbeddings` and study-mode helpers |
| [`materials/agenda/SEMINAR_PLAN.md`](materials/agenda/SEMINAR_PLAN.md) | Full agenda and the locked design decisions |
| [`materials/facilitator-guide/`](materials/facilitator-guide) | Podium walkthrough, cheatsheet, preflight checklist, content audit, and a six-persona smoketest with recorded known-good outputs |
| └─ `BRIDGE_AND_LAB_DECK_SPEC.md` | **A spec, not a deck.** Slide-by-slide content and speaker notes for the 1:15–1:30 bridge — someone still has to build the slides, partly from AWS decks not included here. |

The notebooks, `data/`, and `mlu_utils/` are deliberately kept in one folder — the notebooks
reference them by relative path, so the lab runs unchanged straight out of the download.

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Facilitators: read `materials/facilitator-guide/` before you teach.** Run
   `persona_smoketest.py` across all six personas and diff against
   `persona_test_outputs/` so you know the room will see working output.
3. **Participants: open** `materials/activities/curriculum-embedding-lab/curriculum-embedding-lab.ipynb`
   in SageMaker Studio, set `persona` in Part 0 to match their discipline, and run top to bottom.

Full setup, troubleshooting, and the bring-your-own-document path are in
[the activity README](materials/activities/curriculum-embedding-lab/README.md).

## Reuse and attribution

Documentation is `CC-BY-4.0`; code is `MIT`; bundled data keeps its own per-file licence. See
[`LICENSE.md`](LICENSE.md) for the file-by-file table and [`CITATION.cff`](CITATION.cff) for how to
cite this work.

**One content note for facilitators:** the English-literature persona uses a public-domain Seacole
text that preserves nineteenth-century spelling and racial language. That language is itself an
object of scholarly analysis and part of why the document works — but flag it for participants in
advance rather than letting it arrive unannounced.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
