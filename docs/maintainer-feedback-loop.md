# Maintainer Feedback Loop

This note explains how `codex-skills-cn` turns real maintainer feedback into
small, reviewable repository improvements instead of letting issue templates
collect dust.

## When to use this

Use this workflow after receiving any of the following:

- a filled [`maintainer_feedback_request`](../.github/ISSUE_TEMPLATE/maintainer_feedback_request.md) issue,
- a filled [`maintainer_workflow_report`](../.github/ISSUE_TEMPLATE/maintainer_workflow_report.md) issue,
- a discussion thread with concrete maintainer pain points,
- or a direct reproducible report from a Chinese-speaking OSS maintainer.

## Goal

For each actionable feedback item, decide which artifact should change:

- a skill,
- a sample output,
- a companion eval in `agent-evals-cn`,
- installation or boundary docs,
- or a public roadmap / release-readiness note.

The important part is to preserve evidence and keep the change scoped.

## Triage steps

1. **Confirm the maintainer scenario**
   - Record the repository type, task type, and what the maintainer was trying to finish.
   - Separate "feature wish" from "existing workflow failed here".

2. **Extract the smallest reproducible evidence**
   - Keep only the issue text, PR excerpt, CI log, diff, or prompt snippet needed to explain the problem.
   - Remove secrets, private URLs, tokens, proprietary code, and unpublished vulnerability details.

3. **Classify the gap**

   | Gap type | Preferred change |
   | --- | --- |
   | Skill trigger too vague | Tighten `SKILL.md` trigger / non-use cases |
   | Output misses maintainer evidence | Add or revise a sample output |
   | Problem should stay fixed | Add a companion eval in `agent-evals-cn` |
   | Users do not know where to start | Improve README / installation / boundary docs |
   | Request is larger than one patch | Add a dated roadmap or triage note |

4. **Choose one bounded follow-up**
   - Prefer one small or medium patch.
   - Do not mix unrelated skill rewrites just because the issue mentions several frustrations.

5. **Link the evidence**
   - In the PR or commit message, name the issue number or dated note.
   - In the changed doc, say whether the artifact is based on observed maintainer feedback or maintainer inference.

6. **Validate**
   - Run `python scripts/validate-skills.py` in `codex-skills-cn`.
   - If a new eval artifact is added in `agent-evals-cn`, also run `python scripts/validate.py` there.

7. **Close the loop publicly**
   - Reply with what changed, what was intentionally not changed, and what evidence would help next.
   - If the report stays open, leave a crisp next-step question rather than a generic thank-you.

## Decision rules

- Prefer sample outputs when the skill is correct but maintainers need to see the shape of a good answer.
- Prefer companion evals when a failure mode could regress silently.
- Prefer README or installation docs when multiple issues point to the same discoverability problem.
- Prefer no change when the report has no reproducible evidence yet; ask for the missing artifact first.

## Suggested evidence labels

When writing follow-up notes, tag the source of the conclusion:

- **Observed**: came from a real issue, PR, CI log, or usage report.
- **Maintainer inference**: a reasonable conclusion drawn from the observed report.
- **Not yet verified**: a plausible request that still needs a reproducible example.

## Minimal follow-up checklist

- [ ] Original maintainer scenario is named
- [ ] Sensitive data is removed
- [ ] Chosen artifact type is explicit
- [ ] Validation command output is recorded
- [ ] Public reply or changelog note points back to the evidence

## Why this helps OSS readiness

- It shows that feedback collection is connected to maintenance, not just intake.
- It makes future application evidence easier to inspect.
- It gives `agent-evals-cn` a clear source for realistic new eval cases.
