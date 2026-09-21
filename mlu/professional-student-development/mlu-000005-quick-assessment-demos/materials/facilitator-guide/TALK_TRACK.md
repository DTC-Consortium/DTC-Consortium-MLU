# Talk Track — The Assignment Lifecycle (90 min)

What to say on each slide of `../assessment-lifecycle-deck.pdf`, and what has to have happened
before you click to it. Times are the session clock.

> **This delivery — 2026 AWS-MLU AI Teaching & Research Symposium, Day 1**
>
> | | |
> |---|---|
> | **Monday, September 21, 2026** | Howard University · Armour J. Blackburn Center |
> | **1:30 – 3:00 PM** | 90 minutes exactly — the session clock below maps 1:1 |
> | **Blackburn Ballroom** | Educators Consortium (Faculty) track |
> | Closing plenary | 3:15 PM in the Ballroom, so 3:00 is a hard stop |
>
> **You are straight after lunch** (12:30 – 1:30, same building). People will trickle in for the
> first five minutes and some will still be eating. Slide 0 is up and the QR is scannable before
> anyone sits down — that is the whole reason it exists.
>
> **Wi-Fi details are "shared on-site"** per the Know Before You Go, so you cannot test the
> network until you are in the room. Get there early and load the folder, Quick, and Kiro on the
> presenter machine before the room fills. Everything in this session is cloud-based; there is no
> offline path.

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

That thread used to leak: slide 7's Marcus card read *"Fluent, confident — and wrong about
running times,"* spending the reveal about twenty minutes early. **That clause has been deleted**
— the card now reads "Fluent, confident." Play slide 7 straight; there is nothing to work around
any more.

---

## Before the session

> ### Nothing is pre-built, and that is the design
>
> Attendees build three of the four tools themselves, in the room, by pasting a prompt into
> Amazon Quick. You build the fourth in advance and they watch. No apps are published to anyone's
> account beforehand, and no assets are pre-loaded.
>
> Everything they need arrives through **one Google Drive folder**, reached by the QR code on
> slide 0 and in the corner of every slide after it.
>
> **→ [`../prompts/`](../prompts/README.md)** — the five prompts, each with the steps to read
> aloud and the outputs it must produce on the sample pack.
> **→ [`../prompts/DRIVE-FOLDER.md`](../prompts/DRIVE-FOLDER.md)** — what goes in the folder,
> how to lay it out, and the sharing settings.
>
> **You still have to build F1 and F2 before you can rehearse.** The grading app is a demo, and
> a demo with nothing to demo is thirteen dead minutes.

**Well before — this is the long pole**
- [ ] **F1 and F2 built and tested** against the sample pack. Marcus **F**, Diego **missing**.
- [ ] **Prompts 1–3 run end to end yourself**, on a fresh account, timed. If a build takes four
  minutes on your machine it will take longer on theirs, and slide 13 has twelve.
- [ ] The **shared folder** assembled and its checklist worked through —
  [`../prompts/DRIVE-FOLDER.md`](../prompts/DRIVE-FOLDER.md).
- [ ] `DRIVE_URL` in `session_config.py` matches the folder, and the deck rebuilt after any change.
- [ ] `python3 verify_deck.py` passes: QR on every slide, decoding to that URL.

**48 hours before**
- [ ] Quick invites sent, and accepted by most attendees. Volunteers have the list of anyone who
  hasn't accepted. *(For this delivery both routes are live: attendees got an invitation email,
  and the Know Before You Go told everyone to set Quick up themselves at
  `quick.aws.com/sn?utm_campaign=mlu2026`. Expect a mix, and expect some of both to have done
  neither. Quick is free, so nobody is blocked — they just lose minutes.)*
- [ ] Registration email asked everyone to bring **one assignment prompt and its learning
  objectives, as text — no student work.**

