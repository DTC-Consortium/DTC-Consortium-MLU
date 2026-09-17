# Faculty AI — Curriculum Embedding Lab

**Decide where AI fits in *your* course — and where it doesn't.**

This is **not** a technical lab. There is some Python, but you are not learning to code. You use a
working AI tool, built around a persona from your own discipline, to locate exactly where AI
belongs in a course you actually teach — and to write down where it does not.

The design idea in one line: **the tool is not the deliverable — the decision is.** A faculty
member leaves with a plan and a boundary, not just a demo they watched.

## At a glance

| | |
|---|---|
| **Audience** | Faculty and academic staff. No coding experience required. |
| **Time** | ~90 minutes (Parts 0–7). Originally the seminar's 1:30–3:00 PM afternoon lab. |
| **Runs on** | SageMaker Studio + Amazon Bedrock |
| **Sample data** | Ships with 6 discipline PDFs — runs out of the box, no prep |
| **You end with** | A working tool, a written curriculum plan, an explicit "not here" boundary, and a dated commitment |

By the end, a participant walks out with four things:

1. A working AI tool tailored to their persona's vision
2. A written curriculum plan — course, week, assignment, what AI does, what they still do
3. An explicit boundary for where AI does **not** belong in their teaching
4. A dated Monday-morning commitment to one specific action

## Where this fits

This is the **entry point** of the four-lab AWS-MLU faculty sequence, and the one to run first.
It establishes *where AI fits* before any of the other labs show *how it works* or put it to
work on real student records.

All four labs share one stack — Amazon Bedrock + Nova Lite, the `NovaMultimodalEmbeddings`
helper in `mlu_utils/embeddings.py`, FAISS, LangChain, and SageMaker Studio. Run this one and
the environment for the other three is already familiar.

## Two notebooks in this repo

