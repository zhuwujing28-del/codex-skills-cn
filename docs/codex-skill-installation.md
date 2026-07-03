# Codex Skill 安装教程

本文面向刚开始使用 Codex 的中文用户，说明如何安装和使用本仓库中的 skills。

## 什么是 Codex skill

Codex skill 是一组可复用的本地说明文件，通常以 `SKILL.md` 形式存在。

它可以告诉 Codex：

- 什么时候使用某种工作流
- 执行任务时遵守哪些步骤
- 需要注意哪些安全边界
- 如何验证结果

skill 更像是“专项工作说明”，不是普通聊天提示词。

## 安装位置

在 Windows 上，Codex skills 通常放在：

```text
C:\Users\<你的用户名>\.codex\skills
```

如果你不确定 Codex home 目录在哪里，可以先在 PowerShell 中查看：

```powershell
if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE ".codex" }
```

## 安装单个 skill

从仓库根目录运行：

```powershell
$target = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $env:USERPROFILE ".codex\skills" }
New-Item -ItemType Directory -Force $target | Out-Null
Copy-Item -Recurse -Force .\skills\issue-triage-cn (Join-Path $target "issue-triage-cn")
```

安装后，目录结构应该类似：

```text
C:\Users\<你的用户名>\.codex\skills\issue-triage-cn\SKILL.md
```

## 安装多个 skills

如果你想一次复制本仓库所有 skills：

```powershell
$target = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills" } else { Join-Path $env:USERPROFILE ".codex\skills" }
New-Item -ItemType Directory -Force $target | Out-Null
Copy-Item -Recurse -Force .\skills\* $target
```

## 更新已有 skill

重新执行 `Copy-Item -Recurse -Force` 即可覆盖旧版本。更新前如果你改过本地 `SKILL.md`，请先备份自己的改动。

## 验证安装

安装后重启 Codex，或开启一个新的 Codex 线程，然后用一个明确触发场景测试。例如：

```text
请用 issue-triage-cn 帮我整理这个 bug issue。
```

如果 Codex 能按该 skill 的工作流输出分类、优先级、维护者回复和后续动作，说明安装路径可用。

## 常见问题

- 找不到目录：先确认 `C:\Users\<你的用户名>\.codex` 是否存在；不存在时可以手动创建。
- 复制后没有生效：重启 Codex 或新开线程，避免旧上下文没有重新读取本地 skills。
- 目录层级多了一层：确认最终路径是 `skills\<skill-name>\SKILL.md`，而不是 `skills\<skill-name>\<skill-name>\SKILL.md`。
- 只想试用一个 skill：优先复制单个目录，不必复制整个仓库。
