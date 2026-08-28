# Application evidence snapshot - 2026-08-28

This dated snapshot keeps the Codex for Open Source application narrative tied to
public, reproducible repository evidence instead of broad adoption claims.

## Public repository state

Checked on 2026-08-28 with GitHub REST metadata and local tracked refs.

| Repository | Public head | Latest public commit | Stars | Forks | Open issues | Latest validate run |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `zhuwujing28-del/codex-skills-cn` | `df1c92e` | Add OSS application evidence checklist | 1 | 0 | 7 | success on `df1c92e`, 2026-08-27T16:21:29Z |
| `zhuwujing28-del/agent-evals-cn` | `2fd40fa` | Add maintainer usage report eval replay | 1 | 0 | 2 | success on `2fd40fa`, 2026-08-27T00:23:28Z |

## Evidence that is safe to cite

- `codex-skills-cn` currently publishes 12 Chinese Codex skills for common OSS
  maintainer workflows: onboarding, issue triage, PR review, CI diagnosis,
  dependency upgrades, security advisory triage, context management, release
  notes, OpenAI docs assistance, web extraction, bug reproduction, and small
  verified coding changes.
- The skill repository includes maintainer-facing examples, contribution and
  security docs, CODEOWNERS review routing, issue templates, local validation,
  and GitHub Actions validation.
- `agent-evals-cn` provides the companion eval baseline and replay reports used
  to check evidence handling, manual scoring, and OSS application claims.
- Current usage evidence is best described as repository-maintainer validation
  and sanitized workflow reports, not broad external adoption.

## Local validation to rerun before submission

```powershell
$env:USERPROFILE\.codex\tools\scrapling-venv\Scripts\python.exe scripts\validate-skills.py
cd ..\agent-evals-cn
$env:USERPROFILE\.codex\tools\scrapling-venv\Scripts\python.exe scripts\validate.py
```

Record the command output and the current GitHub Actions status in the final
application text. If either repository has moved, refresh the public head,
counts, and latest validate-run timestamps above before submitting.

## Wording boundary

Use wording like:

> The repositories are early but maintained: both have public validation checks,
> governance files, issue templates, dated readiness notes, and replayable eval
> evidence. Current evidence supports continued maintainer investment; it does
> not yet prove broad external adoption.

Avoid wording like:

- "widely adopted by Chinese open-source maintainers"
- "proven impact across many projects"
- "large user community"

until those claims have public issue, PR, discussion, or release evidence.
