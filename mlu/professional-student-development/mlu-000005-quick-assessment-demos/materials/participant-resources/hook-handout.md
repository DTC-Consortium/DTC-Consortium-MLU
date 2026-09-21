# You're the grader

> *Synthetic sample data — no real individuals or institutions. For training use only.*

**You have 3 minutes.** Grade the paper below using **only** the rubric below — the way any of us
grades at 11 p.m. with forty more to go. You don't need to know computer science.
Grade it the way the rubric tells you to.

**Your score: ______ / 100    Letter: ______**

---

## The rubric

| Criterion | Points | Excellent | Good | Fair | Poor |
|---|:---:|---|---|---|---|
| **Content** | 40 | **36–40** — Thorough, insightful discussion of the topic showing strong understanding of data structures. | **30–35** — Solid discussion showing good understanding. | **24–29** — Some discussion; understanding is limited. | **0–23** — Little discussion of the topic. |
| **Organization** | 30 | **27–30** — Clear introduction, body, and conclusion; flows well. | **22–26** — Organized, with minor lapses. | **18–21** — Some organization. | **0–17** — Disorganized. |
| **Writing Mechanics** | 20 | **18–20** — Few or no errors in grammar, spelling, or punctuation. | **15–17** — Some minor errors. | **12–14** — Frequent errors. | **0–11** — Errors interfere with meaning. |
| **Length & Formatting** | 10 | **9–10** — Meets the length requirement (1–2 pages); formatted correctly. | **7–8** — Slightly off. | **5–6** — Noticeably off. | **0–4** — Far off. |

A 93–100 · A- 90–92 · B+ 87–89 · B 83–86 · B- 80–82 · C+ 77–79 · C 73–76 · C- 70–72 · D 60–69 · F below 60

---

## The paper — Marcus Lee

**Linked Lists and Arrays**

In this paper I will talk about linked lists and arrays and which one is better. Both of them store
a list of things and both are used a lot in programming.

An array stores elements next to each other in memory. You can get any element instantly because
you just go to its index. Adding to the end of an array is always O(1) because you just put the new
element after the last one. This makes arrays really fast for everything.

A linked list stores each element in a node with a pointer to the next node. Because of the
pointers, a linked list can grow forever and you never run out of space, which is the main
advantage. Getting an element is also fast, about O(1), because you follow the pointers to where
you want to go.

Inserting into the middle is where they are different. In a linked list you just change a pointer
so it is O(1). In an array you also just put the element in, so it is also fast. So really they are
pretty similar in most cases.

My conclusion is that linked lists are better because they can grow and you don't have to know the
size ahead of time. Arrays are good too but linked lists win in most situations because of the
pointers.

---

**After the session — don't reuse this rubric.** It is the "before" example the session is built
around, not a model to copy. Slide 9 of the deck explains what's wrong with it, and slides 11–12
show what it costs.

If you want a rubric you can actually use, build one. Scan the code in the corner of any slide,
open **1 — Build the Rubric Builder**, and follow it — about fifteen minutes, no coding. The
**Start here** section of your take-home pack has the same instructions if you have mislaid the
folder.
