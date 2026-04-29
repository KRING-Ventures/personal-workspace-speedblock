# Personal Workspace Speedblock

The **Personal Workspace** Speedblock — the standardised AI-native work environment for KRING Ventures and the companies KRING builds.

A Speedblock ships as two layers:

- **Skill layer** — machine-actionable, loaded by an agent to do the work.
- **Human layer** — deliverables for human eyes (playbook, onboarding guide, role spec) and for human hands (people who run parts of the setup).

Both layers live in this repo.

## Skill layer

| File / folder | What it is |
|---|---|
| [`SKILL.md`](./SKILL.md) | Skill entry point — how an agent provisions a new user on Personal Workspace. |
| [`agent-files/`](./agent-files) | Skill payload — shared OpenClaw framework + per-user blueprints deployed into each user's agent runtime. |

## Human layer

| File | What it is |
|---|---|
| [`playbook.md`](./playbook.md) | Operating manual for Personal Workspace — tool stack, what your assistant does, working rhythm. |
| [`best-practice.md`](./best-practice.md) | The four working practices for getting good output from an agent and not losing work. |
| [`terms.md`](./terms.md) | Must-know vocabulary (branch, pull request, merge, etc.) for working with agents and teammates. |
| [`onboarding.md`](./onboarding.md) | Setup flow — three steps (venture activates → KRING deploys → venture finishes onboarding). |
| [`human-roles.md`](./human-roles.md) | Who does what — the venture, KRING, the user. |
| [`CHANGELOG.md`](./CHANGELOG.md) | What changed per version — product history and migration pointers. |

## Versioning

Semver: `MAJOR.MINOR.PATCH`. Pre-`1.0.0` is the beta phase.

- `main` is the single source of truth. All changes land here.
- Each shipped version is a git tag (`v0.1.0`, `v0.2.0`, …). GitHub's Releases page lists them.
- `CHANGELOG.md` records one entry per version (Keep-a-Changelog format).
- `agent-files/onboarding/STATE_VERSION` records the framework's current version. Each user's assistant keeps its own `STATE_VERSION` and catches up when behind.
- `agent-files/onboarding/MIGRATIONS/<from>-to-<to>.md` — written only when a version changes the shape of per-user state. Pure framework updates (new wording, new templates, new capabilities) don't need a migration.

**Shipping a new version:** update `CHANGELOG.md`, bump `STATE_VERSION`, `git tag v<x.y.z>`, push tag. That's it — no folder copies.

## Current version

**`0.3.0`** — shipped 2026-04-29. See [`CHANGELOG.md`](./CHANGELOG.md).

**Next:** `1.0.0` — target is the framework being stable enough to recommend for general venture deployments without KRING hand-holding.

## Repos involved

- **This repo** (`personal-workspace-speedblock`, public) — skill + human deliverables for Personal Workspace.
- **Shared skills** (`claw-shared`, private) — other OpenClaw skills loaded on demand.
- **Per-user state** — each assistant's `IDENTITY`, `USER`, `TOOLS`, `automations/`, `MEMORY`, `memory/`, `STATE_VERSION` live on the runtime's local filesystem, seeded from the per-user blueprints in this repo at deployment. There is no per-user GitHub repo for state; the assistant doesn't push state back to GitHub.

## Agent layer

**Personal OpenClaw assistant** — one per user. Telegram surface. Built from this repo's `agent-files/` + the runtime's local per-user state.
