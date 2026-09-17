# Bridge + Lab-Guide Deck Spec (1:15–3:00 PM)

**Purpose:** Slide-by-slide build spec for the 14 slides covering the bridge segment (1:15–1:30) and the curriculum-embedding lab (1:30–3:00). A designer should be able to produce the `.pptx`/Keynote/Slides file in ~3–4 hours from this document.

**Total slides:** 14 (5 bridge + 9 lab-guide)
**Total time:** 105 minutes
**Audience:** Multidisciplinary faculty, mostly non-CS (see persona table in `SEMINAR_PLAN.md`)

**Design principle:** Every slide must earn its keep for the *least technical attendee in the room*. If a slide doesn't help Persona 6 (Dr. Lena Hoffmann, low AI comfort) think, learn, or commit — cut it.

---

## Style and build guidelines

- **Template:** Match the AWS MLU template used by source decks in `aws-mlu-eep-generative-ai/` so the look is continuous across the seminar day
- **Typography:** Same as source decks (the deck must feel like the morning didn't end and a new presentation started)
- **Color palette:** AWS purple/blue family
- **Footer:** Include time-remaining countdown on slides L4, L6, L7, L8 (the reflection-heavy slides — countdown prevents overrun without instructor announcements)
- **Slide numbers:** Visible bottom-right — speaker uses them as anchors for "we're on slide 7 of 14"
- **No code on slides.** Even on lab-guide slides. Code lives in the notebook; slides describe what's happening.

---

# Block 1 — Bridge (1:15–1:30, 5 slides, 15 min)

## B1 — What you just built (2 min)

| Field | Content |
|---|---|
| **Slide title** | What you just built |
| **Source** | Custom |
| **Time on slide** | 2 min |
| **Visual** | Screenshot of a PartyRock app from the morning (instructor's demo app works fine). Faded background. Single line of bold text at the bottom: *"You're already farther than 80% of faculty get all year."* |
| **Key text on slide** | Bottom-left, smaller: *"From: I built an app. To: I will use this Tuesday in my course."* |
| **Speaker notes** | "Welcome back. By lunch you all had a working PartyRock app. That's a real accomplishment — most faculty never get to do what you just did. Now we shift from 'I built an app' to 'I will use this Tuesday in my course.' The next 90 minutes are about making that shift concrete. Specific course. Specific week. Specific assignment." |

---

## B2 — AI is showing up everywhere (3 min)

| Field | Content |
|---|---|
| **Slide title** | AI is showing up everywhere — including your classroom |
| **Source** | **LIFT M1 L1 slide 9 verbatim** (the 6-icon mosaic: Healthcare, Education, Finance, Law, Marketing, Customer Service, with FMs in the center) |
| **Time on slide** | 3 min |
| **Visual** | Already perfect in source — keep as-is |
| **Modification** | Add a callout arrow pointing at the "Education" icon: *"You are here."* |
| **Speaker notes** | "AI is everywhere right now — healthcare, finance, law, customer service, marketing. Pick any industry; someone has built an AI tool for it. Education is the icon in the top middle. That's the one we're focused on today. The question isn't whether AI will be in your classroom — it already is, in students' phones, in administrative tools, in the back-office of every system you touch. The question is whether YOU shape how it shows up in your course, or whether it shows up without you." |

---

## B3 — From guessing to grounding (5 min)

| Field | Content |
|---|---|
| **Slide title** | From guessing to grounding |
| **Source** | **Synthesize M3 L3 slide 4 (chatbot+documents visual) with M3 L3 slide 14 (R-A-G three steps)** into one slide |
| **Time on slide** | 5 min |
| **Visual** | Left half: the chatbot+documents diagram from M3 L3 #4 (User → Memory/Prompt → AI brain → Response, with Documents flowing into Prompt). Question mark over the AI brain. Right half: large text "R-A-G" with the three steps stacked: **R**etrieve → **A**ugment → **G**enerate |
| **Key text on slide** | Below the diagram: *"PartyRock guesses. The afternoon lab grounds."* |
| **Speaker notes** | "PartyRock is wonderful for building fast. But under the hood it's still asking the AI to answer from general training — *guessing*, basically — with your document in the context as a hint. That works for most things. But for your discipline's content, you need something stronger: grounding. The afternoon's lab does something called RAG — Retrieval-Augmented Generation. Three steps: **Retrieve** the right piece of your document; **Augment** the prompt with it; **Generate** the answer from THAT, not from general training. The result: answers traceable to your source. No hallucinations. This is the technical reason the lab feels different from PartyRock. You don't need to understand the math. You just need to know: grounded > guessing for teaching tools." |
| **What we deliberately don't say** | Embeddings, vectors, FAISS, chunking, similarity scores. None of this matters at the bridge. Keep RAG at the verb level — *"give the model the textbook before asking the question."* |

---

## B4 — AWS Bedrock: the engine room (3 min)

| Field | Content |
|---|---|
| **Slide title** | AWS Bedrock: the engine room |
| **Source** | **LIFT M1 L1 slide 16** (the provider grid showing Amazon Titan, AI21Labs Jurassic-2, Anthropic Claude, Cohere Command, Meta Llama). Update model names if AWS has refreshed the deck. |
| **Time on slide** | 3 min |
| **Visual** | Provider grid as-is, with an Amazon Bedrock logo prominently at the top |
| **Key text on slide** | One line: *"All of these models. One AWS service. That's what makes today possible."* |
| **Speaker notes** | "Quick acknowledgment: today's seminar runs on AWS Bedrock. Bedrock is the AWS service that makes foundation models available — Amazon's own Titan and Nova, Anthropic's Claude, Meta's Llama, Mistral, Cohere, others. The reason we can have you all simultaneously running AI tools without anyone setting up complex infrastructure is that AWS handles the model hosting. This morning in PartyRock, you were using Bedrock. This afternoon's lab also uses Bedrock — same engine, different interface. If you take one piece of AWS terminology home, let it be 'Bedrock.' It's how AI gets into AWS-hosted educational tools." |
| **What we deliberately don't say** | LangChain. Embeddings APIs. IAM. Inference parameters. Anything else that's developer-facing. The slide names Bedrock once; that's the sponsor moment. |

---

## B5 — This afternoon: build, place, commit (2 min)

| Field | Content |
|---|---|
| **Slide title** | This afternoon: build, place, commit |
| **Source** | Custom |
| **Time on slide** | 2 min |
| **Visual** | Three columns, equal width: **BUILD** (gear icon) | **PLACE** (map-pin icon) | **COMMIT** (calendar icon). Under each, one line: |
| **Key text on slide** | BUILD — *Your persona's actual envisioned tool, running on your discipline's content (~30 min)* · PLACE — *Where in YOUR course this fits: specific course, week, assignment (~20 min)* · COMMIT — *One sentence Monday morning action, emailed to yourself (~10 min)* |
| **Speaker notes** | "Three things in the next 90 minutes. Build — you'll run YOUR persona's actual envisioned tool. Maya's case-study coach. Sarah's primary-source companion. Lena's pre-lab knowledge gate. Whichever you picked at registration, you build that one. Not a generic quiz generator — your tool. Place — once you've seen what it produces, you write down exactly where in your course this goes. Specific course code. Specific week. Specific assignment. Vagueness here means you won't use it Monday. Commit — at the end, one sentence: 'On this date, in this class, I will do this.' You email it to yourself. That's the take-home. Open your notebook now — let's begin." |

---

# Block 2 — Lab guides (1:30–3:00, 9 slides, 90 min)

These slides stay projected throughout the lab. Faculty mostly look at their own notebook screens; the projected slide is the anchor for *"where are we, what's happening, how much time is left."*

---

## L1 — Find your persona (5 min, 1:30–1:35)

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Part 0 — Find your persona |
| **Source** | Custom (data from `SEMINAR_PLAN.md` persona table) |
| **Time on slide** | 5 min |
| **Visual** | 6-row table: # | Persona | Field | Tool you build. Each row colored differently. Persona avatars (generic, not photos) on the left. |
| **Key text on slide** | Top: *"Open your notebook. In the second code cell, set:" `persona = "X"`*. Bottom: *"Pick the row closest to what you teach. When in doubt, pick the one you'll teach next semester."* |
| **Footer countdown** | 5:00 → 0:00 |
| **Speaker notes** | "Open the notebook in SageMaker Studio. The second code cell asks for a persona number 1 through 6. Find your row. Change the variable. Press Shift+Enter to set it. Take a minute now. If you're between two personas, pick the one for the course you'll teach next semester — the discipline matters less than the urgency. I'll walk around — flag me if you're stuck. Five minutes." |

---

## L2 — Setup — watch the instructor (10 min, 1:35–1:45)

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Part 1 — Setup |
| **Source** | Custom |
| **Time on slide** | 10 min |
| **Visual** | Single big graphic: an open laptop with hands visible (faded), big red prohibition sign over hands, with text "WATCH — DON'T CLICK". Below: three bullets with simple icons |
| **Key text on slide** | • Install dependencies *(borrowing tools)* · Connect to AWS Bedrock *(one handshake)* · Load the six tool definitions *(your persona's recipe)* |
| **Footer countdown** | 10:00 → 0:00 |
| **Speaker notes** | "For this part — watch me. Don't click anything on your screen. I'm running three cells: install tools, connect to AWS, load the six tool definitions. While each one runs, I'll tell you what it's doing. Don't worry about reading the code — it's like seeing a recipe in another language; you don't need to understand it to eat the meal. Ten minutes." |

---

## L3 — Build YOUR persona's tool — demo first (5 min, 1:45–1:50)

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Part 2 — Build your tool |
| **Source** | Custom |
| **Time on slide** | 5 min |
| **Visual** | Three boxes, left-to-right with arrows: **Load** *(PDF icon)* → **Index** *(database icon)* → **Run** *(play button icon)*. Above the boxes: *"Three cells. ~30 seconds each."* |
| **Key text on slide** | Below boxes: *"Watch me run this on the Dentistry sample first. Your turn next."* |
| **Speaker notes** | "I'm going to demo this with Persona 1 — Dentistry. Three cells: load the sample document, build a search index over it, run YOUR persona's tool. About a minute total. Watch the output. This is what Maya walks out with — three patient case vignettes pulled from a real periodontal article, at three difficulty levels. Tomorrow's Periodontics class just got a major upgrade. **Pause here, read it out loud.** Now your turn." |

---

## L4 — Now your turn (20 min, 1:50–2:10)

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Part 2 — Your turn |
| **Source** | Custom |
| **Time on slide** | 20 min |
| **Visual** | Large, simple checklist: ☐ Run cell 2.1 (load) · ☐ Run cell 2.2 (index — takes ~1 min) · ☐ Run cell 2.3 (your tool!) |
| **Key text on slide** | Below checklist: *"What you see should be recognizably useful for your course. If not — we'll fix the prompt in a moment."* |
| **Footer countdown** | 20:00 → 0:00 |
| **Speaker notes** | "Your turn. Three cells. Cell 2.2 takes about a minute — that's the embedding step. While it runs, sit with the anticipation. Then cell 2.3 produces your persona's tool output. If you're stuck, raise your hand — TAs are in the room. If your output doesn't quite work for your course, that's fine — we have a 'customize the prompt' cell next. Twenty minutes." |

---

## L5 — Pause and read what your AI made (5 min, 2:10–2:15)

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Part 2 — Stop and notice |
| **Source** | Custom |
| **Time on slide** | 5 min |
| **Visual** | Single line, large: *"Stop. Read what your AI just produced."* Below, four small questions in a 2x2 grid: |
| **Key text on slide** | • Would I actually USE this in my course? In what form? · What would I edit before handing it to students? · What's missing? · What's there that I'd remove? |
| **Speaker notes** | "Stop. Read what your AI produced. Don't worry about answering the questions on screen out loud — just notice. This is the most important pause in the entire afternoon. The next sections capture your noticing in writing. Five minutes. Then we move to placement." |

---

## L6 — Where in YOUR course does this go? (20 min, 2:15–2:35) ⭐ heart of the lab

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Part 3 — Where does this go? |
| **Source** | Custom |
| **Time on slide** | 20 min |
| **Visual** | A worked example projected as a screenshot of the instructor's own filled-in cells (Persona 1 Dentistry). Big heading: *"Specifics or it doesn't happen."* |
| **Key text on slide** | Below the example: 4 prompts: ① Which course, week, assignment? ② What does AI do, what do YOU still do? ③ Who sees output, how often? ④ What concerns you — and how will you mitigate? |
| **Footer countdown** | 20:00 → 0:00 |
| **Speaker notes** | "Generating the cool output was the easy part. The hard part — and the part that determines whether you actually use this Monday — is knowing exactly where in your course it goes. Four cells in the notebook. Fill them with specifics. Not 'someday in my intro class.' Specific course code, specific week, specific assignment. Look at my example here — DDS 4220 Periodontics II, Week 5, pre-class case study warmup, AI generates 3 vignettes, I still pick which one to use and lead the discussion. Be that specific. I'll be walking the room. If you have a bracket placeholder still in your cell at 2:30, expect me to push you to specifics. Twenty minutes." |

---

## L7 — Where AI does NOT belong (10 min, 2:35–2:45) ⭐ skeptic conversion

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Part 4 — Where AI does NOT belong |
| **Source** | Custom |
| **Time on slide** | 10 min |
| **Visual** | Single bold quote-style line: *"Faculty who articulate the boundary are more credible than faculty who say AI is good for everything."* Below: three prompts |
| **Key text on slide** | ① What part of teaching this course you will NOT delegate to AI · ② An assignment you PROTECT from AI (where the struggle matters) · ③ Your one-sentence student AI policy |
| **Footer countdown** | 10:00 → 0:00 |
| **Speaker notes** | "Equally important. Maybe more important. Where in your course is YOU and only YOU? Where would using AI actually harm what you're trying to teach? Three cells. Be honest. If you have no boundary, you probably haven't thought hard enough. This is the section that turns skeptics into thoughtful AI users — when you can articulate your line, you become more credible to yourself and your students. Eight minutes for the writing, two minutes for me to nudge anyone with vague answers." |

---

## L8 — From notebook to your classroom (10 min, 2:45–2:55)

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Parts 5 + 6 — From notebook to your classroom |
| **Source** | Custom |
| **Time on slide** | 10 min |
| **Visual** | Top half: small LMS logos (Canvas, Blackboard, Moodle, Brightspace) with arrows pointing to a generic "your students" icon. Bottom half: a calendar with a date circled and the words *"Email it to yourself"* |
| **Key text on slide** | Top: *"5 min cleanup per artifact. Copy, paste, fix formatting."* Bottom: *"One sentence: On [date], in [class], I will [action]."* |
| **Footer countdown** | 10:00 → 0:00 |
| **Speaker notes** | "Two things in this section, both quick. First — getting the output from the notebook into your LMS. The notebook has step-by-step instructions for Canvas, Blackboard, Moodle. The short version: copy the output, paste into the rich text editor, fix the formatting. Plan five minutes of cleanup per artifact. That's a fraction of what it took to write quizzes from scratch. Second — your Monday commitment. One sentence in the notebook. Run the export cell. Get the artifact file. Then watch me — I'm going to open my email and send it to myself right now on the projector. You do the same. The email is the commitment device. Subject: 'Monday morning AI commitment.' Send. Done. You just made it 3x more likely you'll actually do this." |

---

## L9 — Find someone different (5 min, 2:55–3:00)

| Field | Content |
|---|---|
| **Slide title** | Lab 2 · Part 7 — Find someone different |
| **Source** | Custom |
| **Time on slide** | 5 min |
| **Visual** | Two cartoon figures of different shapes (one with a stethoscope, one with a book) shaking hands. Above: *"Find someone from a different discipline."* |
| **Key text on slide** | Below the figures, in big quote marks: *"What's one thing about how I'm using AI that you would NOT do in your discipline — and why?"* |
| **Speaker notes** | "Find someone from a different discipline than yours. Not the person sitting next to you if they're in your field. Show them: your tool's output, your Monday commitment, your protected assignment. Then ask them the question on the screen: 'What's one thing about how I'm using AI that you would NOT do in your discipline — and why?' That question is more useful than any positive feedback. The cross-discipline disagreement is where the real learning is. Three minutes for the exchange. Then one volunteer shares what they heard — not what they said. Two minutes. Then break." |

---

# Build checklist for the designer

- [ ] Acquire AWS MLU PowerPoint template (from source `aws-mlu-eep-generative-ai/.../Lessons/*/*.pptx` files)
- [ ] Lift slide content from M1 L1 #9 (verbatim) and M1 L1 #16 (verbatim) and M3 L3 #4 + #14 (synthesize into one)
- [ ] Build 9 custom slides per specs above
- [ ] Add countdown footer to L4, L6, L7, L8 (PowerPoint has free countdown plugins; Keynote has Magic Move tricks)
- [ ] Add slide numbers (X of 14) to all slides
- [ ] Set up presenter notes with speaker text from above
- [ ] Print the speaker notes as a 1-page bridge cheat sheet for the instructor
- [ ] Dry-run with a timer; flag any slide that goes over its allocation

---

# Timing risk table

| Slide | Allocated | Realistic risk | Mitigation |
|---|---|---|---|
| B3 (RAG) | 5 min | Could balloon to 7 min if instructor over-explains | Speaker notes are tight — read them; don't ad-lib |
| L4 (Your turn) | 20 min | Embedding cell can hang if PDF too large | Pre-flight checks PDFs; have working sample as fallback |
| L6 (Where does this go) | 20 min | Vague answers prolong feedback loops | Instructor walks room; pushes for specifics |
| L7 (Where AI doesn't belong) | 10 min | Skeptics may want more time | If running ahead, give them 12; if behind, cut to 8 |
| L8 (LMS + commitment) | 10 min | LMS demo can derail | DON'T live-demo LMS; just project the notebook's instructions |
| L9 (Pod share) | 5 min | Faculty pair with same discipline | Instructor intervenes; "find someone different" is the rule |

If running over by 5+ min by L8, cut L9 to 3 minutes. **Never cut L6 or L7** — those are the lab.

---

# Companion docs

- `SEMINAR_PLAN.md` — overall agenda this slot fits into
- `INSTRUCTOR_CHEATSHEET.md` — facilitation script for Lab 2 (lines up with these slides)
- `CONTENT_AUDIT.md` — explains why LangChain is excluded and why grounding is the core concept
- `../curriculum-embedding-lab.ipynb` — the notebook these slides accompany
