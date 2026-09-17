# Faculty AI — Class Participation Scoring Lab

**Score a day's class participation from a Zoom transcript — grounded in the lesson you actually taught.**

Point this notebook at a Zoom transcript of one class meeting and the material you covered that
day. It identifies who spoke, judges what they talked about (on-topic vs. off-topic, grounded
*only* in your lesson), and drafts a **0–4 participation score** for each student — with the
evidence and reasoning behind every score, for you to review.

The scoring logic in one line: **talk a lot and on-topic → high; talk a lot but off-topic → low;
don't speak → 0.**

> ⚠️ **Read this before anything else.** This produces a **draft you review**, not a grade the
> tool assigns on its own. Class recordings and transcripts are student records — make sure
> recording and transcription are covered by your institution's policy and that students were
> notified (FERPA in the US, or your local equivalent). See [Privacy and ethics](#privacy-and-ethics)
> below, the contract at the top of the notebook, and Part 7.

## At a glance

| | |
|---|---|
| **Audience** | Faculty scoring participation in a discussion-based course |
| **Time** | ~10 minutes of compute on the bundled sample. Part 5 review is the real cost and scales with class size. |
| **Runs on** | SageMaker Studio + Amazon Bedrock |
| **Sample data** | Ships with a fabricated transcript, roster, and lesson PDF — runs out of the box |
| **You end with** | A reviewed 0–4 score per student, with evidence, exported as `.md` + `.csv` |

## Where this fits

This is lab **3 of 4** in the AWS-MLU faculty sequence, and the first that touches real student
records. It reuses the exact same stack as the
[Curriculum Embedding Lab](../../../../professional-student-development/mlu-000001-curriculum-embedding-lab) — Amazon Bedrock + **Nova Lite**, the
`NovaMultimodalEmbeddings` helper, **FAISS**, **LangChain**, and SageMaker Studio. If you ran
either of the first two labs, this environment is already familiar.

The key idea it borrows: **"on topic" needs a reference for what the topic is.** So the same
retrieval stack that grounds the curriculum lab's tutor grounds this lab's relevance judgment —
your day's lesson material is embedded, and each student's words are scored against it.

## How a score is built

Each student's score combines three signals:

1. **Quantity** — how much they spoke (turns, words, talk time). Computed directly from the transcript.
2. **Topical relevance** — how much of their talk is on-topic, judged against your embedded lesson
   material. This is what separates a chatty-but-off-topic student from a chatty-and-on-topic one.
3. **Substance** — questions, reasoning, and building on peers vs. filler ("yeah", "agreed") and
   logistics ("is this on the exam?").

The 0–4 rubric:

| Tier | Means |
|:---:|---|
| **4** | Substantive **and** on-topic leadership — probing questions, reasoning, building on peers |
| **3** | Solid on-topic contribution, but not driving the discussion |
| **2** | Some on-topic participation, possibly brief or surface-level |
| **1** | Minimal or off-topic — filler, logistics, or social chatter (even a lot of it) |
| **0** | Did not participate |

Brevity is **not** penalized — one sharp, on-topic question can score a 3 or 4. Volume of
off-topic talk does **not** earn points.

## Quick start

1. **Open SageMaker Studio** in JupyterLab mode.
2. **Clone this repo** — Git icon → **Clone a Repository**.
3. **Open `participation-scoring-lab.ipynb`** and run cells top to bottom (Parts 1–7).
4. It runs out of the box on the bundled sample — a fabricated CS Data Structures class. Then
   swap in your own material.

## Running on your own class

Three values in the notebook:

- **`LESSON_PDF`** (Part 2) — the day's material as a text-based PDF (lecture notes, the reading,
  slides exported to PDF, the chapter).
- **`TRANSCRIPT_PATH`** (Part 3) — your Zoom transcript. Zoom exports these under
  **Recording → Audio Transcript** as a `.vtt` (or `.txt`). Both formats parse.
- **`ROSTER_PATH`** (Part 3, optional) — a CSV with a `student_name` column. With a roster,
  students who attended but never spoke are flagged and scored **0**. Without one, the notebook
  can only score students who actually spoke.

You review and adjust every score in **Part 5**, then export a dated `.md` report and `.csv` in
**Part 6**.

## What's in this repo

