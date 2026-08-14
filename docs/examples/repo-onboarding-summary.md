# Sample Output: Repository Onboarding Summary

This sample shows the kind of concise Chinese repo map `repo-onboarding-cn`
should produce for a maintainer who just entered an unfamiliar project.

## Input

```text
请先帮我快速熟悉这个仓库：
- 说明它是做什么的
- 识别技术栈和主要目录
- 标出我今天最应该先看的文件
- 提醒我有哪些风险区
- 给出我接下来 3 步该做什么

你可以根据仓库结构、README、脚本和文档来判断，但不要编造没有看到的内容。
```

## Expected Maintainer Output

```text
项目一句话：这是一个面向中文用户的 Codex skills 维护仓库，重点是把常见维护工作流沉淀成可复制的 skill、示例和校验脚本。

技术栈：
- 主要内容是 Markdown 文档和 skill 目录
- 校验脚本是 Python
- 通过 GitHub Actions 做结构验证
- 面向 Windows 用户提供了安装与使用示例

主要目录：
- `skills/`：每个 skill 的 `SKILL.md` 和 `README.md`
- `docs/examples/`：可复用的维护者示例输出
- `docs/`：安装、边界、评分、发布和维护说明
- `scripts/`：本地校验脚本
- `.github/`：Issue 模板和 CI 配置

今天先看这几个文件：
1. `README.md`：先确认仓库目标和推荐使用路径
2. `skills/repo-onboarding-cn/SKILL.md`：看入门 skill 的触发、边界和输出格式
3. `docs/example-index.md`：看已有示例覆盖了哪些维护场景
4. `scripts/validate-skills.py`：看仓库如何定义“结构有效”
5. `docs/maintainer-feedback-loop.md`：看真实反馈如何变成下一步改进

风险区：
- 文档类仓库最容易出现“看起来很多，但入口不清楚”的问题
- 示例输出如果没有标明证据，容易变成空泛建议
- 新增 example 时要同步更新索引，否则验证会失效
- 面向公开维护者的模板要避免含糊边界和不可复用措辞

建议下一步：
1. 先跑一遍 `python scripts/validate-skills.py`
2. 按 `docs/example-index.md` 检查哪些场景已经覆盖，哪些还缺
3. 选一个最常见的维护场景，补一个小而真实的示例输出
```

## Why this helps application readiness

- It gives `repo-onboarding-cn` a concrete maintainer-facing artifact.
- It shows how the skill turns a first pass over the repo into a useful map.
- It reinforces that onboarding output should stay short, evidence-based, and
  ready for follow-up work.
