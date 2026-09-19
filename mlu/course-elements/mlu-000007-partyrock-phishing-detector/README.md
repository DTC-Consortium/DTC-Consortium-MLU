# Build, Break, and Question a PartyRock Phishing Detector

**`mlu-000007`** · Course Elements · v1.0.0 · **classroom-tested**

Students build a phishing-email classifier in Amazon PartyRock, with no code. Then the assignment
does something most AI assignments don't: it asks them to **attack the thing they just built**.

First they classify at least 15 emails themselves — before the AI sees any of them — and compare
both sets of verdicts against ground truth the instructor holds. Then they spend a round trying to
fool their own detector, logging each technique and whether it worked. The reflection that closes it
out is worth more points than the build, deliberately, because the build is the part AI can help
with and the reflection is not.

> ## ⚠️ One thing to prepare before you schedule this
>
> **The ground-truth email bank is not included, and the assignment cannot run without it.** You
> need at least 15 pre-labelled sample emails — roughly 40% clearly phishing, 30% clearly
> legitimate, 30% genuinely ambiguous — built from vetted phishing-awareness archives or your
> institution's own security training material. **Never from real captured personal mail.**
> The [facilitation guide](materials/faculty-guide/instructor-facilitation-guide.md) has the full
> spec. This is the real preparation cost of the assignment.

## At a glance

| | |
|---|---|
| **Audience** | Undergraduates; intro–intermediate cybersecurity, digital literacy, or AI literacy |
| **Duration** | 2–3 hours of student work; one 90-minute session, or two 50-minute sessions |
| **Delivery** | In person or hybrid |
| **Runs on** | Amazon PartyRock in a browser. Nothing to install. |
| **Prerequisites** | Free AWS Builder ID; a shared spreadsheet; **an instructor-built ground-truth email bank** |
| **Expected cost** | None in tooling. Real cost is instructor prep time for the email bank. |
| **Sample data** | Not included — you supply the email bank. All student-authored test emails must use fictional companies and names. |
| **You end with** | A published detector, a 15-row human-vs-AI accuracy comparison, an adversarial log, and a 400–600 word evidence-based reflection |

## Learning outcomes

By the end, a student can:

1. Build a functioning AI-powered classification tool without writing code.
2. Compare human judgment against AI judgment on the same task, using a labelled dataset.
3. Design adversarial test cases that probe the limits of an AI system.
4. Judge whether a model's stated confidence tracks its actual correctness.
5. Articulate, in writing, where AI helps, where it fails, and why human review still matters in
   security workflows.

## Contents

| Path | What it is |
|---|---|
| [`materials/assignments/phishing-detector-assignment.md`](materials/assignments/phishing-detector-assignment.md) | The student handout — build instructions, results table, Fool the AI log, five reflection prompts |
| [`materials/assignments/phishing-detector-assignment.docx`](materials/assignments/phishing-detector-assignment.docx) | The author's original Word version, carrying both student and instructor parts in one file |
| [`materials/faculty-guide/instructor-facilitation-guide.md`](materials/faculty-guide/instructor-facilitation-guide.md) | **Start here.** Prep checklist, phase-by-phase facilitation, debrief questions, pitfalls table, and the guardrail to say out loud |
| [`materials/rubrics/phishing-detector-rubric.md`](materials/rubrics/phishing-detector-rubric.md) | The 100-point rubric and how to score the two things students get wrong |

## The design point worth teaching

**Confidence is not correctness.** The assignment is built so students discover, from their own
data, that a model can be assertively wrong — and then asks them what that means for a security
workflow where someone acts on the verdict.

That is also why the human classification must happen *before* the AI's verdict is visible. The
single most common way this assignment fails is a student filling in their own column after reading
the AI's answer, which quietly destroys the comparison the whole thing rests on. The facilitation
guide tells you how to structure the spreadsheet so it can't happen.

## How to use it

1. **Download** this contribution — see [Downloading a contribution](../../../README.md#downloading-a-contribution).
2. **Build the ground-truth email bank and its answer key.** Nothing else can proceed until it
   exists.
3. **Test `partyrock.aws` from a lab machine** a week ahead. Some campus networks block AWS domains;
   the guide names a fallback.
4. **Read the [facilitation guide](materials/faculty-guide/instructor-facilitation-guide.md) end to
   end**, especially the hook and the release timing for the email bank.
5. **Tell students the rubric penalizes generic reflections** when you assign it. Saying so in
   advance changes what they submit.

## Related

Week 4 of the same course is [`mlu-000006`](../mlu-000006-partyrock-marketing-assistant), which
establishes that prompt structure changes output quality. **Run that one first** — this assignment
assumes students already know how to structure a prompt, and asks them to attack one instead.

## Reuse and attribution

Documentation is `CC-BY-4.0`. See [`LICENSE.md`](LICENSE.md) and [`CITATION.cff`](CITATION.cff).
No real email, student work, or student records appear anywhere in this contribution, and the
assignment requires students to use fictional companies and names in every test case they author.

Structured metadata for this contribution lives in [`mlu-contribution.yml`](mlu-contribution.yml).
