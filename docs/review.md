# Review

Every contribution is reviewed by a code owner for its category before publication. This is what a
reviewer does.

## Before you start

Check that automated validation passed. If it did not, the metadata is not ready and the rest of
the review will waste your time — ask for the fix first.

Validation is deliberately narrow: it checks that metadata is structurally valid, that IDs are
unique and registered, and that listed files exist. It cannot check whether a claim is true, whether
a licence is right, or whether the material teaches well. That is your job.

## 1. Rights — settle this first

If the rights are wrong, nothing else matters.

- Can the contributor share this? Did they say so explicitly, not just imply it?
- Is every bundled file accounted for in `LICENSE.md`, including sample data?
- **Is there anything owned by AWS, a publisher, or an institution?** If so, is there written
  authorization, or should it be linked rather than redistributed?
- Does the declared content licence match what the materials actually allow?

When in doubt, ask for the material to be linked rather than bundled. See
[`licensing.md`](licensing.md).

## 2. Privacy

- **Any real student data?** Papers, transcripts, rosters, grades, screenshots, recorded notebook
  output, filenames. Check recorded output especially — it is easy to miss.
- Any credentials, API keys, tokens, or account IDs? Check notebook cells and their stored output.
- Any placeholder identity that could be mistaken for a real person, or any real email address?
- Does sample data announce itself as fabricated, where a reader might assume otherwise?

## 3. Metadata

- Are `prerequisites.accounts` and `expected_cost` specific enough that someone can decide whether
  they can run this? "An AWS account" is not enough if model access must be enabled in a region.
- Is `maturity` honest? `classroom-tested` means it was delivered to learners and revised
  afterwards. Anything else is `pilot`.
- Does `summary` read well in a table? It is what people see in the category index.
- Are `related_ids` and `collection_ids` real, and do the relationships make sense?
- Are future-integration fields still `null`?

## 4. Does it work?

- Open the materials. Do documents render, decks open, notebooks load?
- Run the notebook on its bundled sample if you can. It should work with no preparation.
- Do the internal links resolve? Materials get rearranged during review, and links go stale.
- Where a contribution ships recorded output, does a fresh run roughly agree with it? Model output
  varies run to run, so expect close agreement rather than an exact match.

**Do not run contributed code as part of automated validation.** Running it yourself, deliberately,
in an environment you control, is a different thing — and it is the only way to check this section.

## 5. Documentation

The test: **could someone who has never met the contributor teach from this?**

- Is the audience stated, and the time it takes?
- Are learning outcomes or intended use concrete enough to plan around?
- For anything that drafts an assessment or a grade — is it clear what the human must still decide?
- Is there a facilitator track for anything that will be delivered live?

## 6. Attribution

- Is every borrowed source credited with its licence?
- Does `CITATION.cff` name the right authors and institutions?
- Do reused files from other contributions say where they came from?

## Approving

Approve when all six sections pass. Request changes otherwise, specifically — name the file and what
to do. "Needs work" wastes a round trip.

Stale approvals are dismissed automatically when substantive changes are pushed. Re-review sections
1 and 2 after any change to materials; they are the two that cannot be undone after publication.
