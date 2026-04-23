# Personal Workspace — Playbook

Personal Workspace is KRING's standardised AI-native work environment: a shared tech stack, four AI layers, and a personal OpenClaw agent per user. This is the operating manual.

*DRI: August. Version: beta (2026-04-23).*

---

## Principles

- **Standardised stack, personal layer.** Everyone runs the same tools and AI layers. Your OpenClaw agent is the personal layer on top.
- **AI-native by default.** If an AI layer can do it, delegate to it. Humans approve irreversible or externally-visible actions.
- **Written down, or it doesn't exist.** Handbook, Notion, and GitHub are source of truth. Tribal knowledge is a bug.
- **Push as you go.** Uncommitted work is not saved. Agent and human push every meaningful change same-session.
- **Named concepts, shared vocabulary.** Use the exact terms (Speedblock, Personal Workspace, OpenClaw, Cosmo). See Glossary.

---

## The stack

Locked. No substitutions without an explicit scope change.

| Purpose | Tool |
|---|---|
| Documents, files, mail, calendar, meetings | **Google Workspace** (Drive, Docs, Gmail, Calendar, Meet) |
| Personal AI agent | **OpenClaw on Telegram** |
| Shared org AI agent | **Cosmo on Slack** |
| In-app AI | **Gemini** (inside Google) and **Claude** (standalone) |
| Project management | **Notion** (KRING Ventures workspace) |
| Code and agent files | **GitHub** (`KRING-Ventures/` + each user's private personal-layer repo) |
| Team chat | **Slack** |

---

## The four AI layers

Distinct jobs. Don't conflate them.

| Layer | Surface | Job |
|---|---|---|
| **Gemini** | Inside Google apps | In-app summaries and drafting. Stays where it lives. |
| **Claude** | claude.ai, API | General reasoning, writing, coding help. No memory between sessions. |
| **OpenClaw** (personal) | Telegram, 1:1 | Your personal agent. Memory, tool reach, briefs, drafts, automations. Work-scoped. |
| **Cosmo** (shared) | Slack, KRING channels | Shared org agent. Speedblock work, cross-user coordination. |

Use the lowest-friction layer for the job: Gemini inside a Doc, Claude for a one-off, OpenClaw for anything personal with memory, Cosmo for anything org-shared.

---

## OpenClaw — your personal agent

One instance per user. Your partner for work.

### What it does

- **Memory.** Daily logs in `memory/YYYY-MM-DD.md`. Curated long-term `MEMORY.md`. Context persists across sessions.
- **Briefs.** Morning (calendar, priorities, urgent items). Weekly (open commitments, waiting-on, patterns).
- **Drafts.** Emails, messages, documents. Always drafts; never sends without approval.
- **Tool reach.** Google Workspace, Slack, Notion, GitHub, Telegram.
- **Operations.** Tracks open commitments and follow-ups. Preps non-trivial meetings. Surfaces only what needs attention.
- **Automations.** Builds recurring workflows on request.

### Permission model

| Action | Permission |
|---|---|
| Read, search, draft, research | None |
| Send email, post in Slack, reply to messages | **Ask first** |
| Accept or decline calendar invites | **Ask first** |
| Write to another person's Notion page | **Ask first (per-action)** |
| Any irreversible or externally-visible action | **Ask first** |

Full rules in `agent-files/AGENTS.md`.

### Day one vs over time

- **Day one (after BOOTSTRAP):** knows your name, role, top projects, key contacts, meeting cadence — pulled from your tools during onboarding, not typed by you. Tools wired. Can draft and remember.
- **Over time:** learns preferences, decision patterns, recurring workflows. Memory compounds. Automations get built.

---

## Working rhythm

- **Daily.** Morning brief from OpenClaw → drafting, research, recall throughout the day → end-of-day memory log.
- **Weekly.** Friday EOD or Monday AM weekly review (open commitments, waiting-on, calendar, patterns).
- **Per-session.** Agent pulls from GitHub at start, pushes after every meaningful change. Uncommitted state is not a save.

---

## Onboarding

Two halves:

1. **Human setup** — provision Google / Slack / Notion / GitHub / Telegram, create the user's private personal-layer repo, deploy the OpenClaw instance on Telegram.
2. **Agent-led BOOTSTRAP** — OpenClaw runs the first-session conversation: intro → wire tools one at a time → pull user context from the connected tools → validate and fill the gaps.

Full flow in `onboarding.md`. Script in `agent-files/onboarding/BOOTSTRAP.md`.

---

## Two agent layers — don't mix

- **OpenClaw (personal)** is yours. Telegram. Knows you. Work-scoped. One per user.
- **Cosmo (shared)** is KRING's. Slack. Knows the org. Shared across the company.

Don't ask OpenClaw to take org-wide actions. Don't ask Cosmo to hold personal context. Different memory, different surface, different purpose.

---

## Glossary

- **Personal Workspace** — the standardised AI-native environment every KRING user runs.
- **OpenClaw** — the agent framework. Personal OpenClaw = your instance; Cosmo = the shared KRING instance.
- **Speedblock** — KRING's delivery unit for a bounded project (Scope → Research → Solution → Build).
- **BOOTSTRAP** — the agent-led first-session script that onboards a user into their OpenClaw agent.
- **Heartbeat** — periodic background poll by the agent; silent unless something needs attention.
- **Shared framework** — `personal-workspace-speedblock/agent-files/`, the living source of truth for every agent.
- **Personal layer** — each user's private repo with IDENTITY, USER, TOOLS, automations, and memory.

---

## Meta

- **DRI:** August.
- **Edit:** PR against `main` in `KRING-Ventures/personal-workspace-speedblock`. Conciseness is a hard constraint — if a change doesn't alter how someone acts, don't add it.
- **Version:** beta (2026-04-23). Next: 1.0.
- **Changelog:** `CHANGELOG.md`.
