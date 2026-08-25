# Sample Output: Maintainer Workflow Report

This sample shows how to fill the maintainer workflow usage-report template with
concrete evidence instead of turning one good session into broad adoption claims.

## Input

```text
Skill: repo-onboarding-cn
Project type: small TypeScript CLI
Task type: onboarding + release readiness
Input material: public README, package.json, one GitHub Actions failure excerpt, sanitized changelog draft
Sensitive info: already redacted

Useful observations:
- Codex found the validation command quickly and summarized release blockers.
- The final maintainer reply was paste-ready.

Needs improvement:
- It called the repository "release-ready" before checking the latest GitHub Actions run.
- It did not say whether the CI excerpt came from the latest run.
- The Chinese reply sounded too promotional for a GitHub issue.

Please turn this into a small, actionable maintainer follow-up.
```

## Expected Maintainer Output

```text
Original maintainer scenario: a repo onboarding session exposed a wording problem in the usage report template and a missing evidence-order check.

Sensitive data removed: keep only the redacted CI excerpt, public repo metadata, and sanitized changelog text.

Chosen artifact type: tighten the maintainer workflow report template and add one example sentence that requires latest-run CI evidence before calling a repo release-ready.

Validation command recorded: `python scripts/validate-skills.py`

Public reply or changelog note: "Thanks — I updated the usage-report template so reports must name the latest CI run and keep the public reply grounded in evidence. The fix is small and based on the report above."
```

## Minimal evidence to keep

- report issue link or sanitized screenshot,
- CI run URL or timestamp,
- exact wording that overclaimed release readiness,
- and the validation command output after the template fix.

## Why this helps readiness

- It gives maintainers a concrete filled example of the usage-report template.
- It keeps follow-up small and evidence-first.
- It makes it easier to turn future reports into a doc patch or companion eval.
