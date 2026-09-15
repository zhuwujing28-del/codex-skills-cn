# Application evidence snapshot - 2026-09-15

This dated snapshot keeps the Codex for Open Source application narrative tied
to public repository evidence observed on September 15, 2026. It is not a live
status claim and must be refreshed before reuse if the public state changes.

## Public repository state

| Repository | Evidence commit observed before this refresh | Latest validate run | Stars | Forks | Open issues |
| --- | --- | --- | ---: | ---: | ---: |
| `zhuwujing28-del/codex-skills-cn` | `6998bea` — Clarify application evidence snapshot freshness | success, run `#59`, `6998bea`, 2026-09-12 | 1 | 0 | 7 |
| `zhuwujing28-del/agent-evals-cn` | `a3a5a30` — Clarify application evidence snapshot freshness | success, run `#72`, `a3a5a30`, 2026-09-12 | 1 | 0 | 2 |

The commits above are the validated evidence commits observed before this
documentation refresh. They should not be read as a self-referential claim
that this file's own commit is already independently validated.

## Evidence that is safe to cite

- `codex-skills-cn` publishes 12 Chinese Codex skills for common OSS
  maintainer workflows, with examples, governance files, local validation, and
  GitHub Actions validation.
- `agent-evals-cn` maintains 22 baseline eval cases, structured replay results,
  and an independent replay protocol for reviewing results across environments.
- The two repositories now include a cross-repository local validation helper,
  but this is repository-maintainer evidence rather than proof of broad
  external adoption.

## Local validation to rerun before submission

```powershell
python scripts\validate-skills.py
.\scripts\validate-cross-repo.ps1
```

Record the command output and current GitHub Actions status in the final
application text. Refresh this snapshot if either public head, workflow
status, or repository counts move before submission.

## Wording boundary

Use wording like:

> The repositories are early but maintained: both have public validation
> checks, governance files, issue templates, dated readiness notes, and
> replayable eval evidence. Current evidence supports continued maintainer
> investment; it does not yet prove broad external adoption.

Avoid wording like:

- "widely adopted by Chinese open-source maintainers"
- "proven impact across many projects"
- "large user community"

until those claims have public issue, PR, discussion, or release evidence.
