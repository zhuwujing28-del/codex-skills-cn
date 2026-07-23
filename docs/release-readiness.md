# Release Readiness

This document tracks what is needed before tagging `v0.1.0`.

## Current status

- Skills: 11
- Validation: `python scripts/validate-skills.py` passes and checks each skill package includes `SKILL.md` plus `README.md`
- CI: GitHub Actions runs the same validation on push and pull request, surfaced by a README badge
- Latest maintainer readiness report: [`maintainer-readiness-2026-07-04.md`](maintainer-readiness-2026-07-04.md)
- Latest post-tag audit: [`post-v0.1.0-audit-2026-07-13.md`](post-v0.1.0-audit-2026-07-13.md)
- Release checklist: [`release-checklist.md`](release-checklist.md)
- Patch release checklist: [`v0.1.1-release-checklist.md`](v0.1.1-release-checklist.md)
- Extension boundary guide: [`codex-extension-boundaries.md`](codex-extension-boundaries.md)
- Latest maintainer workflow example: [`maintainer-workflow-session.md`](examples/maintainer-workflow-session.md)
- Latest release-notes example: [`release-notes-output.md`](examples/release-notes-output.md)
- Latest public issue triage: [`public-issue-triage-2026-07-19.md`](public-issue-triage-2026-07-19.md)
- Maintainer feedback intake: [`.github/ISSUE_TEMPLATE/maintainer_feedback_request.md`](../.github/ISSUE_TEMPLATE/maintainer_feedback_request.md)
- Maintainer feedback follow-up loop: [`maintainer-feedback-loop.md`](maintainer-feedback-loop.md)
- Maintainer example index: [`example-index.md`](example-index.md)
- Latest patch tag: `v0.1.1`
- Current `main` includes post-`v0.1.1` documentation updates recorded under `Unreleased` in the changelog.
- Maintainer workflow coverage:
  - repository onboarding
  - issue triage
  - PR review
  - CI failure diagnosis
  - dependency upgrade review
  - security advisory triage
  - context and token budget management
  - release notes
  - maintainer feedback intake
  - OpenAI docs assistance
  - web extraction
  - small verified coding changes

## Remaining before v0.1.0

- [x] Add 2-4 more high-quality skills or example outputs.
- [x] Add at least one sample output for issue triage, PR review, or CI diagnosis.
- [x] Add README badge after the first workflow run is visible.
- [x] Confirm installation instructions on Windows.
- [x] Add a first-release checklist.
- [x] Publish `v0.1.0`.

## Post-v0.1.0 status

The public `v0.1.0` tag exists but points to an older application-materials baseline. Do not rewrite that tag. Later validation, CI, security, installation, and README hardening were packaged in the follow-up `v0.1.1` patch tag.

Use [`v0.1.1-release-checklist.md`](v0.1.1-release-checklist.md) as the audit trail for that follow-up patch tag.

## Release criteria

Do not tag `v0.1.0` just because the repository exists. Tag only when:

- all skills pass validation,
- each skill package includes a maintainer-facing `README.md`,
- the README explains who the project serves,
- examples show realistic single-skill and multi-skill maintainer workflows,
- and the changelog clearly describes what is included.
