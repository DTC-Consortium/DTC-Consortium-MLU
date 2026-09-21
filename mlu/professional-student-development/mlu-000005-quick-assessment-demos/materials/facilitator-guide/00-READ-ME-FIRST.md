# Read me first

This is everything needed to deliver **The Assignment Lifecycle** — a 90-minute session in which
one assignment travels through four AI tools: building its rubric, hardening it against chatbots,
grading it, and letting students check their own drafts before they submit.

You are holding the facilitator edition. Participants get a different, shorter pack.

---

## Three things to know before you plan anything

**1. Nothing is pre-built, and that is the design.** Attendees build three of the four tools
themselves, in the room, from prompts they paste into Amazon Quick. No apps are published to
anyone's account beforehand and no assets are pre-loaded. Everything arrives through **one Google
Drive folder**, reached by the QR code on slide 0 and in the corner of every slide after it.

*The prompt pack* has the five prompts — three for attendees, two for you — each with the steps to
read aloud and the outputs it must produce on the sample data. *The shared folder* says what goes
in the folder and how to share it.

**You still have to build the two facilitator apps before you can rehearse.** The grading demo is
thirteen minutes of the session and it needs something to demo. That is the largest item between
you and delivery, and it is much smaller than it used to be.

**2. The approved copy on the 28 slides may be removed, never added to.** That permission is what
made this restructure possible: the slides that pointed at pre-published apps had their steps
deleted rather than rewritten, and the steps now live on the prompt cards where they can be
revised freely. `verify_deck.py` proves every build is still subtractive and `export_pdf.sh` will
not run until it passes. Slide 0 is new material and sits outside that check. *Deck approval
status* is short; read it before you open any deck file.

**3. All the student work here is invented.** Five students, four papers, one roster — none of it
real. Say so out loud during the session, and do not substitute real student work when you rehearse.
The same rule goes on the screen for attendees at slide 13: assignments and rubrics only.

---

## The order to work in

| # | Read | Why |
|---|---|---|
| 1 | **Deck approval status** | The constraint that shapes everything else |
| 2 | **The prompt pack** | What the room builds, and what you must build first |
| 3 | **The shared folder** | What attendees scan into, and how to set it up |
| 4 | **Talk track** | The session itself, slide by slide, with the clock |
| 5 | **The sample pack** | The five students, and what each is for |
| 6 | **The assignment, the weak rubric, the reference rubric** | The material the tools operate on |
| 7 | **The rubric format** | The interchange format all four tools read and write |
| 8 | **The handout** | Print one per attendee, face down on the tables |

The deck is reproduced in full at the back.

---

## The spine, in one paragraph

If you only protect one thread, protect this one. The room grades a student paper — Marcus Lee's —
using the weak rubric on the handout, cold, before anything is explained. You count their grades;
most rooms say B. The same paper then scores 88 (a B+) under that rubric and an F under a
generated one that asks whether the claims are true. Marcus's three wrong claims are shown against
the course reading. At the very end, the student-facing Triage tool passes his running-time section
anyway, because it checks that things are *present*, not that they are *correct*. Everything else
in the 90 minutes can compress. That thread cannot.

---

## What will go wrong, and what to do

- **Sign-in eats the first twelve minutes.** It is budgeted for. At 0:12 move on regardless and let
  volunteers keep working the room.
- **Someone can't scan the QR code.** Volunteers carry a laptop with the folder open and can
  AirDrop or email the link. Don't spend stage time on it. Fill in `DRIVE_SHORTLINK` in
  `session_config.py` and slide 0 will also carry a typable link.
- **A build is slow, or produces something odd.** Expected, and useful. Tell the app what's wrong
  in plain words and let it revise — say so out loud, because that describe-then-fix loop is
  exactly the contrast you draw against Kiro on slide 17.
- **The room falls behind on slide 13.** Prompts 2 and 3 need *a* rubric, not *their* rubric.
  Point them at `rubric-golden.json` in the folder and let them keep building in the background.
- **The live build on slide 21 is slow.** Have the pre-extended copy open in another tab and switch
  after two minutes. Do not wait on stage.
- **A CS faculty member spots Marcus's errors early.** Ask them to hold it for slide 12, then call
  on them. Note that Marcus makes more than the three errors the slide lists — the talk track says
  which.
- **Someone brought no assignment.** They use the sample.
