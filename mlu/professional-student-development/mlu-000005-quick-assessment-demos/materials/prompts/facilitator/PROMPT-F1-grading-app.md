# PROMPT F1 — The Grading Assistant, in Amazon Quick *(facilitator only)*

**Slides 21–22 · you build this before the session · the room watches**

This one is **not** in the attendee prompts, and it is not the Kiro build on slides 17–19. It is
the Quick app you already have open in the **builder view** when slide 21 goes up, so that
pasting one line in front of the room turns a grader into a triage tool.

Build it in advance. Slide 21 budgets 1–2 minutes for the *extension* to build, not for this.

---

## What to do, in order

1. **Before the session**, build this app from the prompt below and load it with
   `rubric-golden.json` and the four papers. Check the expected results table.
2. **Also build a second copy and extend it in advance** — paste the Triage extension line into
   it and let it finish. That is the fallback. The talk track is explicit: if the live build has
   not finished after two minutes, switch to it and keep talking. Do not wait on stage.
3. **On the day**, have the app open in the **builder** view, not the running view. The room has
   to see the line go in.
4. **On slide 21**, paste the extension line. Talk while it builds — the slide's copy is the
   script.

---

## The app

```text
Build an internal tool for university faculty called Grading Assistant. It grades a set of
student papers against a rubric and produces a DRAFT result for the instructor to review. It
never records a grade anywhere.

INPUTS:
- "Rubric" — paste or upload. Accepts JSON in the "mlu-rubric/1" format: criteria, each with
  id, name, weight, description, present_when, and levels "0" through "4"; plus max_tier and
  grade_bands. Also accepts the Markdown form.
- "Course reading" — a file upload. The source of truth for whether a claim is correct.
- "Papers" — multiple text or document uploads, one per student, named for the student.
- "Roster" — an optional CSV of enrolled students, with a name column.
- A "Grade" button.

HOW GRADING WORKS — these three rules are the whole design:

1. THE MATH IS IN CODE. For each criterion, read that criterion's level descriptors and choose
   the tier from 0 to 4 that the paper matches. That is the only judgment. The percentage is
   then CALCULATED from the tiers and weights: sum(tier / max_tier * weight) / sum(weight),
   as a percentage. The letter comes from grade_bands by lookup. Never estimate a percentage,
   never let the model produce the final number, and never let it adjust one. Show the
   arithmetic in the output so an instructor can check it. The same paper and rubric must give
   exactly the same number every time.

2. CORRECT MEANS CORRECT ACCORDING TO THE UPLOADED READING. Where a criterion is about factual
   correctness, judge each claim against the uploaded course reading and nothing else — not
   general knowledge, not what is usually true. When a claim contradicts the reading, quote the
   student's claim, quote or cite the passage that contradicts it, and say plainly which is
   right. A fluent, confident, well-organised paper that contradicts the reading must receive a
   low tier on that criterion. Do not let good writing pull a correctness tier upward.

3. EVERYONE ON THE ROSTER IS ACCOUNTED FOR. If a roster was supplied, every student on it
   appears in the results. A student with no paper is reported as MISSING — never given a zero,
   never silently skipped, never averaged in. Missing is a fact for the instructor to act on,
   not a grade.

OUTPUT:
A table of every student: name, percentage, letter, and the status (graded / missing). Under it,
a per-student breakdown: each criterion, the tier chosen, the weight, the points contributed,
and one or two sentences of evidence QUOTED FROM THE PAPER for why that tier. For correctness
criteria the evidence must include the contradicting passage from the reading.

Frame every result, on screen, as a DRAFT for the instructor to review and change. Let the
instructor override any tier; when they do, recalculate the total in code and show that it
changed. Export the reviewed results as CSV.

Show this line on the results screen: the model judges, the code counts, the instructor decides.

NEVER: record a grade to any external system, email a student, or present a result as final.
```

---

## The extension line — slide 21, pasted live

This is **slide 21's copy, verbatim**. That slide is legal-approved, so what you paste must match
what is projected behind you, word for word.

```text
Add a Triage Mode for students. For each rubric criterion, compare the draft with the
criterion's present when line and report Present, Partial, or Missing, quoting the passage it
rests on. Never show a score, tier, or grade. Never rewrite the student's text or suggest
wording.
```

If the mode it builds is thin, harden it afterwards with the full rules in
[`../PROMPT-3-triage.md`](../PROMPT-3-triage.md) — but not on stage. The point of the live paste
is that one sentence changes what the tool is for. Let the room see that, then move on.

---

## Before you deliver: prove it works

Run `rubric-golden.json` + the reading + all four papers + `roster.csv`.

| Student | Expected | Why it is in the session |
|---|---|---|
| Aisha Rahman | **91% · A-** | The control |
| Marcus Lee | **38% · F**, with his three wrong claims quoted against the reading | Slides 11–12, 19 |
| Priya Chandra | **13% · F** | Slide 22 — the F that Triage would have caught a week early |
| Leila Haddad | **≈50% · F** | Slide 19 — "what if she'd found out before the deadline?" |
| Diego Alvarez | **MISSING**, not 0% | Slide 18, decision 3 |

- [ ] Grade the same paper twice — identical numbers both times
- [ ] Override one tier — the total recalculates, and says it changed
- [ ] Marcus's evidence quotes the reading, not general knowledge
- [ ] Diego appears, and is not scored
- [ ] The pre-extended fallback copy is built, published, and open in its own tab

> These five figures are **hand-scored predictions**, not recorded results — see the sample
> pack's README. Once you have run your build, replace them there with what you actually got.
> Model output varies run to run; the two that must hold are Marcus **F** and Diego **missing**.
