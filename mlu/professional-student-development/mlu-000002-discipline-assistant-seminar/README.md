# Discipline-Specific AI Teaching Assistant — Seminar Lab

**`mlu-000002`** · Professional and Student Development · v1.0.0 · classroom-tested

The technical lab of the set. In about 15 minutes participants build a grounded, source-citing AI
tutor for their own field, and see directly what grounding buys them — the notebook asks the same
question with and without the source document.

The design idea in one line: **grounding is what separates a tutor from a plausible-sounding
stranger.**

> **The most portable contribution in the set.** The Colab path needs no AWS account at all, which
> matters because most faculty lose cloud access once a seminar ends. They keep a working copy.

## At a glance

| | |
|---|---|
| **Audience** | Faculty and academic staff who want to understand and modify the tooling, not just use it |
| **Duration** | **~15 min self-paced**, or **~90 min as a facilitated lab** — see the note below |
| **Delivery** | In person, online-synchronous, or self-paced |
| **Runs on** | **Google Colab + free Hugging Face account (no AWS)**, *or* SageMaker Studio + Bedrock |
| **Prerequisites** | Colab path: a Google account and a free Hugging Face read token. AWS path: SageMaker Studio and Bedrock model access. |
| **Expected cost** | **None** on the Colab path. Under USD 1 per participant on the AWS path. |
| **Sample data** | Six licence-clean discipline PDFs — runs out of the box, no prep |
| **You end with** | A working, citing tutor plus generated quiz questions, study guides, and rubrics |

## Learning outcomes

By the end, a participant can:

1. Explain how chunking, embedding, and vector retrieval combine to ground a model's answer.
2. Build a tutor that answers only from a supplied document and cites the passage it used.
3. Contrast grounded and ungrounded answers to the same question, and say why the difference
   matters for teaching.
4. Generate quiz questions, study guides, and grading rubrics from a discipline document.

## Contents

| Path | What it is |
|---|---|
| [`materials/activities/discipline-assistant/`](materials/activities/discipline-assistant) | The runnable lab. **Its README is the full usage guide.** |
| ├─ `discipline-assistant-colab.ipynb` | **The recommended path** — Colab + Hugging Face, no AWS |
| ├─ `discipline-assistant.ipynb` | The AWS path — SageMaker Studio + Bedrock |
| └─ `data/` | Six discipline personas, with per-file provenance in `data/README.md` |
| [`materials/agenda/SEMINAR_PLAN.md`](materials/agenda/SEMINAR_PLAN.md) | Background. **This is the superseded v1 day-plan** — the current day-plan lives in [`mlu-000001`](../mlu-000001-curriculum-embedding-lab/materials/agenda/SEMINAR_PLAN.md). Kept for its persona table and risk list. |
| [`materials/facilitator-guide/`](materials/facilitator-guide) | Cheatsheet, preflight checklist, content audit, and a menu of 17 follow-on labs |

### Two durations, and they are both real

| Mode | Time | What it looks like |
|---|---|---|
| **Self-paced** | ~10–15 min | A participant opens the notebook and runs it alone. |
| **Facilitated lab** | ~90 min | Instructor drives Parts 1–2, participants drive Parts 3–4, shared close in Part 5. This is what the cheatsheet scripts. |

Decide which you are running *before* reading the facilitator guide — its clock assumes the
facilitated version.

Neither notebook depends on the other, and neither needs `mlu_utils/` — both are fully
self-contained, so the Colab path works from a single file with nothing else cloned.

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Pick a path.** No AWS access (most faculty) → the Colab notebook. Ongoing SageMaker access →
   the Bedrock notebook. **The two need different lead times** — Colab is same-day, SageMaker needs
   about a week for account and model-access provisioning.
3. **Facilitators: work `materials/facilitator-guide/PREFLIGHT_CHECKLIST.md` before delivery.**
   It opens with a path selector; read your path and skip the other. The Hugging Face free tier
   occasionally rate-limits, and the checklist covers what to do about it.

Full setup and the bring-your-own-document path are in
[the activity README](materials/activities/discipline-assistant/README.md).

## Reuse and attribution

Documentation is `CC-BY-4.0`; code is `MIT`; bundled data keeps its own per-file licence. See
[`LICENSE.md`](LICENSE.md) and [`CITATION.cff`](CITATION.cff).

The six personas are byte-identical to those in
[`mlu-000001`](../mlu-000001-curriculum-embedding-lab), deliberately — a participant who runs both
labs sees familiar material and can focus on what changed. The same content note applies to the
English-literature persona; see `LICENSE.md`.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