```
mlu-000003-participation-scoring/           ← the contribution root
├── README.md                              ← overview, metadata, and how to cite
├── mlu-contribution.yml                   ← structured metadata
├── CHANGELOG.md · LICENSE.md · CITATION.cff
└── materials/
    ├── src/                                   ← you are here; run the tool from this folder
    │   ├── README.md                          ← this file
    │   ├── requirements.txt                   ← pinned packages (same stack as the curriculum lab)
    │   ├── participation-scoring-lab.ipynb    ← the lab notebook (Parts 1–7)
    │   ├── data/
    │   │   ├── README.md                      ← sample data, bring-your-own, and privacy
    │   │   ├── persona2_cs_data_structures.pdf← sample lesson material (CC-BY)
    │   │   ├── sample_class_transcript.vtt    ← sample Zoom transcript (fabricated)
    │   │   └── sample_roster.csv              ← sample roster (fabricated)
    │   └── mlu_utils/
    │       ├── embeddings.py                  ← Bedrock embeddings helper (shared across the labs)
    │       └── transcript_tools.py            ← transcript parsing + scoring (this lab's core)
    └── facilitator-guide/
        └── LAB_WALKTHROUGH.md                 ← run of show + expected outputs for the sample
```

## What you need

- AWS account with **Amazon Bedrock** model access for:
  - `amazon.nova-lite-v1:0`
  - `amazon.nova-2-multimodal-embeddings-v1:0`
- **SageMaker Studio** with a Python 3 (Data Science) kernel, `ml.t3.medium` or larger
- Region: `us-east-1`

Same requirements as the curriculum lab — no new dependencies. The transcript parser uses only
Python's standard library.

## For instructors — before you teach this

Read **`instructor/LAB_WALKTHROUGH.md`** first. It carries the run of show and, more importantly,
the **expected output for the bundled sample** — the fabricated transcript is built so every
participation tier appears at least once, so you can tell a working setup from a broken one
before you stand in front of a room.

**Run the bundled sample end to end before every delivery.** The scoring output depends on model
behaviour, which drifts. If the sample's tiers no longer match the walkthrough, investigate before
teaching rather than during.

Teach **Part 5 as the centre of the lab**, not an epilogue. The reviewing is the pedagogy; the
scoring is just what makes reviewing possible at scale.

## Privacy and ethics

This tool reads student speech and assigns a number to it. Treat it accordingly.

- **Consent and policy.** Recording and transcribing a class is governed by your institution's
  policy and notice requirements (FERPA in the US). Don't run this on a recording students
  weren't told about.
- **The score is a draft.** The notebook is built so you review the evidence and adjust every
  score before it counts. Never wire the raw output straight into a gradebook.
- **Participation ≠ talking.** Quiet students, students processing in a second language, and
  students who contribute in writing are not disengaged. Use this as one signal among several,
  and let Part 5's equity check do its job.
- **Garbage in, garbage out.** Auto-transcription mishears names, drops quiet voices, and
  scrambles cross-talk. Transcription error should never cost a student points.

## Troubleshooting

| Issue | Fix |
|---|---|
| `AccessDeniedException` invoking model | Bedrock model access not enabled — enable Nova Lite + Nova Multimodal Embeddings in the Bedrock console |
| Embedding cell hangs > 90 sec | `LESSON_PDF` is too large — use a smaller excerpt (under ~50 pages) |
| A student who clearly spoke is missing | Their name in the transcript doesn't match the roster — check spelling, or set `ROSTER_PATH = None` to score everyone who spoke |
| A real student shows as "silent" | Zoom labeled their speech under a different display name (a nickname or device name) — rename in the transcript or roster so they match |
| Instructor/TA appears in the score list | They're matching a roster entry — make sure they're **not** on the roster CSV; they'll then be flagged "not scored" |
| Loads 0 pages / garbled lesson text | The PDF is a scan — `PyPDFLoader` can't read image-only PDFs. Use a text-based PDF |
| `⚠️ re-run` in the tier column | The model returned malformed JSON for that student — just re-run the Part 4 cell |

## Related labs

- [Curriculum Embedding Lab](../../../../professional-student-development/mlu-000001-curriculum-embedding-lab) — where AI fits in your course. Start here.
- [Discipline-Specific AI Teaching Assistant](../../../../professional-student-development/mlu-000002-discipline-assistant-seminar) — how RAG works under the hood, with a free no-AWS path.
- [Paper Autograding Lab](../../../../ml-ai-applications/mlu-000004-paper-autograder) — the sibling lab; drafts rubric-based grades for written work.
- [PartyRock Tutor Template](https://github.com/aws-dsu/mlu-faculty-ai-partyrock-template) — the no-code path.
