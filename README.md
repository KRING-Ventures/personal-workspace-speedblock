# Personal Workspace Speedblock

The **Personal Workspace** Speedblock — the standardised AI-native work environment for KRING Ventures and the companies KRING builds.

A Speedblock ships as two layers:

- **Agent payload** — `agent-files/`, deployed into each user's OpenClaw runtime as a clean sheet.
- **Human layer** — deliverables for human eyes (playbook, onboarding guide) and for the people who run the setup.

Both layers live in this repo.

## Agent payload

| File / folder | What it is |
|---|---|
| [`agent-files/`](./agent-files) | Shared OpenClaw framework + per-user blueprints, deployed into each user's agent runtime. KRING deploys this by hand, one runtime per user. |

## Human layer

| File | What it is |
|---|---|
| [`buy-in.md`](./buy-in.md) | The case for Personal Workspace — the pains it solves and the value it delivers, for the user and the venture. Start here. |
| [`playbook.md`](./playbook.md) | Operating manual for Personal Workspace — tool stack, what your agent does, working rhythm. |
| [`ai-commandments.md`](./ai-commandments.md) | The 4 AI Commandments — best practices for working with AI agents, plus the must-know vocabulary (branch, pull request, merge, etc.). |
| [`activation.md`](./activation.md) | Activation flow — how a venture gets deployed (provisioning → KRING sets up and wires the agents → access handover). ~5 business days. |
| [`onboarding.md`](./onboarding.md) | User onboarding flow — the agent-led first conversation each user goes through once they get access. ~16 min. |
| [`WRITING.md`](./WRITING.md) | The writing standard every user-facing page must pass — one job, plain, selective, one screen. |
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

**`1.0.0`** — shipped 2026-06-05. First stable release. See [`CHANGELOG.md`](./CHANGELOG.md).

**Next:** `1.1.0` — expanded tech stack, and an Obsidian-based agent brain/filesystem. Cosmica-native agent access is in the pipeline.

## Repos involved

- **This repo** (`personal-workspace-speedblock`, public) — agent payload + human deliverables for Personal Workspace.
- **Shared skills** (`claw-shared`, private) — other OpenClaw skills loaded on demand.
- **Per-user state** — each assistant's `IDENTITY`, `USER`, `TOOLS`, `automations/`, `MEMORY`, `memory/`, `STATE_VERSION` live on the runtime's local filesystem, seeded from the per-user blueprints in this repo at deployment. There is no per-user GitHub repo for state; the assistant doesn't push state back to GitHub.

## Agent layer

**Personal OpenClaw assistant** — one per user. Slack surface. Built from this repo's `agent-files/` + the runtime's local per-user state.
