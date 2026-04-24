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
| [`playbook.md`](./playbook.md) | Operating manual for Personal Workspace — tool stack, four AI helpers, what the OpenClaw agent does, working rhythm. |
| [`onboarding.md`](./onboarding.md) | Setup flow — human-led provisioning (accounts, private repo, runtime) + handoff to agent-led BOOTSTRAP. |
| [`human-roles.md`](./human-roles.md) | Who operates what — account provisioner, runtime operator, framework maintainer, user. |
| [`CHANGELOG.md`](./CHANGELOG.md) | What changed per version — product history and migration pointers. |

## Versioning

Semver: `MAJOR.MINOR.PATCH`. Pre-`1.0.0` is the beta phase.

- `main` is the single source of truth. All changes land here.
- Each shipped version is a git tag (`v0.1.0`, `v0.2.0`, …). GitHub's Releases page lists them.
- `CHANGELOG.md` records one entry per version (Keep-a-Changelog format).
- `agent-files/onboarding/STATE_VERSION` records the framework's current version. Each user's OpenClaw agent keeps its own `STATE_VERSION` at the root of their private repo and catches up when behind.
- `agent-files/onboarding/MIGRATIONS/<from>-to-<to>.md` — written only when a version changes the shape of per-user state. Pure framework updates (new wording, new templates, new capabilities) don't need a migration.

**Shipping a new version:** update `CHANGELOG.md`, bump `STATE_VERSION`, `git tag v<x.y.z>`, push tag. That's it — no folder copies.

## Current version

**`0.2.0`** — shipped 2026-04-24. See [`CHANGELOG.md`](./CHANGELOG.md).

**Next:** `1.0.0` — target is the framework being stable enough to recommend beyond KRING.

## Repos involved

- **This repo** (`personal-workspace-speedblock`, public) — skill + human deliverables for Personal Workspace.
- **Shared skills** (`claw-shared`, private) — other OpenClaw skills loaded on demand.
- **Per-user personal layers** (private, one per user) — each user creates their own private repo for their personal OpenClaw agent's IDENTITY, USER, TOOLS, automations, and memory. Repo name is up to the user.

## Two agent layers at KRING

- **Cosmo** — the shared KRING-org OpenClaw agent. Slack surface. One instance for the organisation.
- **Personal OpenClaw agent** — one per user. Telegram surface. Built from this repo's `agent-files/` + the user's own personal repo.

See `playbook.md` § *The four AI helpers* for the full picture (Gemini / Claude / OpenClaw / Cosmo).
