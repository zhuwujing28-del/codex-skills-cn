# issue-triage-cn sample output

This sample shows the kind of concrete maintainer-facing artifact `issue-triage-cn`
should produce. It uses a fictional issue so the example can be copied into
tests, docs, or review notes without exposing private project data.

## Input issue

```text
Title: Windows install command fails when the user name contains Chinese characters

Body:
I followed the README command:

Copy-Item -Recurse .\skills\karpathy-style-coding C:\Users\<user>\.codex\skills\

On Windows 11, PowerShell returns "Cannot find path" when my user folder is
C:\Users\康康. I am not sure whether this is a Codex problem or a docs problem.
```

## Triage result

```text
分类：docs / usability
优先级：P2，因为安装路径问题会阻塞新用户试用，但不影响已安装用户。
状态：ready
建议 labels：docs, windows, good-first-issue

判断依据：
- issue 给出了操作系统、执行命令、失败信息和触发条件。
- 问题集中在 README 示例路径，而不是 skill 逻辑或 Codex 运行时。
- 失败条件是中文 Windows 用户名，属于中文用户高概率遇到的安装边界。

建议回复：
感谢反馈。这个更像是安装文档的 Windows 路径示例问题，而不是 Codex skill 本身的问题。
我们会把 README 中的硬编码 `C:\Users\<user>\.codex\skills\` 示例改成基于
`$HOME` 或 `$env:USERPROFILE` 的写法，并补充中文用户名路径的说明。

下一步：
1. 在 README 和安装文档中把 Windows 示例改为：
   `Copy-Item -Recurse .\skills\karpathy-style-coding "$HOME\.codex\skills\"`
2. 补充一句说明：如果路径包含空格或非 ASCII 字符，请用引号包住目标路径。
3. 修改后在 Windows PowerShell 中手动跑一次命令并记录验证结果。
```

## Why this is a good triage output

- It separates a documentation bug from a runtime bug.
- It names the exact missing verification: rerun the command on Windows.
- It gives a maintainer-ready reply instead of only assigning labels.
- It keeps the next step small enough for a first-time contributor.
