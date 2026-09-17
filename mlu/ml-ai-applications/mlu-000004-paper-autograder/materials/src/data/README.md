# Sample data for the Paper Autograding Lab

This folder ships everything the lab needs to run out of the box, plus the slots where you
drop in your own assignment.

## What's here

| File | What it is | Source |
|---|---|---|
| `persona2_cs_data_structures.pdf` | The **course material** — Ch. 1 of *Open Data Structures* (interfaces, ArrayStack, running time, amortized analysis). This is the ground truth for "used the concepts correctly." | Open Data Structures by Pat Morin (CC-BY), Ch. 1 extract. Reused from the curriculum + participation labs. |
| `sample_rubric.py` | A **structured rubric** for a short data-structures paper: four criteria (Thesis, Use of Course Concepts, Evidence, Clarity) with weights and 0–4 descriptors. Plain Python — this is the file you edit. | Original, authored for this lab. |
| `sample_roster.csv` | A **fabricated roster** of four enrolled students. | Original, authored for this lab. |
| `sample_papers/` | **Three fabricated papers**, one per student who submitted. | Original, authored for this lab. All students are invented. |

The sample is built so the output is legible — it exercises the full range of the grader:

- **`Aisha_Rahman.txt`** — strong, on-topic: a clear thesis, correct use of hashing/amortized concepts, evidence for its claims. Should score high across the board.
- **`Marcus_Lee.txt`** — confident and readable but **conceptually wrong** (claims array append and linked-list random access are both O(1), middle insertion is "fast"). Tests whether the grounded-in-material judgment lowers *Use of Course Concepts* even though the writing reads fine.
- **`Priya_Chandra.txt`** — a **reflection, not an analysis**: on-topic in spirit but no thesis, no concepts, no evidence. Tests that fluent, on-task-sounding prose doesn't earn concept/evidence points.
- **Diego Alvarez** is on the roster with **no paper** — surfaces as **missing**, for you to confirm before entering a 0.

## Bring your own

Swap in real material by changing four values in the notebook (Parts 2–3):

- **`LESSON_PDF`** → any text-based PDF of the course material (reading, lecture notes, slides
  exported to PDF, the chapter). Text-based (not a scan), roughly 8–50 pages.
- **`RUBRIC_PATH`** → edit **`sample_rubric.py`** in place, or point at your own `.py`/`.json`
  rubric of the same shape. Weights are relative (they're normalized to sum to 100), so you
  don't have to make them add up yourself.
- **`PAPERS_DIR`** → a folder with **one file per student**. Name files `First_Last.pdf` so the
  student name is inferred correctly. `.pdf`, `.docx`, `.txt`, and `.md` all parse.
- **`ROSTER_PATH`** (optional) → a CSV with a `student_name` column (other columns ignored).
  Without a roster, only students who submitted appear — a non-submitter won't show as missing.

## ⚠️ Privacy first

Student papers are protected records. Before you run this on a real class:

- Keep papers, the roster, and everything the notebook exports on your institution's approved
  storage (FERPA in the US; your local equivalent elsewhere).
- Don't paste real student names or paper text into anything outside your approved environment.
- The grade this lab produces is a **draft you review** — never a grade the tool assigns on its
  own, and never an academic-integrity judgment. See Part 0 and Part 7 of the notebook.
