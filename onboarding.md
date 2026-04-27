# Personal Workspace — Onboarding

How a new user gets onboarded onto Personal Workspace.

The flow has two halves:

1. **Setup** — a human sets up the environment and spins up the OpenClaw agent.
2. **Agent-led onboarding** — the OpenClaw agent itself runs the first-session conversation with the user (via `agent-files/onboarding/BOOTSTRAP.md`).

---

## What 0.1.2 ships

- **Personal OpenClaw assistant on Telegram** — memory across sessions, scoped to work.
- **Daily brief** (morning) — calendar, top priorities, anything urgent.
- **Weekly brief** (Friday EOD) — open commitments, things they're waiting on, patterns.
- **Heartbeats** — periodic background check-ins; surfaces things only when they need attention.
- **Tool reach** — Gmail, Calendar, Drive, Notion, plus any user-specific tools wired during onboarding.
- **Drafting** — emails, messages, docs. Never sent without the user's OK.
- **Automations** — built on request.

Each future version updates this block. Source of truth: `CHANGELOG.md`.

---

## Part 1 — Setup (human-led, one-time)

Done once per new user, before they talk to their agent.

### Prerequisites — the venture's environment must already exist

Before any of the steps below run, the user's tenants must already be set up. The account provisioner (see `human-roles.md`) owns this:

- For **KRING-internal users**, KRING ops/admin handles it against KRING's tenants.
- For **venture deployments**, the *venture itself* is responsible. They must already have Google Workspace (or equivalent), Slack, Notion, GitHub, and any venture-specific tools the agent will need to reach — KRING does not provision into a venture's accounts.

If any of those tenants are missing, runtime wire-up doesn't start. It bounces back to the venture (or KRING ops) until the environment is in place.

### 1. Provision the user's workspace accounts

Issued by the account provisioner against the relevant tenants:

- **Google Workspace** account on the venture's domain (e.g. `@kringventures.com` for KRING-internal users; the venture's own domain otherwise).
- **Slack** invite to the relevant Slack workspace (KRING's, or the venture's).
- **Notion** invite to the relevant Notion workspace.
- **GitHub** invite to the relevant org (if relevant to their role).
- **Telegram** — they use their existing personal Telegram; they'll authorise the OpenClaw bot during wire-up.
- Any **venture-specific tools** the user needs day-to-day that the agent should be able to reach.

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

*Current version: 0.1.2 (shipped 2026-04-24).*
