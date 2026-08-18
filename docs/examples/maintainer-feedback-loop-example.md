# Sample Output: Maintainer Feedback Loop

This sample shows how a real maintainer complaint becomes one bounded repo
improvement instead of a vague "we should fix the docs" note.

## Input

```text
我是一个中文开源仓库维护者。
最近有人反馈：Windows 上复制 Codex skills 的安装说明太跳步了，
他不知道 `$HOME`、`$env:USERPROFILE` 和仓库路径应该怎么对应。
请帮我把这条反馈整理成一个可执行的下一步：
- 先判断应该改哪个 artifact
- 给出最小可保留证据需要留下什么
- 写一段可直接贴到 issue/PR 的维护者回复
```

## Expected Maintainer Output

**Original maintainer scenario:** Windows skill installation instructions are too
implicit for first-time users.

**Sensitive data removed:** Keep only the path example, command snippet, and the
install failure text; remove usernames, screenshots with personal folders, and
any private repo paths.

**Chosen artifact type:** Update `docs/codex-skill-installation.md` with a short
Windows path mapping example and link it from `README.md`.

**Validation command recorded:** `python scripts/validate-skills.py`

**Public reply or changelog note:** "Thanks — I updated the Windows install
section with a concrete `$HOME` / `$env:USERPROFILE` example so the copy step is
easier to follow. The change is small and based on the install feedback above."

## Minimal evidence to keep

- the exact install command the maintainer ran,
- the observed Windows shell and copy path,
- the missing-path confusion in the user report,
- and the validation command output after the doc change.

## Why this helps readiness

- It shows how `docs/maintainer-feedback-loop.md` should be used in practice.
- It gives maintainers a concrete example of evidence-first follow-up.
- It creates a small artifact that can seed a future companion eval in
  `agent-evals-cn`.