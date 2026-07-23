# Maintainer Example Index

This index maps each published maintainer-facing example to the skill or workflow
it demonstrates. Keep it updated whenever a new file is added under
`docs/examples/`; `python scripts/validate-skills.py` checks that every example is
listed here.

## Published examples

| Example | Primary skill / workflow | Readiness evidence |
| --- | --- | --- |
| [`docs/examples/issue-triage-sample.md`](examples/issue-triage-sample.md) | `issue-triage-cn` | Shows issue classification, priority, labels, and maintainer reply drafting. |
| [`docs/examples/ci-failure-output.md`](examples/ci-failure-output.md) | `github-actions-ci-cn` | Shows grounded CI failure diagnosis and contributor follow-up. |
| [`docs/examples/dependency-upgrade-review.md`](examples/dependency-upgrade-review.md) | `dependency-upgrade-cn` | Shows evidence-based merge / hold decisions for dependency PRs. |
| [`docs/examples/release-notes-output.md`](examples/release-notes-output.md) | `release-notes-cn` | Shows user-facing Chinese release notes from shipped changes. |
| [`docs/examples/security-advisory-output.md`](examples/security-advisory-output.md) | `security-advisory-triage-cn` | Shows private-channel escalation and bounded public communication. |
| [`docs/examples/maintainer-workflow-session.md`](examples/maintainer-workflow-session.md) | Multi-skill maintainer workflow | Shows how multiple skills combine during a realistic 45-minute maintenance session. |

## Review checklist

Before adding or changing an example, verify that it:

- starts from a realistic maintainer prompt or issue,
- produces concrete output a maintainer could paste or adapt,
- names evidence and validation steps instead of only giving advice,
- avoids exposing real tokens, private logs, or unreleased project details,
- stays small enough to review in one pass.
