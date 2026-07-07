# v0.1.0 Release Checklist

Use this checklist before tagging the first public skill release.

## Preconditions

- `docs/release-readiness.md` shows only the tag itself as remaining.
- `CHANGELOG.md` summarizes the skills, examples, templates, CI status, and known limits included in the release.
- `python scripts/validate-skills.py` passes locally.
- The public `validate` GitHub Actions workflow is green on `main`.
- README installation guidance has been checked on Windows, including paths under `%USERPROFILE%\.codex\skills`.
- Example outputs do not include private repository names, access tokens, customer data, or unpublished vulnerability details.

## Release steps

1. Run `python scripts/validate-skills.py`.
2. Review `docs/maintainer-readiness-2026-07-04.md` and confirm its remaining-gap section is still accurate.
3. Check the README badge links to the public workflow page.
4. Update `CHANGELOG.md` by moving relevant `Unreleased` notes under `v0.1.0`.
5. Create an annotated tag:

   ```powershell
   git tag -a v0.1.0 -m "codex-skills-cn v0.1.0"
   git push origin v0.1.0
   ```

6. Confirm the GitHub tag or release page renders README links, docs, examples, and skill paths correctly.

## Do not release if

- Any skill is a placeholder or lacks a clear trigger, boundary, workflow, and verification section.
- The validation workflow is failing or missing from the public repository.
- The changelog overstates maturity beyond an early Chinese Codex skill collection.
- Installation instructions rely on local paths that only work on the maintainer's machine.
- Any example output exposes private project, security, account, or customer information.
