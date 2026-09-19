# Assignment Defender — AI-Proofing Assistant

**`mlu-000010`** · ML/AI Applications · v1.0.0 · **classroom-tested**

**[Open the app →](https://quick.aws.com/sn/accounts/905896282634/apps/98715fae-6c9f-41e2-add3-e883ca50d9a3/public/AI-Proofing-Assistant)**
· no account, no code, no install

Give it an assignment — goals, instructions, learning objectives, grading criteria — and tell it the
maximum grade you think an **AI-only submission** should be able to earn. It returns an AI Robustness
Score, a SWOT analysis of the assessment as written, and three redesign options at increasing
strength.

The premise is not that students should be stopped from using AI. It is that an assignment can
quietly stop measuring the thing it was built to measure, and you cannot fix that by detecting
anything. **This tool finds where AI substitutes for the skill being assessed, so a human can decide
what to change.**

## At a glance

| | |
|---|---|
| **Audience** | Faculty, adjuncts, instructional designers, teaching and learning centres |
| **Duration** | ~15–30 minutes per assignment analysed |
| **Delivery** | Self-paced, in a browser |
| **Runs on** | Amazon Quick. The published app needs no account. |
| **Prerequisites** | One assignment you already teach, with its instructions and grading criteria as text |
| **Expected cost** | None to use the published app |
| **Sample data** | Two complete worked analyses of the author's own assignments, with the app's output |
| **You end with** | A robustness score, a SWOT review, and three exportable redesign options to adapt |

## Intended use

This is a **formative instructional-design and decision-support tool**. It produces a draft for
faculty judgment, never a verdict. Three limits are load-bearing rather than boilerplate:

- **It does not make an assignment AI-proof.** The score is an estimate. AI capabilities keep
  changing and no design guarantees AI will not be used.
- **It is not an AI-detection tool**, and its output must never enter an academic-integrity
  decision. It analyses assignments, not submissions.
- **Do not paste student work into it.** No names, IDs, grades, education records, or other
  FERPA-protected information. Assignments, objectives, instructions, and rubrics only.

## Contents

| Path | What it is |
|---|---|
| [`materials/setup/using-the-app.md`](materials/setup/using-the-app.md) | **Start here.** What it does, how to run an assignment through it, what the three redesign levels mean, and the limits |
| [`materials/prompts/app-build-example.md`](materials/prompts/app-build-example.md) | A recorded run of two real assignments, with inputs and the app's own output screenshots |
| [`materials/evaluation/everyday-bureaucracy-analysis.md`](materials/evaluation/everyday-bureaucracy-analysis.md) | Full redesign output for a reflective applied assignment, at a 60% AI-grade ceiling |
| [`materials/evaluation/exploratory-research-analysis.md`](materials/evaluation/exploratory-research-analysis.md) | Full redesign output for a source-based research assignment, at a 70% ceiling |
| [`materials/media/`](materials/media) | Screenshots of the interface and of both analyses |

## The design point worth teaching

Read the two worked analyses side by side and the pattern is unmistakable. The redesigns move points
toward **evidence a model cannot fabricate**:

> *"Names a specific street-level bureaucrat encountered personally — named school, DMV, clinic —
> explains the concrete interaction, and links it to Lipsky's definition."*
>
> *"References at least two specific numeric values from the provided OPM data table with correct
> years and departments."* — because AI cannot reliably access or fabricate figures from an attached
> dataset.

And away from what reads as quality but is cheap to generate: fluent structure, general accuracy,
correct formatting.

The most honest move in the whole output is a criterion the tool leaves at low weight and annotates
**"AI-completable."** Not every criterion can be defended. Knowing which ones cannot is itself the
finding.

**The grade ceiling you set is a pedagogical decision, not a setting.** The two examples use 60% and
70% deliberately and get materially different advice as a result. Decide what the assignment is for
before you pick the number.

## How to use it

1. **Open the [published app](https://quick.aws.com/sn/accounts/905896282634/apps/98715fae-6c9f-41e2-add3-e883ca50d9a3/public/AI-Proofing-Assistant).**
   Nothing to download to try it.
2. **Read [`using-the-app.md`](materials/setup/using-the-app.md)** for the workflow, the three
   redesign levels, and the limits.
3. **Read one worked analysis first.** Seeing what a real redesign looks like sets your expectations
   correctly before you run your own.
4. **Bring one assignment as text**, with its rubric. Output quality tracks input specificity.
5. **Review every recommendation** against course outcomes, accessibility needs, disciplinary
   expectations, workload, and institutional policy before adopting it.

## Related

- [`mlu-000005`](../../professional-student-development/mlu-000005-quick-assessment-demos) — a
  90-minute facilitated session in which an AI-proofing step sits between writing a rubric and
  grading against it. This app is the tool that segment demonstrates.
- [`mlu-000009`](../../course-elements/mlu-000009-project-oracle-ir-lab) — the same author's
  student-facing work on the inverse problem: teaching learners to use and disclose AI honestly.

## Reuse and attribution

Documentation is `CC-BY-4.0`. See [`LICENSE.md`](LICENSE.md) and [`CITATION.cff`](CITATION.cff).

The app itself is a hosted Amazon Quick application, linked rather than bundled — a Quick app is a
live hosted object, not a file. This contribution publishes the documentation, the worked examples,
and the recorded output.

The two example assignments are the author's own teaching material. **No student work or student
records appear anywhere in this contribution.** This repository is not an AWS product, endorsement,
or institutional policy statement; AWS and Amazon product names and trademarks remain the property
of their respective owners.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
