# Content Audit — Discipline Assistant Seminar (`mlu-000002`)

*Is this digestible for non-CS faculty?*

**Purpose:** Honest evaluation of seminar materials through the eyes of non-CS faculty. Documents what works, what loses people, and three paths forward.

**Date of audit:** 2026-05-30
**Auditor:** Reviewed M1 L1 (all 23 slides) + M1 L3 (slides 1–14 of 27) + the Lab 2 notebook we built. **Not yet audited:** M2 L3, M3 L3/L4/L5 surveys for the afternoon, second half of M1 L3.

**When to revisit:** Before locking the final agenda. Before any instructor commits to delivering the morning lectures as-written.

---

## TL;DR

> **The MLU lecture decks are NOT seminar-ready for non-CS faculty as-is.** They were built for technical learners exploring Amazon Bedrock — not for the dentistry/humanities/nursing audience we're targeting. The good news: the *content we need* is in there. The bad news: we have to cut hard and re-frame.
>
> Estimated room engagement on the current plan: roughly **C+/B-** across the 6 personas. We will probably lose 2–3 of the 6 personas before lunch if we run the lectures as-is.

---

## Module 1, Lesson 1 — Introduction to Generative AI (23 slides)

### What works ✅
- **Slide 9 (Revolutionizing various domains):** Healthcare/Education/Finance/Law/Marketing icons. Faculty see themselves.
- **Slides 10–14 (Use cases):** Chatbots, interactive training, creative assistants, productivity tools, data analytics. Real faculty workflow language: "draft, summarize, auto-complete emails," "create slides, exercises, quizzes."

### Where you lose people ⚠️

| Slide | What happens | Who tunes out |
|---|---|---|
| 2 | Opens with a Goodfellow quote labeled *"Computer Scientist"* — frames the day as CS in the first 30 seconds | Persona 3 (English skeptic) already on guard |
| 5 | *"ML models, pre-trained with vast amounts of data"* — undefined acronyms | Persona 6 (Biology, low AI comfort) — *"what's ML?"* |
| 6 | *"Training task: predict the missing word"* — technically clever weather fill-in-blank, but framed as ML internals | Most non-CS faculty glaze |
| 7 | *"How big? 700 GB, $100 million, 80B lines of code"* — impressive trivia, useless to a teacher | Universal "so what?" |
| 15–21 | **Seven straight slides of Amazon Bedrock product pitch** — Titan models, Titan Embeddings, IAM/compliance | Persona 4 (Nursing) confused; Persona 3 actively annoyed; Persona 6 lost |

**Verdict:** Roughly **9 of 23 slides serve our audience**. The middle (Bedrock product pitch) reads like a sales deck that wandered into a teaching workshop.

---

## Module 1, Lesson 3 — Prompt Engineering (27 slides, audited 1–14)

### What works ✅ — much better than L1
- **Slides 4–6 (What are prompts / Components):** Customer email example with color-coded Input/Instruction/Context/Output boxes. **The single best slide in either deck for our audience.** Universally accessible.
- **Slide 7:** Names the core fear (hallucinations) and the core skill (iteration).
- **Slide 12 (Good prompting practices):** Clear, specific, iterative — directly actionable.

### Where it falls apart ⚠️
- **Slides 8–10 (Inference parameters):** Temperature, Top p, Top k, max tokens, stop sequences. **API configuration vocabulary that faculty will never touch in PartyRock and don't need.** Even Lab 2 sets these once and hides them.
- **Slides 13–14 (Model-specific prompts):** Shows `<|prefix_begin|>`, `<|endoftext|>`, `<|assistant|>` token formats. **Developer-level.** Persona 6 closes her laptop here.

**Verdict:** First 7 slides are gold. Slides 8–14 are for someone building applications, not someone using PartyRock.

---

## Lab 2 notebook — re-evaluated through non-CS eyes

| What works ✅ | What's still risky ⚠️ |
|---|---|
| Plain-English markdown framing every cell | Cell 1.2: wall of `from langchain_x import ...` lines — visually intimidating even when told "watch only" |
| 🟢 EDIT ME markers — only 3 cells to touch | Cell 3.4: 30+ line `NovaMultimodalEmbeddings` class definition — non-CS panic moment |
| "Watch the instructor for this part" framing | Variable names: `bedrock_runtime`, `vectordb`, `retriever`, `ChatBedrockConverse` — jargon, never defined |
| Grounded-vs-vanilla 3.7 cell — the killer demo | The fact that it's a notebook at all — non-coders haven't seen one |
| Persona-matched PDF defaults | First impression on opening is intimidating before any narration starts |

**This will work IF** the instructor narrates well during Part 1 and never pauses on the scary cells. It will fail badly without that narration.

---

## Persona-by-persona honest grade

