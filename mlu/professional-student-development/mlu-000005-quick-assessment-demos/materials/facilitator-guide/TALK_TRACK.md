# Talk Track — The Assignment Lifecycle (90 min)

What to say on each slide of `deck/assessment-lifecycle-deck.pdf`, and what has to have happened
before you click to it. Times are the session clock.

Each slide has four parts:

- **Before** — what must already be true in the room when this slide goes up.
- **Say** — talking points, not a script. Say them in your own words.
- **Do** — what you, or the volunteers, physically do.
- **→ Next** — the line that takes you to the next slide.

---

## The one thread to hold onto

Everything hangs on **Marcus's paper**:

1. **Slide 2** — the room grades it, using the weak rubric on the handout.
2. **Slide 4** — you count their grades. Most say B. You reveal nothing.
3. **Slide 11** — the same paper gets ≈B+ under their rubric and F under the generated one.
4. **Slide 12** — the three errors nobody was asked to check.
5. **Slide 23** — even Triage passes him. *Present is not correct.*

If you're short on time, protect that thread. Everything else compresses.

---

## Before the session

> ### ⚠️ The four apps do not ship with this contribution
>
> The checklist below assumes the Rubric Builder, AI-Proofing Assistant, Grading app, and Triage
> extension already exist and are published. **They are not included here — you must build them
> first.**
>
> **→ [`APPS_YOU_MUST_BUILD.md`](APPS_YOU_MUST_BUILD.md)** collects every requirement this talk
> track depends on, plus the exact outputs each app must produce on the sample pack.
>
> Everything else — deck, talk track, handout, sample pack — is complete and rehearsable.

**48 hours before**
- [ ] Quick invites sent, and accepted by most attendees. Volunteers have the list of anyone who
  hasn't accepted.
- [ ] Registration email asked everyone to bring **one assignment prompt and its learning
  objectives, as text — no student work.**

