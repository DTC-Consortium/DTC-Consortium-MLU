# Contributing to DTC-Consortium-MLU

How to submit new materials, update materials you already contributed, and what maintainers check
before anything is published.

> **This file has a custom name.** GitHub looks for `CONTRIBUTING.md`; this repository uses
> `MLU-CONTRIBUTING.md` and links to it from the root README, every issue form, and the pull
> request template.

---

## Before you start: do you have the right to share it?

This is the question that stops most submissions, so settle it first.

- **Material you authored**, for a course you teach, is usually yours to share — check your
  institution's IP policy if you are unsure.
- **Material owned by AWS, a publisher, another institution, or any third party is not yours to
  relicense.** Link to the original instead of redistributing it.
- **Anything derived from student work needs consent**, and usually needs to be rewritten as
  synthetic material instead. See below.
- **If you cannot say what licence a file carries, do not submit that file.** A maintainer cannot
  work it out for you.

`docs/licensing.md` covers the details, including how to mix licences inside one contribution.

### Student data: the rule is simple

**No real student records, ever.** Not in papers, transcripts, rosters, grades, screenshots, or
recorded output. Every existing contribution ships fabricated sample data for exactly this reason —
copy that approach. Names, transcripts, and submissions should be invented, and the contribution's
README should say so plainly.

### Anything confidential

Do not open a public issue. Restricted answer keys, unpublished assessments, or anything under
embargo must go through the approved private channel: email the maintainers at the address listed in
the [organization profile](https://github.com/DTC-Consortium), and they will route it.

---

## Submitting a new contribution

### 1. Open an issue and get an ID

Open a **[New MLU contribution](../../issues/new?template=new-mlu-contribution.yml)** issue
describing what you want to share and linking to the materials.

A maintainer replies with a **permanent ID** in the form `mlu-000042`, recorded in
[`ID-REGISTER.md`](ID-REGISTER.md). **Do not pick your own ID.** IDs are never reused or renumbered,
because citations and release tags depend on them.

### 2. Build the contribution

Copy the [template](templates) for your category into the right place:

| Your material is | It goes in |
|---|---|
| A course, module, lecture, assignment, assessment, or other instructional material | `mlu/course-elements/` |
| A working tool, prompt set, codebase, dataset, or platform | `mlu/ml-ai-applications/` |
| A bootcamp, workshop, training, presentation, or similar initiative | `mlu/professional-student-development/` |

Name the directory `<id>-<short-slug>`, for example
`mlu/course-elements/mlu-000042-responsible-ai-module/`.

Every contribution contains:

| File | What it holds |
|---|---|
| `README.md` | Overview, audience, learning outcomes or intended use, prerequisites, contents, usage |
| `mlu-contribution.yml` | Structured metadata — see below |
| `CHANGELOG.md` | Published versions and what changed |
| `LICENSE.md` | Reuse terms, per file where they differ |
| `CITATION.cff` | How you want to be cited |
| `materials/` | The actual deliverables |

Add `examples/`, `media/`, or `references/` only if you need them.

`LICENSE.md` and `CITATION.cff` are **generated** from your metadata — fill in
`mlu-contribution.yml` and run `python3 scripts/generate_boilerplate.py`.

### 3. Organise `materials/`

Use folders that suit the contribution. Common ones:

| Category | Usual folders |
|---|---|
| Course elements | `syllabus/` `faculty-guide/` `lectures/` `assignments/` `assessments/` `rubrics/` |
| ML/AI applications | `prompts/` `src/` `notebooks/` `sample-data/` `evaluation/` `setup/` |
| Professional/student development | `facilitator-guide/` `agenda/` `slides/` `activities/` `participant-resources/` `evaluation/` |

**Keep runnable things runnable.** If a notebook loads its data and helper modules by relative path,
keep them together in one folder rather than scattering them to match the table above. A layout
someone has to rearrange before it runs is a worse layout. Say what you did in your README.

**Videos and large datasets do not belong in the repository.** Host them somewhere approved, and
list them in your materials manifest with `external: true` and access instructions.

Provide editable source files (`.pptx`, `.docx`, `.ipynb`) alongside PDFs wherever you can. Someone
adapting your work for their own course needs the editable copy.

### 4. Fill in the metadata

`mlu-contribution.yml` drives the category indexes, the catalog, and the search fields — it is not
paperwork. [`schemas/mlu-contribution.schema.json`](schemas/mlu-contribution.schema.json) is the
authoritative list; [`catalog/taxonomy.yml`](catalog/taxonomy.yml) holds the approved vocabulary.

Three fields people get wrong:

- **`prerequisites.accounts` and `prerequisites.expected_cost`** — name every account a participant
  needs and what it will cost them. "An AWS account" is not enough if they also need model access
  enabled in a particular region.
- **`maturity`** — `pilot` until it has been delivered to learners and the resulting revisions folded
  back in. Only then is it `classroom-tested`. There is no shame in `pilot`; there is a problem with
  claiming otherwise.
- **`materials`** — every deliverable, with a real path. Validation fails if a listed path does not
  exist.

**Leave future integration fields empty.** `website_url` and similar stay `null` until those pages
exist. Do not link to a page that has not been built.

### 5. Check it yourself, then open a pull request

```bash
pip install -r scripts/requirements.txt
python3 scripts/generate_boilerplate.py     # writes LICENSE.md and CITATION.cff
python3 scripts/build_catalog.py            # regenerates catalog and indexes
python3 scripts/validate_contributions.py   # must pass
```

Open a pull request. The template's checklist is the same list a reviewer works through, so filling
it in honestly is the fastest route to approval.

---

## Updating a contribution

Open an **[Update a contribution](../../issues/new?template=update-mlu-contribution.yml)** issue,
then a pull request. Keep the same ID — updates never get a new one.

Version it by what changed:

| Change | Bump | Example |
|---|---|---|
| Fixes, clarifications, corrected links | **patch** — `1.0.1` | A broken link, a typo in a rubric |
| New materials that do not break existing use | **minor** — `1.1.0` | A new persona, an extra activity |
| Existing users must change what they do | **major** — `2.0.0` | Restructured folders, a replaced notebook |

Add a `CHANGELOG.md` entry, update `last_reviewed`, and regenerate the catalog.

---

## What a reviewer checks

A code owner for your category reviews every pull request. In roughly this order:

1. **Rights.** Is this yours to share, and is the licence right for every file including sample data?
2. **Privacy.** No student records, no credentials, no private information, no placeholder
   identities that look real.
3. **Metadata.** Valid, honest, and specific — especially prerequisites, costs, and maturity.
4. **It works.** Materials open, notebooks run on their bundled sample, links resolve.
5. **Documentation.** Could someone who has never met you teach from this?
6. **Attribution.** Every borrowed source credited, with its licence.

Reviewers will ask for changes. That is the process working, not a rejection.

---

## After approval

A maintainer publishes a release, `<id>-v<version>` — for example `mlu-000042-v1.0.0` — with a ZIP
of that one contribution and version. Your README and the category index link directly to that
asset. See [`docs/publishing.md`](docs/publishing.md).

---

## Getting help

- Something broken or wrong → **[Report a problem](../../issues/new?template=report-problem.yml)**
- Stuck on metadata or layout → open a draft pull request and ask. Half-finished is fine.
- Not sure you can share something → ask **before** you submit it, not after.
