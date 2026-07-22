# Sample Output: Dependency Upgrade Review

This sample shows the kind of maintainer-facing output `dependency-upgrade-cn`
should produce for a routine dependency PR. It stays grounded in evidence,
validation, and merge criteria rather than vague "looks safe" advice.

## Input

```text
仓库收到一个 Dependabot PR：

- package: `fast-glob`
- from: `3.3.1`
- to: `3.3.3`
- diff: `package.json` 和 `pnpm-lock.yaml`

CI 里 unit tests 通过，但 `docs-build` job 比平时慢了 20%。

请判断要不要合并，并给出维护者回复草稿。
```

## Expected Maintainer Output

```text
结论：先 hold，补一个针对 `docs-build` 变慢的最小验证，再决定是否合并。

判断依据：
- 这是 patch upgrade，表面风险低于 major/minor，但不能只看版本号。
- diff 目前只涉及 `package.json` 和 lockfile，没有直接代码改动，说明风险主要在传递依赖、文件匹配行为或构建性能。
- unit tests 通过是正信号，但 `docs-build` 慢 20% 说明已经出现可观察回归，需要确认是偶发波动还是升级引入。

建议检查：
1. 查看 upstream release notes / changelog，确认 `3.3.2` 和 `3.3.3` 是否涉及 glob 行为、symlink、ignore 规则或性能修复。
2. 对比 PR 前后的 `docs-build` 日志，确认变慢发生在依赖安装、站点生成，还是某个使用 `fast-glob` 的步骤。
3. 本地或 CI 复跑一次 `docs-build`，记录耗时和关键命令，避免因为单次 runner 抖动误判。
4. 如果仓库有直接调用 `fast-glob` 的脚本， spot check 一条典型命令，确认输出文件数和关键路径没有变化。

合并条件：
- changelog 没有 breaking / behavior-sensitive 提示；
- `docs-build` 复跑后恢复正常，或能证明 20% 波动与本 PR 无关；
- 依赖安装、测试、文档构建结果都可复现。

建议维护者回复：

感谢这个升级 PR。当前版本变更看起来是 patch 级别，`package.json` 和 lockfile 之外也没有额外改动，所以基础风险不高。不过现有 CI 显示 `docs-build` 比平时慢了大约 20%，我想先确认这是不是单次波动，避免把潜在性能回归一起合并。

下一步我会：
1. 看一下 upstream changelog；
2. 复跑一次 `docs-build`；
3. 如果仓库里有直接使用 `fast-glob` 的脚本，再补一个 spot check。

如果这些检查都正常，我会继续推进合并；如果性能回归可复现，会先 hold 并补记录。
```

## Why this helps application readiness

- It gives reviewers a concrete artifact for `dependency-upgrade-cn`, not just a skill description.
- It shows Codex helping with a common maintainer workflow that mixes changelog reading, CI interpretation, and bounded verification.
- It models a realistic "hold pending evidence" decision instead of overconfident auto-merge behavior.