**Morning of**
- [ ] On every table, face down: `hook-handout.md` (Marcus's paper + the weak rubric), one per
  person. Plus a table card with sign-in help and the folder QR code.
- [ ] **Scan slide 0 from the back of the room, off the actual projector.** Not off your laptop.
  This is the check that fails in the room and nowhere else.
- [ ] The folder opens **signed out**, in an incognito window, on a phone.
- [ ] Your own Quick account has F1 built, plus the **pre-extended Triage copy** as the fallback.
- [ ] Presenter tabs open, in order: the shared folder → Kiro (`requirements.md` open) → the
  Grading app in the **builder** view (for the live extension) → the pre-extended Triage fallback.
- [ ] On the desktop: `Marcus_Lee.txt`, `Priya_Chandra.txt`, `Leila_Haddad.txt`,
  `rubric-weak.md`, `rubric-golden.md`, and the Triage extension line, ready to paste.
- [ ] The Kiro grader already run once, with the results saved, in case the live run is slow.
- [ ] One volunteer assigned to **count hands on slide 4** and write the tally down.
- [ ] Decide the `rubric-golden` timing question in `DRIVE-FOLDER.md`. Don't leave it to the day.
- [ ] **Get into the room during lunch.** The wi-fi is not testable until you are on it, the
  session is cloud-only, and you are following straight on from the meal in the same building.
- [ ] One volunteer briefed to work the door for the first five minutes: point at slide 0, say
  "scan that," and help anyone who never set up Quick.

---

## 0:00–0:12 · Arrival and sign-in

### Slide 0 — Everything you need is in this folder
**Before:** This is up before you say a word, and it stays up while people find seats. The room
is not signed into anything yet.

**Say** (as soon as a few people are looking):
- "Before anything else — scan the code on the screen. That folder is the whole session."
- "Nothing today is pre-installed and nothing is pre-built. You are going to build three tools
  yourself, from prompts in that folder, in the next ninety minutes. That is deliberate: an app
  I share with your account is something you lose. A prompt is something you keep."
- Read the short link aloud for anyone who can't scan, if you have one.

**Do:** Leave it up. Genuinely leave it up — longer than feels comfortable. People are still
walking in.
**Note:** The same code sits in the bottom-left corner of every slide from here on, so latecomers
can pick it up at any point. Say that once, now, and you won't be asked again.
**Fallback:** If the room's wifi is hostile or the code won't scan, volunteers carry a laptop with
the folder open and AirDrop or email the link. Don't burn stage time on it.
**→ Next:** "Let's get started."

### Slide 1 — Cover
**Before:** People are arriving — **straight from lunch in the same building**, so they will
trickle rather than arrive. Slide 0 has been up throughout and stays up until most seats are
full. Don't start on time to an empty room; start when the room is there, and take it out of the
sign-in window, which is the only twelve minutes with slack in them.
**Say** (once most seats are full, 30 seconds):
- "In the next 90 minutes you'll see four AI tools that take one assignment from start to
  finish: build the rubric, tighten the assignment, grade it, and let students check their own
  work before they hand it in."
- "You'll use two of them on your own course. First, let's get you logged in."

**→ Next:** "Sign-in first, and I've got a job for you while you wait."

### Slide 2 — Get signed in, and start grading
**Before:** Nothing is printed and nothing is on the tables. Everyone is in **one Google Doc** —
*★ THE ASSIGNMENT LIFECYCLE — follow along here* — which holds the paper, the rubric, the
assignment and all three prompts. Volunteers are at the edges of the room, and their first job is
getting people into that document.
**Say:**
- Walk the three steps on screen. *(There used to be a fourth — "find Apps in the left menu,
  today's tools live there." It was deleted: nothing is waiting in that menu. They build the
  tools themselves, starting at slide 13.)*
- **Cover both routes in one breath:** "If you got an invitation email, use it. If you didn't,
  or you can't find it, the sign-up link was on the slide before this one — Quick is free and
  it takes a minute." Don't let anyone conclude they're locked out; nobody is.
- "Scan the code on the screen. It opens one document — that document is the whole session."
- "Scroll to **Step 1**. There's a student paper and the rubric that came with the assignment.
  While sign-in loads — or once you're in — grade it. Three minutes. **Use only that rubric.**
  Write a score and a letter; there's a line for it in the doc."
- "You don't need to know computer science. Grade it the way the rubric tells you to — the way a
  TA would, or the way you would at 11 p.m. with forty more in the pile."

**Do:** Get the document on screen and leave it there while they find it. Volunteers circulate,
checking people are in the doc and scrolled to Step 1 — that is the only thing that matters in
these twelve minutes. Give a two-minute warning at
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
- "Hands up if you gave Marcus an A." Count. "B?" "C?" "F?" **Those are the four letters on the
  slide — don't call for a D.** Anyone holding a B+ or B- raises on "B"; anyone holding a D raises
  on "C" or "F", and it won't change the tally.
- Say the result out loud: "So most of this room gave him a B." Use whatever the tally actually
  shows — slide 11 lands best when the number you say here is the number you call back to.
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

> **This slide used to give Marcus away.** His card read *"Fluent, confident — and wrong about
> running times,"* which spent the slide-11 reveal twenty minutes early and needed a paragraph of
> talk-track to work around. The clause has been deleted — see
> [`../DECK-APPROVAL.md`](../DECK-APPROVAL.md). Play it straight now.

**Say:** One line each, plus what that student tests:
- **Aisha** — the control. What good looks like.
- **Marcus** — "You've already met Marcus. You graded him twenty minutes ago. Keep that grade in
  front of you." **Say nothing else about him.** Don't hint, don't pause meaningfully, don't
  smile. Slide 11 is worth much more if the room is still sure they read him correctly.
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
- "**Half the points** — 60 of the 100 — go to things anyone can see without expertise:
  organization, mechanics, length." *(The slide reads "Half the points." Say it that way, then
  give the number. Don't correct the slide on stage — "Half the points" is the approved wording and
  it can't be reworded, only removed, and it's worth keeping.)*
