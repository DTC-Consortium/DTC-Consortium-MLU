# Post-Seminar Labs — Monday Morning and Beyond

You walked out of the seminar with one working AI teaching assistant. This document is a menu of what to try next.

## How to use this guide

- **Pick one.** Don't try to do them all. Start with whatever fits the time you have today.
- **Do it solo or with a colleague.** The seminar Slack channel is where the help lives — ask there when stuck.
- **Time estimates assume you're starting from your finished Lab 2 notebook.** If you skipped the seminar Lab 2, do that first.
- **Skill labels:**
  - 🟢 Easy — edit a prompt or swap a value, run it, see what changes
  - 🟡 Medium — add a few cells, modify the data flow
  - 🔴 Hard — significant restructuring, adapting patterns from elsewhere

---

## Tier 1 — Quick Wins (under 30 min)

Run today before you close the laptop. Build confidence, see what's possible without leaving the comfort of the seminar notebook.

### 1. Customize the prompt templates for your discipline 🟢
*~15 min · learn: prompt iteration*
The seminar's quiz/study-guide/rubric prompts are generic. Edit them to match the testing style, rubric criteria, or voice your department actually uses. Run, evaluate, iterate.

### 2. Swap in your real syllabus or lecture notes 🟢
*~10 min · learn: how grounding changes with the source*
Change `pdf_path` to a real document from your actual course. Re-run Part 3. Compare the outputs — what does the AI miss vs. what does it nail?

### 3. Compare different models 🟢
*~15 min · learn: model choice matters*
Try swapping `nova_lite` for `nova_pro` or other available models in your AWS account. Same prompts, different voices. Note which model handles your discipline better.

### 4. Stress-test the grounding 🟡
*~25 min · learn: when RAG fails*
Ask the document a question whose answer ISN'T in the document. Watch how the AI handles it. Then ask one whose answer is buried deep. This builds your intuition for when to trust grounded output.

---

## Tier 2 — Build on What You Made (30–90 min)

Take your Lab 2 notebook and extend it. These add real capabilities your seminar version doesn't have.

### 5. Multi-document tutor 🟡
*~60 min · learn: vector store basics, multi-source RAG*
Load your full syllabus PLUS 2–3 textbook chapters into one vector store. Now your AI tutor knows your whole course, not just one document. Watch how cross-document questions get answered.

### 6. Conversation memory 🟡
*~45 min · learn: chat history, state management*
The seminar version answers one question at a time and forgets. Adapt the patterns from `aws-mlu-eep-generative-ai/Module 3 Lab 2 (Chatbots)` to let the AI hold a back-and-forth conversation that remembers earlier turns.

### 7. Always-cite-your-sources mode 🟡
*~30 min · learn: prompt engineering for verifiability*
Modify the QA template so every answer includes specific page numbers from the source. Helpful when faculty need traceability for accreditation or when students question an answer.

### 8. Student-facing safety guardrails 🔴
*~90 min · learn: responsible AI patterns*
Adapt patterns from `Module 2 Lab 4 (Debiasing / Watermarking)` to add safety checks before answers go to students. Block off-topic questions. Refuse to "answer for the student" on assignments. Detect attempts to get the AI to write essays.

---

## Tier 3 — Try Something New (1–2 hours)

These introduce capabilities not covered in the seminar. Most adapt a specific lab from the upstream MLU curriculum.

### 9. Multi-modal lesson companion 🔴
*~2 hr · learn: image inputs · adapts M3 Lab 5*
Add image upload so the AI can analyze clinical photos (dentistry), biology slides, art reproductions, or architectural drawings. Built on Amazon Nova's multimodal capabilities. Especially powerful for visual disciplines.

### 10. Agentic assistant 🔴
*~2 hr · learn: tool use · adapts M3 Lab 4*
Give the AI the ability to take actions — search the web, calculate something, look up a date. Move beyond Q&A into actual task completion. Powerful but more complex; expect debugging.

