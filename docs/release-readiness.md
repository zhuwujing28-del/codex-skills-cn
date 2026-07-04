# Release Readiness

This document tracks what is needed before tagging `v0.1.0`.

## Current status

- Skills: 11
- Validation: `python scripts/validate-skills.py` passes
- CI: GitHub Actions runs the same validation on push and pull request
- Latest maintainer readiness report: [`maintainer-readiness-2026-07-04.md`](maintainer-readiness-2026-07-04.md)
- Maintainer workflow coverage:
  - repository onboarding
  - issue triage
  - PR review
  - CI failure diagnosis
  - dependency upgrade review
  - security advisory triage
  - context and token budget management
  - release notes
  - OpenAI docs assistance
  - web extraction
  - small verified coding changes

## Remaining before v0.1.0

- [x] Add 2-4 more high-quality skills or example outputs.
- [x] Add at least one sample output for issue triage, PR review, or CI diagnosis.
- [ ] Add README badge after the first workflow run is visible.
- [x] Confirm installation instructions on Windows.
- [ ] Tag `v0.1.0`.

## Release criteria

Do not tag `v0.1.0` just because the repository exists. Tag only when:

- all skills pass validation,
- the README explains who the project serves,
- examples show realistic maintainer workflows,
- and the changelog clearly describes what is included.
