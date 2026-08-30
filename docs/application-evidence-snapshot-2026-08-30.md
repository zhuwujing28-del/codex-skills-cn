# Application evidence snapshot - 2026-08-30

This dated snapshot keeps the Codex for Open Source application narrative tied
to current public repository evidence instead of broad adoption claims.

## Public repository state

Checked on 2026-08-30 with GitHub REST metadata, public refs, and workflow
status.

| Repository | Public head | Latest public commit | Stars | Forks | Open issues | Latest validate run |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `zhuwujing28-del/codex-skills-cn` | `3f1a77b` | Keep maintainer feedback templates current | 1 | 0 | 7 | success on `3f1a77b`, 2026-08-29T22:38:43Z |
| `zhuwujing28-del/agent-evals-cn` | `12d7ecb` | Validate contributor command documentation | 1 | 0 | 2 | success on `12d7ecb`, 2026-08-29 |

## Evidence that is safe to cite

- `codex-skills-cn` publishes 12 Chinese Codex skills for common OSS
  maintainer workflows, with maintainer examples, governance files, issue
  templates, local validation, and GitHub Actions validation.
- The feedback and workflow-report templates are currently checked against the
  skill directory so new skills do not silently disappear from maintainer
  intake.
- `agent-evals-cn` provides the companion eval baseline, coverage map, and
  replay reports used to check evidence handling, manual scoring, and OSS
  application claims.
- Current usage evidence is best described as repository-maintainer validation
  and sanitized workflow reports, not broad external adoption.

## Local validation to rerun before submission

```powershell
$env:USERPROFILE\.codex\tools\scrapling-venv\Scripts\python.exe scripts\validate-skills.py
cd ..\agent-evals-cn
$env:USERPROFILE\.codex\tools\scrapling-venv\Scripts\python.exe scripts\validate.py
```

Record the command output and current GitHub Actions status in the final
application text. Refresh this snapshot if either public head or repository
counts move before submission.

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
