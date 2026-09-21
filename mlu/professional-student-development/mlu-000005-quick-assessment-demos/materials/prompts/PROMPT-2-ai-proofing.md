# PROMPT 2 — The AI-Proofing Assistant

**Slide 15 · hands-on · 10 minutes · Amazon Quick**

Second app, built the same way. It reads the assignment you just built a rubric for and tells you
which parts of it a chatbot could satisfy without ever attending your course.

---

## What to do

1. **Predict first — before you open anything.** Look at your assignment. Which single
   requirement could a general chatbot satisfy in thirty seconds, knowing nothing about your
   course? Write it down on your handout. You will check yourself against the tool in a minute.
2. **Create → App** in Amazon Quick, paste the prompt below, send it.
3. **Paste your assignment** and the **rubric you built in prompt 1**.
4. **Read the flags.** Then answer the three questions on the slide.
5. **Choose** the one or two revisions you would actually make. Not all of them.

> **The goal is not to make cheating impossible.** It is to make the assignment *need* your
> course — its reading, its discussion, the student's own process. An assignment a chatbot
> cannot help with at all is usually also an assignment students cannot learn from.

---

## The prompt

```text
Build an internal tool for university faculty called AI-Proofing Assistant. It examines an
assignment and reports which of its requirements a general-purpose chatbot could satisfy
without any knowledge of the specific course. No student data.

INPUTS, on one screen:
- "Assignment prompt" — a large text area.
- "Rubric" — a text area or file upload. Accepts Markdown, or JSON in the "mlu-rubric/1"
  format, which has a criteria array where each criterion has name, weight, objective,
  description, present_when and levels. Read the criteria either way.
- "Course context" — optional: a reading list, a syllabus, notes on what happened in class.
- An "Analyze" button.

WHAT IT DOES:
Break the assignment into its individual requirements — the discrete things a student is being
asked to do. List them. Then judge each one and give it a flag:

  OPEN        A chatbot could satisfy this with no knowledge of the course.
  PARTIAL     A chatbot could produce a plausible version, but not a good one, without
              course-specific material.
  ANCHORED    Satisfying this requires something only a student in this course has — the
              assigned reading, something said in class, their own data, their own process,
              or their own draft history.

For each requirement show: the requirement in the assignment's own words, the flag, and one
or two sentences of reasoning. The reasoning must say WHY, concretely — what a chatbot would
produce and what it could not. Never just restate the flag.

Then do the same pass over the RUBRIC's criteria: which criteria award points for things a
chatbot can reliably produce — structure, fluency, correct formatting, length, coverage of
obvious sub-topics? Show those as OPEN and name them. A rubric whose weight sits mostly on
OPEN criteria is the real finding, so say it plainly when it happens.

Finish with a headline: what share of this assignment's requirements, and what share of the
rubric's weight, are currently OPEN.

SUGGESTED REVISIONS:
For each OPEN or PARTIAL requirement, suggest two or three concrete revisions that would move
it toward ANCHORED. Rewrite the actual sentence where you can, so the user sees the change
rather than a description of it. Prefer revisions that tie the work to:
- the specific assigned reading, cited by section or page
- something that happened in this class — a discussion, a lab, a guest, a local example
- the student's own data, their own draft, or their own earlier work
- a process artifact: a log, a revision history, an annotated bibliography, a recorded
  decision they had to make and defend

For each suggestion, state the cost honestly in one line: what it adds to the student's
workload, and what it adds to the instructor's grading load. A revision that triples grading
time is a real trade-off and the user should see it before they choose.

FRAMING — hold this line, and say it on screen:
This tool does NOT detect AI-written text. It does NOT detect plagiarism. It cannot tell you
whether any particular student used a chatbot, and it must never speculate about that. It
examines the ASSIGNMENT, not any student. The goal is not to make the work impossible for a
chatbot — it is to make the work require the course. State this on the results screen, in
plain words, every time.

Let the user mark individual suggestions as "will do" / "won't do" and export the assignment
with the chosen revisions applied, alongside a short changelog of what was changed and why.

TONE: a colleague reading your assignment over your shoulder, not a compliance scanner. It
suggests. The instructor decides.
```

---

## Before you deliver: prove it works

| Check | Expected |
|---|---|
| Paste `assignment.md` and `rubric-weak.md` | Most of the weak rubric's weight flagged **OPEN** — organization, mechanics and length are exactly what a chatbot does well |
| Paste `assignment.md` and `rubric-golden.json` | The correctness criterion flagged **ANCHORED** — it needs the reading |
| Read any flag's reasoning | It says what a chatbot would produce, not just *"a chatbot could do this"* |
| Look for the disclaimer | On screen, every run, unprompted |
| Try to make it accuse a student | It should refuse, and say it examines assignments |

The contrast between the two rubrics is the segment's point, and it is worth running both on
stage even though the slide only budgets for one.

---

## A note for whoever delivers this next

In the original session this was the least specified of the four tools, and the talk track
carried the author's own note that slide 15's steps had to be rewritten once the app was
finished. That is now moot: **the steps are here, on this card, not on the slide.** Slide 15
shows the title, the prediction check, and the clock.

So if you change this prompt, change the steps above to match and reprint the card. Nothing in
the deck needs to move, and nothing needs to go back to legal.
