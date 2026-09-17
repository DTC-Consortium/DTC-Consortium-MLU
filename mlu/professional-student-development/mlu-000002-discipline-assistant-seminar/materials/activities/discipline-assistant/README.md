# Faculty AI — Discipline-Specific AI Teaching Assistant

**Build a grounded, source-citing AI tutor for your own field — in about 15 minutes.**

This is the technical lab of the set. It teaches **how RAG (Retrieval-Augmented Generation)
actually works** — chunking, embeddings, vector search, grounding — by having you build a tutor
that answers only from a real document in your discipline and cites the passage it used.

The design idea in one line: **grounding is what separates a tutor from a plausible-sounding
stranger.** You see the difference directly, because the notebook asks the same question with and
without the source material.

## At a glance

| | |
|---|---|
| **Audience** | Faculty who want to understand and modify the tooling, not just use it |
| **Time** | ~10–15 minutes end to end |
| **Runs on** | **Google Colab + free Hugging Face account** (no AWS), *or* SageMaker Studio + Bedrock |
| **Sample data** | Ships with 6 discipline PDFs — runs out of the box, no prep |
| **You end with** | A working, citing tutor plus generated quiz questions, study guides, and rubrics |

By the end of either notebook you have a tutor that:

1. **Knows your discipline's content** — grounded in a real document from your field
2. **Cites its sources** — every answer traceable to a passage
3. **Generates ready-to-use teaching artifacts** — quiz questions, study guides, grading rubrics
4. **Travels with you** — download the notebook, swap in new documents any time

## Where this fits

This is lab **2 of 4** in the AWS-MLU faculty sequence. The
[Curriculum Embedding Lab](../../../../../professional-student-development/mlu-000001-curriculum-embedding-lab) establishes *where* AI fits in a
course; this one opens the hood and shows *how* it works. The participation and grading labs then
apply the same retrieval stack to real instructional work.

**This is the most adaptable asset in the set** — the Colab path needs no AWS account at all,
which matters because most faculty lose cloud access once a seminar ends.

## Pick your path

Two notebooks, same lab. Pick whichever matches your situation:

| Your situation | Notebook | Setup |
|---|---|---|
| **No AWS access** (most faculty) | `discipline-assistant-colab.ipynb` | Google Colab + free Hugging Face account |
| You have ongoing AWS / SageMaker access | `discipline-assistant.ipynb` | SageMaker Studio + Bedrock |

The Colab version is a few minutes slower per run but completely free and works in any browser.
Neither notebook depends on the other, and neither needs `mlu_utils/` — both are fully
self-contained, unlike the other three labs.

## Quick start — Colab + Hugging Face (recommended)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/DTC-Consortium/DTC-Consortium-MLU/blob/main/mlu/professional-student-development/mlu-000002-discipline-assistant-seminar/materials/activities/discipline-assistant/discipline-assistant-colab.ipynb)

