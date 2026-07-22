# Sample Output: Release Notes Draft

This sample shows the kind of maintainer-facing output `release-notes-cn`
should produce from a small but real-looking release diff. It focuses on user
impact, upgrade actions, and evidence traceability rather than rewriting raw
commit messages.

## Input

```text
请根据下面这些已合并变更，整理 `v0.1.2` 中文 release notes：

- feat: add maintainer workflow usage-report issue template
- docs: add public issue triage note for open GitHub issues
- docs: add dependency upgrade review sample output
- fix: clarify `v0.1.0` vs `v0.1.1` release note wording

要求：
1. 用中文输出
2. 按“新增 / 改进 / 升级说明”组织
3. 不要把内部提交信息原样贴给用户
4. 如果某条结论是推断，请明确写“根据变更推断”
```

## Expected Maintainer Output

```text
## v0.1.2

### 新增
- 新增维护者工作流反馈 issue 模板，方便在真实开源项目里收集可复现的使用场景、问题证据和下一步改进建议。
- 新增依赖升级审查示例，展示如何基于 CI 结果、上游变更说明和最小验证步骤判断是否合并 Dependabot / Renovate PR。

### 改进
- 补充公开 issue 梳理说明，帮助维护者把“安装教程”“工作流示例”“MCP 与 skill 边界”等历史问题对应到已经发布的文档和建议动作。
- 修正版本说明中的措辞，明确 `v0.1.0` 是首个公开标签，后续硬化内容由 `v0.1.1` 补充承接，避免读者误解标签范围。

### 升级说明
- 本次发布以文档和维护流程增强为主，不涉及 skill 安装结构变化。
- 已经在使用现有 skills 的用户通常不需要修改本地目录，只需要按需查看新增示例和维护说明。
- 根据变更推断：如果你正在准备公开申请材料或维护者工作流证据，这个版本更适合作为引用依据，因为它补齐了反馈收集、issue 对齐和依赖升级审查样例。
```

## Why this helps application readiness

- It gives `release-notes-cn` a concrete maintainer artifact, not just a skill definition.
- It shows Codex translating raw repo history into user-facing release communication.
- It reinforces that this repo covers end-to-end OSS maintenance, including how shipped work is explained publicly.
