# Sample Output: Maintainer Workflow Session

This sample shows how several Chinese Codex skills can be chained in one realistic
open-source maintainer session. It is intentionally small: the goal is to show the
handoff between skills, not to invent a large automation system.

## Input

```text
我是一个 TypeScript CLI 项目的维护者，今天只有 45 分钟。

当前有 3 件事：

1. 有用户反馈 Windows 安装文档看不懂。
2. Dependabot 开了一个 minor upgrade PR。
3. main 分支的 release workflow 因 npm provenance 报错失败。

请帮我排优先级、安排处理顺序，并给出可以直接贴到 issue/PR 的维护者回复草稿。
```

## Expected Maintainer Output

建议先处理 release workflow，再处理 Windows 文档 issue，最后审查 Dependabot PR。

原因：

1. `github-actions-ci-cn`：release workflow 失败会阻断发布，且 provenance 错误通常需要先看 workflow、权限和 npm 发布配置。
2. `issue-triage-cn`：Windows 文档问题影响新用户安装，但可以先用标签、复现信息和短回复稳定预期。
3. `dependency-upgrade-cn`：minor upgrade PR 需要看 changelog、lockfile 和测试结果，风险通常低于发布阻断。
4. `release-notes-cn`：如果 release workflow 修复需要补发 patch release，可在最后整理用户可读说明。

45 分钟安排：

| 时间 | 动作 | 产出 |
| --- | --- | --- |
| 0-15 分钟 | 查看失败的 release job、定位 npm provenance 报错 | 失败原因、修复假设、需要验证的命令 |
| 15-25 分钟 | 回复 Windows 安装文档 issue | labels、复现请求、临时解决步骤 |
| 25-40 分钟 | 审查 Dependabot diff、changelog、测试结果 | merge / hold 决策和验证清单 |
| 40-45 分钟 | 汇总当天维护状态 | issue/PR 回复草稿和下一步 |

可贴回复草稿：

```text
感谢反馈。我会先补一段 Windows 安装路径说明，重点区分 `$HOME`、`$env:USERPROFILE` 和 Codex skills 目录。为了确认问题范围，麻烦补充一下：Codex 版本、PowerShell 版本、你执行的复制命令，以及报错截图或完整错误文本。
```

```text
这个 release workflow 失败看起来和 npm provenance / OIDC 发布配置有关。我会先检查 workflow permissions、npm publish 参数和 tag 触发条件；修复后会贴出本地验证和 GitHub Actions run 链接。
```

```text
Dependabot 这个 minor upgrade 我会按普通依赖升级处理：先看 upstream changelog 和 breaking-change 提示，再跑现有测试。如果 lockfile 是唯一变更且 CI 通过，可以合并；如果运行时依赖或 peer dependency 有变化，会先 hold 并补测试说明。
```

检查清单：

- issue triage 是否给出标签、复现信息和下一步负责人；
- CI 诊断是否引用失败 job、关键日志和验证命令；
- 依赖升级是否检查 changelog、lockfile、runtime impact 和 peer dependency；
- session 是否保留时间边界，没有承诺一次完成所有维护工作。

## Why this helps application readiness

- It shows Codex as a maintainer assistant across issue, CI, dependency, and release work.
- It demonstrates bounded timeboxing instead of vague "do everything" automation.
- It gives reviewers a concrete artifact for how the skills help Chinese OSS maintainers.
- It creates a realistic example for roadmap item `v0.2 maintainer workflow examples`.
