# Maintenance

Keeping published material trustworthy after publication.

## Reviewing what is already published

Every contribution carries `last_reviewed`. Review on a yearly cycle, and sooner when a tool it
depends on changes — a renamed model, a deprecated API, a changed console flow.

A review means: open it, check the links, check the prerequisites and costs are still accurate, and
either update `last_reviewed` or open an issue. **Bumping the date without looking is worse than
leaving it stale**, because it tells a reader something false.

## Broken links

`check-links.yml` runs on a schedule and opens an issue listing public links that failed. It flags
for review; it does not edit anything.

Most failures are transient. A link that fails twice in a row is worth chasing. When an external
resource is gone for good, update the contribution — a dead link in a prerequisites section stops
someone before they start.

## Problem reports

| Kind | Response |
|---|---|
| **Private information published** | Immediate. Remove the content and the release asset, then work out how it got there. |
| **Unauthorized third-party material** | Immediate. Unpublish, then resolve rights before republishing. |
| Broken materials or wrong instructions | Normal review cycle, with the contributor. |
| A disagreement about content | Discuss in the issue. The contributor decides within their own contribution. |

For the first two, act first and discuss afterwards. Removing something wrongly published is
reversible; leaving it up is not.

**A private-information report must never be handled in a public issue.** If one arrives that way,
remove the details from the issue, then continue privately.

## Withdrawing a contribution

Contributors may withdraw their work. When that happens:

1. Remove the materials and the release assets.
2. Mark the ID **Withdrawn** in `ID-REGISTER.md`. **The ID stays listed and is never reissued** —
   a citation that points at it should resolve to "withdrawn", not to someone else's work.
3. Rebuild the catalog.
4. Note it in the contribution's `CHANGELOG.md` if the directory remains as a tombstone.

## Collections

Collections in [`collections/`](../collections) are curated lists — cohort, institution, course kit,
event. A collection holds no materials of its own; it points at contributions.

Adding one is a pull request adding `<id>.yml`. Validation checks that every member ID resolves, so
a collection can never quietly point at something that has been withdrawn.

## Generated files

These are derived, and editing them by hand is always wrong:

| File | Generator |
|---|---|
| `catalog/mlu-contributions.json` · `.csv` | `scripts/build_catalog.py` |
| `mlu/<category>/README.md` | `scripts/build_catalog.py` |
| `collections/README.md` | `scripts/build_catalog.py` |
| The category table in the root `README.md` | `scripts/build_catalog.py` |
| Each contribution's `LICENSE.md` · `CITATION.cff` | `scripts/generate_boilerplate.py` |

Both scripts take `--check`, which fails without writing. CI uses that to catch a metadata change
whose generated output was never regenerated.

## The taxonomy

[`catalog/taxonomy.yml`](../catalog/taxonomy.yml) holds the approved vocabulary. Validation *warns*
on values outside it rather than failing, so a contributor is never blocked by a missing term — but
warnings should be resolved, either by fixing the value or by adding the term.

Add terms when a real contribution needs them, not speculatively. A taxonomy full of unused terms is
harder to browse than a short one.
