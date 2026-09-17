# Curriculum Embedding Lab — Pre-Flight Checklist

**For:** The instructor team setting up Lab 2 (curriculum-embedding) infrastructure before the seminar.
**Companion docs:** `INSTRUCTOR_CHEATSHEET.md` (run-of-show), `SEMINAR_PLAN.md` (full agenda), `CONTENT_AUDIT.md` (why this lab exists).

The MLU bootcamp materials don't cover SageMaker setup — they assume you stay in PartyRock all day. We added this lab, so this setup is on us.

---

## Timeline

| When | What | Owner |
|---|---|---|
| **2 weeks before** | Source 4 remaining sample PDFs (Persona 3, 4, 5, 6) | — |
| **1 week before** | AWS accounts + Bedrock model access provisioned | — |
| **3 days before** | Full dry run on a real attendee account | — |
| **Day before** | Sample PDFs and notebook deployed to all accounts | — |
| **Morning of** | Kernels pre-warmed, Slack channel live | — |

Assign an owner for each row before scheduling.

---

## 2 weeks before — content prep

### Sample PDFs (the biggest open item)

- [ ] **Persona 1 (Dentistry)** ✅ already staged — Cureus 2026 case report (CC-BY)
- [ ] **Persona 2 (CS)** ✅ already staged — Open Data Structures Ch. 1 (CC-BY)
- [ ] **Persona 3 (English Lit)** — source from Project Gutenberg
- [ ] **Persona 4 (Nursing)** — source from OpenStax Pharmacology for Nurses
- [ ] **Persona 5 (Business)** — source from MIT Sloan LearningEdge
- [ ] **Persona 6 (Biology)** — source from OpenStax AP Bio Lab Manual or CUNY OER

For each PDF:
- [ ] License documentation saved alongside (CC-BY or public domain only)
- [ ] Loads cleanly in `PyPDFLoader`
- [ ] < 50 pages (extract a chapter if source is larger)
- [ ] Embedding completes in < 90 seconds
- [ ] Generates substantive output when persona's prompt runs against it

### Notebook

