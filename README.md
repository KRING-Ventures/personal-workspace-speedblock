# Personal Workspace Speedblock

Deliverables for the **Personal Workspace** Speedblock — the standardised AI-native work environment for KRING Ventures and the companies KRING builds.

This repo is the source of truth for every Personal Workspace deliverable: playbook, onboarding, and the shared OpenClaw agent file set.

## What's here

| File / folder | What it is |
|---|---|
| [`playbook.md`](./playbook.md) | The operating manual — what Personal Workspace is, the tech stack, the four AI layers, OpenClaw purpose & capabilities, working rhythm. |
| [`onboarding.md`](./onboarding.md) | How a new user gets onboarded — human setup + agent-led BOOTSTRAP conversation. |
| [`agent-files/`](./agent-files) | Shared OpenClaw framework file set (SOUL, AGENTS, KRING, HEARTBEAT, templates, BOOTSTRAP). |
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

**`0.1.0`** — shipped 2026-04-23. See [`CHANGELOG.md`](./CHANGELOG.md).

**Next:** `1.0.0` — target is the framework being stable enough to recommend beyond KRING.

## Repos involved

- **This repo** (`personal-workspace-speedblock`, public) — playbook, onboarding, shared agent-file framework.
- **Shared skills** (`claw-shared`, private) — OpenClaw skill library loaded on demand.
- **Per-user personal layers** (private, one per user) — each user creates their own private repo for their personal OpenClaw agent's IDENTITY, USER, TOOLS, automations, and memory. Repo name is up to the user.

## Two agent layers at KRING

- **Cosmo** — the shared KRING-org OpenClaw agent. Slack surface. One instance for the organisation.
- **Personal OpenClaw agent** — one per user. Telegram surface. Built from this repo's `agent-files/` + the user's own personal repo.

See `playbook.md` § *The four AI layers* for the full picture (Gemini / Claude / OpenClaw / Cosmo).
