# Post-v0.1.0 Audit - 2026-07-13

This note records the state of the public `v0.1.0` tag after later readiness work landed on `main`.

## Tag status

- Published tag: `v0.1.0`
- Tag target: `a3c7975` (`Prepare Codex OSS application materials`)
- Current `main` during audit: `1e35073` (`Require skill README files`)
- Latest public validation run checked: `validate` on `1e35073`, successful on 2026-07-11

## Changes after the tag

The current `main` branch includes useful readiness work that is not part of the published `v0.1.0` tag:

- local Markdown link validation,
- maintainer PR template,
- security reporting policy,
- context budget skill,
- Windows installation guide,
- maintainer readiness report,
- CI readiness badge,
- first-release checklist,
- required `README.md` files for every skill package.

## Maintainer decision

Do not move or force-update the existing public `v0.1.0` tag. Treat it as the first application-materials baseline.

Use the current `main` branch as the candidate for a follow-up patch tag, likely `v0.1.1`, after one final validation run and changelog update.

## Recommended next release steps

1. Run `python scripts/validate-skills.py`.
2. Confirm the public `validate` workflow remains green on current `main`.
3. Add a `v0.1.1` changelog entry summarizing post-`v0.1.0` hardening.
4. Create an annotated `v0.1.1` tag from current `main`.
