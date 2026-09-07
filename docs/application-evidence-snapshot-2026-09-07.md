# Application evidence snapshot - 2026-09-07

This dated snapshot keeps the Codex for Open Source application narrative tied
to current public repository evidence instead of broad adoption claims.

## Public repository state

Checked on 2026-09-07 with GitHub REST metadata, public refs, and workflow
status.

| Repository | Evidence commit observed before this refresh | Latest public commit | Stars | Forks | Open issues | Latest validate run |
| --- | --- | --- | ---: | ---: | ---: | --- |
| `zhuwujing28-del/codex-skills-cn` | `11d7957` | Refresh application evidence snapshot | 1 | 0 | 7 | success on `11d7957`, run #56, 2026-09-07T15:42:28+08:00 |
| `zhuwujing28-del/agent-evals-cn` | `6d137a2` | Refresh application evidence snapshot | 1 | 0 | 2 | success on `6d137a2`, run #70, 2026-09-07T07:39:46+08:00 |

The commits above are the validated evidence commits observed before this
documentation refresh. They should not be read as a self-referential claim that
this file's own commit is already independently validated.

## Evidence that is safe to cite

- `codex-skills-cn` publishes 12 Chinese Codex skills for common OSS
  maintainer workflows, with examples, governance files, issue templates,
  local validation, and GitHub Actions validation.
- `agent-evals-cn` maintains 22 baseline eval cases, structured replay results,
  and an independent replay protocol for reviewing results across environments.
- Current usage evidence is best described as repository-maintainer validation,
  sanitized workflow reports, and replay protocols—not broad external adoption.

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
