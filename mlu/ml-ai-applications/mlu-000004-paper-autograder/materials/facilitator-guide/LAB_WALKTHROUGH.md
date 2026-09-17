# Instructor Walkthrough — Paper Autograding Lab

This is a faculty-tool sibling of the participation and curriculum labs. Like the participation
lab, it's meant to be **used repeatedly by a single faculty member** on their own assignments —
there's no run-of-show clock. The notes below are for whoever demos, supports, or maintains it.

## The one-sentence pitch

"Drop in your course material, your rubric, and a folder of papers, and it drafts a per-criterion
grade for each one — grounded in what you taught, with the evidence and a note for the student
shown — for you to review."

## How it works (the architecture in 30 seconds)

1. **Part 2** embeds the course-material PDF into FAISS — this *is* the ground truth for "used the
   concepts correctly."
2. **Part 3** loads the structured rubric (`mlu_utils/paper_tools.load_rubric`), the papers folder
   (`load_papers`, one Submission per file across `.pdf/.docx/.txt/.md`), and reconciles against the
   roster (matched vs. missing vs. off-roster).
3. **Part 4** grades each paper with **one grounded Nova Lite call**: it retrieves the slice of the
   course material the paper engages, then scores every rubric criterion at once and returns JSON
   (per-criterion tier, evidence quotes, rationale, a student note, plus two paper-level summaries).
   The **overall percentage is computed in code** from the tiers and the rubric weights — the model
   never does the arithmetic. Missing papers are handled in code, never sent to the model.
4. **Part 5** is the human-in-the-loop override + fairness check. **Part 6** exports `.csv`, a `.md`
   record, and one student-facing feedback file per student (private rationale excluded).

All grading/loading logic lives in `mlu_utils/paper_tools.py`, keeping the notebook readable — same
convention as the participation lab's `transcript_tools.py`.

## The sample is engineered to show the full range

`data/sample_papers/` holds three papers on a Ch. 1 *Open Data Structures* assignment (the same
`persona2` PDF, used here as the course material), plus a roster with a non-submitter. Expected
outcomes when you run Part 4:

| Student | What the paper is | Expected shape |
|---|---|---|
| **Aisha Rahman** | Clear thesis (hash table vs. array for membership), correct use of hashing / load factor / average-vs-worst-case, evidence for each claim | **High** — 3–4 on every criterion |
| **Marcus Lee** | Reads fluently and confidently but is **conceptually wrong**: claims array append and linked-list random access are both O(1), middle insertion is "fast" | **Split** — decent Clarity, **low Use of Course Concepts / Evidence** |
| **Priya Chandra** | A **reflection**, not an analysis: on-topic in spirit, but no thesis, no concepts, no evidence | **Low** — 0–1 on Thesis / Concepts / Evidence |
| **Diego Alvarez** | On the roster, **no paper submitted** | flagged **missing** (no score) |

The two outcomes to point at when demoing:

- **Marcus (fluent, wrong) scores below Aisha (fluent, correct) on the concept criteria** even
  though both read well. This is the whole thesis of the lab — grounded correctness, not polish.
  It only works because *Use of Course Concepts* is judged against the embedded material.
- **Diego appears as `missing`** *because* a roster was supplied. Set `ROSTER_PATH = None` and he
  vanishes — a good way to show why the roster matters.

Exact tiers vary slightly run to run (Nova Lite, temperature 0.2) — especially Priya's 0-vs-1 and
Marcus's 1-vs-2. That's expected and is exactly why Part 5 exists.

## Common support issues

- **A student who submitted shows as `missing`.** The paper's filename doesn't match the roster
  name. Rename the file `First_Last.pdf`, or drop `ROSTER_PATH = None`. The matcher (`_names_match`,
  shared with the participation lab) handles "Last, First" and first-initial cases but not a
  filename unrelated to the roster name.
- **A paper shows `⚠️ unreadable`.** It's a scanned/image PDF with no text layer — `pypdf` returns
  nothing. `load_papers` degrades to empty text and the grader flags it rather than crashing the
  batch. Ask for a text-based PDF or `.docx`.
- **`⚠️ re-run` in the grade cell.** The model returned unparseable JSON for that paper. Re-run
  Part 4; the parser degrades gracefully.
- **`.docx` raises ImportError.** `python-docx` isn't installed — re-run Part 1.

## Runs on Bedrock *or* locally on Ollama

Part 1 has a `PROVIDER` toggle (`"bedrock"` | `"ollama"`). The pipeline is provider-agnostic;
`PaperGrader` takes an injected `llm=` (any LangChain chat model), and only the Bedrock branch
imports `langchain-aws` — lazily — so a local Ollama-only install can `import paper_tools` without it.
The Ollama path needs `ollama pull qwen2.5:7b nomic-embed-text` and **`num_ctx=8192`** (the notebook
sets it; Ollama's 2048 default truncates the paper + rubric). Verified end-to-end on `llama3.2:3b` +
`nomic-embed-text`: full sample in ~26s, and Marcus's *Use of Course Concepts* still lands at 1 vs.
Aisha's 4 — the grounded judgment survives the smaller model, though 7B/14B judge more calibratedly
(3B grades noticeably harsher).

## Maintenance notes

- **Two dependencies vs. the participation lab:** `python-docx` (for `.docx` papers) and
  `langchain-ollama` (for the local path). PDF uses `pypdf`; `.txt/.md` are stdlib. Rubric loading
  and the overall-grade math are stdlib-only.
- **Overall grade is deterministic.** `Rubric.overall_percent` computes the weighted score in code
  and renormalizes around any criterion the model failed to score, so one bad criterion widens the
  confidence gap instead of zeroing the paper. Weights don't need to sum to 100 — they're normalized.
- **Model IDs** are pinned in `paper_tools.py` (`PaperGrader.__init__`) and the notebook's Part 1,
  matching the sibling labs (`amazon.nova-lite-v1:0`, `amazon.nova-2-multimodal-embeddings-v1:0`).
- **Sample students are invented.** Safe to ship publicly. Never commit a real paper or roster.

## What to stress about scope (say this out loud in a demo)

- It is **not** a plagiarism or AI-writing detector. It doesn't know who wrote the paper. Do not let
  anyone use the confidence score in an integrity case.
- "Grounded" means grounded in **the material you loaded**. A thin or off-target course PDF makes the
  concept judgment thin. A paper that reaches beyond the material is treated as neutral, not wrong.
- The student-facing feedback files (Part 6) contain **only** the student notes — the professor's
  private rationale is never written into them. Point at a generated file to show the separation.

## Pre-demo checklist

- [ ] Bedrock access for both Nova models in `us-east-1`.
- [ ] `pip install -r requirements.txt` completes clean (includes `python-docx`).
- [ ] Parts 1–6 run top to bottom on the bundled sample with no edits.
- [ ] Marcus's *Use of Course Concepts* lands below Aisha's; Diego flagged `missing`.
- [ ] Part 6 writes a dated `grades_*/` folder with `grades.csv`, `grades.md`, and a `feedback/` dir.
