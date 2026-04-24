# Personal Workspace — Onboarding

How a new user gets onboarded onto Personal Workspace.

The flow has two halves:

1. **Setup** — a human sets up the environment and spins up the OpenClaw agent.
2. **Agent-led onboarding** — the OpenClaw agent itself runs the first-session conversation with the user (via `agent-files/onboarding/BOOTSTRAP.md`).

---

## What beta ships

- **Personal OpenClaw assistant on Telegram** — memory across sessions, scoped to work.
- **Daily brief** (morning) — calendar, top priorities, anything urgent.
- **Weekly brief** (Friday EOD) — open commitments, things they're waiting on, patterns.
- **Heartbeats** — periodic background check-ins; surfaces things only when they need attention.
- **Tool reach** — Gmail, Calendar, Drive, Slack, Notion, GitHub.
- **Drafting** — emails, messages, docs. Never sent without the user's OK.
- **Automations** — built on request.

Each future version updates this block. Source of truth: `CHANGELOG.md`.

---

## Part 1 — Setup (human-led, one-time)

Done once per new user, before they talk to their agent.

### 1. Provision the user's KRING Workspace accounts

- **Google Workspace** account (`@kringventures.com` or the relevant domain).
- **Slack** invite to the KRING workspace.
- **Notion** invite to the KRING Ventures workspace.
- **GitHub** invite to the `KRING-Ventures` org (if relevant to their role).
- **Telegram** — they use their existing personal Telegram; they'll authorise the OpenClaw bot during wire-up.

### 2. Create the user's private personal-layer repo

Each user has their own **private GitHub repo** for their personal OpenClaw agent layer (IDENTITY, USER, TOOLS, automations, memory).

- The user (or Corey) creates the repo. Name it whatever makes sense — no mandated convention.
- Seed it from `personal-workspace-speedblock/agent-files/` — copy the per-user blueprints (`IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/AUTOMATIONS.md`, empty `MEMORY.md`, empty `memory/`, empty `STATE_VERSION`). Leave `{{FROM_BOOTSTRAP}}` markers in place — the agent fills them in.

### 3. Wire the OpenClaw runtime

Per-user deployment of the OpenClaw agent on Telegram. Owned by Corey.

- Deploy a new OpenClaw instance scoped to this user.
- Point it at both file-layer sources: the shared framework (`KRING-Ventures/personal-workspace-speedblock/agent-files/`) and the user's private repo.
- Connect Telegram (bot token, chat binding).

### 4. Hand off to the agent

Send the user the Telegram handle and tell them: **start the first conversation**. The agent runs the rest.

---

## Part 2 — Agent-led onboarding

The user sends a first message. The OpenClaw agent runs `agent-files/onboarding/BOOTSTRAP.md` — a structured conversation where it introduces itself, walks the user through wiring up tools one at a time, pulls everything it can from those tools into `USER.md`, and fills the human gaps in conversation.

**The agent runs this. No human intermediary.** Don't pre-fill `USER.md`, don't wire tools on the user's behalf, don't run BOOTSTRAP "for" them — it's a conversation between the agent and its user. That's where the relationship starts.

Full script: `agent-files/onboarding/BOOTSTRAP.md`.

---

## References

- `agent-files/onboarding/BOOTSTRAP.md` — full agent-led script.
- `agent-files/AGENTS.md` — session boot + operational rules.
- `agent-files/TOOLS.md` — per-user tool table filled during BOOTSTRAP.
- `playbook.md` — what Personal Workspace is.

---

*Current version: beta (shipped 2026-04-23).*
