# Instructor facilitation guide — PartyRock Phishing Detector

This guide walks you through preparing for, running, and grading the assignment. It assumes one
90-minute session; a two-session split of 50 + 50 minutes is noted where relevant.

## Before class — prep checklist

- [ ] **Confirm students can reach `partyrock.aws` on the school or lab network.** It requires only
      a free AWS Builder ID — no credit card — but some school networks block AWS domains. Test this
      in advance.
- [ ] **Prepare the ground-truth email bank**: at least 15 sample emails, roughly 40% clearly
      phishing, 30% clearly legitimate, 30% genuinely ambiguous or "suspicious." Pull from a vetted
      phishing-awareness archive or your own institution's IT security training materials. **Do not
      use real captured personal emails.**
- [ ] **Pre-label the ground truth** for each sample email and keep an answer key for yourself,
      separate from what students receive.
- [ ] **Set up a shared spreadsheet** (Google Sheets or Excel Online) with the results-table format
      pre-built, one tab per student or team, so you can monitor progress live.
- [ ] **Decide individual vs. pairs.** Pairs work well here — one student can paste and test while
      the other tracks results, and both can prompt-engineer together.
- [ ] **Skim 2–3 finished example PartyRock phishing-detector prompts yourself** beforehand, so you
      can recognize a weak prompt (e.g. just "is this phishing? yes/no") from a strong one during
      walk-around.

## Step-by-step facilitation notes

### 1. The hook (Part 1 setup)

Before students touch PartyRock, show two real-style phishing examples — one obvious, one
well-crafted — and take a quick class vote by show of hands.

The point isn't the trivia. It is demonstrating that **even attentive humans miss well-crafted
phishing**, which motivates why an AI assistant could plausibly help, while also seeding healthy
skepticism about whether it will help *enough*.

### 2. Building the detector

Most first-attempt prompts are too vague ("Is this a phishing email?"). As you circulate, look for
the three things below and help students who are missing them:

- Does the prompt specify a **structured output format** — verdict, confidence, red flags, reasoning?
  If not, results will be hard to compare later.
- Does the prompt **tell the model what signals to look for**, or is it just asking the model to
  guess unaided?
- Did the student **sanity-test on an obvious phishing and an obvious legitimate email** before
  moving to real testing?

If a group is stuck, suggest they look at their flow's output for an obviously-phishing email and
ask: *"what's missing that a security analyst would want to know?"* — then add that to the prompt.

### 3. Test and compare

**Release the email bank only after apps are functional.** Releasing it too early causes students to
spend testing time on broken prompts.

Circulate during this phase to catch the most common issue: students copying the AI's verdict into
the "your verdict" column without actually forming their own judgment first. Remind them the human
classification must happen **before** they see the AI's answer, or the comparison is meaningless.

### 4. Fool the AI

This is usually the most energetic part of class — let it be a little competitive. If working in
groups, ask each group to share their single best successful trick with a neighboring group, then
quickly poll the room for the most common evasion category: typosquatted domains vs. well-written
phishing with no red-flag language. This sets up the debrief perfectly.

### 5. Debrief discussion questions

Use these as seeds for a discussion board or an in-person discussion.

- Was there a type of email humans were more accurate on than the AI, or vice versa? What does that
  suggest about dividing labor between analyst and tool?
- Did any AI detector express **high confidence while being wrong**? Why is that specifically
  dangerous in a security context, compared to a tool that's wrong but says "low confidence, please
  review"?
- For the tricks that worked — could a real email filter or SOC analyst be fooled the same way?
  What's the real-world equivalent of what you just did?
- Should an organization ever let a tool like this auto-delete or auto-quarantine email without a
  human in the loop? Under what conditions, if any?

## Common pitfalls and fixes

| Pitfall | Fix |
|---|---|
| Students record their "human" verdict after already seeing the AI's answer, biasing the comparison. | Structure the handout or spreadsheet so the "Your Verdict" column must be filled before the AI is run on that row; spot-check during walk-around. |
| Prompt returns free-text prose with no consistent structure, making the results table hard to fill in. | Require the app's output to name a verdict, confidence, and red flags explicitly. Show a counter-example during the live demo. |
| Fool the AI emails are joke or nonsense content rather than genuine adversarial attempts. | Require each row to name a specific technique from the brainstormed list, or an original one. A technique-less row doesn't count toward the 5 minimum. |
| Reflection restates generic "AI is good/bad" talking points instead of citing the student's own data. | The rubric explicitly penalizes reflections that don't cite specific rows from the student's own tables. Say this out loud when you assign it. |
| School network blocks `partyrock.aws`. | Test access a week ahead. Have a backup plan: a different no-code AI builder, or a shared instructor-run PartyRock app students query collaboratively. |

---

## Why this assignment exists

Context from the author's Faculty Fellow presentation *From Prompt to Program: Scaffolding AI
Literacy from No-Code to Code* (AWS-MLU Fall 2026 AI Teaching & Research Symposium).

This is week 7 of **AI Essentials**, an 8-week no-code introduction to AI taken across majors. Week
4 — [`mlu-000006`](../../../mlu-000006-partyrock-marketing-assistant) — establishes that prompt
structure changes output quality. Week 7 asks the harder question: *what happens when the output is
a judgment someone might act on?*

**The student's role here is prompt engineer and skeptical auditor.** They build and tune the AI's
instructions so it classifies emails well, then deliberately stress-test and second-guess its
judgment rather than trusting it.

### The guardrail to say out loud

**Treat the AI as an aid, not an authority.** The clearest risk across this assignment is
over-trusting a confident-sounding verdict — a phishing call that is wrong with high apparent
confidence. Three rules make that concrete:

- **Require evidence, not just a verdict.** The app must show the reasoning behind a classification.
- **Use only sample or synthetic email data.** Never real personal correspondence.
- **Keep a human-in-the-loop rule.** No security decision ships on the AI's output alone.

### What students walk away with

- **Prompt engineering** — structuring role, context, constraints, and output format deliberately.
- **Critical evaluation** — scoring AI outputs against ground truth instead of accepting them.
- **Cyber and AI hygiene** — recognizing where automated judgment is reliable and where it needs a
  human check.
- **Iterative build-test thinking** — plan an input, inspect the output, fine-tune, retest.
