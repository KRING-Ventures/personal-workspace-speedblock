# CHANGELOG

All notable changes to the Personal Workspace framework are recorded here, newest first. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); version numbers follow [semver](https://semver.org/) (`MAJOR.MINOR.PATCH`, pre-`1.0.0` is beta).

Each entry lists what changed, and — when a version changes the shape of per-user state — points at the `agent-files/onboarding/MIGRATIONS/<from>-to-<to>.md` file an OpenClaw agent runs to catch up.

The current framework version lives in `agent-files/onboarding/STATE_VERSION`. Each OpenClaw agent's repo records its last-synced version in its own `STATE_VERSION` file at the repo root. The session-boot rule in `agent-files/AGENTS.md` describes how the comparison and catch-up runs.

---

## [0.1.1] — 2026-04-24

Cleanup pass: strip dead references, orphan placeholders, and schema drift. No per-user state changes.

### Changed
- `IDENTITY.md` — hardcoded vibe and emoji (🚀); removed unused `{{ORG}}` and `{{AGENT_AVATAR_PATH_OR_TBD}}` placeholders.
- `USER.md` — cut "Blind spots" + "Gap between self-image and others' experience" (personality-leaning, not work-PA scope); cut "Tools and systems" section (overlaps with `TOOLS.md` and BOOTSTRAP Phase 3 auto-pull).
- `TOOLS.md` — split Google Workspace row into Gmail / Calendar / Drive to match BOOTSTRAP Phase 2 wire-up flow; Telegram flipped to `✅ Connected` (pre-wired at runtime); added missing Slack row + section.
- `BOOTSTRAP.md` — softened automation invitation (no longer references a specific skill).
- `AGENTS.md` — catch-up loop simplified to framework-only.
- `AUTOMATIONS.md` — removed reference to the automation-builder skill.
- Version-string cleanup across `playbook.md`, `onboarding.md`, `TOOLS.md`, `AUTOMATIONS.md`, example daily log.
- "per-pilot" → "per-user" wording throughout.

### Removed
- `SPEEDBLOCKS.md` references (multi-Speedblock subscription machinery) — not needed with a single shipped Speedblock.
- `automation-builder` skill references — skill doesn't exist in `claw-shared`.

### Migrations
- None. Pure framework cleanup.

---

## [0.1.0] — 2026-04-23

First shipped version of the Personal Workspace framework.

### Added
- `playbook.md` — Personal Workspace operating manual: locked tech stack (Google Workspace, Telegram, Notion, GitHub, Claude, Slack), four AI layers (Gemini / Claude / OpenClaw / Cosmo), OpenClaw purpose and capabilities, working rhythm.
- `onboarding.md` — human setup (Google/Slack/Notion/GitHub accounts, user's private personal-layer repo, OpenClaw runtime deployment) + agent-led BOOTSTRAP conversation.
- `agent-files/` — shared OpenClaw framework: `SOUL`, `AGENTS`, `KRING`, `HEARTBEAT`, `IDENTITY`/`USER`/`TOOLS`/`MEMORY` per-user blueprints, `templates/` (daily / weekly / email-draft), `automations/AUTOMATIONS.md`, `onboarding/BOOTSTRAP.md`, `onboarding/STATE_VERSION`, `onboarding/MIGRATIONS/`.
- Tools-first BOOTSTRAP ordering (wire tools → pull drafts from real data → validate with user → fill human gaps → close).

### Changed
- Product renamed from "Workspace Beta" to "Personal Workspace".
- Shared framework moved from `workspace-beta-agent-files` (deleted) to `personal-workspace-speedblock/agent-files/`.

### Removed
- KRING-managed per-pilot repos (`op-august`, `op-jesper`, `op-johan`). Each user now creates their own private personal-layer repo; name is the user's choice.

### Migrations
- None. First shipped version.

### Pilots shipped to
- August Kring, Jesper Kring, Johan Rishede Duus.
