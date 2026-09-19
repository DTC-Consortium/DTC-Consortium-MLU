# Build, Break, and Question a PartyRock Phishing Detector

**AI in Cybersecurity — Student Assignment**

| | |
|---|---|
| **Estimated student time** | 2–3 hours |
| **Tools needed** | AWS PartyRock (free), a web browser, a shared spreadsheet |
| **Level** | Intro–intermediate cybersecurity, digital literacy, or AI-literacy courses |

In this assignment you will build a working phishing-email detector using PartyRock — Amazon's
no-code generative AI app builder — test it against real and fabricated emails, try to intentionally
trick it, and reflect on what the experience teaches us about relying on AI in cybersecurity work.

## Learning objectives

- Build a functioning AI-powered classification tool without writing code.
- Compare human judgment against AI judgment on the same task, using a real dataset.
- Design adversarial test cases that probe the limits of an AI system.
- Articulate, in writing, where AI helps, where it fails, and why human review still matters in
  security workflows.

## What you'll turn in

1. Your **PartyRock app link** (shared/public) or exported prompt configuration.
2. A completed **results table** comparing your classifications, the AI's classifications, and the
   ground truth for at least 15 emails.
3. A short **"Fool the AI" log** documenting at least 5 adversarial attempts and outcomes.
4. A written **reflection (400–600 words)** — see Part 4 for the exact prompts.

---

## Part 1 — Build a PartyRock phishing detector

1. Go to [partyrock.aws](https://partyrock.aws) and sign in with an Amazon/AWS Builder ID. It is
   free and requires no credit card.
2. Create a new app (now **Flows**) **from scratch — do not use a template** — and name it something
   like "Phishing Email Detector."
3. Add a **text input widget** where a user can paste the full text of an email. Headers optional,
   body required.
4. Add a **generative text or chat widget** that takes that pasted email as input and outputs a
   structured judgment. At minimum, your prompt should instruct the model to return:
   - a **verdict**: Phishing / Suspicious / Legitimate;
   - a **confidence level**: Low / Medium / High;
   - **2–3 specific red flags** it noticed, or "none found";
   - a **one-sentence explanation** of its reasoning.
5. **Iterate on your prompt.** A weak prompt — "Is this phishing?" — gives vague answers. A strong
   prompt tells the model what to look for (sender/domain mismatches, urgency language, suspicious
   links, spoofed branding, requests for credentials or payment, generic greetings, grammar issues)
   and tells it exactly what format to answer in.

**Optional stretch goal:** add a second widget that rewrites a flagged email into a short "why this
is dangerous" explanation aimed at a non-technical coworker.

> **Tip.** Test your app on 2–3 obvious phishing emails and 2–3 obviously safe emails before moving
> on. If it can't get the obvious cases right, revise your prompt before you start real testing.

---

## Part 2 — Test and compare: you vs. the AI

Your instructor will provide, or direct you to, a shared bank of at least 15 sample emails with a
known ground-truth label (Phishing / Legitimate / Suspicious) that your instructor has
pre-classified. If no bank is provided, you may build your own using real reported-phishing archives
— for example your organization's IT security awareness materials. **Never use real personal or
confidential email.**

1. **Before running anything through your AI**, read each email yourself and record your own
   classification and confidence.
2. Then paste each email into your PartyRock app and record its verdict, confidence, and stated red
   flags.
3. Fill in the comparison table below, or the shared spreadsheet your instructor provides, for every
   email.

### Results table

| # | Email summary | Your verdict | AI verdict | Ground truth | Match? (You / AI) | Notes |
|---|---|---|---|---|---|---|
| 1 | e.g. "Your Account Suspended" from IT-support@… | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |

After completing all rows, calculate:

- **Your own accuracy rate** (correct / total).
- **The AI's accuracy rate** (correct / total).
- **Cases where you and the AI disagreed** — and who was right.
- **Any pattern in what the AI consistently got wrong** — well-written phishing, spoofed internal
  senders, legitimate-but-unusual emails.

---

## Part 3 — "Fool the AI" experiment

Now switch roles. Instead of testing accuracy, try to **break** the detector. Your goal is to craft
at least 5 emails that you believe will cause the AI to misclassify — either a phishing email that
slips through as "Legitimate," or a legitimate-sounding email that gets wrongly flagged as
"Phishing."

Brainstorm techniques real attackers use to evade AI and spam filters, for example:

- Removing urgency language while keeping a malicious link.
- Using a legitimate-looking but slightly altered domain, e.g. `micros0ft-support.com`.
- Splitting suspicious keywords with invisible characters or unusual spacing.
- Mimicking a real internal email format — IT ticket, HR notice, calendar invite.
- Writing an unusually formal, well-written phishing attempt with no typos.

Craft your 5+ test emails using **fictional companies and names only** and run each through your app.

### Fool the AI log

| # | Technique used | Intended trick | AI's actual verdict | Did you fool it? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

---

## Part 4 — Reflection (400–600 words)

Write a short reflection responding to all of the following. **Refer to specific examples from your
results table and Fool the AI log — don't answer in the abstract.**

1. **Accuracy.** How did your accuracy compare to the AI's? Were there types of emails the AI was
   clearly better or worse at than you?
2. **Limitations.** Based on your Fool the AI experiment, what kinds of phishing techniques does
   this AI tool struggle with? Why do you think it struggles there?
3. **Confidence vs. correctness.** Did the AI's confidence level actually track with whether it was
   right? What are the risks of an AI that sounds confident but is wrong?
4. **Human oversight.** Given everything you observed, describe one specific way you'd design a real
   security workflow so that an AI phishing detector like this one *assists* a human analyst rather
   than replaces them.
5. **If you had one more hour.** What is one change you'd make to your prompt or app to fix a
   weakness you found?

---

## Grading rubric

Total 100 points. See [`materials/rubrics/`](../rubrics/phishing-detector-rubric.md) for the full
version, including what each band is looking for.

| Component | Points |
|---|---|
| Working PartyRock app | 20 |
| Results table (Part 2) | 25 |
| Fool the AI log (Part 3) | 20 |
| Written reflection (Part 4) | 30 |
| Clarity & submission | 5 |
