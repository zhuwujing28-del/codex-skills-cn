# Security Policy

`codex-skills-cn` 主要维护 Codex skills、中文说明和示例输出。这个仓库通常不运行线上服务，但仍然可能出现会误导用户、泄露敏感信息或鼓励不安全操作的内容问题。

## Supported Scope

Please report security-sensitive issues when a skill, example, or workflow:

- asks users to paste API keys, cookies, tokens, private logs, or credentials into public issues or prompts;
- recommends bypassing access controls, paywalls, CAPTCHAs, login restrictions, or site terms;
- gives unsafe guidance for dependency upgrades, vulnerability triage, CI secrets, or repository permissions;
- includes an example that accidentally exposes real credentials, private URLs, personal data, or non-redacted logs;
- weakens the stated safety boundaries of a skill in a way that could mislead future Codex runs.

普通文案错误、格式问题和缺少示例可以直接提交 issue 或 PR。涉及密钥、漏洞利用细节、私有日志或未脱敏数据的问题，请先使用私下渠道联系维护者，避免公开贴出敏感内容。

## Reporting

If you find a security-sensitive problem:

1. Open a minimal public issue only if it can be described without secrets or exploit details.
2. If public reporting would expose sensitive data, contact the maintainer privately through the GitHub profile email or another agreed channel.
3. Include the affected file path, the risky instruction, why it is unsafe, and a suggested safer wording if possible.
4. Redact all tokens, cookies, internal hostnames, private repository names, user identifiers, and logs before sharing.

## Maintainer Response

Maintainers should triage security-sensitive reports before ordinary content improvements. A typical response is:

1. confirm whether the issue affects a published skill, example, template, or contribution workflow;
2. remove or rewrite unsafe guidance with the smallest clear change;
3. add or adjust validation, examples, or contribution guidance when the same failure could recur;
4. document the fix in `CHANGELOG.md` when it changes public guidance.

## Non-Goals

This repository does not accept reports that require bypassing third-party access controls, scraping private systems without authorization, publishing exploit payloads, or sharing unredacted private data.
