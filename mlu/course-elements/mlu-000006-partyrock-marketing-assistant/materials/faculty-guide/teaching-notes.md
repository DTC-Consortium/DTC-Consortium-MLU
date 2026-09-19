# Teaching notes — AI Marketing Assistant

Context for an instructor deciding whether this assignment fits their course, and what it is
supposed to accomplish once it does. Drawn from the author's Faculty Fellow presentation
*From Prompt to Program: Scaffolding AI Literacy from No-Code to Code* (AWS-MLU Fall 2026 AI
Teaching & Research Symposium).

## The problem this was built to solve

**AI Essentials** is an 8-week, no-code introduction to AI designed to be taken across majors —
business to the arts. Students already researched AI examples in their own field and presented video
solutions for each assignment. What was missing was the chance to **actually build something**.

> The challenge: give a mixed-major, non-coding audience a tactile way to *experience* machine
> learning, generative AI, and prompt engineering, instead of only describing those topics to them.

## Why PartyRock

PartyRock is Amazon Bedrock's free, no-code generative-AI app builder. Students describe what they
want in plain language and PartyRock assembles a working app with editable input widgets and live
model output.

- **No-code by design** — fits the course's core promise: every major, no programming background.
- **Editable, testable prompts** — students see and revise the underlying prompt driving each
  widget, so they can plan, test, refine, and repeat.
- **A real foundation-model sandbox** — built on Bedrock's foundation models, so students are
  working against the same class of system they read about.

## What changed in the course

| Before | After |
|---|---|
| Research examples in your major, then present a video walking through your solution. | Two PartyRock builds embedded directly in the assignment sequence — this one in week 4 (generative AI), the [phishing detector](../../../mlu-000007-partyrock-phishing-detector) in week 7 (cybersecurity). |
| Reflective but entirely observational. Students had a theoretical understanding of the concept and no direct contact with a working model. | Each build follows the same loop: plan the input, inspect the output, fine-tune, retest. |

## What students walk away with

- **Prompt engineering** — structure role, context, constraints, and output format to shape AI
  output deliberately.
- **Critical evaluation** — score AI outputs against a standard instead of accepting them at face
  value.
- **Iterative build-test thinking** — plan an input, inspect the output, fine-tune, retest. A real
  design loop.

## The guardrail to say out loud

**Treat the AI as an aid, not an authority.** The clearest risk in this assignment is that a student
accepts a fluent marketing claim that no supplied fact supports. Prompt C exists partly for this
reason — it ends with *"Do not make claims that are not supported by the information provided"*, and
comparing its output against Prompt A's is the moment to point that out.

Require evidence, not just output: ask students to identify, for each generated claim, which input
field it came from. Anything that came from nowhere is the lesson.

## Running it

- **Where it fits:** any course with a unit on generative AI, prompt engineering, or marketing
  communication. No programming background needed from students or instructor.
- **Pairs or solo:** either works. Pairs tend to produce better Part 3 comparisons because students
  argue about the scoring.
- **Check the network first.** Some campus networks block AWS domains. Test `partyrock.aws` from a
  lab machine before the session — this is the single most common day-of failure.
- **The comparison table is the assignment.** The app build is the hook; Part 3 is where the
  learning is. If time is short, cut Part 2 polish, never Part 3.

## Adapting this to your own course

The same three-step loop transfers to any discipline with a clear input/output:

1. **Pick one concept** already on your syllabus — generative AI, classification, forecasting.
2. **Build a PartyRock app around it.** Free, no-code, editable; students can be building within a
   class period.
3. **Compare, then break it.** Have students test two or three prompt variants, evaluate the output
   against ground truth, and try to make the app fail.
