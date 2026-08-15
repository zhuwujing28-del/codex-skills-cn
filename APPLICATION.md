# Codex for Open Source Application Notes

This repository is an early-stage but actively maintained Chinese Codex skills collection for open-source maintainers.

## One-line summary

`codex-skills-cn` helps Chinese-speaking open-source maintainers use Codex for real maintainer workflows: repository onboarding, issue triage, bug reproduction, PR review, CI failure diagnosis, dependency upgrades, security advisory triage, release notes, OpenAI docs assistance, and safe web extraction.

## Why this project matters

Many Chinese-speaking developers are beginning to use Codex, but high-quality Chinese skills for open-source maintenance are still scarce. Existing examples often focus on generic prompting rather than repeatable maintainer workflows.

This project turns recurring OSS maintainer work into reviewed, reusable Codex skills with:

- clear trigger conditions,
- explicit non-use cases,
- verification steps,
- safety boundaries,
- and Chinese output expectations.

## Maintainer workflows covered

- Repository onboarding for new contributors.
- Issue triage and maintainer replies.
- Bug report minimization and reproduction evidence.
- Pull request review focused on bugs, regressions, and tests.
- GitHub Actions CI failure diagnosis.
- Dependency upgrade and Dependabot/Renovate PR review.
- Security advisory triage and responsible disclosure.
- Release notes and upgrade guidance.
- OpenAI developer docs assistance using official sources.
- Lawful web extraction boundaries.
- Small, verified coding changes.

## How Codex helps this project

Codex is used to:

- draft and refine skills,
- run structure validation,
- add regression examples,
- maintain changelog and release readiness notes,
- evaluate skills through `agent-evals-cn`,
- and improve repository documentation.

## Current status

- 12 maintainer-oriented skills.
- Validation script and GitHub Actions workflow.
- Changelog and release readiness notes.
- Sample maintainer workflow outputs.
- Skill / MCP / plugin boundary guide.
- Companion eval repository: `agent-evals-cn`.

## Application packet checklist

Before submitting the OSS application, keep the packet small and explicit:

- one-sentence project summary and maintainer audience,
- current skill list and the maintainer workflows covered,
- validation evidence (`python scripts/validate-skills.py` plus the CI badge),
- release or readiness notes and any post-release audit links,
- one or two representative examples or workflow reports,
- a short note on current scope limits.

If reviewers ask for the project's main differentiator, point to the fact that
this repo turns recurring maintainer work into Chinese, reusable, validated
skills with a companion eval loop in `agent-evals-cn`.

## Why support would help

The maintainer relies on Codex-assisted workflows to keep the project moving. ChatGPT Pro access would make it easier to continue:

- improving Chinese Codex skill quality,
- reviewing and evaluating skills,
- responding to issues,
- preparing releases,
- and documenting repeatable workflows for other Chinese-speaking OSS maintainers.

## Honest scope

This is an early-stage project. It is not yet a widely adopted ecosystem project. The value is in its focused niche and active maintenance: building reusable Chinese Codex skills for open-source maintainers.
