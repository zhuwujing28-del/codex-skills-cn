# Sample Output: CI Failure Diagnosis

This is an example output for `github-actions-ci-cn`.

## Input

```text
PR 的 GitHub Actions 挂了。失败 job 是 test，日志最后显示：

Error: Cannot find module '@app/config'
Require stack:
- packages/api/src/server.test.ts

这个 PR 只改了 tsconfig paths 和 package exports。
```

## Expected Maintainer Output

结论：

这更像是配置/模块解析回归，不是随机 CI 问题。PR 修改了 `tsconfig paths` 和 `package exports`，失败日志指向 `@app/config` 无法解析，和改动范围直接相关。

失败位置：

- workflow / job / step：test job
- 关键日志：`Cannot find module '@app/config'`

判断：

- 类型：配置问题 / 代码回归
- 依据：失败模块和 PR 修改的路径解析配置相关

建议动作：

1. 本地运行失败 job 对应的 test 命令，确认能复现。
2. 检查 `tsconfig.json`、package `exports`、test runner alias 配置是否一致。
3. 补一个覆盖 `@app/config` import 的测试或 smoke check。
4. 修复前不建议合并。

本地验证：

- 已运行：未提供本地执行证据
- 未运行：完整 CI matrix

给贡献者的回复：

这个失败看起来和本 PR 的路径解析改动有关，不像 flaky test。请先确认 test runner 中 `@app/config` 的 alias / exports 配置是否仍然生效，并在本地跑一次失败的 test job。修复后我们可以重新跑 CI。