1. **Click the badge above** to open the notebook in Colab.
2. Sign in with your Google account.
3. Create a free [Hugging Face account](https://huggingface.co/join) if you don't have one.
4. Generate a free [HF API token](https://huggingface.co/settings/tokens) with **read** access.
5. **Run cells top to bottom** (Parts 1–4). Part 2 downloads a sample document for you.

Under the hood: **Mistral 7B Instruct** (LLM, via HF's free Inference API),
**sentence-transformers/all-MiniLM-L6-v2** (embeddings, runs locally in Colab — no API),
**FAISS** (vector store), **LangChain** (orchestration).

## Quick start — SageMaker + Bedrock

1. **Open SageMaker Studio** in JupyterLab mode.
2. **Clone this repo** — Git icon → **Clone a Repository**.
3. **Open `discipline-assistant.ipynb`** and run cells top to bottom (Parts 1–5).
4. It runs out of the box on a bundled persona PDF; swap in another from `data/` any time.

Under the hood: **Amazon Nova Lite** (LLM) and **Amazon Nova Multimodal Embeddings**, both via
Bedrock, plus **FAISS** and **LangChain** — the same stack as the other three labs.

## Running on your own material

Drop a **text-based** PDF into `data/` (Colab: upload it to the session, or point the Part 2
`curl` at your own URL) and update the path variable in Part 2 or 3. Keep it under ~50 pages, and
make sure it is not a scan — `PyPDFLoader` cannot read image-only PDFs.

## The six sample documents

One per discipline persona, shared with the curriculum lab so a participant sees familiar
material across both labs:

| # | Field | File |
|---|---|---|
| 1 | Dentistry — Periodontics | `persona1_dentistry_perio_case.pdf` |
| 2 | Computer Science — Data Structures | `persona2_cs_data_structures.pdf` |
| 3 | English Literature — Victorian | `persona3_english_victorian_essay.pdf` |
| 4 | Nursing — Pharmacology | `persona4_nursing_pharmacology.pdf` |
| 5 | Business — Leadership MBA | `persona5_business_leadership_case.pdf` |
| 6 | Biology — Cell Biology Lab | `persona6_biology_lab_protocol.pdf` |

Persona 3 is the one to demo to a skeptical humanities audience: the point is that grounding
*preserves* close reading rather than replacing it.

## What's in this repo

```
mlu-000002-discipline-assistant-seminar/    ← the contribution root
├── README.md                              ← overview, metadata, and how to cite
├── mlu-contribution.yml                   ← structured metadata
├── CHANGELOG.md · LICENSE.md · CITATION.cff
└── materials/
    ├── activities/discipline-assistant/       ← you are here; run the lab from this folder
    │   ├── README.md                          ← this file
    │   ├── requirements.txt                   ← pinned packages for the SageMaker path only
    │   ├── discipline-assistant-colab.ipynb   ← Colab + Hugging Face notebook (Parts 1–4, no AWS)
    │   ├── discipline-assistant.ipynb         ← SageMaker + Bedrock notebook (Parts 1–5)
    │   └── data/
    │       ├── README.md                      ← per-file provenance and licensing
    │       └── persona1..6_*.pdf              ← 6 sample documents, one per persona
    ├── agenda/
    │   └── SEMINAR_PLAN.md                    ← agenda and design decisions
    └── facilitator-guide/
        ├── INSTRUCTOR_CHEATSHEET.md           ← the one-pager to hold while teaching
        ├── PREFLIGHT_CHECKLIST.md             ← setup checks before delivery
        ├── CONTENT_AUDIT.md                   ← why the lab is shaped this way
        └── POST_SEMINAR_LABS.md               ← menu of 17 follow-on labs
```

There is no `mlu_utils/` here by design — both notebooks are self-contained so the Colab path
works from a single file with nothing else cloned.

## What you need

**Colab + Hugging Face path:**
- A Google account (for Colab)
- A free Hugging Face account and read-access API token
- A modern browser — nothing installed

**SageMaker + Bedrock path:**
- AWS account with **Amazon Bedrock** model access for `amazon.nova-lite-v1:0` and
  `amazon.nova-2-multimodal-embeddings-v1:0`
- **SageMaker Studio**, Python 3 (Data Science) kernel, `ml.t3.medium` or larger
- Region: `us-east-1`

## For instructors — before you teach this

Read `instructor/` in this order:

1. **`CONTENT_AUDIT.md`** — why the lab is shaped this way.
2. **`SEMINAR_PLAN.md`** — agenda and the locked design decisions.
3. **`PREFLIGHT_CHECKLIST.md`** — run before delivery.
4. **`INSTRUCTOR_CHEATSHEET.md`** — the one-pager to keep open while teaching.

These were written when this lab was the seminar's afternoon session. It has since been replaced
in that slot by the [Curriculum Embedding Lab](../../../../../professional-student-development/mlu-000001-curriculum-embedding-lab), so treat the
agenda timings as reference rather than a current run of show — the technical content and the
preflight checks are still accurate.

**Test the Colab path on the day.** It depends on Hugging Face's free tier, which rate-limits
during peak hours. If you are teaching to a large group, have participants stagger their runs, or
run the SageMaker path instead.

## Privacy and ethics

This lab runs entirely on the bundled open-licence sample documents or on teaching material you
choose. It does **not** touch student records — unlike the participation and grading labs.

- **Don't upload student work.** Use your own teaching material if you swap in a document.
- **The Colab path sends your document to a third-party API.** Hugging Face's Inference API
  processes the text you send it. Use published or openly licensed material there, not anything
  confidential or FERPA-protected.
- **Grounding reduces hallucination; it does not eliminate it.** Every generated teaching
  artifact still needs your eye before it reaches a student.

## Troubleshooting

| Issue | Path | Fix |
|---|---|---|
| `AccessDeniedException` invoking model | SageMaker | Bedrock model access not enabled — enable Nova Lite + Nova Multimodal Embeddings in the Bedrock console |
| HF rate-limit errors | Colab | Wait a few minutes; the HF free tier limits requests during peak hours |
| `huggingface_hub.errors.GatedRepoError` | Colab | The model needs approval — switch to a non-gated model, e.g. `Qwen/Qwen2.5-7B-Instruct` |
| Embeddings run slow on the first cell | Colab | First run downloads the model (~90 MB); later runs are fast |
| Embedding cell hangs > 90 sec | SageMaker | PDF is too large — use an excerpt under ~50 pages |
| `Could not load PDF` / 0 pages | Both | The PDF is a scan with no text layer — `PyPDFLoader` can't read it |
| Kernel disconnected | Both | Restart the kernel and re-run the setup cells |

## What to do next

`POST_SEMINAR_LABS.md` is a menu of **17 follow-on labs** — quick wins, extensions of what you
just built, and deeper paths (multi-document tutors, conversational memory, custom assessment
generators, agentic versions).

## Built on

This lab adapts components from the
[AWS MLU EEP Generative AI](https://github.com/aws-samples/aws-mlu-eep-generative-ai) curriculum —
specifically the RAG patterns from Module 3 Lab 3a. Recommended next reads in that curriculum:
Module 3 Lab 2 (Chatbots), Module 3 Lab 4 (Agents), Module 2 Lab 4 (Debiasing & Watermarking).

## Related labs

- [Curriculum Embedding Lab](../../../../../professional-student-development/mlu-000001-curriculum-embedding-lab) — where AI fits in your course. Start here.
- [Class Participation Scoring Lab](../../../../../ml-ai-applications/mlu-000003-participation-scoring) — score participation from a Zoom transcript.
- [Paper Autograding Lab](../../../../../ml-ai-applications/mlu-000004-paper-autograder) — draft rubric-based grades for a stack of papers.
- [PartyRock Tutor Template](https://github.com/aws-dsu/mlu-faculty-ai-partyrock-template) — the no-code path.
