# CHANGELOG

All notable changes to the Personal Workspace framework are recorded here, newest first. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); version numbers follow [semver](https://semver.org/) (`MAJOR.MINOR.PATCH`, pre-`1.0.0` is beta).

Each entry lists what changed, and — when a version changes the shape of per-user state — points at the `agent-files/onboarding/MIGRATIONS/<from>-to-<to>.md` file an OpenClaw agent runs to catch up.

The current framework version lives in `agent-files/onboarding/STATE_VERSION`. Each OpenClaw agent's repo records its last-synced version in its own `STATE_VERSION` file at the repo root. The session-boot rule in `agent-files/AGENTS.md` describes how the comparison and catch-up runs.

---

## [Unreleased]

### Changed — Email triage & brief rhythm (v1.1 draft)

Reshapes how the agent handles mail and how the daily/weekly briefs split. User-visible capability change → requires a "what's new" message on catch-up (see `agent-files/AGENTS.md`). No per-user state shape change → no migration.

- `agent-files/SCHEDULES.md` — daily brief moves to **08:00 every day** (was weekdays 07:30); weekly review moves to **Mondays 08:00**. New sixth job **Inbox triage** — every 30 min, 24/7 (silent outside 08:00–18:00, so drafts are ready overnight without pinging). Heartbeat now runs every day and explicitly cedes email to the triage job. Updated the "five → six" counts and added the daily-brief↔triage rhythm note.
- `agent-files/templates/email-draft.md` — new **Triage mode**: the agent drafts ~95% of mail **straight into the Gmail Drafts folder** and marks **only the drafted emails** as read; everything it doesn't draft stays unread and flagged. Existing per-email Telegram approval is retained as **Interactive mode**. Still never sends without approval.
- `agent-files/templates/daily.md` — brief now summarises triage output: *Drafts ready to review (N)*, *Left for you (M — not drafted)*, *Still in Drafts from before* (day-after reminder for unsent drafts), plus tasks/reminders. Email is summarised, never pasted.
- `agent-files/templates/weekly.md` — explicitly **email-free big picture**: added *Open commitments* and *Week ahead — milestones & events*; reinforced that individual emails belong in the daily brief only.
- `agent-files/AGENTS.md` — added an *Inbox triage* operations subsection; updated *Daily brief* (08:00, all week, draft summary) and the scheduled-jobs list/counts.
- `playbook.md` — user-facing "what it does" and "working rhythm" updated to the 8:00 all-week brief + all-day Gmail-Drafts triage model.

### Fixed — Meeting prep now actually fires (v1.1 draft)

The v1.0 meeting-prep capability was defined in `AGENTS.md` but had no real trigger — it rode the hourly heartbeat, whose "skip routine standups" filter swallowed it, and which never ran before 08:00. In practice prep rarely arrived. Now on two dedicated triggers, no per-user state change.

- `agent-files/SCHEDULES.md` — new seventh job **Meeting prep**: every 15 min, 06:00–22:00, every day. Fires ~30 min before any meeting with other attendees, once per meeting. Heartbeat row updated to cede meeting prep to it. "Six → seven" counts updated.
- `agent-files/AGENTS.md` — rewrote *Meeting prep*: two layers (morning pass in the 08:00 brief + just-in-time job), preps **all** meetings with attendees incl. recurring standups, skips solo/all-day/declined, fires once per meeting (event ID logged in the daily memory file), read-only.
- `agent-files/templates/meeting-prep.md` — **new** template: who / context / your angle / handy links, with a collapsed one-line variant for the daily brief.
- `agent-files/templates/daily.md` — Calendar section now carries the morning prep note per meeting (who + the one thing to know), covering early meetings.
- `agent-files/onboarding/BOOTSTRAP.md`, `runbooks/updating-an-agent.md` — register seven jobs, not six.
- `agent-files/EVALS.md` — new golden prompt #9: prep fires for a routine standup and flags an external attendee.

_Not yet shipped to the fleet: `STATE_VERSION` stays at 1.0.0 until sign-off. Bumping it to 1.1.0 is the final step that makes the update check offer this to deployed agents._

---

## [1.0.0] — 2026-06-05

First stable release — the framework graduates from beta. Highlights: Microsoft 365 → Google Workspace migration, the one-way Syncthing local backup mirror, the procedures/evals layer, a standard agent-update path, and the human/agent rule split tidy-up (the user-facing "4 AI Commandments" one-pager finally gets the filename it's been called by everywhere).

### Removed
- `SKILL.md` — deleted. It was written as a recipe for an *agent* that provisions users, but deployment is manual: KRING stands up each runtime by hand and drops in `agent-files/` as a clean sheet. With no deploying agent reading it, SKILL.md only duplicated `onboarding.md`. Its one load-bearing rule — deploy as a clean sheet, don't pre-fill `USER.md` / invent a personality / wire tools beyond Telegram — moved into `onboarding.md` Phase 2.

### Added
- `runbooks/repurposing-an-existing-agent.md` — procedure for converting an existing agent (with its own memory/automations/personality) into Personal Workspace without data loss. Distinguishes clean-sheet vs version-update vs repurpose; load-bearing rule is setting `STATE_VERSION` to current so `BOOTSTRAP` is suppressed; covers operator reconciliation steps (Part A) and the user-facing *upgrade conversation* — continuity, not reset (Part B). `agent-files/AGENTS.md` catch-up section gains a *Repurposing an existing agent* pointer.
- `runbooks/syncthing-local-mirror.md` — one-way (Send Only → Receive Only) Syncthing setup so each user keeps a read-only local backup of their agent's files for resilience/visibility. Part A = runtime side (KRING), Part B = Mac/PC side (user). The agent stays sole writer; local edits never propagate back.
- `agent-files/TOOLS.md` — new `## Local mirror (Syncthing)` section so the agent knows the passive one-way mirror exists and that it remains the sole writer of its files.
- `onboarding.md` — Phase 2 gains a runtime-side mirror step (+ Device ID handoff); Phase 4 gains an optional `### Local backup mirror (Syncthing)` section for the user's Mac/PC side.
- `playbook.md` — new `## Your files, mirrored locally` section explaining the one-way local backup in plain terms.
- `runbooks/migrations/ms-to-google.md` — human-facing migration playbook (mail, files, calendar, contacts, cut-over checklist, daily-work guidance, common gotchas).
- `agent-files/runbooks/ms-to-google-overlap.md` — agent-side rules for handling a user with a Microsoft 365 read-only archive alongside Google Workspace.
- `agent-files/TOOLS.md` — new `## Microsoft 365 (legacy)` section template that onboarding fills in (account, cut-over date, access mode, status, auto-forward window, rules) for users who migrated from M365.
- `agent-files/AGENTS.md` — new `## Procedures` section with `verify-before-stating` (covers "never hallucinate") and `clear-and-complete-instructions` (covers the simple-but-detailed synergy). Each procedure has Trigger / Steps / Fallback / Proof. The boot sequence now anchors them: *"before any user-facing reply, run the procedures whose triggers fired; if Proof is missing, revise before sending."*
- `agent-files/EVALS.md` — six golden test prompts to manually re-run when procedures change, so we can spot-check that the behaviour actually held.
- `agent-files/SCHEDULES.md` — fifth scheduled job: a weekly **update check** (Mondays ~09:00). Pulls the framework, compares versions, and if there's a new one, tells the user what it adds and **asks before applying** (notify-first, not auto-apply — so a freshly shipped version can't silently roll out across the fleet, and each user chooses when to take it). This is the proactive trigger behind the "what's new" rule — without it, a user who rarely opens a session would never learn an update landed. Registered in BOOTSTRAP Phase 5 and self-healed at boot alongside the other jobs.
- `runbooks/updating-an-agent.md` — the standard path for bringing an existing PW agent up to the current version. Holds a reusable update prompt (the consistent version of the hand-written "update to latest + activate cron/heartbeat + preserve personalization" message), a KRING ship checklist whose load-bearing step is bumping `STATE_VERSION` (the trigger that makes an update actually reach agents), and a post-update verification checklist. `agent-files/AGENTS.md` catch-up section gains an *Updating to a new version* pointer.

### Changed
- `best-practice.md` → `ai-commandments.md` — renamed (no content changes). The user-facing file is now named what it actually is.
- `agent-files/AGENTS.md` — added a header note explaining the split: universal practices live in `ai-commandments.md` (root, human-readable); agent-only operational rules live here. One home per rule.
- `onboarding.md` — Phase 4 now asks if the user has legacy MS data; if yes, routes them into the migration playbook and tells the agent to log a Microsoft 365 (legacy) entry in `TOOLS.md`. New `### Microsoft 365 legacy data` section above References summarises the migration steps.
- `playbook.md` — added a `## Migrations` section pointing at the new playbook; added `Cut-over date` to the glossary.
- `README.md`, `SKILL.md`, `onboarding.md`, `agent-files/AGENTS.md`, `agent-files/onboarding/BOOTSTRAP.md` — pointers updated to `ai-commandments.md`.
- `agent-files/AGENTS.md` — catch-up is no longer fully silent. Cosmetic/wording updates stay silent as before, but a version that adds or changes a *user-visible capability* now requires a short "what's new" message, so existing users actually learn what their agent can newly do (previously a user could gain a morning brief and never be told). New *Updating to a new version* subsection points at `runbooks/updating-an-agent.md`.

### Migrations
- None — no per-user state shape change. Users without legacy MS data are unaffected. Existing assistants pick up the new behaviour, filename, and header on next session boot via the catch-up loop in `agent-files/AGENTS.md`. The `## Microsoft 365 (legacy)` block in `TOOLS.md` is opt-in per user.

---

## [0.3.6] — 2026-06-03

Fix the missing trigger layer — the reason the proactive capabilities (morning brief, Monday review, heartbeat checks) never fired for anyone. The framework described them but nothing ever scheduled them. Plus a folder rename to kill the `playbook.md` vs `playbooks/` naming clash.

### Added
- `agent-files/SCHEDULES.md` — canonical list of the four recurring jobs every agent runs (daily brief, weekly review, hourly heartbeat check, memory distill), with default cadences and rules. The agent owns all four as `cron` jobs — no runtime setting, no manual step. The heartbeat is just an hourly cron that runs the `HEARTBEAT.md` protocol. This is the trigger layer the proactive capabilities depend on.
- `agent-files/onboarding/BOOTSTRAP.md` — new **Phase 5 — Set up the rhythm (schedules)**: the agent registers all four `cron` jobs *silently* using the timezone already pulled in Phase 3 and default times. No new questions — onboarding length unchanged. (Renumbered old Phase 5 Close → Phase 6; added a schedule-confirmation step to *After the conversation*.)
- `agent-files/AGENTS.md` — new **Operations layer → Scheduled jobs** with a boot self-heal: on every main session the agent verifies its four jobs are registered and recreates any missing ones (so agents onboarded before this version pick the schedule up automatically, no redeploy). Boot-sequence step 9 now points at it.

### Changed
- `playbooks/` → `runbooks/` and `agent-files/playbooks/` → `agent-files/runbooks/` — removes the collision with the top-level `playbook.md` operating manual. All references updated (`onboarding.md`, `agent-files/TOOLS.md`, both migration files, this changelog).
- `agent-files/README.md` — layout now lists `SCHEDULES.md`; clarified `HEARTBEAT.md` is the *what to do when a check fires*, `SCHEDULES.md` is the *what makes it fire*.
- `onboarding.md` — Phase 2 notes the agent self-schedules its own brief/review/heartbeat in Phase 4, so KRING has no schedule step at deploy.

### Migrations
- None — no per-user state shape change. Existing assistants self-heal their schedule on next main session via the new boot check in `agent-files/AGENTS.md`, using the timezone already in their `USER.md`. Nothing for KRING to do per runtime.

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
