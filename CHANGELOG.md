# CHANGELOG

All notable changes to the Personal Workspace framework are recorded here, newest first. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); version numbers follow [semver](https://semver.org/) (`MAJOR.MINOR.PATCH`, pre-`1.0.0` is beta).

Each entry lists what changed, and — when a version changes the shape of per-user state — points at the `agent-files/onboarding/MIGRATIONS/<from>-to-<to>.md` file an OpenClaw agent runs to catch up.

The current framework version lives in `agent-files/onboarding/STATE_VERSION`. Each OpenClaw agent's repo records its last-synced version in its own `STATE_VERSION` file at the repo root. The session-boot rule in `agent-files/AGENTS.md` describes how the comparison and catch-up runs.

---

## [Unreleased] — v1.0 integration branch

First v1.0 feature: Microsoft 365 → Google Workspace migration. New users coming from M365 get a step-by-step migration path, and their agent learns to handle the dual-system overlap window (search the right system based on the cut-over date).

### Added
- `playbooks/migrations/ms-to-google.md` — human-facing migration playbook (mail, files, calendar, contacts, cut-over checklist, daily-work guidance, common gotchas).
- `agent-files/playbooks/ms-to-google-overlap.md` — agent-side rules for handling a user with a Microsoft 365 read-only archive alongside Google Workspace.
- `agent-files/TOOLS.md` — new `## Microsoft 365 (legacy)` section template that onboarding fills in (account, cut-over date, access mode, status, auto-forward window, rules) for users who migrated from M365.

### Changed
- `onboarding.md` — Phase 4 now asks if the user has legacy MS data; if yes, routes them into the migration playbook and tells the agent to log a Microsoft 365 (legacy) entry in `TOOLS.md`. New `### Microsoft 365 legacy data` section above References summarises the migration steps.
- `playbook.md` — added a `## Migrations` section pointing at the new playbook; added `Cut-over date` to the glossary.

### Migrations
- None — no per-user state shape change. Users without legacy MS data are unaffected. Existing assistants pick up the new behaviour on next session boot via the catch-up loop in `agent-files/AGENTS.md`. The `## Microsoft 365 (legacy)` block in `TOOLS.md` is opt-in per user.

---

## [0.3.5] — 2026-05-06

Sharpen the heartbeat protocol: explicit importance filter and an explicit *nudge → offer → draft/prep → confirm → act* flow so the assistant never acts on the user's behalf without a go-ahead, and never nudges on junk mail, newsletters, or routine calendar items.

### Changed
- `agent-files/HEARTBEAT.md` — added `## Importance filter` (signal not coverage; flag only when a human is waiting, a decision is needed, real prep is needed, or a deadline is close) and `## The flow: nudge → offer → draft/prep → confirm → act` with the two canonical patterns: inbound mail/message (*"want me to draft? I'll send it once you confirm"*) and time-based meeting prep (*"here's the prep — anything to change?"*). Updated the "How to reach out" examples to end with a concrete offer rather than a vague heads-up.

### Migrations
- None — no per-user state shape change. Existing assistants pick up the new wording on next session boot via the catch-up loop in `agent-files/AGENTS.md`.

---

## [0.3.4] — 2026-05-04

Aggressive readability cuts on the human files. Drop `human-roles.md` (the role split lives in `onboarding.md` already). Trim filler from `playbook.md` and `onboarding.md` so a venture reader can scan once and act. Compress `best-practice.md` to a literal one-A4-page printout.

### Removed
- `human-roles.md` — redundant with `onboarding.md`. Step 1 / Step 2 / Step 3 already say who does what.

### Changed
- `best-practice.md` — compressed to fit on one A4 page when printed (verified via Chrome print-to-PDF, A4, 1.6 cm × 2 cm margins). The four practices are now inline `**bold label**` paragraphs with the example prompt and a one-line tail; the glossary is a single bullet list with one-line definitions; "why these matter" collapsed to a single sentence.
- `onboarding.md` — dropped the "you / we / your team" terminology block at the top; collapsed Step 2 from a 5-bullet breakdown into two sentences (the venture doesn't need our internal deploy steps); tightened "What this version ships" wording; removed the duplicate `CHANGELOG.md` pointer from the body (still in the footer).
- `playbook.md` — dropped the "this document explains what's in it" meta-paragraph; tightened the assistant-intro line; trimmed each "What it does for you" bullet; rephrased "Your assistant drafts and researches freely" → "Drafts and research are free".
- `README.md`, `SKILL.md` — references to `human-roles.md` removed.

### Migrations
- None — no per-user state shape change. Existing assistants pick up the new wording on next session boot via the catch-up loop in `agent-files/AGENTS.md`.

---

## [0.3.3] — 2026-05-04

Readability pass on the human-facing docs — same content, fewer words, clearer for readers who are new to KRING.

### Changed
- `playbook.md` — removed duplicated "owned by KRING" line at the top (footer kept).
- `onboarding.md` — replaced internal term *Heartbeats* with *Proactive check-ins*; trimmed the 4 Commandments line so it stops re-listing the practices (they live in `best-practice.md`); removed "fixed beta tech stack" jargon — now reads "These are the required tools."
- `best-practice.md` — split the dense intro paragraph into two; rephrased "versioned, reviewable changes" to "saved, reviewable steps" so the framing lands for non-developers.
- `human-roles.md` — converted the long "Does" paragraphs for Venture / KRING / User into bulleted lists so each role's job is scannable in one read; opened with "The humans this Speedblock relies on" instead of "active human layer."

### Migrations
- None — no per-user state shape change. Existing assistants pick up the new wording on next session boot via the catch-up loop in `agent-files/AGENTS.md`.

---

## [0.3.2] — 2026-05-04

Combine the working-practices doc and the glossary into a single file so both live in one place.

### Changed
- `best-practice.md` — now carries the 4 Commandments **and** the must-know vocabulary (seven terms + "why these matter") in one document. Glossary moved in as a bottom section.
- `playbook.md`, `README.md`, `SKILL.md`, `onboarding.md` — references to `terms.md` collapsed into the single `best-practice.md` pointer.
- `agent-files/onboarding/BOOTSTRAP.md` — Phase 5 script now points at `best-practice.md` only; the "walk the must-know terms" step refers to the glossary section at the bottom of the same file.

### Removed
- `terms.md` — content lives in `best-practice.md`.

### Migrations
- None — no per-user state shape change. Existing assistants continue against the same `agent-files/` payload; the catch-up loop in `agent-files/AGENTS.md` will pick up the new doc layout on next session boot.

---

## [0.3.1] — 2026-04-30

Align the working-practices layer to the canonical *4 Commandments* one-pager: rebrand, drop one practice, add KISS, and trim the glossary from nine terms to seven.

### Changed
- `best-practice.md` — title changed to **The 4 Commandments**; subtitle "Best practices for working with AI agents." The four practices are now: (1) Make the agent repeat back your prompt, (2) Work in small batches — and save as you go (consolidates the previous *save what matters* + *lock work in small chunks*), (3) KISS — keep it simple and understandable (new), (4) In shared projects: work on a copy, then merge it. Each practice carries the canonical example prompt verbatim from the one-pager.
- `terms.md` — trimmed to seven terms: repo, branch, main branch, commit, pull request, merge, work tree.
- `agent-files/AGENTS.md` — *Working practices* section retitled to *Working practices — The 4 Commandments* and rewritten to match the four canonical practices.
- `agent-files/onboarding/BOOTSTRAP.md` — Phase 5 retitled to *Teach the 4 Commandments and terms*; walk-through scripts updated to the four canonical practices and the seven-term glossary; the must-know split (always-cover vs. if-they-code) is gone — all seven terms are always covered.
- `playbook.md` — *How to work with your assistant* section retitled to *The 4 Commandments* with the same content shape.
- `README.md`, `SKILL.md`, `onboarding.md` — descriptions of `best-practice.md` updated to the new framing.

### Removed
- *Version* and *Fork* from `terms.md` — superseded by the trimmed seven-term list.
- The *save what matters* practice as a standalone item — merged into Commandment 2.

### Migrations
- None — no per-user state shape change. Existing users continue against the same `agent-files/` payload; the catch-up loop in `agent-files/AGENTS.md` will surface the new framing on next session boot.
- **For existing users:** start using the four Commandments straight away (they are how the agent now operates) and surface `best-practice.md` / `terms.md` naturally next time it's relevant — no forced re-teach.

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
