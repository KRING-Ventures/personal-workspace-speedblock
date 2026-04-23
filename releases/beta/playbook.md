# Personal Workspace — Playbook

The operating manual for Personal Workspace: what it is, the tech stack it runs on, the four AI layers, and the OpenClaw agent at the centre of it.

---

## What Personal Workspace is

A standardised, AI-native work environment for every person at KRING Ventures (and the companies KRING builds).

It replaces the ad-hoc mix of tools each person used to assemble on their own with a **shared, opinionated stack** — and puts an **OpenClaw agent** in front of the whole thing so the stack feels like a partner, not a toolbelt.

The goal: every user at KRING gets the same baseline productive environment on day one, connected to the same AI layers, with a personal agent that already knows the org and learns them over time.

---

## The tech stack

The locked stack for Personal Workspace. New users are set up against this exactly — no substitutions without explicit scope change.

### Productivity — Google Workspace

The primary workspace for documents, files, mail, calendar, and meetings.

| Surface | Use |
|---|---|
| **Drive** | Files, folders, shared org drive |
| **Docs / Sheets / Slides** | Documents, spreadsheets, decks |
| **Email** (Gmail) | Primary inbox |
| **Calendar** (+ meeting booking) | Scheduling, availability, booking links |
| **Meetings** (Google Meet) | Calls |

### Agent surface — Telegram

Where each user talks to their **personal OpenClaw agent**. One-to-one chat, always-on, cross-device.

### Project management — Notion

KRING Ventures workspace. Project pages, tasks, Speedblocks, PM databases.

### Code & agent files — GitHub

Each user's personal OpenClaw agent files live in their own private GitHub repo. The shared framework + speedblock deliverables live in public KRING-Ventures repos.

### AI — Claude

General-purpose AI for writing, thinking, analysis. Distinct from the OpenClaw agent.

### Team chat — Slack

Real-time team communication. Not the surface for personal agent conversations — that's Telegram.

---

## The four AI layers

Personal Workspace includes four AI layers. Each has a distinct job. Don't conflate them.

| Layer | Where it lives | Who owns it | Job |
|---|---|---|---|
| **Gemini** | Inside Google Workspace | Google | In-product AI inside Docs, Sheets, Gmail — quick summaries, drafting inside the doc, smart compose. Stays in-app. |
| **Claude** | Standalone (claude.ai, API) | Anthropic | General-purpose reasoning, writing, coding help. The model you reach for outside any specific tool. |
| **OpenClaw** (personal) | Telegram | Each user | Your **personal agent**. Memory across sessions, wired into your tools, runs drafts and briefs and operations on your behalf. Work-scoped. |
| **Cosmo** | Slack (KRING channels) | KRING (shared) | The **shared KRING-org agent**. One instance for the whole organisation. Org-level context, Speedblock work, cross-user coordination. |

The split matters because the wrong layer in the wrong place creates friction. Use:
- **Gemini** for tasks that never leave the Google app you're already in.
- **Claude** for thinking work that isn't tied to a specific tool or person.
- **OpenClaw** for anything personal that needs memory and tool reach.
- **Cosmo** for anything org-shared, cross-user, or Speedblock-related.

---

## The OpenClaw agent — purpose and capabilities

OpenClaw is the agent at the centre of Personal Workspace. Each user gets their own personal instance. This is the layer that makes the stack feel like a partner.

### Purpose

A personal assistant for **work**: a thinking partner, hands-on operator, and institutional memory — scoped to the user's professional life, not life-outside-work.

### Capabilities

**Memory**
- Daily logs per session in `memory/YYYY-MM-DD.md`.
- Curated long-term memory in `MEMORY.md`.
- Context persists across sessions and surfaces.

**Daily and weekly briefs**
- Morning brief: today's calendar, top priorities, urgent items from inbox/Slack.
- Friday EOD / Monday review: open commitments, waiting-on items, patterns from the week.

**Drafting**
- Emails, messages, documents. Always drafts first; **never sends without explicit approval**.

**Tool reach**
- Google Workspace (Gmail, Calendar, Drive, Docs).
- Slack.
- Notion.
- GitHub.
- Telegram (its own surface).

**Operations layer**
- Track open commitments and follow-up loops.
- Meeting prep (who, what's relevant, what to accomplish) for non-trivial meetings.
- Surface things only when they actually need attention — no nagging.

**Heartbeats**
- Periodic background polls (cron-driven).
- Silent unless something requires attention — urgent email, upcoming meeting needing prep, stalled commitment.

**Automations**
- User can ask the agent to automate recurring work.
- The agent has a skill for building new automations.

### Permission model (default)

| Action | Permission |
|---|---|
| Read anything in the workspace | None |
| Draft messages or documents | None |
| Organise / search / research | None |
| Send email, post in Slack, reply to messages | **Ask first** |
| Accept/decline calendar invites | **Ask first** |
| Write to another person's Notion page | **Ask first (per-action)** |
| Any irreversible or externally-visible action | **Ask first** |

See `agent-files/AGENTS.md` for the full permission table and operational rules.

### What day one looks like vs. grows into

**Day one** (after BOOTSTRAP): agent knows your name, role, top projects, key contacts, meeting cadence, and working-hour patterns — all pulled from your tools during onboarding, not typed by you. Tools are wired. It can read and draft and remember.

**Over time**: the agent learns your preferences, communication style, decision patterns, recurring workflows. Memory compounds. Automations get built for repetitive work. The morning brief and weekly review become real operational backbone.

---

## Working rhythm

### Daily
- Morning: OpenClaw delivers the daily brief (calendar + top priorities + anything urgent).
- Throughout the day: use OpenClaw for drafting, research, context recall, inbox triage. Use Gemini inside Docs/Sheets. Use Claude for standalone thinking work. Cosmo lives in Slack for org-level work.
- End of day: OpenClaw writes the daily memory log.

### Weekly
- Friday EOD or Monday morning: OpenClaw offers a weekly review (open commitments, waiting-on items, calendar overview, patterns).

### Per-session
- Agent pulls latest from GitHub at session start (framework + personal layer).
- Agent pushes after every meaningful change. Uncommitted local state is not a valid save.

---

## Two agent layers — don't mix

- **OpenClaw (personal)** is yours. Lives in Telegram. Knows you specifically. Work-scoped. One instance per user.
- **Cosmo (shared)** is KRING's. Lives in Slack. Knows the org. Shared across users.

Don't ask OpenClaw to take org-wide actions. Don't ask Cosmo to remember personal context. Different memory, different surface, different purpose.

---

## References

- `agent-files/` — the shared framework file set (SOUL, AGENTS, KRING, HEARTBEAT, IDENTITY template, USER template, TOOLS template, memory templates, working templates, BOOTSTRAP).
- `onboarding.md` — how a new user gets set up with Personal Workspace.
- `agent-files/onboarding/BOOTSTRAP.md` — the agent-led first-session script.
- `agent-files/AGENTS.md` — full operational rules for the OpenClaw agent.
- `releases/beta/` — frozen snapshot of what shipped at the beta milestone.

---

*Current version: beta (shipped 2026-04-23). Next version: 1.0.*