- "'Understanding' is never defined, so every grader supplies their own standard — or none."
- "Nothing asks whether a single claim is true."
- "And learning objective 2 — running-time guarantees — isn't assessed by any criterion."
- The key line: "**Hand this rubric to an AI grader and you get the same B, just faster.
  Automation doesn't fix a rubric. It scales it.**"

**Do:** Before you move on — "Go back to Step 1 in your doc and type **WEAK RUBRIC — DON'T
REUSE** above that table." Wait for it. They are saving a copy of that document at the end, and
without the mark it carries a clean, professional-looking rubric that someone will reuse in March.

**→ Next:** "So the first tool fixes the rubric."

### Slide 10 — What the Rubric Builder does *(1 min)*
**Do:** Switch to your own copy of the Rubric Builder — the one you built from
[`PROMPT-1`](../prompts/PROMPT-1-rubric-builder.md) while preparing — with the sample assignment
already pasted. Generate, or show the pre-generated rubric.
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
- "Under the original rubric: 88 out of 100 — a B+." Then use the tally: "**That's where most of
  you landed too. You graded exactly the way the rubric told you to.**"
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
**Before:** Everyone is signed into Quick and has the follow-along doc open at **Step 2**.

> **Everyone uses the same assignment.** Nobody brought their own and nobody needs to — the
> assignment and its four objectives are in the doc, ready to paste. The slide title says "your
> assignment"; say **"the assignment in your doc"** and nobody will notice. It buys the segment
> four or five minutes and it means forty people hit the same problems at the same time, which is
> what makes the volunteers effective.

> **The slide no longer carries the steps.** It shows the title, the "check it" questions and the
> clock. The steps are on the prompt card —
> [`PROMPT-1`](../prompts/PROMPT-1-rubric-builder.md), *"1 — Build the Rubric Builder"* in the
> folder. Read them aloud once while people find it, then let them work from the card. That is
> why they were moved: the card can be revised, the slide cannot.

**Say:**
- "Step 2 in your doc. Copy **Prompt 1** — it's between the two marker lines. Click before the
  first word, shift-click after the last."
- "Paste it into Quick, into the box that asks you to describe your app. Send it. It takes about
  ninety seconds to build — while it does, read the three questions on the screen."
- "When it's ready, the assignment and the objectives are in the doc right under the prompt.
  Paste both in and generate."
- Then the three "check it" questions, and the privacy rule: **assignments and rubrics only,
  never student work.**

**Do:** Start the timer and circulate. The first two minutes are a build, not a task — expect the
room to go quiet and then noisy.
- At 3 minutes: "Everyone should have an app by now. If you don't, raise a hand."
- At 6 minutes: "If you've generated a rubric, start on the check questions."
- At 10 minutes: "**Save or copy your rubric. You'll need it twice more.**"

**If something goes wrong:**
- No assignment → use `assignment.md` from the folder.
- **The build fails or produces something odd** → tell it what's wrong in plain words and let it
  revise. Say this out loud when it happens — that describe-then-fix loop is exactly the contrast
  you draw on slide 17.
- The output cuts off → regenerate with fewer criteria.
- Can't reach the folder → a volunteer AirDrops or emails the link.
- **Badly behind at 10 minutes** → have them use `rubric-golden.json` from the folder for the next
  two segments and keep building afterwards. Prompts 2 and 3 need *a* rubric, not *their* rubric.

**→ Next:** "You have a rubric. Now: could a chatbot just do the assignment?"

---

## 0:36–0:46 · Tool 2: the AI-Proofing Assistant