| Notebook | Audience | Purpose |
|---|---|---|
| **`curriculum-embedding-lab.ipynb`** | Faculty | Decide where AI fits in your course — the main lab, described throughout this README |
| **`study-mastery-lab.ipynb`** | **Students** | A grounded study tool you can hand directly to students. See [For students](#for-students-the-study--mastery-partner-lab). |

Both run in the same environment and share `mlu_utils/`. Everything below describes the faculty
lab unless noted.

## Quick start

1. **Open SageMaker Studio** in JupyterLab mode. In a facilitated session your instructor gives
   you the URL; on your own, open it from the SageMaker console in your AWS account.
2. **Clone this repo** — Git icon in the sidebar → **Clone a Repository**.
3. **Open `curriculum-embedding-lab.ipynb`.**
4. **Set your persona** in Part 0 — one line, `persona = "1"`. Change `"1"` to `"2"`–`"6"` to
   match your discipline. It runs out of the box on persona 1.
5. **Run cells top to bottom** through Parts 0–7.
6. **Don't skip the writing cells.** They matter more than the code cells.

## How this lab is different from a normal coding lab

There are two kinds of cells:

- **Watch-along code cells** (Part 1, parts of Part 2) — the instructor runs these; no edits needed.
- **🟢 EDIT ME cells** — you fill in values: your persona, your course, your commitment.

A blank reflection cell means a missing plan. **Don't leave them blank.**

## The six personas

Each persona is a documented faculty problem plus a matched sample document, so nobody has to
bring their own material on day one. Pick the closest fit — it does not have to be exact.

| # | Persona | Field | Tool you build | Sample document |
|---|---|---|---|---|
| 1 | Dr. Maya Patel | Dentistry — Periodontics | Case Study Coach (3-level patient vignettes) | `persona1_dentistry_perio_case.pdf` |
| 2 | Prof. James Chen | Computer Science — Data Structures | Code Critique Generator (Socratic, no-answer) | `persona2_cs_data_structures.pdf` |
| 3 | Dr. Sarah Whitman | English Literature — Victorian Lit | Primary Source Companion (no plot-summary prompts) | `persona3_english_victorian_essay.pdf` |
| 4 | Prof. Diane Okafor | Nursing — Pharmacology | Med-Calc Drill (dosing problems with safety red-flags) | `persona4_nursing_pharmacology.pdf` |
| 5 | Dr. Marcus Reyes | Business — Leadership MBA | Stakeholder Roleplay (AI plays CFO/CMO from the case) | `persona5_business_leadership_case.pdf` |
| 6 | Dr. Lena Hoffmann | Biology — Cell Biology Lab | Pre-Lab Knowledge Gate (quiz students must pass) | `persona6_biology_lab_protocol.pdf` |

Persona 3 is deliberately the **AI-skeptic** of the set — the tool has to demonstrate that
grounding *preserves* close-reading discipline rather than replacing it. If you are adapting this
for a humanities-heavy audience, start there.

## Running on your own course material

The lab is designed to run on the bundled samples, but you can swap in your own:

- Drop a **text-based** PDF into `data/` (not a scan — `PyPDFLoader` cannot read image-only PDFs).
- Keep it under ~50 pages; the notebook's embedding budget assumes it.
- Point the persona's `default_pdf` at your file, or set `SOURCE_PDF` in the student lab.

## What's in this repo

```
mlu-000001-curriculum-embedding-lab/        ← the contribution root
├── README.md                              ← overview, metadata, and how to cite
├── mlu-contribution.yml                   ← structured metadata
├── CHANGELOG.md · LICENSE.md · CITATION.cff
└── materials/
    ├── activities/curriculum-embedding-lab/   ← you are here; run the lab from this folder
    │   ├── README.md                          ← this file
    │   ├── requirements.txt                   ← pinned Python packages
    │   ├── curriculum-embedding-lab.ipynb     ← faculty lab notebook (Parts 0–7)
    │   ├── study-mastery-lab.ipynb            ← student lab notebook (Parts 0–7)
    │   ├── data/
    │   │   ├── README.md                      ← per-file provenance and licensing
    │   │   └── persona1..6_*.pdf              ← 6 sample documents, one per persona
    │   └── mlu_utils/
    │       ├── embeddings.py                  ← Bedrock embeddings helper (shared by all four labs)
    │       └── study_tools.py                 ← study-mode prompts (student lab)
    ├── agenda/
    │   └── SEMINAR_PLAN.md                    ← full agenda and design decisions
    └── facilitator-guide/                     ← run-of-show docs — not for participants
        ├── LAB_WALKTHROUGH.md                 ← what to say, part by part
        ├── INSTRUCTOR_CHEATSHEET.md           ← the one-page version to hold while teaching
        ├── PREFLIGHT_CHECKLIST.md             ← morning-of setup checks
        ├── CONTENT_AUDIT.md                   ← why this lab exists in this form
        ├── BRIDGE_AND_LAB_DECK_SPEC.md        ← slide spec for the lab intro
        ├── persona_smoketest.py               ← run all 6 personas before teaching
        └── persona_test_outputs/              ← recorded known-good output per persona
```

The notebooks, `data/`, and `mlu_utils/` are kept together on purpose: the notebooks
reference them by relative path, so the lab runs unchanged from `activities/`.

## What you need

- AWS account with **Amazon Bedrock** model access for:
  - `amazon.nova-lite-v1:0`
  - `amazon.nova-2-multimodal-embeddings-v1:0`
- **SageMaker Studio** with a Python 3 (Data Science) kernel, `ml.t3.medium` or larger
- Region: `us-east-1`

If you are a participant, your instructor has handled all of this — ask them rather than
troubleshooting AWS during the lab.

## For instructors — before you teach this

Read `instructor/` in this order. It takes about 45 minutes and is the difference between
running this lab and re-deriving it:

1. **`CONTENT_AUDIT.md`** — why the lab is shaped this way. Read first.
2. **`SEMINAR_PLAN.md`** — the full agenda and the locked design decisions.
3. **`LAB_WALKTHROUGH.md`** — the run of show, part by part. This is what you carry into the room.
4. **`PREFLIGHT_CHECKLIST.md`** — run on the morning of.
5. **`INSTRUCTOR_CHEATSHEET.md`** — the one-pager to keep open while teaching.

**Run `instructor/persona_smoketest.py` before every delivery.** It exercises all six personas
end to end; compare against the recorded output in `instructor/persona_test_outputs/` to catch
model or dependency drift before a room full of faculty finds it for you.

## What this lab is NOT

- **Not a technical deep-dive on RAG, vector stores, or LangChain.** That is the
  [Discipline-Specific AI Teaching Assistant](../../../../../professional-student-development/mlu-000002-discipline-assistant-seminar) lab.
- **Not a coding tutorial.** You will see about five cells of Python and do not need to
  understand them. The writing cells matter more.
- **Not a sales pitch for AI.** Part 4 explicitly asks you to articulate where AI does **not**
  belong in your teaching. That is intentional, and it is the part most worth protecting when
  you run short on time.

## For students: the Study & Mastery Partner lab

`study-mastery-lab.ipynb` is a **student-facing** companion — a grounded study tool. Students
point it at their own course material and use three modes:

- **Quiz Me** — a practice quiz generated from the material, with a hidden answer key to self-test against.
- **Socratic Hint** — paste a problem you are stuck on; it returns the *next question to ask yourself*, never the answer.
- **Explain-Back** — write a concept in your own words and have it checked against the source, so you see your gaps.

It ships with a sample chapter so it runs immediately; students swap in their own PDF by dropping
a file into `data/` and changing one line (`SOURCE_PDF`, Part 2). It ends with an
academic-integrity reflection — **use AI to study, not to do the thinking you are graded on** —
and a take-home study plan.

**What it is NOT:** not a way to get answers to graded work (Socratic and Explain-Back modes
deliberately withhold answers), and not a coding tutorial. It is self-paced and can be run
independently of the seminar.

## Privacy and ethics

This lab runs on bundled sample documents and on course material you choose — it does **not**
touch student records, unlike the participation and grading labs. Two things still apply:

- **Don't upload student work here.** If you swap in your own PDF, use your own teaching
  material — a reading, your lecture notes, a chapter. Not student submissions.
- **The boundary exercise is the point.** Part 4 exists because "where AI does not belong" is a
  judgment only the instructor can make. Don't cut it for time.

## Troubleshooting

| Issue | Fix |
|---|---|
| `AccessDeniedException` invoking model | Bedrock model access not enabled — enable Nova Lite + Nova Multimodal Embeddings in the Bedrock console |
| Embedding cell hangs > 90 sec | Source PDF is too large — use an excerpt under ~50 pages |
| `No such file or directory` for a PDF | Wrong persona number in Part 0, or the file isn't in `data/` — check the file browser on the left |
| Kernel disconnected | Restart the kernel and re-run from Part 1 |
| _(student lab)_ `No such file or directory` for your PDF | Your file isn't in `data/`, or `SOURCE_PDF` doesn't match its filename |
| _(student lab)_ Loads 0 pages / garbled text | Your PDF is a scan, not text — `PyPDFLoader` can't read image-only PDFs. Use a text-based PDF |
| _(student lab)_ Socratic Hint gave away the answer | A known limitation of smaller models — re-run the cell; don't trust a leaked answer blindly |

## After the lab

The downloaded artifact (`my_curriculum_plan_*.md`) is yours. The two most effective things to do
with it:

1. **Email it to yourself** with the subject `Monday morning AI commitment`. Calendar reminders
   get ignored; emails do not.
2. **Tell one colleague** what you committed to. Social accountability is the strongest
   commitment device available.

## Related labs

- [Discipline-Specific AI Teaching Assistant](../../../../../professional-student-development/mlu-000002-discipline-assistant-seminar) — how RAG actually works, with a free no-AWS Colab path.
- [Class Participation Scoring Lab](../../../../../ml-ai-applications/mlu-000003-participation-scoring) — score participation from a Zoom transcript.
- [Paper Autograding Lab](../../../../../ml-ai-applications/mlu-000004-paper-autograder) — draft rubric-based grades for a stack of papers.
- [PartyRock Tutor Template](https://github.com/aws-dsu/mlu-faculty-ai-partyrock-template) — the no-code path to the same six persona tools.