### 11. Conversational tutor with role-play 🟡
*~90 min · learn: persona prompting + chat*
For business/case-method disciplines: have the AI role-play as a stakeholder (CFO, patient, customer) and let students practice difficult conversations grounded in the case material.

### 12. Discipline-specific evaluator 🟡
*~75 min · learn: rubric application + structured output*
Feed the AI a sample student response and have it apply your rubric. Not for actual grading — for self-check during course design ("does my rubric produce consistent judgments?").

---

## Tier 4 — Pedagogical / Curriculum Design (no code required)

Sometimes the highest-value next step isn't more code.

### 13. AI-augmented syllabus audit 🟢
*~30 min · learn: using AI for course design*
Use your tool to find gaps in your existing course material: ask it "what topics aren't well-covered here?" or "what assumptions does this material make about student background?" Use the answers to drive curriculum revision conversations.

### 14. Assessment redesign sprint 🟡
*~90 min · learn: AI-resistant assessment*
Use your tool to identify which assignments in your course are most vulnerable to student AI use. Redesign one assignment to either require AI use (transparently) or be genuinely AI-resistant (process-focused, in-class, oral).

### 15. Cross-discipline collaboration 🟡
*~60 min · learn: how patterns transfer between fields*
Pair with a faculty member in a different discipline. Walk through each other's notebooks. Identify which patterns transfer and which are field-specific. Often the most generative post-seminar activity.

---

## Tier 5 — When You Don't Have Ongoing AWS Access

The seminar AWS accounts may have a time limit. These options let you keep going without one.

### 16. SageMaker Studio Lab variant 🔴
*~3 hr to port · ongoing free*
Studio Lab (studiolab.sagemaker.aws) is free, requires only email signup, but has NO Bedrock access. Porting requires replacing Bedrock calls with Hugging Face Inference API or local Sentence Transformers. Significant refactoring; results won't be identical.

### 17. Local laptop with Ollama 🔴
*~2 hr to set up · ongoing free*
Run a smaller open-source model (Llama 3, Mistral 7B) on your laptop via Ollama. Embeddings via Sentence Transformers. Slower, smaller model, but fully under your control and no ongoing cost. Good for sensitive course material you don't want in cloud APIs.

---

## Where to go deeper

The full MLU EEP Generative AI curriculum is at [aws-samples/aws-mlu-eep-generative-ai](https://github.com/aws-samples/aws-mlu-eep-generative-ai). It contains 14 lessons and 13 labs across:

- **Module 1** — Foundation models, prompting (covered in seminar)
- **Module 2** — Responsible AI, evaluation, security (surveyed at 3:15)
- **Module 3** — Apps with foundation models: LangChain, RAG, chatbots, agents, multimodal (we did RAG)

Specific labs worth knowing about:
- **M3 Lab 2 — Chatbots** — direct path for Tier 2 #6
- **M3 Lab 4 — Agents** — direct path for Tier 3 #10
- **M3 Lab 5 — Multimodal** — direct path for Tier 3 #9
- **M2 Lab 4 — Debiasing & Watermarking** — direct path for Tier 2 #8

---

## How to choose

| If you... | Start with |
|---|---|
| Have 30 min and want a quick win | Tier 1, any |
| Have a real syllabus you want to teach with AI | #2 → #5 |
| Are worried about students misusing AI | #8 → #14 |
| Teach a visual discipline | #9 |
| Teach a case-method discipline | #11 |
| Want to redesign your course | #13 → #14 → #15 |
| Won't have AWS after the seminar | #16 or #17 |
| Want to take it furthest | #5 → #6 → #9 → #10 (full custom tutor) |

---

## What this guide is NOT

- Not a step-by-step implementation manual — pick a lab, then either work from the upstream MLU curriculum links or ask in Slack
- Not promises that every lab works without modification — your AWS account and the source documents shape what's possible
- Not an exhaustive list — these are the seven or eight most useful directions; there are dozens more

The point is: you have a working AI tutor. The next step is making it actually useful for your students. Pick one path and start.
