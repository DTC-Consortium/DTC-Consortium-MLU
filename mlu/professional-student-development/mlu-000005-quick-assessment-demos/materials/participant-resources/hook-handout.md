# You're the grader

> *Synthetic sample data — no real individuals or institutions. For training use only.*

**You have 3 minutes.** Grade the paper below using **only** the rubric below — the way a TA, an
adjunct, or you at 11 p.m. with forty more to go would. You don't need to know computer science.
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

A 90–100 · B 80–89 · C 70–79 · D 60–69 · F below 60

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
