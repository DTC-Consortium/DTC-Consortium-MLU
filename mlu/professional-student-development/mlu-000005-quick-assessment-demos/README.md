# The Assignment Lifecycle — Quick Assessment Demo Session

**`mlu-000005`** · Professional and Student Development · v0.1.0 · **pilot**

A 90-minute facilitated session that walks a room through one assignment's full lifecycle: write the
rubric, stress-test it, grade against it, and triage submissions before the deadline.

The whole session hangs on **one student paper** — fluent, confident, and wrong. It earns roughly a
**B+** under a vague rubric and an **F** under a rubric that names what "correct" means. The room
grades it themselves before anyone reveals that.

> **Maturity: pilot.** The materials are complete and rehearsable, but the expected outcomes in the
> sample pack are **hand-scored predictions, not recorded results**. Run the rehearsal and replace
> them with real numbers before treating this as classroom-tested.

## At a glance

| | |
|---|---|
| **Audience** | Faculty, workshop facilitators, instructional designers |
| **Duration** | ~90 minutes |
| **Delivery** | In person |
| **Runs on** | Nothing to install. The session demonstrates chat-based AI tools. |
| **Prerequisites** | Participants bring one assignment prompt and its learning objectives, **as text — no student work** |
| **Expected cost** | None for the materials; any per-seat cost depends on which AI tool the facilitator demonstrates |
| **You end with** | A rubric that names what correct looks like, tested against a paper built to exploit a weak one |

## Learning outcomes

By the end, a participant can:

1. Diagnose why a rubric that rewards visible surface features misgrades a confidently wrong paper.
2. Write a rubric whose criteria name what correct looks like and map to stated learning objectives.
3. Stress-test a rubric against a paper designed to exploit its weaknesses.
4. Use pre-deadline triage to surface missing criteria while students can still act on it.

## Contents

| Path | What it is |
|---|---|
| [`materials/slides/`](materials/slides) | The 90-minute deck as `.pdf` and editable `.pptx`, plus `build_deck.py` which regenerates it |
| [`materials/facilitator-guide/TALK_TRACK.md`](materials/facilitator-guide/TALK_TRACK.md) | Per-slide talk track — what must be true before each slide, what to say, what to do, and **the one thread to protect if time runs short** |
| [`materials/participant-resources/hook-handout.md`](materials/participant-resources/hook-handout.md) | The opening handout the room grades from |
| [`materials/activities/sample-pack/`](materials/activities/sample-pack) | One assignment, one course reading, two rubrics, five students |
| [`materials/activities/rubric-format.md`](materials/activities/rubric-format.md) | The `mlu-rubric/1` format shared by the session tools |

### The five students

| Student | The paper | Its job in the session |
|---|---|---|
| **Aisha Rahman** | Strong and correct | The control — high on every rubric |
| **Marcus Lee** | **Fluent, confident, and wrong** | The centrepiece. ≈B+ under the weak rubric, F under the golden one. |
| **Priya Chandra** | A reflection, not an analysis | Triage surfaces three Missing flags before the deadline |
| **Leila Haddad** | An unfinished draft | Shows what **Partial** looks like |
| **Diego Alvarez** | Nothing submitted | Flagged **missing** rather than silently skipped |

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Read [`TALK_TRACK.md`](materials/facilitator-guide/TALK_TRACK.md) end to end**, including the
   48-hours-before checklist. The session depends on the room grading Marcus's paper cold, so the
   handout must go out before anyone sees the golden rubric.
3. **Rehearse against the sample pack** and record what the tools actually produce. Replace the
   predicted outcomes in `sample-pack/README.md` with those results.
4. **Ask participants in the registration email** to bring one assignment prompt and its learning
   objectives as text. No student work.

## Related

Rubrics written in the `mlu-rubric/1` format load unchanged into
[`mlu-000004`](../../ml-ai-applications/mlu-000004-paper-autograder), which is the automated
counterpart to the grading demo in this session.

## Reuse and attribution

Documentation is `CC-BY-4.0`; code is `MIT`; bundled data keeps its own per-file licence. See
[`LICENSE.md`](LICENSE.md) and [`CITATION.cff`](CITATION.cff). **No real student appears anywhere in
this contribution** — all five students and their papers are invented.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
