# Handover

What was built, what still needs doing before this repository goes live, and how to verify it.

**Repository:** <https://github.com/DTC-Consortium/DTC-Consortium-MLU> — **live and public.**
**Scope:** the GitHub repository foundation only. Google Doc/Sheet integration and changes to
dtcconsortium.org are later stages and are not started here.

---

## Done

| | |
|---|---|
| Repository created | `DTC-Consortium/DTC-Consortium-MLU`, **public**, default branch `main`, description and website field set per the specification |
| Content pushed | 185 files; five contributions; four workflows registered and active |
| Validation | 5 contributions, 0 errors, 0 warnings; catalog and generated files current; no broken local links |
| `main` protected | Full section 6 settings applied, including code owner review — see below |

### On the repository name

The specification contradicts itself: its settings table says **`DTC-Consortium-MLU`**, while two
lines later it gives the address as **`github.com/DTC-Consortium/AWS-MLU`**. `DTC-Consortium-MLU`
was chosen, so the organization name repeats in the URL.

**Renaming is still possible but is no longer free.** GitHub redirects the old URL, but published
citation URLs in each `CITATION.cff`, and the release links once releases exist, would need
rewriting. If the organization wants `AWS-MLU`, do it now rather than after the first release:

```bash
gh repo rename AWS-MLU --repo DTC-Consortium/DTC-Consortium-MLU
grep -rl "DTC-Consortium-MLU" . --exclude-dir=.git   # then update these
python3 scripts/generate_boilerplate.py && python3 scripts/build_catalog.py
```

---

## ⚠️ Create the CODEOWNERS teams before inviting contributors

`main` is protected with **require code owner review** enabled, but the four teams
`.github/CODEOWNERS` points at **do not exist yet**:

- `mlu-maintainers`
- `mlu-course-elements`
- `mlu-ml-ai-applications`
- `mlu-professional-student-development`

**Until they exist, no pull request can be merged by a non-admin.** GitHub has no code owner to
request a review from, so the requirement can never be satisfied.

Creating them needs `admin:org`, which the setup token did not have. Create each team in the
`DTC-Consortium` organization and give it **write** access to this repository:

```bash
gh auth refresh -h github.com -s admin:org
for t in mlu-maintainers mlu-course-elements mlu-ml-ai-applications \
         mlu-professional-student-development; do
  gh api -X POST orgs/DTC-Consortium/teams -f name="$t" -f privacy=closed
  gh api -X PUT "orgs/DTC-Consortium/teams/$t/repos/DTC-Consortium/DTC-Consortium-MLU" \
    -f permission=push
done
```

### The escape hatch, and why it exists

Branch protection was applied with **`enforce_admins: false`**, so repository administrators can
still push to `main` directly. That is deliberate: with the teams missing and no second reviewer,
enforcing on admins too would leave nobody able to merge anything, including the fix.

**Once the teams exist and there is more than one maintainer, turn it on:**

```bash
gh api -X POST repos/DTC-Consortium/DTC-Consortium-MLU/branches/main/protection/enforce_admins
```

Leaving it off indefinitely means an administrator can bypass review entirely, which is the
one hole left in section 6.

## Still outstanding

| # | Task | Why it matters |
|---|---|---|
| 1 | **Create the four CODEOWNERS teams**, above | No pull request is mergeable by a non-admin until they exist |
| 2 | Grant the four organization-approved administrators admin access | They are named in the specification, deliberately not in this repository — see below |
| 3 | Create the labels the issue forms apply: `contribution: new`, `contribution: update`, `problem`, `links`, `needs triage` | Forms still work without them, but triage gets harder |
| 4 | Enable `enforce_admins` once there is a second maintainer | Otherwise an admin can bypass review |

### On the administrator addresses

The specification names four individual email addresses for administrators. **They are deliberately
not written into this repository**, because it is public and that would publish them. `CODEOWNERS`
uses organization teams instead, which is also what the specification asks for and what survives
someone leaving.

Grant those four people admin access through the GitHub organization settings, and add them to the
`mlu-maintainers` team. Keep the list of who they are wherever the organization already keeps such
records — not here.

### Branch protection as applied

| Setting | State |
|---|---|
| Require a pull request before merging | on |
| Required approving reviews | 1 |
| Require code owner review | on — **needs the teams above** |
| Dismiss stale approvals on new commits | on |
| Required status check | `Metadata, catalog, and local links`, branch must be up to date |
| Force pushes | blocked |
| Branch deletion | blocked |
| Conversation resolution required | on |
| Enforced on administrators | **off** — see the escape hatch above |

The validation workflow deliberately has **no `paths` filter**. As a required check it must report
on every pull request; a filtered check simply never reports on a pull request outside its paths,
which blocks that pull request forever.

### Then

| # | Task |
|---|---|
| 5 | Run **Validate MLU contributions** manually once to confirm the checks pass in CI as well as locally |
| 6 | Run **Publish an MLU contribution** for `mlu-000001` as a **draft**, download the ZIP, confirm it opens and contains what it should |
| 7 | Set `github.download_url` for each published contribution, then run `python3 scripts/build_catalog.py` and commit |

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
| The Colab badge in `mlu-000002` resolves | **Verified** — the notebook returns HTTP 200 from `raw.githubusercontent.com` now that the repository is public |

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
