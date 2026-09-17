# Paper Autograder — Rubric-Based Draft Grading

**`mlu-000004`** · ML/AI Applications · v1.0.0 · classroom-tested

Point this notebook at your course material, a grading rubric, and a folder of student papers. For
each paper it scores every rubric criterion, backs each score with verbatim quotes, computes a
**weighted overall grade**, and drafts two sets of notes — one for you explaining *why* it landed
where it did, and one you can hand back to the student.

The grading logic in one line: **score each criterion against your rubric, judge "did they use the
concepts correctly" only against your material, then let the weights do the arithmetic — in code,
not in the model.**

> ### ⚠️ Read this before anything else
>
> This produces a **draft you review**, not a grade the tool assigns on its own. Student papers are
> **student records** — handle them under your institution's policy (FERPA in the US, or your local
> equivalent). This is **not** a plagiarism or AI-writing detector: never use its output in an
> academic-integrity decision. The Ollama path keeps every paper on your own machine.

## At a glance

| | |
|---|---|
| **Audience** | Faculty and adjunct faculty grading written work against a rubric |
| **Duration** | ~5 minutes of compute on the bundled 3-paper sample. The Part 5 review is the real cost and scales with stack size. |
| **Runs on** | SageMaker Studio + Bedrock, **or fully local via Ollama — nothing leaves your laptop** |
| **Prerequisites** | Bedrock path: AWS account with SageMaker Studio and Nova Lite access. Local path: none beyond Ollama. |
| **Expected cost** | Under USD 1 per stack on Bedrock. **None** on the Ollama path. |
| **Sample data** | Three fabricated papers, a rubric, a roster, and course material — runs out of the box |
| **You end with** | A reviewed weighted grade per student, with quoted evidence, as `.csv`, `.md`, and per-student feedback files |

## Intended use

Drafts rubric-based grades for written work. Each paper's grade combines, per criterion:

1. **A tier (0–4)** picked against your rubric's own descriptors.
2. **Grounded correctness** — where a criterion is about *using the course concepts correctly*, the
   judgment is made only against your embedded material. A confident, well-written paper that
   misuses the concepts scores **lower** on those criteria, not higher.
3. **Evidence** — 1–2 verbatim quotes behind every tier, a rationale for you, and an actionable note
   for the student.

The overall grade is computed **in code** from the tiers and your criterion weights, then mapped to
a letter via configurable bands. The model never does the arithmetic.

Using it well means being able to:

- Express a grading rubric in a machine-readable form with explicit criterion weights.
- Distinguish fluent writing from correct reasoning when reviewing drafted grades.
- Review evidence-backed drafts and override them before recording any grade.

**Part 5 is a mandatory human review step.**

## Is this a workshop?

**No — it is a tool one faculty member uses on their own classes.** There is no run-of-show, no
participant handout, and no 90-minute slot to fill.

You can absolutely *demo* it to faculty or administrators, and
[`materials/facilitator-guide/LAB_WALKTHROUGH.md`](materials/facilitator-guide/LAB_WALKTHROUGH.md)
opens with a 20-minute demo shape for exactly that. But if you came looking for a facilitated
session on assessment, deliver
[`mlu-000005`](../../professional-student-development/mlu-000005-quick-assessment-demos) instead and
point at this as the automated counterpart.

## Contents

| Path | What it is |
|---|---|
| [`materials/src/`](materials/src) | The runnable tool. **Its README is the full usage guide.** |
| ├─ `paper-grading-lab.ipynb` | The tool, Parts 1–7 |
| ├─ `data/` | Three fabricated papers, a structured rubric, a roster, and course material |
| ├─ `mlu_utils/` | `NovaMultimodalEmbeddings`, plus paper loading, rubric handling, and grading |
| └─ `requirements.txt` | Pinned dependencies, including `langchain-ollama` for the local path |
| [`materials/evaluation/sample-output-2026-07-31/`](materials/evaluation/sample-output-2026-07-31) | A recorded run against the bundled sample — diff your output against it before delivery |
| [`materials/facilitator-guide/LAB_WALKTHROUGH.md`](materials/facilitator-guide/LAB_WALKTHROUGH.md) | Run of show and expected outputs, for delivering this as a lab |

The notebook, `data/`, and `mlu_utils/` are deliberately kept in one folder — the notebook
references them by relative path, so it runs unchanged straight out of the download. The notebook
writes each run to a fresh timestamped `grades_<stamp>/` directory beside itself; the copy under
`materials/evaluation/` is one such run, preserved for comparison.

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Run it on the bundled sample first**, and diff against
   `materials/evaluation/sample-output-2026-07-31/`. The sample includes a paper that is fluent,
   confident, and *wrong* — check that the tool marks it down rather than up. Model output varies
   run to run, so expect close agreement, not an exact match.
3. **Replace the rubric** in `data/sample_rubric.py` with your own criteria and weights.
4. **Review every draft in Part 5** before recording anything.

Setup, the Ollama path, and the privacy section are in [the tool README](materials/src/README.md).

## Related

Sibling of [`mlu-000003`](../mlu-000003-participation-scoring), which applies the same
grounded-judgment idea to spoken participation. Rubrics written in the `mlu-rubric/1` format from
[`mlu-000005`](../../professional-student-development/mlu-000005-quick-assessment-demos) load into
this tool unchanged.

## Reuse and attribution

Documentation is `CC-BY-4.0`; code is `MIT`; bundled data keeps its own per-file licence. See
[`LICENSE.md`](LICENSE.md) and [`CITATION.cff`](CITATION.cff). **No real student appears anywhere in
this contribution** — every paper, name, and roster entry is invented.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
