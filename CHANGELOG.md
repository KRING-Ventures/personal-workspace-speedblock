# CHANGELOG

All notable changes to the Personal Workspace framework are recorded here, newest first. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); version numbers follow [semver](https://semver.org/) (`MAJOR.MINOR.PATCH`, pre-`1.0.0` is beta).

Each entry lists what changed, and — when a version changes the shape of per-user state — points at the `agent-files/onboarding/MIGRATIONS/<from>-to-<to>.md` file an OpenClaw agent runs to catch up.

The current framework version lives in `agent-files/onboarding/STATE_VERSION`. Each OpenClaw agent's repo records its last-synced version in its own `STATE_VERSION` file at the repo root. The session-boot rule in `agent-files/AGENTS.md` describes how the comparison and catch-up runs.

---

## [0.3.0] — 2026-04-29

Add the *working-practices* layer: how a person should actually work with their assistant, the must-know vocabulary that makes it possible, and the BOOTSTRAP step that teaches both during a new user's first conversation.

### Added
- `best-practice.md` (repo root) — the four practices for working with an agent: make it restate the prompt, save what matters, lock work in small chunks, branch and PR in shared repos.
- `terms.md` (repo root) — must-know vocabulary glossary (repo, branch, main, commit, pull request, merge, work tree, version, fork) with a "why these matter" tail.
- `agent-files/AGENTS.md` — new **Working practices** section. The agent now follows the four practices and nudges the user when one is being skipped.
- `agent-files/onboarding/BOOTSTRAP.md` — new **Phase 5: Teach the working practices and terms**. Inserted after Phase 4 (validation + gap-fill); the previous Close becomes Phase 6.

### Changed
- `playbook.md` — new **How to work with your assistant** section: tight summary of the four practices + pointers to `best-practice.md` and `terms.md`.
- `README.md` — Human layer table now lists `best-practice.md` and `terms.md`. Current version line bumped.
- `onboarding.md` — *What this version ships* block now mentions the Learning phase in the first conversation.

### Migrations
- None — no per-user state shape change.
- **For existing users (already past BOOTSTRAP):** don't run Phase 5 retroactively. Start applying the four practices straight away (they're now part of how you operate), and surface `best-practice.md` / `terms.md` naturally next time it's relevant — not as a forced teaching session unless the user asks for one.

---

## [0.2.0] — 2026-04-24

Repackage the repo as a Speedblock in the new two-layer shape: a **skill layer** (agent-loadable) and a **human layer** (deliverables read or operated by people). No changes to `agent-files/` content or per-user state shape — existing users pull and continue, no migration.

### Added
- `SKILL.md` — skill entry point at repo root. Describes the skill's job (provisioning a new user on Personal Workspace), when to use and not use it, the handoff to agent-led BOOTSTRAP, and what `agent-files/` ships as the payload.
- `human-roles.md` — names the four active human roles this Speedblock assumes (account provisioner, runtime operator, framework maintainer, user) and the handoffs between them.

### Changed
- `README.md` — restructured to present the repo as a Speedblock with explicit skill layer and human layer sections.

### Migrations
- None. `agent-files/` is unchanged — same paths, same content, same per-user state shape. The repo is now skill-shaped *around* the same payload.

---

## [0.1.2] — 2026-04-24

Correct the shipped tool-reach set: the agent is not wired to Slack or GitHub in 0.1.x. Wire-up covers Telegram (pre-wired), Gmail, Calendar, Drive, Notion, plus any user-specific tools.

### Changed
- `TOOLS.md` — removed Slack and GitHub rows + sections; added a "User-specific tools" table so additional tools can be wired during onboarding.
- `BOOTSTRAP.md` — removed Slack + GitHub from Phase 1 tool list, Phase 2 wire-up priority order, and Phase 3 auto-pull sections; added a step for user-specific tools after the standard set.
- `AGENTS.md` — removed "Group / shared session" type (not applicable without Slack); dropped Slack mentions from daily brief cue and permission table.
- `IDENTITY.md` — removed Slack from the Surface line.
- `playbook.md` — updated "Uses your tools" and Phase 2 wire-up flow to reflect the actual tool set.
- `onboarding.md` — tool-reach line updated; version block updated.
- `AUTOMATIONS.md` — surfaces-touched example no longer lists Slack.

### Removed
- Agent-side Slack and GitHub wire-up (not supported in 0.1.x). Slack remains part of the human tool stack for team chat and Cosmo; GitHub remains the source-of-truth repo layer handled by the runtime.

### Migrations
- None. Users who already onboarded against 0.1.1 can simply pull the framework — no per-user state shape changes.

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
