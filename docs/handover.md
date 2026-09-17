# Handover

What was built, what still needs doing before this repository goes live, and how to verify it.

**Repository:** `DTC-Consortium/DTC-Consortium-MLU` — not yet created on GitHub.
**Scope:** the GitHub repository foundation only. Google Doc/Sheet integration and changes to
dtcconsortium.org are later stages and are not started here.

---

## ⚠️ Decide the repository name first

The specification contradicts itself. Its settings table says the repository name is
**`DTC-Consortium-MLU`**; two lines later it gives the resulting address as
**`github.com/DTC-Consortium/AWS-MLU`**. Both cannot be true.

Everything here is built as **`DTC-Consortium-MLU`**, giving
`github.com/DTC-Consortium/DTC-Consortium-MLU` — note the organization name repeats in the URL.

**If the organization prefers `AWS-MLU`, change it before the first push.** Afterwards, published
citation URLs and release links would have to be rewritten. The name appears in:

```bash
grep -rl "DTC-Consortium-MLU" . --exclude-dir=.git
```

---

## Before the first push

| # | Task | Why it blocks |
|---|---|---|
| 1 | Settle the repository name, above | Every citation URL depends on it |
| 2 | Create the repository: `DTC-Consortium` org, **public**, default branch `main`, description and website field per the specification | — |
| 3 | **Create the four GitHub teams** named in `.github/CODEOWNERS`, and give each write access | Until they exist, GitHub cannot assign reviewers and "require code owner review" blocks every pull request |
| 4 | Grant the four organization-approved administrators admin access | They are named in the specification, deliberately not in this repository — see below |
| 5 | Create the labels the issue forms apply: `contribution: new`, `contribution: update`, `problem`, `links`, `needs triage` | Forms still work without them, but triage gets harder |

### On the administrator addresses

The specification names four individual email addresses for administrators. **They are deliberately
not written into this repository**, because it is public and that would publish them. `CODEOWNERS`
uses organization teams instead, which is also what the specification asks for and what survives
someone leaving.

Grant those four people admin access through the GitHub organization settings, and add them to the
`mlu-maintainers` team. Keep the list of who they are wherever the organization already keeps such
records — not here.

## After the first push

| # | Task |
|---|---|
| 6 | Protect `main`: require a pull request, at least one approving review, approval from the relevant code owner, and successful metadata and catalog validation. Block force pushes and branch deletion. Dismiss stale approvals when substantive changes are pushed. |
| 7 | Run **Validate MLU contributions** manually once to confirm the checks pass in CI |
| 8 | Run **Publish an MLU contribution** for `mlu-000001` as a **draft**, download the ZIP, confirm it opens and contains what it should |
| 9 | Set `github.download_url` for each published contribution, then run `python3 scripts/build_catalog.py` and commit |
| 10 | Verify the Colab badge in `mlu-000002` resolves — it points into this repository and only works once the repository is public |

---

## Verifying the setup

The specification's handover checklist, and how to check each item.

| Check | How |
|---|---|
| A signed-out visitor can browse and download published packages | Open the repository URL in a private window. Follow a category index to a contribution, then to its release asset. |
| Every published contribution has a unique ID and complete metadata | `python3 scripts/validate_contributions.py` — currently **5 contributions, 0 errors, 0 warnings** |
| Category indexes and catalog files agree | `python3 scripts/build_catalog.py --check` — both are generated from the same metadata, so they cannot disagree unless someone hand-edited one |
| ZIP files contain the expected materials and open successfully | `python3 scripts/package_contribution.py mlu-000001 --out /tmp/x`, then unzip it |
| A sample submission triggers validation and reviewer assignment | Open a pull request touching `mlu/` from a branch. Requires task 3 to be done. |
| Branch protection prevents unreviewed changes to `main` | Try to push directly to `main` after task 6. It should be refused. |
| No placeholder identities, credentials, or private information published | Verified at build: no secrets, and the only email addresses anywhere are `@example.edu` in fabricated rosters |

---

## The walkthrough

### Submitting

A contributor opens a **New MLU contribution** issue. A maintainer assigns the next ID from
[`ID-REGISTER.md`](../ID-REGISTER.md) in a pull request and replies with it. The contributor copies
the [template](../templates) for their category, fills it in, runs the scripts, and opens a pull
request. Full guide: [`MLU-CONTRIBUTING.md`](../MLU-CONTRIBUTING.md).

### Reviewing

Automated validation runs first — read-only, no credentials, and it never executes contributed code.
A code owner for the category then reviews: rights, privacy, metadata, does it work, documentation,
attribution, in that order. Rights and privacy come first because they are the two that cannot be
undone after publication. Full guide: [`review.md`](review.md).

### Publishing

A maintainer runs the **Publish an MLU contribution** workflow with the contribution's ID. It
validates, packages, and creates a release tagged `<id>-v<version>` with a single ZIP. It refuses to
run from anywhere but `main`, and refuses to overwrite an existing release.

Then set `github.download_url`, rerun `build_catalog.py`, and commit. Until that step, the catalog
shows *not yet released* and no download button — which is correct, because the button would 404.
Full guide: [`publishing.md`](publishing.md).

### Updating

Same ID, always. Open an **Update a contribution** issue, then a pull request: patch for fixes,
minor for additions, major when existing users must change what they do. Add a `CHANGELOG.md` entry,
update `last_reviewed`, regenerate the catalog, publish a new release.

---

## What is in the repository today

Five contributions, migrated from the AWS-MLU Faculty Fellows Impact Inventory:

| ID | Title | Category | Maturity |
|---|---|---|---|
| `mlu-000001` | Curriculum Embedding Lab | professional-student-development | classroom-tested |
| `mlu-000002` | Discipline Assistant Seminar | professional-student-development | classroom-tested |
| `mlu-000003` | Class Participation Scoring | ml-ai-applications | classroom-tested |
| `mlu-000004` | Paper Autograder | ml-ai-applications | classroom-tested |
| `mlu-000005` | Quick Assessment Demo Session | professional-student-development | **pilot** |

`mlu/course-elements/` is intentionally empty — none of the five fits it. Its index says so and
points at the template. The specification asks for one contribution per category in the pilot, so a
course element is the obvious next submission.

### Two things a maintainer should know

**`mlu-000005` is a genuine pilot.** Its expected outcomes are hand-scored predictions, not recorded
results, and the session has not been delivered to a room. That is recorded in its metadata, its
README, and its changelog. Move it to `classroom-tested` only after a real delivery.

**Three inherited external links are dead**, carried over from the source materials:

- `github.com/aws-dsu/mlu-faculty-ai-partyrock-template` — HTTP 404
- `github.com/aws-samples/aws-mlu-eep-generative-ai` — HTTP 404 (and its `LESSONS.md`)

They may be private rather than gone. Confirm which, then either restore access or update the
contributions that reference them. `check-links.yml` will keep reporting them weekly until then.

### One deviation from the specification, on purpose

The specification suggests folder names inside `materials/` — `notebooks/`, `sample-data/`, `src/`
and so on. The migrated notebooks load their data and helper modules **by relative path**, so
splitting them across those folders would break every notebook and force anyone downloading a ZIP
to rearrange it before it runs.

So each runnable bundle is kept together in one folder, and the suggested names are used for what
genuinely separates out — facilitator guides, agendas, slides, recorded evaluation output. Each
contribution's file tree says so. `MLU-CONTRIBUTING.md` records this as the general rule for future
contributions: keep runnable things runnable, and explain the layout in the README.
