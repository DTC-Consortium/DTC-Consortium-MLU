# Sample Pack — one assignment through four tools

> *Synthetic sample data — no real individuals or institutions. For training use only.*

Everything the four session demos grade, harden, and triage. One assignment, one course reading,
two rubrics, five students.

## What's here

| File | What it is | Used by | Source |
|---|---|---|---|
| `assignment.md` | The assignment prompt and four learning objectives | Rubric Builder (input), AI-Proofing | Original |
| `persona2_cs_data_structures.pdf` | The **course reading** — *Open Data Structures* Ch. 1–2 extract, 31 pp. "Correct" means correct according to this. | All four | Pat Morin, CC-BY. Byte-identical to the copy in `mlu-paper-autograder/data/`. |
| `rubric-weak.md` | The "original" rubric: vague, unweighted toward correctness | Hook, Stress Test | Original, weak on purpose |
| `rubric-golden.json` / `.md` | The reference rubric, in [`mlu-rubric/1`](../rubric-format.md) format | Stress Test, Grading Assistant, Triage | Original |
| `papers/` | Four papers — see below | All four | Three reused from `mlu-paper-autograder`; `Leila_Haddad.txt` new |
| `roster.csv` | Five enrolled students, one of whom submitted nothing | Grading Assistant | Original, fabricated |

## The five students

| Student | What the paper is | Its job in the session |
|---|---|---|
| **Aisha Rahman** | Strong: hash table vs. array for membership tests; correct analysis, a scenario, trade-offs | The control. High on every rubric. |
| **Marcus Lee** | **Fluent, confident, and wrong.** Claims array append is "always O(1)", linked-list access is "about O(1)", and middle insertion into an array is "fast". | Demo A's centerpiece: the weak rubric rewards him; the golden rubric doesn't. Also the honest limit of Triage — his running times are *present*. |
| **Priya Chandra** | A reflection on the class, not an analysis | Demo B's centerpiece: Triage surfaces Missing ×3 before the deadline; Grade mode shows the F it would have been. |
| **Leila Haddad** | A **draft** — right thesis, right idea, unfinished: no big-O, no alternative, two `[TODO]` markers | Shows what **Partial** looks like in Triage. |
| **Diego Alvarez** | On the roster, no paper | The Grading Assistant flags him **missing** rather than silently skipping him. |

## Where Marcus is wrong — grounded in the reading

The golden rubric's correctness criterion is only useful because the reading settles these:

| Marcus says | The reading says |
|---|---|
| "Adding to the end of an array is always O(1)" | ArrayStack add at the end is O(1) **amortized** — `resize()` copies the whole array when it fills (§2.1, Theorem 2.1). Not O(1) every time. |
| Linked-list access is "about O(1), because you follow the pointers" | DLList `get(i)` is O(1 + min{i, n − i}) (Table 1.1). Following pointers *is* the cost. |
| Middle insertion into an array "is also fast" | ArrayStack `add(i, x)` is O(1 + n − i) — elements are shifted to make room (§2.1). |

## Expected outcomes — **predicted, not yet verified**

Hand-scored against each rubric's descriptors to set expectations for the rehearsal. Replace with
recorded results once the apps have run; model output will vary run to run.

| Student | Weak rubric | Golden rubric (tiers: thesis / running-time / evidence / trade-offs / clarity) | Triage (same order) |
|---|---|---|---|
| Aisha | ≈ A | 4 / 3 / 4 / 4 / 4 → **≈91% A-** | Present ×5 |
| Marcus | **≈ B+ (~88)** — organized, clean, right length, "discusses the topic" | 2 / 1 / 1 / 1 / 3 → **≈38% F** | Present / **Present** / Missing / Partial / Present |
| Priya | ≈ C- (~72) | 1 / 0 / 0 / 0 / 2 → **≈13% F** | Missing / Missing / Missing / Missing / Partial |
| Leila | — (a draft; not graded in the demo) | 3 / 2 / 2 / 0 / 2 → ≈50% F if submitted as-is | Present / Partial / Partial / Missing / Partial |
| Diego | — | **missing** | — |

The two numbers the session turns on: **Marcus drops from ≈B+ to F** when the rubric names what
correct looks like, and **Priya's F surfaces as three Missing flags** while there's still time to
fix it.

## Why the weak rubric is weak (facilitator notes — not on the handout)

- **60 of 100 points go to what's visible without expertise** — organization, mechanics, length.
- **"Understanding" is never defined**, so the grader supplies their own standard, or none.
- **Nothing checks correctness.** No criterion asks whether a claim is true.
- **Not mapped to the learning objectives.** LO2 (running-time guarantees) isn't assessed at all.
- **Point ranges without distinguishing descriptors** — what separates a 32 from a 35?
