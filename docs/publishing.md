# Publishing

Turning an approved contribution into a downloadable release. Maintainers only.

## Assigning an ID

When a submission is accepted, add the next unused ID to [`ID-REGISTER.md`](../ID-REGISTER.md) in a
pull request, and reply on the issue with it.

- **Never reuse an ID**, including after a withdrawal. Citations and release tags depend on them.
- **Never renumber.** An ID is permanent from the moment it is assigned.
- A module gets its own ID when it is independently reusable and downloadable. Otherwise it stays in
  its parent package, and that package's README describes it. If it does get one, set `parent_id`.

## One canonical copy

Each contribution exists in exactly one place. To associate it with several institutions,
disciplines, or programs, use metadata and [collections](../collections) — never a second copy.
Two copies drift, and the wrong one always gets downloaded.

## Cutting a release

Publication runs from `main` after approval, through `publish-mlu-contribution.yml`.

**Tag:** `<id>-v<version>` — for example `mlu-000042-v1.0.0`
**Asset:** `<id>-v<version>.zip` — for example `mlu-000042-v1.0.0.zip`

The ZIP contains that one contribution: its `README.md`, `mlu-contribution.yml`, `CHANGELOG.md`,
`LICENSE.md`, `CITATION.cff`, and `materials/`.

It does **not** contain videos, large datasets, or anything not cleared for redistribution. Those
appear in `RESOURCES.md`, generated into the ZIP from the external entries in the materials manifest,
with access instructions for each.

### After the release exists

1. Set `github.download_url` in `mlu-contribution.yml` to the version-specific asset URL.
2. Run `python3 scripts/build_catalog.py`.
3. Commit both.

**Order matters.** Until step 1, the catalog shows `not yet released` and shows no download button.
That is correct: a download button that 404s is worse than no button.

**Never link a repository-wide "latest release"** for an individual contribution. Someone following
it gets whichever contribution was released most recently, which is almost never the one they
wanted. Link the specific asset.

## Permissions

| Workflow | Permissions |
|---|---|
| Validation on pull requests | Read-only. No publishing credentials, no secrets. |
| Catalog build | Write to the repository, on `main` only. |
| Publishing | Write to contents and releases, on `main` only, triggered manually by a maintainer. |

Pull request validation runs against submitted content and must never hold a credential that could
publish. **Metadata validation does not execute submitted application code.**

## Republishing a version

Don't. Cut a new patch version instead. Anyone who downloaded the old ZIP has no way to learn it
changed underneath them.

The exception is a published package containing private information or unauthorized third-party
material. Then: delete the asset immediately, then follow [`maintenance.md`](maintenance.md).
