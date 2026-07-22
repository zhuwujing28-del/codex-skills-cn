# codex-skills-cn

[![validate](https://github.com/zhuwujing28-del/codex-skills-cn/actions/workflows/validate.yml/badge.svg)](https://github.com/zhuwujing28-del/codex-skills-cn/actions/workflows/validate.yml)

面向中文用户的 Codex skills 收藏、适配和维护仓库。

这个项目不是简单搬运链接，而是把好用的 Codex skills、开发原则和工具接入方式整理成中文说明，并尽量补齐适用场景、安装方式、使用边界和示例。

很多中文开发者已经开始用 Codex 参与开源维护、代码审查、issue triage、文档整理和自动化开发，但高质量中文 skill 仍然很少。本仓库希望把这些工作流沉淀为可复用、可审查、可维护的开源资产。

## 项目目标

- 收集适合 Codex 的实用 skills 和工作流。
- 将英文说明适配成中文用户容易理解的版本。
- 记录每个 skill 适合做什么、不适合做什么。
- 提供可复制的 `SKILL.md` 模板和目录规范。
- 帮助新用户更安全、更有效地使用 Codex。
- 帮助中文开源维护者更高效地处理 issue、PR、release 和项目 onboarding。

## 当前内容

| Skill | 用途 | 状态 |
| --- | --- | --- |
| `karpathy-style-coding` | 小步、直接、可验证的编码原则 | 初版 |
| `repo-onboarding-cn` | 陌生仓库入门、架构地图、运行和验证方式整理 | 初版 |
| `pr-review-cn` | 中文 PR/code review，聚焦 bug、回归、测试缺口 | 初版 |
| `issue-triage-cn` | 中文 issue 分类、优先级、标签和维护者回复 | 初版 |
| `github-actions-ci-cn` | 中文 GitHub Actions CI 失败排查和维护者回复 | 初版 |
| `dependency-upgrade-cn` | 中文依赖升级、Dependabot/Renovate PR 风险评估和验证计划 | 初版 |
| `security-advisory-triage-cn` | 中文安全公告、漏洞影响评估和负责任披露 triage | 初版 |
| `context-budget-cn` | 中文 Codex context / token budget 管理和渐进式 skill 设计 | 初版 |
| `release-notes-cn` | 从 commits/PR/diff 生成中文发版说明和升级提示 | 初版 |
| `openai-docs-cn` | 基于 OpenAI 官方资料回答中文 API、模型和 Codex 开发问题 | 初版 |
| `scrapling-web-extraction` | 使用 Scrapling 做网页采集、动态页面提取和 AI 友好清洗 | 初版 |

## 推荐使用路径

如果你刚开始用 Codex 维护项目，可以按这个顺序试：

1. `repo-onboarding-cn`：先让 Codex 读项目，输出项目地图和风险区域。
2. `issue-triage-cn`：把模糊 issue 转成可执行维护动作。
3. `pr-review-cn`：合并前做一次中文 review。
4. `github-actions-ci-cn`：CI 挂掉时定位失败 job、原因和修复动作。
5. `dependency-upgrade-cn`：审查依赖升级和安全升级 PR。
6. `security-advisory-triage-cn`：处理漏洞报告和安全公告。
7. `context-budget-cn`：压缩长上下文，控制 token 和 skill 膨胀。
8. `release-notes-cn`：发版时把技术变更整理成用户能读懂的说明。
9. `karpathy-style-coding`：日常修 bug 和小功能时约束 Codex 小步、直接、可验证。

## 目录结构

```text
codex-skills-cn/
  skills/
    skill-name/
      SKILL.md
      README.md
  scripts/
    validate-skills.py
  docs/
    examples/
      issue-triage-sample.md
      ci-failure-output.md
      security-advisory-output.md
      maintainer-workflow-session.md
    skill-template.md
    codex-skill-installation.md
    release-readiness.md
  CONTRIBUTING.md
  APPLICATION.md
  CHANGELOG.md
  ROADMAP.md
  LICENSE
```

## 维护者工作流示例

- [`issue-triage-cn` sample output](docs/examples/issue-triage-sample.md)
- [`github-actions-ci-cn` sample output](docs/examples/ci-failure-output.md)
- [`dependency-upgrade-cn` sample output](docs/examples/dependency-upgrade-review.md)
- [`release-notes-cn` sample output](docs/examples/release-notes-output.md)
- [`security-advisory-triage-cn` sample output](docs/examples/security-advisory-output.md)
- [`maintainer workflow session`](docs/examples/maintainer-workflow-session.md)

## 使用方式

复制某个 `skills/<name>/SKILL.md` 到你的 Codex skills 目录，或将其中的规则整理进 Codex 个性化设置。

Windows 示例：

```powershell
Copy-Item -Recurse .\skills\karpathy-style-coding C:\Users\<你的用户名>\.codex\skills\
```

更多安装方式见 [`docs/codex-skill-installation.md`](docs/codex-skill-installation.md)。

## 质量检查

本仓库提供一个轻量检查脚本，确保每个 skill 至少包含必要元数据和关键章节：

```powershell
python .\scripts\validate-skills.py
```

检查范围包括：

- `SKILL.md` 是否存在。
- frontmatter 是否包含 `name` 和 `description`。
- 目录名是否与 `name` 一致。
- 是否包含适用场景、边界、工作流、验证方式等基础内容。

## 收录原则

- 优先收录真实可用、维护成本低的 skill。
- 每个 skill 必须说明触发场景、使用边界和验证方式。
- 不收录鼓励绕过访问控制、侵犯隐私或规避网站规则的内容。
- 不为追热点堆砌空壳 skill。
- 对工具类 skill，优先说明合法合规边界、失败模式和验证方法。
- 对开源维护类 skill，优先服务 issue、PR、release、onboarding 等真实协作场景。

## OpenAI Codex for Open Source 申请说明

本仓库计划申请 OpenAI Codex for Open Source 支持。当前维护重点：

- 扩充中文 Codex skill 基础库。
- 建立可审查的 skill 质量标准。
- 提供面向开源维护者的工作流样例。
- 收集真实项目使用反馈，并据此改进 skill。

如果你也是中文开源维护者，欢迎提交 issue，描述你最希望 Codex 帮你处理的维护场景。已经在真实项目中试用过 skill 的维护者，也欢迎通过 [Maintainer workflow report](.github/ISSUE_TEMPLATE/maintainer_workflow_report.md) 反馈可复现的使用证据和改进点。

申请材料草稿见 [`docs/codex-for-oss-application-notes.md`](docs/codex-for-oss-application-notes.md)。更完整的申请说明见 [`APPLICATION.md`](APPLICATION.md)。

## 许可证

本仓库使用 MIT License。引用、改写或适配第三方内容时，请保留原始来源和许可证说明。
