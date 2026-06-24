# Codex for Open Source 申请材料草稿

这份文档用于整理本仓库申请 OpenAI Codex for Open Source 时可复用的信息。提交申请前请根据当时的官方表单要求调整措辞。

## 项目简介

`codex-skills-cn` 是一个面向中文开发者和开源维护者的 Codex skills 仓库。项目目标是把真实可用的 Codex 工作流整理成中文、可安装、可审查、可维护的 skills，降低中文用户使用 Codex 参与开源维护的门槛。

## 为什么需要 Codex 支持

中文开发者正在快速采用 Codex，但高质量中文 skill 资源仍然分散，很多用户不知道如何安全地让 Codex 做 repo onboarding、issue triage、PR review、release notes、OpenAI API 查询和网页数据提取。

本项目希望把这些工作流沉淀成开源资产，并通过真实项目反馈不断改进。

## 当前成果

- 已建立 MIT 开源仓库。
- 已提供 7 个初版 skills：
  - `karpathy-style-coding`
  - `repo-onboarding-cn`
  - `issue-triage-cn`
  - `pr-review-cn`
  - `release-notes-cn`
  - `openai-docs-cn`
  - `scrapling-web-extraction`
- 已提供贡献指南、路线图、安装文档和 skill 模板。
- 已提供 `scripts/validate-skills.py`，用于检查 skill 元数据和基础结构。

## 对开源社区的价值

- 帮助中文维护者更高效地处理 issues、PRs、release notes 和项目文档。
- 帮助新贡献者更快理解陌生仓库，减少维护者重复答疑成本。
- 提供中文安全边界说明，降低错误使用 agent 的风险。
- 为更多第三方 Codex skills 提供中文适配和质量检查范式。

## 未来 3 个月计划

1. 增加 10-15 个中文 Codex skills，覆盖 GitHub 维护、测试、调试、前端验证、后端排错、文档生成和 API 接入。
2. 为每个 skill 补充真实使用示例。
3. 收集中文开发者反馈，建立 skill 质量评分标准。
4. 增加 CI 检查，确保 PR 中新增 skill 结构完整。
5. 整理一篇中文 Codex 开源维护工作流指南。

## 可衡量指标

- skills 数量和质量检查通过率。
- issues / PRs / discussions 中的真实使用反馈。
- README 安装路径是否清晰。
- 中文开发者是否能直接复制使用并成功完成维护任务。

## 申请时可强调的一句话

This project helps Chinese-speaking open-source maintainers use Codex safely and effectively by turning recurring maintainer workflows into reviewed, reusable, Chinese Codex skills.
