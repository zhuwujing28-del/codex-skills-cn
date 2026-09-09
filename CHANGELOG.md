# Changelog

## Unreleased

### Added

- Added `scripts/validate-cross-repo.ps1` to run both repository validators
  from one command when `codex-skills-cn` and `agent-evals-cn` are checked out
  together.
- Refreshed the 2026-09-07 application evidence snapshot so current public
  evidence commits, workflow status, and claim boundaries stay auditable without
  making self-referential head claims.
- Added a 2026-09-07 application evidence snapshot aligned with the latest
  public heads, validation runs, repository counts, and claim boundaries.
- Added a 2026-09-05 application evidence snapshot refreshing public heads,
  validation status, repository counts, and claim boundaries.
- Clarified release-readiness tracking so the completed `v0.1.0` checklist is
  historical context and current checks focus on maintainer evidence and the
  next release decision.
- Updated the public roadmap to distinguish shipped OSS-readiness work from the next feedback and evidence priorities.
- Added a current application evidence snapshot covering the latest public heads, validation status, and honest adoption-claim boundaries.
- Added validation that maintainer feedback and usage-report templates list every current skill, preventing intake drift as the collection grows.
- Added a dated OSS application evidence snapshot tying public repo state, CI status, and adoption-claim boundaries to reproducible sources.
- Added an OSS application evidence checklist that separates repository proof, CI evidence, usage feedback, and unsupported adoption claims.
- Extended skill validation to catch stale maintainer example-index links.
- Extended skill validation to require core OSS governance files before release.
- Added least-privilege read-only permissions to the GitHub Actions validation workflow.
- Added a worked maintainer feedback loop example so real OSS complaints can be turned into a small, evidence-based follow-up.
- Added a repository onboarding sample output that shows the first-pass map, key files, risks, and next steps a maintainer should capture.
- Added `bug-reproduction-cn` for Chinese bug report minimization, reproduction evidence, and maintainer-ready verification notes.
- Added a `pr-review-cn` sample output that demonstrates finding a stale state transition, requesting a focused regression test, and drafting a maintainer reply.
- Added a maintainer example index and validation check so sample outputs remain discoverable as the repository grows.
- Added a maintainer feedback loop note explaining how to turn real OSS usage reports into scoped skill, docs, or eval follow-ups.
- Added a dedicated maintainer feedback request template for collecting structured Chinese OSS maintainer feedback.
- Added `CODEOWNERS` so public contributions route through explicit maintainer review ownership.
- Added a `release-notes-cn` sample output showing Chinese release communication grounded in shipped maintainer-facing changes.
- Added a `dependency-upgrade-cn` sample output showing evidence-based merge/hold decisions for routine Dependabot PRs.
- Added a public issue triage note mapping open setup, boundary, workflow-example, and maintainer-feedback issues to shipped docs and next actions.
- Added a maintainer workflow usage-report issue template for collecting real OSS feedback.
- Added a filled maintainer workflow report example showing how to keep usage reports evidence-first and privacy-preserving.
- Added a GitHub issue template config that disables blank issues and points maintainers to the skill docs path.
- Redirected the issue template config link to the maintainer boundary guide instead of the repo root.
- Added a multi-skill maintainer workflow session example for v0.2 application evidence.
- Added a Codex extension boundary guide explaining when to use skills, MCP, plugins, or personal settings.

### Changed

- Refreshed the Codex for Open Source application notes so the current 12-skill maintainer workflow coverage includes bug reproduction evidence.
- Repaired mojibake in the maintainer feedback request issue template so public OSS feedback can be submitted in readable Chinese.
- Repaired mojibake in the maintainer workflow usage-report issue template so real OSS usage reports can be filed in readable Chinese.
- Tightened public issue follow-up reply templates with clearer next steps for completed setup and boundary issues.
- Corrected the `v0.1.0` release note to point at the published `v0.1.1` hardening tag.

## v0.1.1 - 2026-07-15

### Added

- Added a `v0.1.1` patch-release checklist for packaging post-`v0.1.0` hardening without moving the published tag.
- Added a post-`v0.1.0` audit documenting the published tag target and follow-up patch-release path.
- Added `context-budget-cn` for Codex context and token budget management.
- Added `SECURITY.md` with reporting scope and maintainer response guidance.
- Added a dated maintainer readiness report for `v0.1.0` preparation.
- Added README validation badge for visible CI status.
- Added a `v0.1.0` release checklist for tag readiness review.

### Improved

- Extended validation to catch broken local Markdown links.
- Extended validation to require a `README.md` beside every skill `SKILL.md`.
- Completed Windows Codex skill installation instructions.

## v0.1.0 - 2026-07-08

The first public tag captured the early application-materials baseline. Later validation, CI, security, installation, and README hardening was packaged in the `v0.1.1` patch tag.

### Added

- Added `APPLICATION.md` for Codex for Open Source application preparation.
- Added sample CI failure diagnosis output.
- Added sample security advisory triage output.
- Added `context-budget-cn` for Codex context and token budget management.
- Added a realistic `issue-triage-cn` sample output for maintainer workflow documentation.
- Added GitHub Actions validation for skill structure checks.
- Added `github-actions-ci-cn` for Chinese GitHub Actions CI diagnosis and maintainer replies.
- Added `dependency-upgrade-cn` for dependency upgrade risk assessment and validation planning.
- Added `security-advisory-triage-cn` for safe vulnerability triage and responsible disclosure workflows.
- Added `repo-onboarding-cn` for unfamiliar repository onboarding.
- Added `issue-triage-cn` for issue classification, priority, labels, and maintainer responses.
- Added `pr-review-cn` for Chinese PR/code review focused on regressions and missing tests.
- Added `release-notes-cn` for Chinese release notes and upgrade guidance.
- Added `openai-docs-cn` for Chinese OpenAI developer docs assistance using official sources.
- Added `scripts/validate-skills.py` for skill structure validation.
- Added issue templates for skill requests and bug reports.
- Added Codex for Open Source application notes.

### Improved

- Expanded README with maintainer workflow positioning and recommended usage path.
- Expanded contribution guide with quality standards.
- Updated roadmap toward OSS maintainer workflows and real usage examples.