### Slide 14 — Section: The AI-Proofing Assistant
**Say:** "Second tool. Ten minutes, on the same assignment you just built a rubric for."

### Slide 15 — Could a chatbot do this assignment? *(10 min, hands-on)*
**Say:**
- **Prediction first, before anyone opens anything:** "Look at your assignment. Which requirement
  could ChatGPT meet in 30 seconds, knowing nothing about your course? Write it down." Wait for
  pens. This is the whole segment — the tool is just the answer key.
- "Now: folder, item *2 — Build the AI-Proofing app*. Same routine. Copy, paste, send."
- Then they paste the assignment and the rubric they built, and read the flags.
- The framing: "The goal isn't to make cheating impossible. It's to make the assignment *need*
  your course — your reading, your class discussion, the student's own process."

**Do:** In the last 2 minutes, debrief: "Did it flag something you didn't predict? Which change
would you actually make?" Take two answers.
**Note:** The steps are on [`PROMPT-2`](../prompts/PROMPT-2-ai-proofing.md), not on the slide.
The original talk track carried a note here that slide 15's steps had to be rewritten to match
the finished app — that is settled. The steps live on the card now, and the card is yours to
change.
**→ Next:** "Now grading. This one you watch."

---

## 0:46–0:59 · Tool 3: the Grading Assistant (Kiro)

### Slide 16 — Section: The Grading Assistant
**Say:** "Third tool, built in Kiro. A grader is the tool where being wrong costs the most, so it's
the one we built most carefully."

### Slide 17 — Review the spec before the code *(4 min)*
**Do:** Switch to Kiro and show `requirements.md` — the one you prepared from
[`PROMPT-F2`](../prompts/facilitator/PROMPT-F2-kiro-grader.md).
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
**Do:** Run the grader in Kiro on all five, or show the saved results. (Saved results are the
safer choice and nobody minds — say you're showing a run from this morning.)
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
**Do:** In the Quick builder view of **your** Grading app — the one you built in advance from
[`PROMPT-F1`](../prompts/facilitator/PROMPT-F1-grading-app.md) — paste the extension line. It is
slide 21's copy verbatim, so what you paste matches what is projected behind you. While it builds
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
**Before:** They need a Triage app of their own to attack, and they don't have one yet — yours is
an extension of a grading app they never built. **Start them building at the top of this segment:**
folder, item *3 — Build Triage* ([`PROMPT-3`](../prompts/PROMPT-3-triage.md)). It builds while you
talk through slides 22 and 23, and it's ready when this slide goes up.

**Do:** Everyone opens the Triage app they just built.
**Say:** "For the next seven minutes, you're the student who wants the answer. Get it to rewrite
your work, score it, or even hint at a grade. Use the four on screen, then invent your own."
**Collect:** "Did anything get through?" A volunteer writes each one down, word for word. "If it
got through, that's a finding, not a failure — it goes straight into the test script."
**→ Next:** "Now make it yours."

### Slide 25 — Your turn: Triage for your rubric *(1:14–1:22, 8 min)*
**Before:** They built the app in the last segment. This is where they point it at their own
rubric.
**Say:** "Paste the rubric you built in the first hands-on — the one you generated, not the weak
one from your handout. Triage reads the *present when* lines, and the handout rubric hasn't got
any." Then: "A three-sentence fake draft is enough to see Present, Partial, and Missing. Check
that every status quotes a passage — **a status without a quote is a guess.**"
**Note:** Steps are on [`PROMPT-3`](../prompts/PROMPT-3-triage.md); the slide shows only the
check, because the check is the part that has to be on screen while they work.
**→ Next:** "Let's wrap up."

---

## 1:22–1:30 · Wrap

### Slide 26 — What you leave with *(2 min)*
**Say:** The three things they made today, plus the take-home kit, and where to find it.
- Point at the QR code in the corner: "Same folder, all day. It'll stay up for «say how long»."
- Land the reason it was built this way: "**You didn't get given three apps. You built three
  apps, and you still have the prompts.** That's the part that survives — accounts expire, shared
  apps get unshared. A prompt in a folder you saved works next semester."

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
| "Does Amazon Quick cost anything?" | No — it's free to set up and use, and that's what everything today ran on. Link: `quick.aws.com/sn?utm_campaign=mlu2026` |
| "Will I still have these apps next week?" | The apps live in your own account, so yes. And if you ever lose them, the three build files in the folder rebuild each one in about ninety seconds. That's the part worth saving. |
