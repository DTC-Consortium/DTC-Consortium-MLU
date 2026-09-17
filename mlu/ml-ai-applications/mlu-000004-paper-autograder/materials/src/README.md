# Faculty AI — Paper Autograding Lab

**Draft a rubric-based grade for a stack of student papers — grounded in the course material you actually taught.**

Point this notebook at your course material, a grading rubric, and a folder of student papers. For
each paper it scores every rubric criterion, backs each score with quotes from the paper, computes
a **weighted overall grade**, and drafts **two sets of notes** — one for you explaining *why* it
landed where it did, and one you can hand back to the student.

The grading logic in one line: **score each criterion against your rubric, judge "did they use the
concepts correctly" only against your material, then let the weights do the arithmetic — in code,
not in the model.**

> ⚠️ **Read this before anything else.** This produces a **draft you review**, not a grade the
> tool assigns on its own. Student papers are student records — handle them under your
> institution's policy (FERPA in the US, or your local equivalent). And this is **not** a
> plagiarism or AI-writing detector: never use its output in an academic-integrity decision. See
> [Privacy and ethics](#privacy-and-ethics), the overview at the top of the notebook, and Part 7.

## At a glance

| | |
|---|---|
| **Audience** | Faculty grading written work against a rubric |
| **Time** | ~5 minutes of compute on the bundled 3-paper sample. Part 5 review is the real cost and scales with stack size. |
| **Runs on** | SageMaker Studio + Amazon Bedrock, **or fully local via Ollama — no AWS, nothing leaves your laptop** |
| **Sample data** | Ships with 3 fabricated papers, a rubric, a roster, and course material — runs out of the box |
| **You end with** | A reviewed weighted grade per student, with quoted evidence, exported as `.csv`, `.md`, and per-student feedback files |

## Where this fits

This is lab **4 of 4** in the AWS-MLU faculty sequence — a sibling of the
[Class Participation Scoring Lab](../../../../ml-ai-applications/mlu-000003-participation-scoring) and the
[Curriculum Embedding Lab](../../../../professional-student-development/mlu-000001-curriculum-embedding-lab). It reuses the exact same stack —
Amazon Bedrock + **Nova Lite**, the `NovaMultimodalEmbeddings` helper, **FAISS**, **LangChain**,
and SageMaker Studio. If you ran either lab, this environment is already familiar.

The key idea it borrows: **"correct" and "on-topic" need a reference for what the topic is.** The
same retrieval stack that grounds the participation lab's relevance judgment grounds this lab's
grading — your course material is embedded, and each paper is judged against *what you taught*,
not against the model's own knowledge of the subject.

## How a grade is built

Each paper's grade combines, per rubric criterion:

1. **A tier (0–4)** picked against your rubric's own descriptors for that criterion.
2. **Grounded correctness** — where a criterion is about *using the course concepts correctly*,
   the judgment is made only against your embedded material, retrieved for the parts of the
   material this paper actually engages. A confident, well-written paper that misuses the concepts
   scores **lower** on those criteria, not higher.
3. **Evidence** — 1–2 verbatim quotes from the paper behind every tier, plus a one-sentence
   rationale for you and a one-sentence actionable note for the student.

The **overall grade** is then computed **in code** from the tiers and your criterion weights
(normalized to sum to 100), and mapped to a letter via configurable bands. The model never does
the arithmetic.

## Quick start

1. **Open SageMaker Studio** in JupyterLab mode.
2. **Clone this repo** — Git icon → **Clone a Repository**.
3. **Open `paper-grading-lab.ipynb`** and run cells top to bottom (Parts 1–7).
4. It runs out of the box on the bundled sample — three fabricated papers for a CS Data Structures
   assignment, plus a roster with a non-submitter. Then swap in your own.

The notebook ships with `PROVIDER = "bedrock"` in Part 1. To run without AWS, see below.

## Run it locally, no AWS (Ollama)

The whole pipeline is provider-agnostic — only the two model calls touch AWS. Set
**`PROVIDER = "ollama"`** in Part 1 and the lab runs entirely on your own machine, nothing leaving
your laptop. Good for trying it out, for privacy-sensitive drafts, or if you don't have Bedrock
access.

1. Install [Ollama](https://ollama.com) and start it (`ollama serve`).
2. Pull the two models:
   ```
   ollama pull qwen2.5:7b        # the grader (qwen2.5:14b is better if your RAM allows)
   ollama pull nomic-embed-text  # the embeddings
   ```
3. `pip install -r requirements.txt` (includes `langchain-ollama`).
4. In Part 1, set `PROVIDER = "ollama"` and run top to bottom.

Two things to know:

- **Context window.** The notebook sets `num_ctx=8192` on the model — this is essential. Ollama
  defaults to 2048 tokens, which silently truncates the paper + rubric and grades garbage.
- **Grading quality is model-dependent.** A local 7B model is a real step down from Nova Lite at
  the nuanced "fluent-but-wrong" discrimination, and smaller models tend to grade harsher. Treat
  local grades as a rougher draft and lean harder on Part 5. `qwen2.5:14b` closes much of the gap
  if you can run it.

The bundled sample grades on `qwen2.5:7b` in well under a minute on a modern laptop.

## Running on your own assignment

Four values (Parts 2–3 of the notebook):

- **`LESSON_PDF`** (Part 2) — the course material as a text-based PDF: the reading, lecture notes,
  the chapter, slides exported to PDF. This is the ground truth for "used the concepts correctly."
- **`RUBRIC_PATH`** (Part 3) — a structured rubric. Open **`data/sample_rubric.py`** and edit it in
  place; it's plain Python — criteria, weights, and 0–4 descriptors, readable top to bottom. (A
  `.json` rubric of the same shape works too.)
- **`PAPERS_DIR`** (Part 3) — a folder with **one file per student**. The filename becomes the
  student's name (`Aisha_Rahman.pdf` → "Aisha Rahman"). `.pdf`, `.docx`, `.txt`, and `.md` all parse.
- **`ROSTER_PATH`** (Part 3, optional) — a CSV with a `student_name` column. With a roster,
  enrolled students who submitted **no paper** are flagged **missing**, and a paper whose name
  matches nobody is flagged **off-roster** (a misnamed file). Without one, only students who
  submitted are visible.

You review and adjust every grade in **Part 5**, then export a dated `.csv`, a `.md` record, and
per-student feedback files in **Part 6**.

## What's in this repo

```
mlu-000004-paper-autograder/                ← the contribution root
├── README.md                              ← overview, metadata, and how to cite
├── mlu-contribution.yml                   ← structured metadata
├── CHANGELOG.md · LICENSE.md · CITATION.cff
└── materials/
    ├── src/                                   ← you are here; run the tool from this folder
    │   ├── README.md                          ← this file
    │   ├── requirements.txt                   ← shared stack + python-docx + langchain-ollama
    │   ├── paper-grading-lab.ipynb            ← the lab notebook (Parts 1–7)
    │   ├── data/
    │   │   ├── README.md                      ← sample data, bring-your-own, and privacy
    │   │   ├── persona2_cs_data_structures.pdf← sample course material (CC-BY)
    │   │   ├── sample_rubric.py               ← sample structured rubric (edit this)
    │   │   ├── sample_roster.csv              ← sample roster (fabricated)
    │   │   └── sample_papers/                 ← three fabricated sample papers
    │   │       ├── Aisha_Rahman.txt           ←   strong, on-topic
    │   │       ├── Marcus_Lee.txt             ←   confident but conceptually wrong
    │   │       └── Priya_Chandra.txt          ←   off-topic / reflection, not analysis
    │   └── mlu_utils/
    │       ├── embeddings.py                  ← Bedrock embeddings helper (shared across the labs)
    │       └── paper_tools.py                 ← paper loading + rubric + grading (this lab's core)
    ├── evaluation/
    │   └── sample-output-2026-07-31/          ← a recorded sample run, for comparison
    └── facilitator-guide/
        └── LAB_WALKTHROUGH.md                 ← run of show + expected outputs for the sample
```

## What you need

- AWS account with **Amazon Bedrock** model access for:
  - `amazon.nova-lite-v1:0`
  - `amazon.nova-2-multimodal-embeddings-v1:0`
- **SageMaker Studio** with a Python 3 (Data Science) kernel, `ml.t3.medium` or larger
- Region: `us-east-1`

Same stack as the participation and curriculum labs, plus **`python-docx`** so `.docx` papers can
be read, and **`langchain-ollama`** for the local path. The paper loaders and rubric use only the
standard library. **Or skip all of the above and use the Ollama path** — no AWS account needed.

## For instructors — before you teach this

Read **`instructor/LAB_WALKTHROUGH.md`** first. It carries the run of show and the **expected
output for the bundled sample**, which is the fastest way to tell a working setup from a broken one.

The sample is built to expose the failure mode that matters, so **teach it deliberately**:

- **`Aisha_Rahman.txt`** — strong and on-topic. Should score high across the board.
- **`Marcus_Lee.txt`** — fluent, confident, and **conceptually wrong**. This is the one to dwell
  on: it must score *lower* on "Use of Course Concepts" than its prose quality suggests. If it
  doesn't, the grounding isn't working — check Part 2 loaded your material.
- **`Priya_Chandra.txt`** — a reflection, not an analysis. On-topic in spirit, but earns no
  concept or evidence points.
- **Diego Alvarez** is on the roster with no paper — surfaces as **missing**, for you to confirm.

`../evaluation/sample-output-2026-07-31/` holds a recorded run of that sample, so you can diff your output against a
known-good one before delivery.

Teach **Part 5 as the centre of the lab**, not an epilogue. The reviewing is the pedagogy.

## Privacy and ethics

This tool reads a student's paper and assigns a number to it. Treat it accordingly.

- **The grade is a draft.** The notebook is built so you review the evidence and adjust every
  grade before it counts. Never wire the raw output straight into a gradebook.
- **Not a plagiarism or AI detector.** It has no idea who wrote the paper or whether it's
  original, and it is not built to guess. Do not use it — or its confidence score — in an
  academic-integrity case.
- **Grounded means grounded in *your* material.** The "used the concepts correctly" judgment is
  only as good as what you load in Part 2. A paper that goes beyond the material is treated as
  neutral, not wrong.
- **Bias and voice.** Automated scoring can penalize multilingual writers, valid-but-unconventional
  structure, and original arguments a rubric didn't anticipate. Use Part 5's fairness check and
  read the low-confidence and low-scoring papers yourself.
- **Consent and policy.** Student papers are protected records (FERPA in the US). Keep them, and
  everything this notebook exports, inside your institution's approved systems. The Ollama path
  exists partly for this reason — nothing leaves your machine.

## Troubleshooting

| Issue | Fix |
|---|---|
| `AccessDeniedException` invoking model | Bedrock model access not enabled — enable Nova Lite + Nova Multimodal Embeddings in the Bedrock console |
| Embedding cell hangs > 90 sec | `LESSON_PDF` is too large — use a smaller excerpt (under ~50 pages) |
| A student who submitted shows as **missing** | Their paper's filename doesn't match the roster name — rename the file (`First_Last.pdf`), or set `ROSTER_PATH = None` |
| A paper shows as **⚠️ unreadable** | The file is a scanned/image PDF with no text layer — `pypdf` can't read it. Ask for a text-based PDF or `.docx`, or grade it by hand |
| Reading a `.docx` raises an ImportError | `python-docx` isn't installed — re-run Part 1, or ask the student for a PDF |
| `⚠️ re-run` in the grade column | The model returned malformed JSON for that paper — just re-run the Part 4 cell |
| Every grade rides on one criterion | Your rubric weights may be lopsided — adjust `weight` in `data/sample_rubric.py` |
| **(Ollama)** `ConnectionError` / connection refused | Ollama isn't running — start it with `ollama serve` |
| **(Ollama)** `model 'x' not found` | Pull it first: `ollama pull qwen2.5:7b` and `ollama pull nomic-embed-text` |
| **(Ollama)** grades look truncated or nonsensical | `num_ctx` too low — keep it at 8192+ so the paper + rubric fit (Ollama's default 2048 truncates them) |
| **(Ollama)** `does not support embeddings` (501) | You pointed `EMBED_MODEL` at a chat model — use a real embedding model like `nomic-embed-text` |

## Related labs

- [Curriculum Embedding Lab](../../../../professional-student-development/mlu-000001-curriculum-embedding-lab) — where AI fits in your course. Start here.
- [Discipline-Specific AI Teaching Assistant](../../../../professional-student-development/mlu-000002-discipline-assistant-seminar) — how RAG works under the hood, with a free no-AWS path.
- [Class Participation Scoring Lab](../../../../ml-ai-applications/mlu-000003-participation-scoring) — the sibling lab; scores spoken participation from a Zoom transcript.
- [PartyRock Tutor Template](https://github.com/aws-dsu/mlu-faculty-ai-partyrock-template) — the no-code path.
