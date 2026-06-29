# CHANGELOG

All notable changes to the Personal Workspace framework are recorded here, newest first. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); version numbers follow [semver](https://semver.org/) (`MAJOR.MINOR.PATCH`, pre-`1.0.0` is beta).

Each entry lists what changed, and — when a version changes the shape of per-user state — points at the `agent-files/onboarding/MIGRATIONS/<from>-to-<to>.md` file an OpenClaw agent runs to catch up.

The current framework version lives in `agent-files/onboarding/STATE_VERSION`. Each OpenClaw agent's repo records its last-synced version in its own `STATE_VERSION` file at the repo root. The session-boot rule in `agent-files/AGENTS.md` describes how the comparison and catch-up runs.

---

## [Unreleased]

### Added — Feedback ledger: capture real-use corrections, harvest them upstream (WIP, toward 1.1)

Fixes surfaced in real use (a user says *"why didn't you run my inbox triage?"*, the agent fixes it) used to die in the chat — the next agent shipped with the same gap. New **agent → repo** channel so a fix found once becomes a framework fix for all:

- `agent-files/feedback/IMPROVEMENTS.md` — **new.** A per-user, local, **write-mostly** ledger (lives with `memory/`, `automations/`; survives updates untouched). The agent appends a classified entry on each correction: trigger / root cause / fix applied / **type** (`personal` vs `framework`) / maps-to template file / status. Explicitly **not loaded at boot** — written on correction, read only at harvest, so it costs no context budget.
- `agent-files/AGENTS.md` — small trigger added (the only boot-loaded part): *Capturing fixes* — when the user corrects how you operate, fix it now **and** log a classified entry; `feedback/` added to the per-user state list with the write-mostly/not-at-boot note. Kept tight to protect the boot bundle.
- `agent-files/runbooks/harvesting-improvements.md` — **new.** KRING operator loop: collect ledgers across agents → cluster by what they touch → promote `framework` entries into the templates (+ CHANGELOG/STATE_VERSION via `updating-an-agent.md` Part A) → mark `promoted`. `personal` is the firewall and is never promoted. Optional: `agent-hygiene` can flag "ready to harvest" so ledgers don't rot.

### Fixed — Calendar invites awaiting a response are now surfaced proactively (WIP, toward 1.1)

Live gap (August): incoming calendar invites were never surfaced with an accept/decline offer. The heartbeat's Calendar section only watched the *shape* of the day (conflicts, overload, focus blocks), and every "urgent invite" rule across the framework was scoped to invites *affecting today's calendar* — so a normal future invite sitting in `needsAction` fell through every proactive path and, at best, appeared as a silent line in the daily brief. Fixed by adding pending invites as a first-class heartbeat signal:

- `agent-files/HEARTBEAT.md` — new *Calendar invites awaiting a response* check: detect any event where the user's own `responseStatus` is `needsAction`, surface it with decision context (title/when/organiser/attendees). Anchored on the **calendar event status, not the invite email**, so it fires even when the Gmail invite is auto-filed or never arrives. **On a clash it offers real orchestration choices** — decline and keep what's booked; accept and rearrange the conflict (move a *solo* block freely; rescheduling a meeting *with others* needs the OK and proposes new times to them only on confirm); or propose an alternative time to the organiser. All Ask-first — options laid out, nothing sent/moved on the user's behalf. Added a reach-out example; de-dupe via the existing "don't re-flag across heartbeats" rule.
- `agent-files/runbooks/smart-triggers.md` — heartbeat gate gains a wake condition for an unseen `needsAction` invite (with a cooldown so the same invite doesn't re-fire hourly). Without this the prefiltered gate would never wake the agent for the new signal.
- `agent-files/SCHEDULES.md` — heartbeat row coverage now lists invites awaiting a response.
- `agent-files/scripts/smart-trigger.py` — **the real root cause at code level.** The reference heartbeat gate's `calendar_conflict_signal` only looked for double-bookings in the next 8h; a pending invite produced no signal, so the gate never woke the agent and the doc rule could never fire. Added `calendar_invite_signal` — scans the next 30 days for an event where the user's own `responseStatus` is `needsAction` (skips cancelled) — and `signal_for("heartbeat")` now returns conflict **or** pending-invite. The existing 240-min unchanged-signal cooldown keys on the event id, so the same invite won't re-nag hourly.

No new job and no `STATE_VERSION` bump — folds into the existing hourly heartbeat; behaviour + gate-script change only.

### Changed — Repurpose onboarding hardened into a scripted, transition-aware flow (WIP, toward 1.1)

The repurpose path (`runbooks/repurposing-an-existing-agent.md` Part B) was loose prose while `BOOTSTRAP.md` had become fully scripted, locked copy — so repurposed/returning users got a less reliable onboarding than new ones. Brought Part B up to BOOTSTRAP's standard and synced it to the current framework (self-serve cold start, answer-then-bridge, completion checklist, `STATE_VERSION` 1.0.3):

- **Part B is now an agent-followed script** with the same block shape as BOOTSTRAP (Goal / Send this exactly / Capture / Then) and an at-a-glance flow table. New **locked copy** for the three transition-specific moments — **R1 Welcome back & what's changing**, **R4 Confirm migrated basics**, **R7 Live** — while the shared teaching steps (2 core features, 3 best practices) and optional demos (5, 6) are delivered from BOOTSTRAP's locked blocks verbatim, so there's one source of truth for that copy and no drift.
- **The opening now names the transition** — R1 tells the user *what the agent is becoming* (their Personal Workspace assistant), *what's new* (the built-in features/ways of working), and *what stays* (memory, history, automations, personality). The prior cold "hi, I'm your new assistant" framing is gone; identity is confirmed (R4), never re-collected.
- **Wording rules carried over:** locked copy sent word-for-word, faithful translation into the user's *already-known* language (no language gate — that was BOOTSTRAP's only gate and it's already satisfied), answer-then-bridge and the mandatory-step completion checklist.
- **Notion de-listed as a "PW-standard" tool.** Both the Part A `TOOLS.md` reconcile and the old Part B "offer the gaps" step called Notion (and GitHub) standard tools the agent should offer/wire. They're **Recommended/self-serve** now (`playbook.md` → Recommended stack) — the user wires them. Reconcile guidance fixed to never mark them connected by default; the "extras" offer now covers the real opt-in (Syncthing local mirror) and points recommended tools back to self-serve.
- **One script, both paths.** `updating-an-agent.md` → Part C already reaches for this continuity-aware flow when an agent was updated/repurposed before onboarding existed — so hardening Part B hardens the update path too. Cross-references aligned in both directions.

`STATE_VERSION` not bumped — runbook/wording change, no per-user state shape change.

### Added — BOOTSTRAP installs the framework into itself (WIP, toward 1.1)

Root cause behind the Flimmer drift: "pull the latest framework from GitHub" was prose, not an action — nothing in `agent-files/` actually fetched anything (no clone/pull/curl), so the agent fell back to memory and paraphrased locked copy. `BOOTSTRAP.md` now opens with a concrete **Step 0**:

- A literal `git clone --depth 1` of this (public) repo into a temp dir, `cp -r agent-files .` into the workspace (refreshes the framework; leaves per-user state at the workspace root untouched), then an `ls` that must find `AGENTS.md` + `BOOTSTRAP.md`.
- **Hard stop on failure:** if the clone fails or the files aren't there, the agent says so and stops — it must *never* continue onboarding from training/memory.
- **Files beat memory:** once on disk, the pulled files are the source of truth; locked copy is read from the file and pasted, never reconstructed. Closes the gap that let Flimmer onboard from recollection.

### Changed — Cold start is self-serve; KICKOFF brief removed (WIP, toward 1.1)

The `KICKOFF.md` fill-in brief was over-built: four of its five fields were already known (agent name in `IDENTITY.md`, repo in `AGENTS.md`, support/Moss in `BOOTSTRAP.md`, user first name seeded at provisioning). Only the user's Slack ID was genuinely missing — and the agent can resolve that itself. Replaced the manual handover with zero-touch cold-start behaviour:

- `agent-files/onboarding/KICKOFF.md` — **removed.** No brief to fill or paste.
- `agent-files/AGENTS.md` — first-session logic now *is* the cold start: identify the user from your 1:1 Slack channel, save a name→ID map to `MEMORY.md`, reach out yourself, run BOOTSTRAP. Fallback: ask once if the channel has multiple humans; use a seeded `Slack member ID` if present.
- `agent-files/onboarding/BOOTSTRAP.md` — *Before you start* now opens with the cold-start "you reach out first / identify the user" instruction; fixed the last passive "user sets the pace" line.
- `agent-files/USER.md` — new `Slack member ID` Basics field (resolved on first boot, or optionally seeded at provisioning).
- `activation-kring.md` — Step 9 now says "nothing to paste — the agent cold-starts itself," with optional Slack-ID seed.

### Changed — Onboarding proactivity + don't re-ask (WIP, toward 1.1)

Two failure modes seen live (Flimmer ↔ Martin): the agent waited on the user to drive each step instead of leading, and it re-asked for info the user had already volunteered (Martin gave his role/tasks; the agent asked again because Step 4 says to). Fixed in `BOOTSTRAP.md`:

- New *"Carrying the conversation"* section: **(1) you lead** — the agent owns reaching Step 7; "next" is the user's breather, not a prompt the agent waits on; nudge forward when they go quiet, never park mid-flow. **(2) don't re-ask what you already know** — check the conversation / kickoff brief / files first; confirm known info instead of re-asking.
- Carve-out on the global "send word-for-word" lock: it locks the *teaching/welcome* copy, **not** re-asking an already-answered question — where a step *gathers* info, confirm what you have.
- Step 4 gets a pointed note: if role/projects were already volunteered, reflect back to confirm and only ask for what's still missing.

### Added — Deployment handover / kickoff brief (WIP, toward 1.1)

A fresh agent wakes with files installed but no idea who it is, who its human is, or that it should start — in the first live onboarding, KRING had to hand the agent everyone's Slack IDs by hand mid-conversation. New `KICKOFF.md` closes the gap *before* `BOOTSTRAP.md`:

- `agent-files/onboarding/KICKOFF.md` — **new.** A human-filled deployment handover the deployer pastes as the agent's first message. Seeds four things the agent can't safely infer: repo location (+ install confirmed), the onboarding user (name + **Slack ID**), the support contact, and the instruction to *proactively* tag the user and open BOOTSTRAP Step 1. Plus agent-side steps: pre-read files, seed identity + a Slack name→ID map into `MEMORY.md`, confirm it's a genuine fresh deploy (`STATE_VERSION` empty), then reach out first. Handed-brief by design — self-discovering "who is my human's Slack ID" is exactly what fails.
- `activation-kring.md` — Step 9 now points at `KICKOFF.md` instead of a vague "the agent leads," making the handover a concrete, repeatable trigger.

### Added — Onboarding tangent handling (WIP, toward 1.1)

From the first live onboarding (Martin Nellemann ↔ Flimmer): the user asked questions outside the script and the linear 7-step flow had no rule for it, so the agent risks either stonewalling or pivoting and never completing setup. Added an **answer-then-bridge** protocol to `BOOTSTRAP.md` plus an agent-owned completion checklist:

- `agent-files/onboarding/BOOTSTRAP.md` — new section *"When {{USER_FIRST_NAME}} steps off the script"*: answer briefly → bridge back → return to the next unfinished **mandatory** step (1·2·3·4·7 + finalisation; 5·6 optional). Step 1 (name + language) is the one hard gate; everything after is flexible. Progress tracked in `memory/YYYY-MM-DD.md` so a dropped/resumed session doesn't lose the thread. Locked copy blocks untouched.
- `activation.md` — Part 2 gains one user-facing line: ask questions anytime, the agent answers and resumes, so you still get the full setup. (Kept in step with BOOTSTRAP.)

### Changed — Activation / onboarding split (WIP, toward 1.1)

Splits the single setup doc into two flows that were previously mashed together: **activation** (how a venture gets deployed) and **user onboarding** (the agent-led first conversation). Driven by the v1.1 Activation Flow + Onboarding Flow designs. WIP on `feat/activation-onboarding-split` — refining before dry-run; `STATE_VERSION` not bumped yet. Human files and agent files are kept in step.

**Later in this cycle, the two venture-facing docs were merged back into one.** `onboarding.md` folded into `activation.md` as *Part 2 — Your first conversation* (Part 1 is getting set up), so the venture has a single doc for the whole journey — fewer files. `BOOTSTRAP.md` stays the agent-side script. Also: the `playbook.md` tech-stack tables became small HTML tables sharing one `colgroup` so both render at matching column widths (middle widest, left medium, right least) — plain Markdown can't set column widths. Refs updated (`README`, `activation-kring`, repurposing runbook); `tool-setup.md` link removed from `activation.md` (its content lives in `activation-kring.md` now). And `WRITING.md` was folded into `README.md` as a short **House style** section and deleted — one fewer file; the standard still lives in writing.

- `onboarding.md` — split. Now **only** the agent-led user onboarding: a 6-step flow (Welcome & intro → Gets to know you → Maps your needs → optional First real task → optional First automation → Live), ~16 min core / ~30 min with the optional steps. Always-on in-thread support footer.
- `activation.md` — **new.** The venture-and-KRING deployment process across three stages (Provisioning ~1 day → Setup ~3–4 days → Onboarding handover). Absorbs the old venture-side phases plus the full tool-wiring detail (Google Workspace, Notion, GitHub, M365 legacy, Syncthing) — wiring now happens during activation, performed by KRING, not by the user during onboarding.
- `agent-files/onboarding/BOOTSTRAP.md` — restructured to match the 6-step user flow. Phase-2 live tool-wiring removed (tools are wired in activation); Step 2 now confirms the already-wired state and pulls basics; schedule registration folds into Step 3 (Maps your needs); the 4 AI Commandments become a light reference in Step 1 rather than a dedicated teaching phase; optional first-task and first-automation demos added.
- `agent-files/onboarding/BOOTSTRAP.md` — rewritten as an **agent-followed script** (was closer to a spec). Every step now has a consistent block — Goal / "Say it like this" reference delivery / Capture / Then — so the agent runs a repeatable onboarding instead of improvising each turn (previously only Step 1 had scripted language). Added the v1.1 screenshot's "personal agent vs. shared team agent" beat to Step 1, an at-a-glance flow table, and a Support note (Moss).
- `README.md`, `playbook.md`, `agent-files/README.md`, `runbooks/migrations/ms-to-google.md` — pointers and "wired during your first conversation" wording updated to the activation/onboarding split.
- **Surface swap — Telegram → Slack.** Slack is now the channel each user talks to their agent on, throughout the human-facing docs. Telegram removed from the product.
- **Tech stack split — Mandatory vs Recommended.** `playbook.md` now separates the apps required to run Personal Workspace (Google Workspace, Slack, ChatGPT) from the recommended ones users self-wire (Notion, GitHub, Whispr Flow, Claude). GitHub moved to Recommended/self-service; M365 migration stays optional and KRING-run.
- **Plain-language + value pass.** Rewrote `activation.md`, `onboarding.md`, and the `playbook.md` intro to lead with what the user/venture is doing and the value it provides, in simple language with a cleaner layout. Venture-facing docs now show outcomes, not our internal mechanics; the technical steps live only in `activation-kring.md`.
- **App-provisioning detail folded into `activation-kring.md`** (under Step 5 — Tech-stack confirmation) instead of a separate `tool-setup.md` — KRING activation now contains the whole story (accounts → wiring → handover) in one doc, fewer files to keep in sync. Covers the three required apps (plan/tier, link, how many, time, per-app steps). **Ownership stays explicit: the venture owns its whole tech stack — accounts and billing stay with them, nothing runs through KRING; KRING only connects the agents.** ChatGPT is the venture's own **ChatGPT Business (Team)** account (one seat per person, run via the **Codex CLI** over the subscription, not a metered OpenAI API account). Usage-ceiling question (base Business seat vs. credits/higher tier for an always-on agent) flagged as an **Ask Corey** placeholder in `activation-kring.md`.
- `playbook.md` — "What it does for you" converted from bullets to a two-column table.
- `activation-kring.md` — Stage 2 now states the work runs in parallel: build agents from names while the venture sets up tools; wiring waits on the tools; then deploy.
- `agent-files/TOOLS.md` — the blueprint now shows Google Workspace (Gmail · Calendar · Drive/Docs) as **✅ Connected — pre-wired at provisioning (gog, per-user OAuth)**, alongside Slack which was already pre-wired. Since these are wired during activation *before* the agent's files land, the seeded `TOOLS.md` reflects reality at boot — a new agent knows it's connected instead of treating Google as "not connected" and refusing to use it. Safe because the claim is now universally true at provisioning; previously it would have been a false default for un-onboarded agents.
- `WRITING.md` — added the rule that action steps must carry enough detail to finish (where/what/how long); long steps move to their own do-it guide.
- **Consistency pass** (against the v1.1 Activation + Onboarding designs): fixed onboarding timing to ~16 min core / ~30 with optional steps (`onboarding.md`, in step with `BOOTSTRAP.md`); added the escalation path to onboarding's support footer; corrected `BOOTSTRAP.md`, which still told the agent Notion/GitHub were KRING-wired during activation (they're recommended/self-serve — agent no longer claims they're connected); aligned the playbook ChatGPT row to Business Team + Codex CLI and the venture-owns framing; marked the Notion/GitHub steps in `activation-kring.md` as self-serve reference.
- `WRITING.md` — **new.** A testable writing standard every user-facing page must pass (one job, plain, selective, one screen). Added after the first value pass still read as too dense — the standard is the durable guard so pages stay clear, not just today.
- **One-screen cut.** Rebuilt `buy-in.md`, `activation.md`, and `onboarding.md` to pass the standard — each now fits one screen, leads with the reader's one job, and pushes detail into its own file.
- `buy-in.md` — **new.** The value case for Personal Workspace — the three big time drains it targets (~28% of the week on email, ~1.8 h/day searching, ~10 h/month on calendar) and what each user and the venture gets. Sourced from the Workspace solution deck. Rewritten in the onboarding-script voice, and the cost table now carries **real per-seat list prices in EUR (Danish/EU, ex VAT, annual)**: Google Workspace Business Standard ~€14, Slack Pro ~€7, ChatGPT Business ~€21, hosting ~€4 → **~€46/user/mo**. Plan settled on **Business Standard** (was inconsistently "Starter") — `activation.md` and `activation-kring.md` updated to match.
- `ai-commandments.md` — rewritten in the plain onboarding voice: each commandment is now a one-line *what to do* + a "try saying this" example + a one-line *why*, plus a short plain-language vocabulary list. Same four commandments, far more approachable.

**Open for refinement:** depth of the 4 AI Commandments in onboarding; the exact Venture/KRING/User labor split (flagged "needs Corey's eyes" in the design); a separate KRING-as-its-own-venture activation flow (raised, not yet built).

---

## [1.0.3] — 2026-06-22

### Added — Weekly agent hygiene keeps agent files from bloating

- `agent-files/SCHEDULES.md` — added a weekly silent-unless-action-needed `agent-hygiene` job after the Monday update check. It checks boot budget, root clutter, oversized files, and memory bloat, and only messages the user when a decision is needed.
- `agent-files/runbooks/agent-hygiene.md` — new runbook with the standard cleanup loop: run `openclaw doctor`, check largest files, keep boot files essential-only, curate `MEMORY.md`, move generated files out of root, archive instead of deleting, and log meaningful cleanup.
- `agent-files/AGENTS.md` — scheduled-job list now includes agent hygiene, and file-hygiene guidance now tells agents to explain the best-practice reason when recommending cleanup because users are not expected to know agent-file conventions.
- `agent-files/automations/AUTOMATIONS.md` — maintenance automations now explicitly explain recommendations before asking the user to choose.
- `agent-files/onboarding/BOOTSTRAP.md`, `agent-files/runbooks/updating-an-agent.md`, and `agent-files/runbooks/repurposing-an-existing-agent.md` — standard schedule setup now includes the hygiene job and avoids stale fixed job counts.
- `agent-files/README.md` — runbook/layout wording updated so the hygiene runbook is part of the standard agent-file set.

### Fixed — Primary language and inbox-noise filtering are now structurally defined

- `agent-files/USER.md` — added an explicit `Primary language` field so onboarding has a durable place to store the user's selected language.
- `agent-files/onboarding/BOOTSTRAP.md` — capture instructions now write the selected default language to `USER.md` → `Primary language`.
- `agent-files/templates/daily.md`, `weekly.md`, `meeting-prep.md`, and `email-draft.md` — clarified that proactive user-facing output defaults to the user's primary language, while replies mirror the thread/recipient language.
- `agent-files/runbooks/smart-triggers.md` — expanded the inbox-noise filter into a standard policy: skip newsletters, notifications, automated/product/service/marketing/bulk mail unless urgent, never interrupt for cleanup noise, and do not archive/delete/unsubscribe without explicit user permission.
- `agent-files/scripts/smart-trigger.py` — added a reusable token-free pre-agent gate for inbox triage and heartbeat so the filter can be enforced by deployed agents, not only described in prose.
- `agent-files/SCHEDULES.md` — inbox triage now points at the shipped smart-trigger script as the reference implementation.

### Fixed — Proactive jobs must be gated before they can make noise

- `agent-files/SCHEDULES.md` — standard jobs are now explicitly typed as **visible**, **prefiltered**, or **silent**. Inbox triage is no longer described as a normal 30-minute agent cron; it must run through a hard pre-agent gate such as `scripts/smart-trigger.py inbox-triage` and wake the agent only on real signal.
- `agent-files/AGENTS.md` — scheduled-job self-heal now preserves job type. A missing prefiltered job must be recreated as a gated trigger, not as a direct agent cron. This prevents high-frequency background work from leaking final assistant text into the user channel.
- `agent-files/HEARTBEAT.md` — heartbeat no longer handles general email. It may interrupt on email only for immediate high-consequence cases: same-day human decision, deadline within 24 hours, account lockout/security compromise, payment failure, or today's calendar impact.
- `agent-files/templates/email-draft.md` — empty/no-value triage outcomes must return `HEARTBEAT_OK` / no visible summary. Silence is an architecture requirement, not just a style preference.
- `agent-files/runbooks/smart-triggers.md` — new runbook defining the pre-agent gate contract for inbox triage and heartbeat.
- `agent-files/AGENTS.md` — KISS now has an incident-response rule: for failures or noisy automation, answer first with one short cause and the fix; details only if asked.

---

## [1.0.2] — 2026-06-16

**Boot-budget + KISS pass on the agent files.** The boot bundle (files OpenClaw injects every session — `AGENTS.md`, `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`, `MEMORY.md`, `HEARTBEAT.md`) was overflowing OpenClaw's ~60k-char context budget, so the runtime truncated it — and per-user `MEMORY.md`, loaded last, was getting **dropped entirely** (long-term memory stopped reaching the agent). `AGENTS.md` alone was 27.8k, over half the budget. Shipped as a patch — no roadmap scope, no new capabilities. Aligned with the official guidance at <https://docs.openclaw.ai/concepts/memory> (keep boot files compact; push detail to on-demand files; never let long-term memory be the file that drops).

**This update changes the shape of the boot files, so it has a migration: `agent-files/onboarding/MIGRATIONS/1.0.1-to-1.0.2.md`.** Existing agents must adopt the new lean structure (and re-apply any personal edits they made to their own `AGENTS.md`/`SOUL.md` on top of it) — see that file.

- `agent-files/AGENTS.md` — **rewritten leaner: 27.8k → 12.6k (−55%).** No rules dropped — verbose explanation collapsed and detailed how-tos moved to pointers (`runbooks/`, `SCHEDULES.md`, `templates/`, loaded on demand). Permission table, calendar ask-first split, KRING rules, and the 4 AI Commandments kept in full.
- **The three heavy `## Procedures` → a light `## How you answer`.** `verify-before-stating`, `clear-and-complete-instructions`, and `do-first-then-ask` were Trigger/Steps/Fallback/**Proof** blocks, with a boot anchor forcing the agent to emit "Proof" in *every* reply — which forced a source ref on every factual claim and made replies read like an audit log. Replaced with three plain principles (don't state guesses as facts; do it yourself before handing it back; make handed-over instructions followable). Behaviour unchanged; the bar is now "don't pass a guess off as certainty," not "cite a source on every sentence."
- `agent-files/SOUL.md` — dropped the do-freely/ask-first/never permission lists that duplicated the `AGENTS.md` permission table (now a pointer); voice, character, hard KRING rules, and privacy kept intact. 7.0k → 6.4k.
- `agent-files/AGENTS.md` — `KRING.md` moved **off the boot path** — read on demand when a KRING/org question comes up, not every session. `SCHEDULES.md` stays at boot (job self-heal needs it).
- `agent-files/AGENTS.md` — new **Keep the boot bundle lean** section codifies the rule: boot files hold only what's needed in-hand every session; procedures and reference go to `runbooks/`.
- `agent-files/SCHEDULES.md` — the weekly **update check** now also runs a context-budget check (`openclaw doctor`); on truncation it moves detail to `runbooks/` rather than letting `MEMORY.md` drop. Standing guard so the bundle can't silently regrow. Also trimmed prose that re-explained the jobs table.
- `agent-files/EVALS.md` — pass/fail contract updated to match: verify evals no longer fail an answer for lacking a source ref (only for fabrication / answering without checking); labels renamed from the old procedure names.
- `agent-files/runbooks/building-automations.md` — pointer updated to the renamed habit.

**Runbooks consolidated + repurpose/update now delivers onboarding.**

- **Runbooks moved into the agent's reach.** `updating-an-agent.md`, `repurposing-an-existing-agent.md`, `syncthing-local-mirror.md`, and `migrations/ms-to-google.md` moved from the repo-root `runbooks/` into `agent-files/runbooks/`. `AGENTS.md`/`TOOLS.md` pointed agents at `runbooks/…`, but those files lived outside the agent's workspace, so the pointers didn't resolve for a deployed agent. Root operator docs (`activation-kring.md`) updated to the new paths.
- **Repurposed users now get the full onboarding, not just an upgrade note.** `repurposing-an-existing-agent.md` Part B rewritten: a repurposed agent runs the same onboarding *beats* as `BOOTSTRAP.md` (core features, best practices, the optional email-draft demo and first-automation) — it just skips the identity collection it already has. Rule: *deliver the onboarding, skip the introductions.* Fixes users being quietly dropped onto Personal Workspace and never shown what it means.
- `updating-an-agent.md` — added step 7: if an update reaches a user who never received the onboarding (repurposed/updated before the flow existed), run the continuity-aware onboarding rather than a one-line what's-new.
- Stale counts fixed: "five cron jobs" → seven (`updating-an-agent.md`), "four standard jobs" → seven (`repurposing-an-existing-agent.md`), "eight prompts" → count-agnostic (`EVALS.md`).

---

## [1.0.1] — 2026-06-08

Completes and fixes what Beta + 1.0 already promised — reliable meeting prep, real calendar management, the refined email-triage/brief rhythm, and an automation-building guide. Shipped as a patch: no new roadmap scope (1.1 is reserved for the NEXT features — Slack, Obsidian brain, techstack, onboarding flow, repurpose, Cosmica MCP). No per-user state shape change, so no migration; existing agents pick it up via the catch-up loop plus a "what's new" message for the user-visible changes.

### Changed — Email triage & brief rhythm

Reshapes how the agent handles mail and how the daily/weekly briefs split. User-visible capability change → requires a "what's new" message on catch-up (see `agent-files/AGENTS.md`). No per-user state shape change → no migration.

- `agent-files/SCHEDULES.md` — daily brief moves to **08:00 every day** (was weekdays 07:30); weekly review moves to **Mondays 08:00**. New sixth job **Inbox triage** — every 30 min, 24/7 (silent outside 08:00–18:00, so drafts are ready overnight without pinging). Heartbeat now runs every day and explicitly cedes email to the triage job. Updated the "five → six" counts and added the daily-brief↔triage rhythm note.
- `agent-files/templates/email-draft.md` — new **Triage mode**: the agent drafts ~95% of mail **straight into the Gmail Drafts folder** and marks **only the drafted emails** as read; everything it doesn't draft stays unread and flagged. Existing per-email Telegram approval is retained as **Interactive mode**. Still never sends without approval.
- `agent-files/templates/daily.md` — brief now summarises triage output: *Drafts ready to review (N)*, *Left for you (M — not drafted)*, *Still in Drafts from before* (day-after reminder for unsent drafts), plus tasks/reminders. Email is summarised, never pasted.
- `agent-files/templates/weekly.md` — explicitly **email-free big picture**: added *Open commitments* and *Week ahead — milestones & events*; reinforced that individual emails belong in the daily brief only.
- `agent-files/AGENTS.md` — added an *Inbox triage* operations subsection; updated *Daily brief* (08:00, all week, draft summary) and the scheduled-jobs list/counts.
- `playbook.md` — user-facing "what it does" and "working rhythm" updated to the 8:00 all-week brief + all-day Gmail-Drafts triage model.

### Fixed — Meeting prep now actually fires

The v1.0 meeting-prep capability was defined in `AGENTS.md` but had no real trigger — it rode the hourly heartbeat, whose "skip routine standups" filter swallowed it, and which never ran before 08:00. In practice prep rarely arrived. Now on two dedicated triggers, no per-user state change.

- `agent-files/SCHEDULES.md` — new seventh job **Meeting prep**: every 15 min, 06:00–22:00, every day. Fires ~30 min before any meeting with other attendees, once per meeting. Heartbeat row updated to cede meeting prep to it. "Six → seven" counts updated.
- `agent-files/AGENTS.md` — rewrote *Meeting prep*: two layers (morning pass in the 08:00 brief + just-in-time job), preps **all** meetings with attendees incl. recurring standups, skips solo/all-day/declined, fires once per meeting (event ID logged in the daily memory file), read-only.
- `agent-files/templates/meeting-prep.md` — **new** template: who / context / your angle / handy links, with a collapsed one-line variant for the daily brief.
- `agent-files/templates/daily.md` — Calendar section now carries the morning prep note per meeting (who + the one thing to know), covering early meetings.
- `agent-files/onboarding/BOOTSTRAP.md`, `runbooks/updating-an-agent.md` — register seven jobs, not six.
- `agent-files/EVALS.md` — new golden prompt #9: prep fires for a routine standup and flags an external attendee.

### Added — Calendar management

The Beta sheet promised calendar "orchestration" but v1.0 only read the calendar and accepted/declined invites with permission. Now the agent actively manages time. No per-user state change.

- `agent-files/AGENTS.md` — new *Calendar management* subsection. Permission line: **own time is free to manage; anything touching other people asks first.** No-ask = read calendar, read others' free/busy in the venture workspace, block own focus time, draft proposed times. Ask-first = create/move/cancel meetings with attendees, send booking invites, accept/decline. Documents the two moves the user wants: booking-style invites (offer 2–3 slots, attendees pick) and read-the-room scheduling (check workspace free/busy, propose the least-disruptive slot). Permission table gains four rows.
- `agent-files/HEARTBEAT.md` — calendar section refocused from per-meeting prep (now its own job) to **calendar load**: conflicts, back-to-back days, no deep-work/lunch — with an offer to block focus time.
- `playbook.md` — new user-facing *Manages your calendar* capability + four permission-table rows.
- `agent-files/EVALS.md` — new golden prompt #10: agent blocks own focus time without asking but asks before moving a meeting with attendees.

### Added — Automation-building guide

v1.0 had a place to *log* automations (`AUTOMATIONS.md`) but no *how-to* — the agent had no consistent build process and users had no idea what to ask for. No per-user state change.

- `agent-files/runbooks/building-automations.md` — **new**. What counts as an automation + what's buildable on the stack (digests, reminders/escalations, inbox rules, calendar reactions, Notion triggers); a five-step build process (confirm scope → check permission line → build as cron/event job → log with rollback → test + confirm); act-vs-ask guidance; and change/remove discipline (respect "off").
- `agent-files/AGENTS.md` — new *Building automations* subsection in the Operations layer pointing at the runbook, with the act-then-confirm vs ask-first line.
- `playbook.md` — *Builds automations* expanded with example asks so users know what's possible.
- `agent-files/EVALS.md` — new golden prompt #11: agent confirms scope, logs with rollback, and refuses to silently schedule mail to other people.

### Migrations
- None — no per-user state shape change. Existing agents pick up the new behaviour, the new seventh cron job (Meeting prep, self-healed at boot like the others), and the new/updated templates on next session boot via the catch-up loop in `agent-files/AGENTS.md`, plus a "what's new" message for the user-visible changes.

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
