# codex-skills-cn

面向中文用户的 Codex skills 收藏、适配和维护仓库。

这个项目不是简单搬运链接，而是把好用的 Codex skills、开发原则和工具接入方式整理成中文说明，并尽量补齐适用场景、安装方式、使用边界和示例。

## 项目目标

- 收集适合 Codex 的实用 skills 和工作流。
- 将英文说明适配成中文用户容易理解的版本。
- 记录每个 skill 适合做什么、不适合做什么。
- 提供可复制的 `SKILL.md` 模板和目录规范。
- 帮助新用户更安全、更有效地使用 Codex。

## 当前内容

| Skill | 用途 | 状态 |
| --- | --- | --- |
| `karpathy-style-coding` | 小步、直接、可验证的编码原则 | 初版 |
| `scrapling-web-extraction` | 使用 Scrapling 做网页采集、动态页面提取和 AI 友好清洗 | 初版 |

## 目录结构

```text
codex-skills-cn/
  skills/
    skill-name/
      SKILL.md
      README.md
  docs/
    skill-template.md
  CONTRIBUTING.md
  ROADMAP.md
  LICENSE
```

## 使用方式

复制某个 `skills/<name>/SKILL.md` 到你的 Codex skills 目录，或将其中的规则整理进 Codex 个性化设置。

Windows 示例：

```powershell
Copy-Item -Recurse .\skills\karpathy-style-coding C:\Users\<你的用户名>\.codex\skills\
```

## 收录原则

- 优先收录真实可用、维护成本低的 skill。
- 每个 skill 必须说明触发场景、使用边界和验证方式。
- 不收录鼓励绕过访问控制、侵犯隐私或规避网站规则的内容。
- 不为追热点堆砌空壳 skill。

## 许可证

本仓库使用 MIT License。引用、改写或适配第三方内容时，请保留原始来源和许可证说明。
