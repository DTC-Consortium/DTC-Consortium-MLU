# Class Participation Scoring — Transcript to Draft Score

**`mlu-000003`** · ML/AI Applications · v1.0.0 · classroom-tested

Point this notebook at a Zoom transcript of one class meeting and the material you covered that
day. It identifies who spoke, judges what they talked about — on-topic vs. off-topic, grounded
*only* in your lesson — and drafts a **0–4 participation score** per student, with the evidence and
reasoning behind every score.

The scoring logic in one line: **talk a lot and on-topic → high; talk a lot but off-topic → low;
don't speak → 0.**

> ### ⚠️ Read this before anything else
>
> This produces a **draft you review**, not a grade the tool assigns on its own. Class recordings
> and transcripts are **student records**. Before pointing this at a real class, confirm that
> recording and transcription are covered by your institution's policy and that students were
> notified — FERPA in the US, or your local equivalent. The bundled sample is entirely fabricated,
> so you can evaluate the tool without touching real records.

## At a glance

| | |
|---|---|
| **Audience** | Faculty and adjunct faculty scoring participation in a discussion-based course |
| **Duration** | ~10 minutes of compute on the bundled sample. The Part 5 review is the real cost and scales with class size. |
| **Runs on** | Amazon SageMaker Studio + Amazon Bedrock (Nova Lite) |
| **Prerequisites** | AWS account with SageMaker Studio and Bedrock Nova Lite access; institutional clearance to use class recordings |
| **Expected cost** | Under USD 1 per class meeting scored |
| **Sample data** | A fabricated transcript, roster, and lesson PDF — runs out of the box |
| **You end with** | A reviewed 0–4 score per student, with evidence, exported as `.md` + `.csv` |

## Intended use

Drafts class-participation scores from a recorded class transcript, so an instructor reviews
evidence-backed drafts instead of scoring from memory. Each score combines three signals:

1. **Quantity** — turns, words, and talk time, computed directly from the transcript.
2. **Topical relevance** — judged against *your* embedded lesson material, which is what separates a
   chatty-but-off-topic student from a chatty-and-on-topic one.
3. **Substance** — questions, reasoning, and building on peers vs. filler and logistics.

Using it well means being able to:

- Ground a relevance judgment in supplied course material rather than model priors.
- Review and override AI-drafted scores using the evidence attached to each one.
- Apply institutional policy on class recording and student records before using real transcripts.

**Part 5 is a mandatory human review step.** No score should be recorded without it.

## Contents

| Path | What it is |
|---|---|
| [`materials/src/`](materials/src) | The runnable tool. **Its README is the full usage guide.** |
| ├─ `participation-scoring-lab.ipynb` | The tool, Parts 1–7 |
| ├─ `data/` | Fabricated transcript, roster, and lesson PDF, plus the bring-your-own slots |
| ├─ `mlu_utils/` | `NovaMultimodalEmbeddings` and transcript parsing and scoring |
| └─ `requirements.txt` | Pinned dependencies |
| [`materials/facilitator-guide/LAB_WALKTHROUGH.md`](materials/facilitator-guide/LAB_WALKTHROUGH.md) | Run of show and expected outputs, for delivering this as a lab |

The notebook, `data/`, and `mlu_utils/` are deliberately kept in one folder — the notebook
references them by relative path, so it runs unchanged straight out of the download.

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Run it on the bundled sample first.** The sample is built so the output is legible: it spans a
   strong on-topic contributor, a chatty-but-off-topic student, a filler-only student, and students
   who never spoke. Confirm you agree with its judgments before trusting it on your own class.
3. **Swap in your own material** by changing two lines, in Parts 2 and 3 — but only after the
   privacy checks above.
4. **Review every draft in Part 5.** Override freely; the evidence is there so you can.

Setup, the rubric tiers in full, and the privacy section are in
[the tool README](materials/src/README.md).

## Related

Sibling of [`mlu-000004`](../mlu-000004-paper-autograder), which applies the same grounded-judgment
idea to written work. Both build on the retrieval stack introduced in
[`mlu-000001`](../../professional-student-development/mlu-000001-curriculum-embedding-lab) and
[`mlu-000002`](../../professional-student-development/mlu-000002-discipline-assistant-seminar).

## Reuse and attribution

Documentation is `CC-BY-4.0`; code is `MIT`; bundled data keeps its own per-file licence. See
[`LICENSE.md`](LICENSE.md) and [`CITATION.cff`](CITATION.cff). **No real student appears anywhere in
this contribution** — every name, transcript line, and roster entry is invented.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
