# Release Readiness

This document tracks what is needed before tagging `v0.1.0`.

## Current status

- Skills: 8
- Validation: `python scripts/validate-skills.py` passes
- CI: GitHub Actions runs the same validation on push and pull request
- Maintainer workflow coverage:
  - repository onboarding
  - issue triage
  - PR review
  - CI failure diagnosis
  - release notes
  - OpenAI docs assistance
  - web extraction
  - small verified coding changes

## Remaining before v0.1.0

- [ ] Add 2-4 more high-quality skills or example outputs.
- [ ] Add at least one sample output for issue triage, PR review, or CI diagnosis.
- [ ] Add README badge after the first workflow run is visible.
- [ ] Confirm installation instructions on Windows.
- [ ] Tag `v0.1.0`.

## Release criteria

Do not tag `v0.1.0` just because the repository exists. Tag only when:

- all skills pass validation,
- the README explains who the project serves,
- examples show realistic maintainer workflows,
- and the changelog clearly describes what is included.
