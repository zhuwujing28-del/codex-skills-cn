# Public Issue Triage - 2026-07-19

This note reconciles the currently open public GitHub issues with the docs and
examples that have already landed on `main`. It is intended as maintainer
evidence for closing stale setup issues, leaving roadmap issues open, and
asking for real usage reports instead of adding placeholder content.

## Snapshot

- Repository: `zhuwujing28-del/codex-skills-cn`
- Public check time: 2026-07-19
- Local state checked: clean `main`, aligned with `origin/main`
- Public open issues checked through the GitHub API: 7
- Latest public commits checked:
  - `6a87256` - maintainer workflow report template
  - `8751f35` - application notes refresh
  - `2cb4ea1` - multi-skill maintainer workflow example

## Recommended issue actions

| Issue | Topic | Evidence on `main` | Suggested action |
| --- | --- | --- | --- |
| #1 | Codex skill installation tutorial | [`codex-skill-installation.md`](codex-skill-installation.md) and README installation path exist. | Close as completed after posting the doc link. |
| #2 | More Chinese Codex workflow examples | Single-skill examples and [`maintainer-workflow-session.md`](examples/maintainer-workflow-session.md) exist, but broader examples can continue. | Keep open as umbrella roadmap; link existing examples. |
| #3 | Codex skill installation tutorial | Same scope as #1. | Close as duplicate/completed with the installation doc link. |
| #4 | MCP vs skill distinction | [`codex-extension-boundaries.md`](codex-extension-boundaries.md) directly answers the boundary question. | Close as completed after posting the doc link. |
| #5 | More Chinese Codex workflow examples | Same scope as #2, with newer examples now available. | Keep open only if it tracks additional examples; otherwise deduplicate into #2. |
| #6 | v0.2 maintainer workflow examples | [`maintainer-workflow-session.md`](examples/maintainer-workflow-session.md) covers a multi-skill maintainer session. | Keep open for more real project sessions; add current example as first evidence. |
| #7 | Feedback from Chinese-speaking OSS maintainers | `.github/ISSUE_TEMPLATE/maintainer_workflow_report.md` now gives a structured intake path. | Keep open and ask maintainers to file reports with sanitized evidence. |

## Suggested maintainer replies

### Installation tutorial issues (#1 and #3)

```text
已补充安装文档：docs/codex-skill-installation.md，并在 README 中保留了安装入口。
如果还有 Windows/macOS/Linux 上的具体失败命令或截图，欢迎开一个新的 bug report。
这个 issue 先按已完成关闭。
```

### MCP / skill boundary issue (#4)

```text
已补充说明：docs/codex-extension-boundaries.md。
这份文档区分了 skill、MCP、plugin 和个人设置的适用边界，也给出开源维护场景下的选择建议。
如果你有具体扩展场景，可以继续用 skill_request 模板补一个案例。
```

### Maintainer workflow feedback issue (#7)

```text
已新增 Maintainer workflow report 模板，用来收集真实 OSS 维护场景中的使用反馈。
欢迎用该模板提交：使用的 skill、任务类型、脱敏输入材料、Codex 输出、哪些地方有帮助、哪些地方需要改进。
```

## Next maintenance focus

Do not add more generic examples just to reduce the issue count. The next useful
step is to collect at least one real maintainer workflow report through #7, then
turn any repeated failure pattern into a targeted skill or doc improvement.