**Morning of**
- [ ] On every table, face down: `hook-handout.md` (Marcus's paper + the weak rubric), one per
  person. Plus a table card with sign-in help and the app links.
- [ ] Apps published and shared with every attendee account: Rubric Builder, AI-Proofing,
  Grading app (Grade mode only), and a **pre-extended Triage copy** as the fallback.
- [ ] Presenter tabs open, in order: Rubric Builder (sample assignment pasted) → AI-Proofing →
  Kiro (`requirements.md` open) → the Grading app in the **builder** view (for the live
  extension) → the Triage fallback.
- [ ] On the desktop: `Marcus_Lee.txt`, `Priya_Chandra.txt`, `Leila_Haddad.txt`,
  `rubric-weak.md`, `rubric-golden.md`, and the Triage extension line, ready to paste.
- [ ] The Kiro grader already run once, with the results saved, in case the live run is slow.
- [ ] One volunteer assigned to **count hands on slide 4** and write the tally down.

---

## 0:00–0:12 · Arrival and sign-in

### Slide 1 — Cover
**Before:** People are arriving. This slide is up while they sit down.
**Say** (once most seats are full, 30 seconds):
- "In the next 90 minutes you'll see four AI tools that take one assignment from start to
  finish: build the rubric, tighten the assignment, grade it, and let students check their own
  work before they hand it in."
- "You'll use two of them on your own course. First, let's get you logged in."

**→ Next:** "Sign-in first, and I've got a job for you while you wait."

### Slide 2 — Get signed in, and start grading
**Before:** Handouts are face down on the tables. Volunteers are standing at the edges of the
room.
**Say:**
- Walk the four steps on screen.
- "On your table is a student paper and the rubric that came with the assignment. While sign-in
  loads — or once you're in — grade it. Three minutes. **Use only that rubric.** Write a score
  and a letter at the top."
- "You don't need to know computer science. Grade it the way the rubric tells you to — the way a
  TA would, or the way you would at 11 p.m. with forty more in the pile."

**Do:** Tell them to turn the handouts over. Volunteers circulate. Give a two-minute warning at
0:10. **At 0:12, move on regardless:** "If you're not in yet, pair with a neighbor. A volunteer
will keep working on yours."
**Don't:** Say *anything* about whether the paper is good or bad. The whole point of slide 4 is
that they grade it cold.
**→ Next:** "Pencils down. Here's where we're going."

---

## 0:12–0:18 · Setting up the thread

### Slide 3 — Today's session *(30 seconds)*
**Before:** Grading is done. Handouts are in people's hands.
**Say:** "Three of these you'll do hands-on, on your own assignment. The Kiro one you'll watch.
But first: the paper you just graded."
**→ Next:** "So. Marcus."

### Slide 4 — What grade did you give Marcus? *(2 min)*
**What this slide is for:** It records the room's honest grade *before* anyone knows anything,
so that on slide 11 you can show the rubric produced that grade, not their judgment. It's the
setup; slides 11 and 12 are the payoff.

**Before:** Everyone has graded Marcus using only the weak rubric. The volunteer counting hands
is ready.
**Say:**
- "Hands up if you gave Marcus an A." Count. "B?" "C?" "D?" "F?"
- Say the result out loud: "So most of this room gave him a B."
- "Write your grade on your handout if you haven't. Hold onto it. We're coming back to it in
  about fifteen minutes."

**Do:** The volunteer writes the tally somewhere you can see it. **You need that number on
slide 11.**
**Expect:** Most rooms land on B or B+. The paper is organized, readable, the right length, and
on topic — everything that rubric awards points for.
**Don't:** Reveal that he's wrong. If a CS faculty member starts explaining the errors, stop them
kindly: "Hold that thought — I'm going to ask you to say it on slide 12." If someone gave an F:
"Great. Tell me why in fifteen minutes."
**→ Next:** "Why does that matter? Because every grading tool, human or AI, is only as good as the
rubric behind it. Here's what we're building today."

### Slide 5 — One assignment, four tools *(1 min)*
**Say:**
- The four stages, left to right. "These aren't four separate demos. They're four stages of the
  same assignment — the rubric we build in the first tool is literally the file the other three
  read."
- "Three are built in Amazon Quick, with no code. The grader is built in Kiro, where you approve
  the spec before any code exists. You'll see why that matters for a tool that assigns grades."

**→ Next:** "Here's the assignment we'll follow through all four."

### Slide 6 — The assignment we'll follow *(1 min)*
**Say:**
- "A sophomore data-structures paper: pick an operation a program does over and over, and argue
  which structure fits it. Five requirements, four learning objectives."
- "Notice requirement two: running times, *and* which kind of guarantee each one is. Keep that
  in mind."
- "Most of you don't teach CS, and that's deliberate. Watch what the tools make visible to
  someone who isn't an expert — because that's the position a TA, an adjunct, or a tired grader
  is in."

**→ Next:** "Five students were enrolled. Four turned something in."

### Slide 7 — Meet the five students *(1.5 min)*
**Say:** One line each, plus what that student tests:
- **Aisha** — the control. What good looks like.
- **Marcus** — "You've met Marcus." Say nothing more yet.
- **Priya** — wrote a reflection instead of an analysis. "She's the one the last tool saves."
- **Leila** — an unfinished draft. "She shows what 'Partial' looks like."
- **Diego** — submitted nothing. "He tests whether the grader notices."
- "All five are invented. No real student work is used anywhere today — and none should go into
  tools like these at home unless your institution has approved them."

**→ Next:** "Let's start where every assignment should: the rubric."

---

## 0:18–0:36 · Tool 1: the Rubric Builder

### Slide 8 — Section: The Rubric Builder
**Say:** "First tool. Six minutes of me, then twelve of you."

### Slide 9 — A tool is only as good as its rubric *(1.5 min)*
**Before:** People still have their Marcus grade in mind.
**Say:**
- "This is the rubric you just used. Be honest — it looks like a lot of rubrics we've all
  written."
- "**60 of the 100 points** go to things anyone can see without expertise: organization,
  mechanics, length."
- "'Understanding' is never defined, so every grader supplies their own standard — or none."
- "Nothing asks whether a single claim is true."
- "And learning objective 2 — running-time guarantees — isn't assessed by any criterion."
- The key line: "**Hand this rubric to an AI grader and you get the same B, just faster.
  Automation doesn't fix a rubric. It scales it.**"

**→ Next:** "So the first tool fixes the rubric."

### Slide 10 — What the Rubric Builder does *(1 min)*
**Do:** Switch to the Rubric Builder app, with the sample assignment already pasted. Generate, or
show the pre-generated rubric.
**Say:**
- Walk the four steps.
- Point at the correctness criterion in the output: "This one names what 'correct' looks like,
  and it's tied to the course reading."
- Point at a *present when* line: "Remember that phrase. It comes back in the last tool."

**→ Next:** "Now the test: same paper, two rubrics."

### Slide 11 — Stress test: one paper, two rubrics *(1.5 min)*
**Do:** In the app's Stress Test tab, run Marcus against both rubrics. Then show this slide as
the summary, or use it as the fallback if the live run is slow.
**Say:**
- "Under the original rubric, about a B+." Then use the tally: "**Most of you gave him a B. You
  graded exactly the way the rubric told you to.**"
- "Under the generated rubric: F."
- "Same paper. Same words. The only thing that changed is the rubric."
- Reassure the room: "Nobody here graded badly. You followed the rubric. It just never asked the
  question that mattered."

**→ Next:** "So what did it catch that you weren't asked to?"

### Slide 12 — What the new rubric caught *(1.5 min)*
**Say:** Walk the three rows, with a plain-language version of each for non-CS faculty:
- "He says adding to the end of an array is *always* instant. The reading says it's *usually*
  instant, but every so often the whole array has to be copied. 'Always' is wrong."
- "He says jumping to any spot in a linked list is instant. The reading says you have to walk
  there one link at a time. The walking *is* the cost."
- "He says inserting into the middle of an array is fast. The reading says everything after that
  spot has to shift over to make room."
- If a CS faculty member flagged the errors back on slide 4, call on them now.
- The key line: "**The rubric carries the expertise, so the grader doesn't have to.** That's what
  you want for TAs, adjuncts, and multi-section courses."

**→ Next:** "Your turn — a rubric for your own assignment."

### Slide 13 — Your turn: a rubric for your assignment *(0:24–0:36, 12 min)*
**Before:** Everyone is signed in and has their own assignment (from the registration email) or
is using the sample.
**Say:** The four steps, the three "check it" questions, and the privacy rule: assignments and
rubrics only, never student work.
**Do:** Start the timer and circulate.
- At 6 minutes: "If you've generated one, start on the check questions."
- At 10 minutes: "**Save or copy your rubric. You'll need it twice more.**"

**If something goes wrong:**
- No assignment → use the sample.
- The output cuts off → regenerate with fewer criteria.
- Can't see the app → a volunteer helps.

**→ Next:** "You have a rubric. Now: could a chatbot just do the assignment?"

---

## 0:36–0:46 · Tool 2: the AI-Proofing Assistant

### Slide 14 — Section: The AI-Proofing Assistant
**Say:** "Second tool. Ten minutes, on the same assignment you just built a rubric for."

### Slide 15 — Could a chatbot do this assignment? *(10 min, hands-on)*
**Say:**
- **Prediction first:** "Before you open the tool, look at your assignment. Which requirement
  could ChatGPT meet in 30 seconds, knowing nothing about your course? Write it down."
- Then they paste the assignment and rubric, and read the flags.
- The framing: "The goal isn't to make cheating impossible. It's to make the assignment *need*
  your course — your reading, your class discussion, the student's own process."

**Do:** In the last 2 minutes, debrief: "Did it flag something you didn't predict? Which change
would you actually make?" Take two answers.
**Note:** Update these steps to match the final AI-Proofing app before rehearsal.
**→ Next:** "Now grading. This one you watch."

---

## 0:46–0:59 · Tool 3: the Grading Assistant (Kiro)

### Slide 16 — Section: The Grading Assistant
**Say:** "Third tool, built in Kiro. A grader is the tool where being wrong costs the most, so it's
the one we built most carefully."

### Slide 17 — Review the spec before the code *(4 min)*
**Do:** Switch to Kiro and show `requirements.md`.
**Say:**
- "In Quick, you describe an app and fix it after you see it. In Kiro, you approve the
  requirements, then the design, then the task list — and only then is code written."
- Poll the room: "Two requirements. Which one can't you test?" Take answers.
- **Answer: ②.** "'Fairly' has no pass or fail. What would fair mean? The same paper gets the
  same score twice? Scores don't change with the student's name? Each of those *is* testable.
  'Fairly' isn't."
- "Fixing it now costs a sentence. Fixing it after the code exists costs a rebuild. Fixing it
  after it's graded 200 papers costs much more."

**→ Next:** "Three decisions in that spec carry the whole tool."

### Slide 18 — Three design decisions *(2 min)*
**Say:**
- **The math is in code.** "The model picks a 0–4 tier for each criterion. The weighted grade is
  calculated, never generated — models are unreliable at arithmetic, and a grade has to be
  exactly reproducible."
- **Correct means correct per your reading.** "This is why Marcus fails. His claims are checked
  against the course reading, not the model's general sense of the topic."
- **Everyone is accounted for.** "Diego shows up as missing, not as a silent zero."
- The key line: "The model judges. The code counts. The instructor decides."

**→ Next:** "Let's run it on all five."

### Slide 19 — Five students, one rubric *(3 min)*
**Do:** Run the grader in Kiro on all five, or show the saved results.
**Say:**
- Marcus: F, with his wrong claims quoted back as evidence.
- Diego: "Flagged missing. It doesn't hand him a zero — it asks you to confirm."
- "Every one of these is a draft. The instructor reads them, adjusts them, and only then records
  anything."
- Leila, 50%: "And Leila hadn't finished. What if she'd found that out *before* the deadline?"

**→ Next:** That question *is* the next tool.

---

## 0:59–1:22 · Tool 4: Pre-Assessment Triage

### Slide 20 — Section: Pre-Assessment Triage
**Say:** "The last tool is for students — and it's the one I'm going to build live."

### Slide 21 — One line turns grading into triage *(3 min)*
**Do:** In the Quick builder view of the Grading app, paste the extension line. While it builds
(1–2 minutes), talk.
**Say:**
- Read the line aloud. "The limits are part of the instruction: Present, Partial, or Missing,
  with the quote it's based on. Never a score. Never a rewrite."
- "It only reads the *present when* lines — never the weights. It doesn't have the information
  it would need to calculate a grade."

**Fallback:** If the build hasn't finished after 2 minutes, switch to the pre-extended copy. Don't
wait on stage.
**→ Next:** "Let's give it Priya's paper."

### Slide 22 — Priya's draft, a week early *(3 min)*
**Do:** Upload Priya's paper in Triage mode, then run the same paper in Grade mode.
**Say:**
- "Four Missing, one Partial — each with the quote it's based on, or 'no passage found.'"
- "In Grade mode, that's a 13 — an F. In Triage mode, she sees it while there's still time to
  fix it."
- Then Leila, quickly: "Partial. The thesis is there, and she describes running times, but
  there's no big-O and no alternative structure. An honest unfinished draft."

**→ Next:** "Now the limits — which are the point."

### Slide 23 — The limits are the design *(2 min)*
**Say:**
- Walk the four limits.
- The honest limit: "Run Marcus through Triage and his running-time section comes back
  **Present**. It's there. It's wrong. Triage checks that things are there, not that they're
  right — that's the grader's job, and yours. **The moment a student-facing tool starts judging
  correctness, it's giving grades.**"

**→ Next:** "Your turn to try to break it."

### Slide 24 — Break it *(1:07–1:14, 7 min, hands-on)*
**Do:** Everyone opens the Triage app on their own account.
**Say:** "For the next seven minutes, you're the student who wants the answer. Get it to rewrite
your work, score it, or even hint at a grade. Use the four on screen, then invent your own."
**Collect:** "Did anything get through?" A volunteer writes each one down, word for word. "If it
got through, that's a finding, not a failure — it goes straight into the test script."
**→ Next:** "Now make it yours."

### Slide 25 — Your turn: Triage for your rubric *(1:14–1:22, 8 min)*
**Say:** The four steps. "A three-sentence fake draft is enough to see Present, Partial, and
Missing. Check that every status quotes a passage — a status without a quote is a guess."
**→ Next:** "Let's wrap up."

---

## 1:22–1:30 · Wrap

### Slide 26 — What you leave with *(2 min)*
**Say:** The three things they made today, plus the take-home kit, and where to find it.

### Slide 27 — Ground rules *(2 min)*
**Say:** One sentence on each rule. End on: "**These tools prepare. You decide.**"

### Slide 28 — Thank you / questions *(to 1:30)*
Likely questions, with short answers:

| Question | Answer |
|---|---|
| "Can students game Triage?" | It can't give them a grade or new text to game. The worst case is a student learning which sections they're missing — which is the point. |
| "Is this FERPA-compliant?" | The tools aren't the issue; where the data goes is. Use approved systems for real student work. Today used only synthetic data. |
| "Does it work outside CS?" | Yes — the rubric is what carries the discipline. Everything today started from an assignment prompt and a reading. |
| "Can it plug into my LMS?" | Not directly today. Export the rubric and paste it in; the grader's output is a draft you enter by hand. |
| "Why not let it grade and be done?" | Slide 11. The grade is only as good as the rubric, and a person has to own it. |
