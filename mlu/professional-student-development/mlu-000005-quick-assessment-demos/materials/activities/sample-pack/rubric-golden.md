# Rubric — Choose the Right Structure (short paper)

> *Synthetic sample data — no real individuals or institutions. For training use only.*
>
> Human-readable copy of `rubric-golden.json` (format: `mlu-rubric/1`). Paste this version into a
> Quick app or chat window. If the two ever disagree, the JSON wins.

**Assignment:** `assignment.md` · **Judged against:** `persona2_cs_data_structures.pdf`
**Scale:** 0–4 per criterion · **Weights:** relative, total 100
**Grade bands:** A 93 · A- 90 · B+ 87 · B 83 · B- 80 · C+ 77 · C 73 · C- 70 · D 60 · F below 60

---

### 1. Thesis & Choice of Structure — weight 20 · LO1
*Does the paper name one operation and the structure it recommends for it, and argue that choice
throughout?*
**Present when:** a sentence states which data structure the paper recommends and for which
operation.

| Tier | Descriptor |
|:---:|---|
| 4 | A specific, arguable thesis names the operation and the recommended structure; every section advances it. |
| 3 | A clear thesis names the operation and the structure; the argument mostly stays on it. |
| 2 | A recommendation is present but vague — e.g. "X is better" — without naming the operation it is better for. |
| 1 | No real thesis: the paper describes structures without recommending one for a specific operation. |
| 0 | Off-prompt or missing. |

### 2. Correctness of Running-Time Analysis — weight 35 · LO2
*Are the running-time claims correct according to the course reading, and does the paper say which
kind of guarantee each one is?*
**Present when:** the paper gives a big-O running time for the key operation in the recommended
structure and in at least one alternative.

| Tier | Descriptor |
|:---:|---|
| 4 | Every running-time claim matches the course reading, and the paper distinguishes worst-case, amortized, and expected guarantees where they differ — e.g. adding to the end of an ArrayStack is O(1) amortized because of resize(), not O(1) worst-case. |
| 3 | Claims match the course reading, with one guarantee type left unstated or one minor imprecision — e.g. "average" where the reading says "expected". |
| 2 | Mostly correct, but one claim contradicts the course reading, or correct running times are asserted with no explanation. |
| 1 | Two or more claims contradict the course reading — e.g. constant-time access to the i-th element of a linked list (the reading gives O(1 + min{i, n − i}) for DLList), or constant-time insertion into the middle of an array (O(1 + n − i) for ArrayStack). |
| 0 | No running-time analysis. |

### 3. Evidence & Scenario — weight 20 · LO3
*Is the argument grounded in a concrete scenario, with claims backed by analysis or by the course
reading?*
**Present when:** the paper describes at least one concrete program or task, and refers to the
course reading at least once.

| Tier | Descriptor |
|:---:|---|
| 4 | A concrete scenario carries the argument, the analysis is applied to it (e.g. total cost over a whole input stream), and the reading is cited where it supports a claim. |
| 3 | A concrete scenario with supporting analysis; the reading is referenced, but loosely. |
| 2 | A scenario is mentioned but not analyzed, or claims rest on assertion rather than evidence. |
| 1 | Generic claims only: no scenario and no reference to the reading. |
| 0 | No supporting evidence. |

### 4. Trade-offs & Limits — weight 10 · LO1
*Does the paper say where its recommended structure is the worse choice?*
**Present when:** the paper names at least one situation in which the recommended structure is the
worse choice.

| Tier | Descriptor |
|:---:|---|
| 4 | Names a specific case where the recommended structure loses, and explains why in running-time or memory terms. |
| 3 | Names a case where the recommendation loses, with a brief reason. |
| 2 | Acknowledges limits in general terms only — "it depends". |
| 1 | Claims the structure is the best choice in all or most situations. |
| 0 | No discussion of trade-offs. |

### 5. Clarity & Structure — weight 15 · LO4
*Is the paper organized and readable for a peer?*
**Present when:** the paper has an introduction that states its claim, body paragraphs, and a
conclusion.

| Tier | Descriptor |
|:---:|---|
| 4 | Tight structure and clean prose; easy to follow throughout. |
| 3 | Well organized; an occasional awkward passage. |
| 2 | Understandable, but disorganized or repetitive in places. |
| 1 | Hard to follow; little structure. |
| 0 | Incoherent. |