- [ ] `curriculum-embedding-lab.ipynb` reviewed by all instructors
- [ ] Package versions pinned in `requirements.txt` (already done — version drift is the #1 silent killer)
- [ ] Notebook executes top-to-bottom on a clean SageMaker Studio instance without errors for at least one persona

---

## 1 week before — AWS infrastructure

### Per-attendee AWS account access

- [ ] Each registered attendee has an AWS account (or shared seminar account with IAM users)
- [ ] Region locked to `us-east-1` (Bedrock model availability assumes this)
- [ ] SageMaker Studio domain created in each account
- [ ] IAM execution role for SageMaker has Bedrock invoke permissions

### Bedrock model access

Bedrock models require **per-account opt-in**. This is the #1 thing that fails on seminar day. Verify in the Bedrock console under "Model access" for each account:

- [ ] `amazon.nova-lite-v1:0` — used for the persona tools
- [ ] `amazon.nova-2-multimodal-embeddings-v1:0` — used for the RAG search index

> **Note:** This lab uses fewer models than the v1 Lab 2. There's no model-swap demo (we removed it — the embedding focus is more valuable than seeing Nova vs Mistral side-by-side). If you previously enabled Mistral for v1, that's fine but not required.

### SageMaker Studio domains

- [ ] Instance type: `ml.t3.medium` or larger (smaller instances run out of memory during embedding)
- [ ] Kernel: Python 3 (Data Science) image, or whatever matches the package install
- [ ] EFS storage allocated (5 GB minimum per user)
- [ ] Internet access enabled (needed for `pip install` in cell 1.1)

---

## 3 days before — dry run

**Do not skip this step.** Find someone outside the instructor team — ideally a real faculty member from one discipline — and have them run the notebook end-to-end on a real attendee account.

- [ ] They can log into SageMaker Studio without help
- [ ] Notebook opens with no errors
- [ ] All 6 sample PDFs are visible in the `data/` folder
- [ ] They successfully change their persona variable and run their tool
- [ ] **They fill in Part 3 and Part 4 reflection cells without confusion** ← the new critical test
- [ ] The exported artifact contains both AI output and their curriculum plan
- [ ] Total time from launch to Part 7 ≤ 90 minutes
- [ ] **They can articulate, when asked, where in their course this fits** ← if they can't, the lab failed its core goal

**If anything fails:** Fix it before seminar morning. Most fixable issues are package version mismatches, missing Bedrock access, or vague reflection prompts that need worked examples added.

---

## Day before — content distribution

- [ ] All 6 sample PDFs copied to every attendee's `data/` folder
- [ ] Notebook copied to every attendee's SageMaker Studio home
- [ ] `mlu_utils/` folder copied alongside the notebook (contains the embeddings helper)
- [ ] Verify on at least 3 random attendee accounts: open notebook, run Parts 1–2, confirm no errors
- [ ] Persona-PDF mapping decided based on registration (which persona each attendee picked)
- [ ] Slack workspace ready, persona threads pre-created in the share-out channel
- [ ] Backup plans documented (see below)

---

## Morning of — final pre-flight (8:30 AM)

The seminar starts at 9. The curriculum-embedding lab starts at 1:30. You have all morning to pre-warm.

### 8:30 – 9:00 (before participants arrive)

- [ ] Sign in to your instructor SageMaker Studio account
- [ ] Open the notebook
- [ ] Run cells 1.1, 1.2, 1.3 (warms the kernel for your demo)
- [ ] Set `persona = "1"` and run cells 2.1, 2.2, 2.3 — verify Dentistry vignettes generate cleanly
- [ ] Leave the notebook open in a tab — you'll come back to it after lunch

### During PartyRock (11:00 – 12:30)

- [ ] Spot-check that 3 attendee accounts also have warm kernels (have a TA do this)
- [ ] Monitor Slack for "I can't sign into AWS" messages — catch infrastructure issues during PartyRock, not during the lab

### Lunch (12:30 – 1:15)

- [ ] **Pre-warm all attendee kernels.** Open the notebook on each account and run cell 1.2 (imports). This eats kernel startup time so 1:30 is instant.
- [ ] Confirm projection equipment ready
- [ ] Slack channel pinned to top of workspace

### Bridge (1:15 – 1:30)

- [ ] Lab instructor takes seat at front
- [ ] Notebook open and visible on projector
- [ ] `persona = "1"` set for the demo
- [ ] Your own example values for Part 3/4 reflection cells prepared (see INSTRUCTOR_CHEATSHEET for the worked example you'll project)

---

## Backup plans

### If Bedrock model access fails for an attendee

- Fallback model IDs to try (in order):
  1. `amazon.nova-pro-v1:0` (replaces Nova Lite — better quality, slightly higher cost)
  2. `amazon.titan-text-express-v1` (last resort — older but broadly enabled)
- If even fallbacks fail: pair them with another attendee for the lab

### If SageMaker Studio is slow/down for everyone

- Run the notebook locally on the instructor laptop, project it as demo-only
- Have attendees fill out Part 3, 4, 6 reflection cells on paper instead
- **Reflection still works without code.** That's actually the lab.

### If the embedding cell fails for everyone

- This means Bedrock embeddings model isn't accessible
- Pivot to text-only Q&A: pass the raw PDF text directly to the model instead of using vector retrieval
- Loses the grounded-search elegance but keeps the workflow
- For most personas, the prompt is robust enough that this still works

### If the network is bad

- Pre-download all PDFs into the SageMaker instances (no internet dependency during lab)
- Pre-install packages in the Studio image so the `pip install` cell becomes optional

### If the reflection cells get vague answers from everyone

- This is the most pedagogically dangerous failure mode
- Stop the lab. Project your own worked example. Make 3 faculty read theirs out loud.
- Restart Part 3 with the requirement: *"Replace every bracket placeholder with a real specific value."*

---

## Post-seminar (within 1 week)

- [ ] Archive notebooks + Slack share-outs
- [ ] Survey attendees: **what did you actually do on the date you committed to?** (the real metric)
- [ ] Document issues → update this checklist for next time
- [ ] Decommission AWS accounts or transfer ownership to attendees

---

## Owner sign-off

| Section | Owner | Date complete |
|---|---|---|
| 2 weeks: Sample PDFs 3–6 | | |
| 2 weeks: Notebook review | | |
| 1 week: AWS provisioning | | |
| 1 week: Bedrock model access | | |
| 3 days: Dry run with non-instructor | | |
| Day before: Distribution | | |
| Morning of: Pre-warm | | |