| Persona | M1 L1 deck | M1 L3 deck | PartyRock | Lab 2 |
|---|---|---|---|---|
| 1. Maya (Dentistry, cautious) | C+ | B | A | B+ *(with instructor support)* |
| 2. James (CS, high comfort) | C *(too basic + boring)* | B+ | B *(might find it too basic)* | A |
| 3. Sarah (English, skeptic) | **D** *(loses her at slide 5)* | B early, **F** later | A | C+ *(notebook intimidates)* |
| 4. Diane (Nursing, moderate) | C *(survives, bored)* | B | A | B |
| 5. Marcus (Business, enthusiast) | B *(connects)* | B | A | A |
| 6. Lena (Biology, low comfort) | **D** *(loses her at slide 5)* | B early, **F** later | B+ | C *(needs hand-holding)* |

**Average across the room: C+/B-.** The morning lecture content is the weakest link.

---

## Three paths forward

### Path A — Use MLU decks as-is, take the hit
Run them at speed (~2 min/slide), apologize to non-CS folks, count on PartyRock and Lab 2 to recover them.
**Risk:** lose 2–3 of the 6 personas before lunch.
**Effort:** zero.

### Path B — Cherry-pick from MLU + add custom framing slides
- Take 7–8 *good* slides from L1 (use cases, domain icons, what FMs are conceptually) — skip Bedrock product pitch
- Take 7 *good* slides from L3 (what prompts are, components, best practices)
- Add 3–5 custom faculty-framing slides up front (*"Why this matters for your course"* — not *"How LLMs work"*)
- Replace technical examples with academic ones throughout
**Effort:** ~4 hours of slide editing per deck.

### Path C — Rewrite the morning as a 1-hour "demo + frame" session
Skip the formal lecture entirely. Open PartyRock in front of the room. Demo three things relevant to the audience (write a quiz from a syllabus, summarize a research paper, draft a rubric). Use those demos to explain prompts, hallucinations, and grounding **as concepts emerge** from what people see. No slides. Just doing.
**Effort:** ~6 hours of demo design + dry runs.

---

## Recommended path: Hybrid B + C

**Mornings should feel like a workshop, not a presentation.** Specifically:

1. **9:15–9:45 (was 9:15–10:00):** 30-min faculty-framed talk with **~12 cherry-picked slides** from L1 + custom intro slides. End with one live PartyRock demo.
2. **10:00–10:30 (was 10:15–11:00):** 30-min prompt engineering talk with **~10 slides** from L3 (skip inference parameters and model-specific tokens). End with a "now you try" pause where everyone opens PartyRock and writes one prompt.
3. **Reclaim 30 minutes** for PartyRock onboarding (account creation, first app) before lunch — currently the 11:00–12:30 lab block eats this.

For Lab 2:
- **Add an instructor walkthrough script** for cell 1.2 and cell 3.4 specifically — narrate them out loud so non-coders don't fixate on the wall of text. (*"This is just setting tools out on the workbench, like opening drawers in a kitchen. You don't need to read it."*)
- **Consider refactoring cell 3.4** — import the embedding class from a separate helper file. The class definition is visually scary and adds nothing to comprehension.
- **Consider collapsing scary cells** by default using Jupyter cell metadata.

---

## Concrete next steps (if we commit to hybrid B + C)

1. **Slide manifest** — produce a markdown file listing exactly which slides to keep from each MLU deck (L1, L3, M2 L3, M3 L3/L4/L5 surveys). An instructor can build the day's deck from it in ~30 min.
2. **Custom intro slides** — write 3–5 academic-framing slides for the morning ("Why this matters for your course"). Replace the lost MLU slides.
3. **Lab 2 notebook refactor** — move the embeddings class into `mlu_utils/embeddings.py` (or similar). Replace cell 3.4 with a one-line import. Same functionality, far less visual weight.
4. **Instructor narration scripts** — write a 30-second script for each potentially-scary cell. Add to `INSTRUCTOR_CHEATSHEET.md`.
5. **Audit the afternoon decks** — M2 L3, M3 L3/L4/L5. Likely similar pattern (good slides buried under technical ones). Plan 1–2 hours for this audit.

---

## What we have NOT yet evaluated

- **M2 Lesson 3 — Dimensions of Responsible AI** (34 slides) — the primary deck for the afternoon survey
- **M3 Lessons 3/4/5** (43 + 28 + 29 slides = 100 slides) — afternoon "what's next" survey content
- **Second half of M1 L3** (slides 15–27) — likely contains advanced prompting (CoT, few-shot, etc.) which could be useful but may be too deep
- **PartyRock workshop PDF (Bootcamp Prep Part 1)** — looked at structurally but not audited for jargon/accessibility
- **The actual delivered tone** of any lecture — we audited slide text only; an experienced instructor can rescue a weak slide with the right framing

---

## Key principle to revisit

> **Faculty don't need a "lesson" — they need to see AI doing something useful in their field and then learn the why as they need it.**

The MLU decks invert this. They teach the why first (foundation models, LLMs, inference parameters) and then offer use cases at the end. For our audience, this is backwards. Lead with the demo. The concepts will land when the audience is curious about them, not before.

---

## Companion docs

- `SEMINAR_PLAN.md` — the locked plan this audit critiques
- `INSTRUCTOR_CHEATSHEET.md` — where the narration scripts would land
- `../discipline-assistant.ipynb` — the Lab 2 notebook this audit re-evaluates
- `../POST_SEMINAR_LABS.md` — already accessible / faculty-framed; can serve as a tone reference
