# Discipline Assistant Seminar (`mlu-000002`) — Pre-Flight Checklist

**For:** The instructor team setting up this lab before delivery.
**Companion docs:** `INSTRUCTOR_CHEATSHEET.md` (run-of-show), `SEMINAR_PLAN.md` (background — note it is the superseded v1 day-plan).

> **A note on numbering.** "Lab 2" throughout this document means *the seminar's second lab* — the
> afternoon slot, after a morning no-code session. That it also happens to be **lab 2 of 4** in the
> published teaching sequence is a coincidence.
>
> Watch out for this: [`mlu-000001`](../../../mlu-000001-curriculum-embedding-lab) **also** calls
> itself "Lab 2" in its own facilitator docs, because it took over that same afternoon slot. Two
> documents, same label, different labs. Go by the contribution ID, not the lab number.

---

## ⚠️ First: which path are you running?

The two paths have **completely different preparation**. Read the right one and skip the other.

| | **Colab + Hugging Face** | **SageMaker + Bedrock** |
|---|---|---|
| Notebook | `discipline-assistant-colab.ipynb` | `discipline-assistant.ipynb` |
| AWS account needed | **No** | Yes, one per attendee |
| Lead time | **Same day** | **~1 week** for account and model-access provisioning |
| Cost | **None** — free tiers | Under USD 1 per attendee |
| Prep below | **[Colab path](#colab-path--the-short-version)** only | Everything from *2 weeks before* onward |
| Best when | Most faculty. They keep a working copy after they lose seminar cloud access. | Attendees already have durable SageMaker access |

**If you are not sure, run the Colab path.** It is the one the participant README recommends, it
needs no provisioning, and the notebook is self-contained.

---

## Colab path — the short version

Everything below this section is SageMaker-specific and does not apply.

**Up to a week before**
- [ ] Confirm attendees can reach `colab.research.google.com` and `huggingface.co` on the venue
      network. Some campus networks block one or both — check from the actual room if you can.
- [ ] Registration email asks each attendee to bring a **Google account** and to create a **free
      Hugging Face account** in advance.

**Day before**
- [ ] Send the Colab link (the badge in the activity README opens the notebook directly).
- [ ] Send the one-page instruction for generating a Hugging Face **read** token. Doing this live
      costs 10 minutes of room time; doing it in advance costs none.
- [ ] Run the notebook yourself end to end, on the token you will demo with.

**Morning of**
- [ ] Open the notebook in your own browser and run it once — Colab sometimes needs a fresh
      runtime, and you want that discovered before the room is watching.
- [ ] Have a spare Hugging Face token ready in case yours rate-limits mid-demo.
- [ ] Know the fallback: the free inference tier can throttle under a roomful of simultaneous
      requests. If that happens, switch to demonstrating from your own screen and have participants
      follow along, then let them run it themselves afterwards.

**Known limits of this path**
- A few minutes slower per run than Bedrock. Build that into your timings.
- Colab runtimes disconnect when idle. If you break for more than ~20 minutes, expect a re-run.

---

## SageMaker path — everything below

## Timeline

| When | What | Owner |
|---|---|---|
| **1 week before** | AWS accounts + Bedrock model access provisioned | — |
| **3 days before** | Full dry run on a real attendee account | — |
| **Day before** | Notebook and data distributed to all accounts | — |
| **Morning of** | Kernels pre-warmed, share-out channel live | — |

Assign an owner for each row before scheduling.

---

## 2 weeks before — content prep

### Sample PDFs — already done, verify only

**All six sample PDFs ship with this contribution**, in
`../activities/discipline-assistant/data/`, licence-checked, with per-file source and page count in
that folder's `README.md`. There is no sourcing work.

- [ ] Confirm the six PDFs are present after download or clone
- [ ] Spot-check one end to end: loads in `PyPDFLoader`, embeds, and the grounded-vs-vanilla
      comparison shows a meaningful difference
- [ ] Decide how they reach each attendee account (clone the repo in Studio is simplest)

> **Content note:** the English-literature persona uses a public-domain Seacole text that preserves
> nineteenth-century spelling and racial language. Flag it for participants in advance rather than
> letting it arrive unannounced.

### Notebook

- [ ] `discipline-assistant.ipynb` reviewed by all instructors
- [ ] Package versions pinned (`langchain`, `langchain-aws`, `langchain-community`, `faiss-cpu`, `pypdf`) — version drift breaks notebooks
- [ ] Notebook executes top-to-bottom on a clean SageMaker Studio instance without errors

---

## 1 week before — AWS infrastructure

### Per-attendee AWS account access

- [ ] Each registered attendee has an AWS account (or shared seminar account with IAM users)
- [ ] Region locked to `us-east-1` (Bedrock model availability assumes this)
- [ ] SageMaker Studio domain created in each account
- [ ] IAM execution role for SageMaker has Bedrock invoke permissions

### Bedrock model access

Bedrock models require **per-account opt-in**. This is the #1 thing that fails on seminar day. Verify in the Bedrock console under "Model access" for each account:

- [ ] `amazon.nova-lite-v1:0` — for Q&A and direct prompting
- [ ] `amazon.nova-2-multimodal-embeddings-v1:0` — for RAG embeddings
- [ ] `mistral.mixtral-8x7b-instruct-v0:1` — for Part 2 comparison
  - *Confirmed working in MLU training accounts (used in M3 Lab 3a). The MLU `mlu-bedrock-studio-models-SageMakerDomainRole` does NOT grant Anthropic Claude access — do not substitute Claude without verifying IAM policy first.*

### SageMaker Studio domains

- [ ] Instance type: `ml.t3.medium` or larger (smaller instances run out of memory during embedding)
- [ ] Kernel: Python 3 (Data Science) image, or whatever matches the package install in cell 1.1
- [ ] EFS storage allocated (5 GB minimum per user — vector store can be a few hundred MB)
- [ ] Internet access enabled (needed for `pip install` in cell 1.1)

---

## 3 days before — dry run

**Do not skip this step.** Find someone outside the instructor team and have them run the notebook end-to-end on a real attendee account.

- [ ] They can log into SageMaker Studio without help
- [ ] Notebook opens with no errors
- [ ] All 6 sample PDFs are visible in the `data/` folder
- [ ] Default PDF path works (Persona 1 Dentistry)
- [ ] All cells execute top to bottom without errors
- [ ] Total time from launch to Part 5 ≤ 90 minutes
- [ ] Generated outputs are substantive

**If anything fails:** Fix it now, not seminar morning. Most fixable issues found during dry runs are package version mismatches or Bedrock access not propagated.

---

## Day before — content distribution

- [ ] All 6 sample PDFs copied to every attendee's `data/` folder
- [ ] Notebook copied to every attendee's SageMaker Studio home
- [ ] Verify on at least 3 random attendee accounts: open notebook, run Parts 1–3, confirm no errors
- [ ] Persona-PDF mapping decided based on registration (which persona each attendee picked)
- [ ] Default `pdf_path` in each attendee's notebook updated to their persona (or left at Persona 1 as universal default)
- [ ] Slack workspace ready, persona threads pre-created in the share-out channel
- [ ] Backup plan documented (see below)

---

## Morning of — final pre-flight (8:30 AM)

The seminar starts at 9. Lab 2 starts at 1:30. You have all morning to pre-warm.

### 8:30 – 9:00 (before participants arrive)

- [ ] Sign in to your instructor SageMaker Studio account
- [ ] Open the notebook
- [ ] Run cells 1.1 – 1.3 (warms the kernel for your demo)
- [ ] Confirm both Nova Lite and Mistral respond (run Part 2)
- [ ] Confirm sample dentistry PDF loads and embeds (run Part 3.2 – 3.4)
- [ ] Leave the notebook open in a tab — you'll come back to it after lunch

### During PartyRock (11:00 – 12:30)

- [ ] Spot-check that 3 attendee accounts also have warm kernels (have a TA do this)
- [ ] Monitor Slack for "I can't sign into AWS" messages — catch infrastructure issues during PartyRock, not during Lab 2

### Lunch (12:30 – 1:15)

- [ ] **Pre-warm all attendee kernels.** Open the notebook on each account and run cell 1.2 (imports). This eats the kernel startup time so 1:30 is instant.
  - Tip: scripted approach is faster than clicking through each account
- [ ] Confirm projection equipment ready
- [ ] Slack channel pinned to top of workspace

### Bridge (1:15 – 1:30)

- [ ] Lab 2 instructor takes seat at front
- [ ] Notebook open and visible on projector
- [ ] Dentistry sample PDF path set as default in instructor notebook

---

## Backup plans

### If Bedrock model access fails for an attendee

- Fallback model IDs to try (in order):
  1. `amazon.nova-pro-v1:0` (replaces Nova Lite)
  2. `mistral.mistral-7b-instruct-v0:2` (smaller Mistral, lower-tier access)
  3. `amazon.titan-text-express-v1` (last resort — older but broadly enabled)
- If even fallbacks fail: pair them with another attendee for the lab

### If SageMaker Studio is slow/down for everyone

- Run the notebook locally on the instructor laptop, project it as a demo-only
- Have attendees follow along visually
- Lose hands-on but preserve learning

### If the embedding cell fails for everyone

- This means Bedrock embeddings model isn't accessible
- Pivot to text-only Q&A: replace `vectordb.as_retriever()` with passing the raw PDF text directly to the model
- Loses the RAG architecture lesson but keeps the workflow

### If the network is bad

- Pre-download all PDFs into the SageMaker instances (no S3 dependency)
- Disable the `pip install` cell (pre-install packages in the Studio image)

---

## Post-seminar (within 1 week)

- [ ] Archive notebooks + Slack share-outs
- [ ] Survey attendees: what did you actually use Monday? (the real metric)
- [ ] Document issues that came up → update this checklist for next time
- [ ] Decommission AWS accounts or transfer ownership to attendees

---

## Owner sign-off

| Section | Owner | Date complete |
|---|---|---|
| 2 weeks: Sample PDFs | | |
| 2 weeks: Notebook review | | |
| 1 week: AWS provisioning | | |
| 1 week: Bedrock model access | | |
| 3 days: Dry run | | |
| Day before: Distribution | | |
| Morning of: Pre-warm | | |
