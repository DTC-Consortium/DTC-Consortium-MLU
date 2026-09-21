# PROMPT 1 — The Rubric Builder

**Slide 13 · hands-on · 12 minutes · Amazon Quick**

You are going to build this app yourself, in the room, from the prompt below. Nothing is
pre-installed. It takes about 90 seconds to build.

---

## What to do

1. **Sign in** to Amazon Quick and choose **Create → App**.
2. **Copy the prompt** in the grey block below — all of it — and paste it into the
   *describe your app* box. Send it.
3. **Wait** while it builds. About 90 seconds. Read the "Check it" questions on the slide
   while you wait.
4. **Upload the course reading** when the app asks for it, or skip it — the app works without
   one, it just can't check whether claims are *true*. The sample reading
   (`persona2_cs_data_structures.pdf`) is in the shared folder.
5. **Paste your own assignment prompt and learning objectives**, and generate.
6. **Read every criterion.** Edit anything you wouldn't actually grade on.
7. **Save or copy the rubric.** You need it twice more today — in prompts 2 and 3.

> **Assignments and rubrics only. Never student work.**
> Everything in the shared folder is synthetic. Your own real student work does not go into this
> app, today or at home, unless your institution has approved it.

**No assignment with you?** Use `assignment.md` from the shared folder.

---

## The prompt

```text
Build an internal tool for university faculty called Rubric Builder. It turns an assignment
prompt into a grading rubric that other tools can read. No sign-up, no student data.

INPUTS, on one screen:
- "Assignment prompt" — a large text area.
- "Learning objectives" — a text area, one objective per line, labelled LO1, LO2, LO3...
- "Course reading" — an optional file upload (PDF or text). This is the source of truth for
  whether a claim in a student paper is correct.
- A "Generate rubric" button.

WHAT IT PRODUCES:
A rubric of 4 to 6 weighted criteria. For each criterion:
- a short name
- a weight out of 100, all weights summing to 100
- the learning objective it assesses, by label
- a one-line description of what it measures
- a "present when" line
- five level descriptors, for tiers 4, 3, 2, 1 and 0

RULES THAT MATTER MORE THAN ANYTHING ELSE:

1. Every criterion must map to one of the stated learning objectives, and every objective must
   be covered by at least one criterion. After generating, show a coverage line: which
   objectives are assessed and which are not. If an objective has no criterion, say so loudly.

2. At least one criterion must assess CORRECTNESS — whether the factual claims in the work are
   true. If a course reading was uploaded, this criterion must judge claims against that
   reading and nothing else, and its level descriptors must quote or cite specific passages
   from it. Name the criterion for the specific knowledge being tested, not "Accuracy".
   If no reading was uploaded, still create the criterion, and warn the user that without a
   reading it can only check internal consistency.

3. Level descriptors must DISTINGUISH, not measure. Each descriptor says what is observably
   different about work at that tier. Never write a point range. Never write "excellent",
   "good", "fair", "poor" on their own. A colleague who has never seen the assignment must be
   able to tell a 2 from a 3 by reading the two descriptors side by side. Write tier 4 and
   tier 1 first, then fill the middle.

4. The "present when" line states what must physically be on the page for the criterion to
   count as ATTEMPTED — not done well, just there. It is observable, never evaluative, and
   it is self-contained: a later tool reads this line and nothing else from the criterion, so
   it cannot refer to "the above" or to the criterion's name. Count things where you can.
   Good: "Gives a big-O running time for the operation in the recommended structure and in at
   least one alternative." Bad: "Analyzes running time well."
   If a "present when" line contains "and also", split it into two criteria.

5. Weight the criteria by what the assignment is actually for. If more than half the weight
   sits on things a reader can judge without knowing the subject — organization, mechanics,
   length, formatting — warn the user on screen in plain words: most of this rubric's points
   do not require expertise, and a grader who knows nothing about the topic would produce
   nearly the same grade.

OUTPUT FORMAT — this matters, because three other tools read it:
Show the rubric as a readable table on screen, and offer two downloads, same content:
- Markdown, for reading and pasting.
- JSON, in exactly this shape:

{
  "format": "mlu-rubric/1",
  "title": "...",
  "assignment": "...",
  "course_material": "...",
  "max_tier": 4,
  "grade_bands": [[93,"A"],[90,"A-"],[87,"B+"],[83,"B"],[80,"B-"],[77,"C+"],[73,"C"],
                  [70,"C-"],[67,"D+"],[63,"D"],[60,"D-"],[0,"F"]],
  "criteria": [
    {
      "id": "short-slug",
      "name": "...",
      "weight": 20,
      "objective": "LO1",
      "description": "...",
      "present_when": "...",
      "levels": {"4":"...","3":"...","2":"...","1":"...","0":"..."}
    }
  ]
}

Keep "format" exactly "mlu-rubric/1". Use "max_tier": 4 and levels "0" through "4" as strings.
Give every criterion a short stable id slug. Include grade_bands exactly as above unless the
user edits them.

EDITING: every field must be editable on screen after generation — text, weights, descriptors
and the "present when" lines. Re-export after edits. If edited weights no longer sum to 100,
say so rather than silently rescaling.

SECOND TAB — "Stress Test":
Let the user upload or paste ONE student paper and TWO rubrics, then grade that paper against
both and show the two results side by side: the letter grade, the percentage, and a per-
criterion breakdown for each. Under the comparison, list in plain sentences which criteria
caused the difference and why. This tab exists to show that the same paper gets different
grades from different rubrics, so make the difference legible, not just the numbers.

For grading in this tab: the model picks a tier from 0 to 4 for each criterion by reading that
criterion's level descriptors. The percentage is then CALCULATED in code from the tiers and
weights — never estimated, never produced by the model. Show the arithmetic. The same paper and
rubric must give the same number every time.

TONE: this drafts a rubric for a human to edit. It never records a grade and never claims to be
finished. Say so on screen.
```

---

## Before you deliver: prove it works

Build the app from this prompt, then run the sample pack through it. The session's spine depends
on the last two lines.

| Check | Expected |
|---|---|
| Paste `assignment.md` + its four objectives, upload the reading, generate | 4–6 criteria, all four LOs covered |
| Read the correctness criterion | It cites the reading — section numbers or a table — not general knowledge |
| Read any two adjacent descriptors | You can tell them apart without having seen the assignment |
| Stress Test: `Marcus_Lee.txt` vs `rubric-weak.md` | **≈88 / 100 · B+** |
| Stress Test: `Marcus_Lee.txt` vs `rubric-golden.json` | **F, ≈38%** |

Compare your generated rubric against `rubric-golden.json` — that is what good looks like here.
Your wording will differ; the shape and the correctness criterion should not.

**If the two Stress Test grades do not diverge, stop and fix it before rehearsing.** Slides 11
and 12 are the centre of the session and they have nothing to show without that gap.

**If the build produces something close but not right,** tell the app what is wrong in plain
words and let it revise — that describe-then-fix loop is itself the contrast with Kiro on
slide 17. It is worth saying that out loud when it happens on stage.
