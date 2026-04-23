# Personal Workspace Speedblock

Deliverables for the **Personal Workspace** Speedblock — the standardised AI-native work environment for KRING Ventures and the companies KRING builds.

This repo is the source of truth for every Personal Workspace deliverable: playbook, onboarding, and the shared OpenClaw agent file set. Versioned as a living root with frozen release snapshots.

## What's here

| File / folder | What it is |
|---|---|
| [`playbook.md`](./playbook.md) | The operating manual — what Personal Workspace is, the tech stack, the four AI layers, OpenClaw purpose & capabilities, working rhythm. |
| [`onboarding.md`](./onboarding.md) | How a new user gets onboarded — human setup + agent-led BOOTSTRAP conversation. |
| [`agent-files/`](./agent-files) | Shared OpenClaw framework file set (SOUL, AGENTS, KRING, HEARTBEAT, templates, BOOTSTRAP). The **living** version — evolves continuously. |
| [`releases/`](./releases) | Frozen snapshots of prior releases. Archive only — not active deployment targets. |
| [`CHANGELOG.md`](./CHANGELOG.md) | What changed per release. |

## Versioning model

**Living root + frozen release snapshots.**

- Root = the one living source of truth. We evolve it continuously. New users always onboard from root (latest).
- `releases/<version>/` = immutable snapshots cut at release milestones. Historical record, not deployment targets.
- Git tags (`v0.1-beta`, `v1.0`, …) back the snapshots so the history is clean.

When we cut the next version, we copy the current root state into `releases/<version>/` and tag it.

## Current version

**beta** (shipped 2026-04-23). Frozen snapshot in [`releases/beta/`](./releases/beta). See [`CHANGELOG.md`](./CHANGELOG.md) for what's in it.

**Next:** 1.0.

## Repos involved

- **This repo** (`personal-workspace-speedblock`, public) — playbook, onboarding, shared agent-file framework, release snapshots.
- **Shared skills** (`claw-shared`, private) — OpenClaw skill library loaded on demand.
- **Per-user personal layers** (private, one per user) — each user creates their own private repo for their personal OpenClaw agent's IDENTITY, USER, TOOLS, automations, and memory. Repo name is up to the user.

## Two agent layers at KRING

- **Cosmo** — the shared KRING-org OpenClaw agent. Slack surface. One instance for the organisation.
- **Personal OpenClaw agent** — one per user. Telegram surface. Built from this repo's `agent-files/` + the user's own personal repo.

See `playbook.md` § *The four AI layers* for the full picture (Gemini / Claude / OpenClaw / Cosmo).
