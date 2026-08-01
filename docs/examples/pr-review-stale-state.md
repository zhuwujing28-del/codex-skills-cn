# Sample Output: PR Review for Stale State

This sample shows the kind of evidence-based Chinese review that
`pr-review-cn` should produce. It uses a fictional settings page and keeps the
finding tied to the changed behavior rather than to formatting preferences.

## Input

```text
PR title: Persist selected repository after switching organizations

The PR adds a repository selector to a settings page. The selected repository
is saved in component state so a user can edit notification settings.

Relevant diff summary:
- `OrganizationSelect` calls `setOrganization(nextOrganization)`.
- `RepositorySelect` keeps `selectedRepository` in local state.
- The save request sends `{ organization, repository: selectedRepository }`.
- The PR adds a test for selecting a repository inside one organization.

Please review this PR before merge and reply in Chinese.
```

## Expected Maintainer Output

```text
Findings:

- [P1] `SettingsForm.tsx:42` - Switching organization can submit a repository from the previous organization
  Impact: `selectedRepository` is not cleared or revalidated when
  `organization` changes. A user can select `org-a/repo-1`, switch to `org-b`,
  and save before choosing a new repository. The request then pairs `org-b`
  with a repository that does not belong to it. Depending on server handling,
  this can create an invalid setting or update the wrong target.
  Suggested fix: reset `selectedRepository` when the organization changes, and
  disable Save until a repository from the current organization is selected.
  Keep the reset next to the organization-change handler so the relationship is
  explicit.

Open questions:
- Does the API reject a repository that is outside the selected organization?
  Client-side reset is still needed for the user-visible state, but the API
  should enforce this relationship as well.

Verification:
- Reviewed: the changed state flow and the existing single-organization test.
- Add a regression test: select a repository in `org-a`, switch to `org-b`,
  then assert that Save is disabled or that the request cannot contain
  `org-a/repo-1`.
- Not run: the project test suite was not included in the supplied PR context.

Maintainer reply:

感谢这个改动。这里有一个需要在合并前处理的状态回归：用户在 `org-a`
选择仓库后切换到 `org-b`，当前实现仍可能把旧仓库带进保存请求。请在切换组织时
清空或重新校验已选仓库，并补一个“切换组织后不能提交旧仓库”的回归测试。现有测试只
覆盖单个组织内的选择，不能覆盖这个路径。
```

## Why this helps application readiness

- It shows a real behavioral finding with a precise state transition and merge
  condition.
- It separates inspected evidence, required regression coverage, and work that
  was not run.
- It gives Chinese-speaking maintainers a concise review comment they can adapt
  without inventing low-value findings.
