# Sample Output: Security Advisory Triage

This is an example output for `security-advisory-triage-cn`.

## Input

```text
有人在公开 issue 里说登录 token 校验可能能被绕过，并贴了复现步骤。
请判断影响并帮我回复。
```

## Expected Maintainer Output

结论：

- 影响：unknown，需要私密 triage
- 严重度：potentially high

依据：

- 报告涉及 token 校验绕过，属于认证边界。
- 当前信息出现在公开 issue，继续公开讨论可能泄露利用细节。
- 需要先确认受影响版本、代码路径和复现条件。

受影响范围：

- package / module：认证或 token 校验模块，待确认
- versions：待确认
- reachable path：登录态校验路径，待确认

建议动作：

1. 立即请报告者转到私密安全渠道。
2. 临时编辑或隐藏公开 issue 中的可利用细节。
3. 在私密渠道收集最小复现、版本、环境和影响范围。
4. 维护者本地复现并补回归测试。
5. 修复后准备安全公告和 patch release。

公开沟通建议：

感谢报告。这个问题可能涉及认证安全边界，我们不适合在公开 issue 中继续讨论复现细节。请通过项目安全披露渠道继续沟通；我们会在私密渠道确认影响范围，并在修复后发布说明。

不能公开的信息：

- 复现步骤
- token 样例
- 绕过条件
- 未修复代码路径
