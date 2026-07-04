# Maintainer Readiness Report: 2026-07-04

This report records the current OSS readiness state for `codex-skills-cn` before a possible `v0.1.0` tag. It is intentionally short: the goal is to make maintainer evidence easy to inspect, not to inflate activity.

## Repository state

- Public repository: `zhuwujing28-del/codex-skills-cn`
- Current skill count: 11
- License: MIT
- Validation command: `python scripts/validate-skills.py`
- Companion eval repository: `zhuwujing28-del/agent-evals-cn`

## Maintainer workflow coverage

The current skill set covers a practical open-source maintenance loop:

| Workflow | Skill |
| --- | --- |
| Repository onboarding | `repo-onboarding-cn` |
| Issue triage | `issue-triage-cn` |
| Pull request review | `pr-review-cn` |
| GitHub Actions failure diagnosis | `github-actions-ci-cn` |
| Dependency upgrade review | `dependency-upgrade-cn` |
| Security advisory triage | `security-advisory-triage-cn` |
| Context and token budget control | `context-budget-cn` |
| Release notes | `release-notes-cn` |
| OpenAI documentation answers | `openai-docs-cn` |
| Lawful web extraction | `scrapling-web-extraction` |
| Small verified coding changes | `karpathy-style-coding` |

## Quality signals

- Each skill is expected to include trigger guidance, non-use cases, workflow steps, verification guidance, and safety or boundary notes.
- GitHub Actions runs the same validation script used locally.
- The repository includes issue templates, a pull request template, contribution guidance, a security policy, and release readiness notes.
- Installation guidance has been checked for Windows users, including `$CODEX_HOME` and default `.codex` paths.

## Companion eval coverage

`agent-evals-cn` currently provides baseline cases for the main workflow categories this repository targets:

- PR review
- issue triage
- CI failure diagnosis
- release readiness
- dependency upgrade review
- security advisory triage
- context budget management
- OpenAI docs answers
- web extraction boundaries
- MCP vs Codex skill boundary decisions

This gives the project a lightweight regression loop: new or changed skills can be checked against concrete maintainer scenarios instead of judged only by how plausible the instructions look.

## Remaining gaps before `v0.1.0`

- Add a README CI badge after confirming the public workflow status is stable.
- Tag `v0.1.0` only after validation passes on the tagged commit.
- Keep collecting real usage reports, especially failure cases that can become companion evals.

## Release recommendation

`codex-skills-cn` is close to a small `v0.1.0` release. The repository has enough focused maintainer workflows, validation, and contribution scaffolding for an initial tag, but should not be presented as a mature ecosystem project yet. The honest positioning is: early-stage, actively maintained, focused on Chinese-speaking OSS maintainers, and paired with a companion eval loop.
