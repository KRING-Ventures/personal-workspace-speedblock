# Personal Workspace — Onboarding

How a new user gets onboarded onto Personal Workspace.

The flow has two halves:

1. **Setup** — a human sets up the environment and spins up the OpenClaw agent.
2. **Agent-led onboarding** — the OpenClaw agent itself runs the first-session conversation with the user (via `agent-files/onboarding/BOOTSTRAP.md`). This is where the agent learns the user.

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

- The user (or Corey) creates the repo in `KRING-Ventures/` or their personal GitHub account.
- Name it whatever makes sense to the user — there's no mandated naming convention.
- Seed it from the template files in `personal-workspace-speedblock/agent-files/` — copy over the per-user blueprints (`IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/AUTOMATIONS.md`, empty `MEMORY.md`, empty `memory/`, empty `STATE_VERSION`). Leave `{{FROM_BOOTSTRAP}}` markers in place — the agent fills them in during BOOTSTRAP.

### 3. Wire the OpenClaw runtime

This is the per-user deployment of the OpenClaw agent on Telegram. Owned by Corey (platform / agent infra).

- Deploy a new OpenClaw instance scoped to this user.
- Point it at the two file-layer sources:
  - **Shared framework:** `KRING-Ventures/personal-workspace-speedblock`, under `agent-files/`.
  - **Personal layer:** the user's own private repo (from step 2).
- Connect Telegram (bot token, chat binding).
- Agent is now live but not yet onboarded.

### 4. Hand off to the agent

Send the user the Telegram handle of their new agent and tell them: **start the first conversation**. The agent runs the rest.

---

## Part 2 — Agent-led onboarding (the OpenClaw agent runs it)

The user sends a first message. The OpenClaw agent runs `agent-files/onboarding/BOOTSTRAP.md` as a structured conversation. This is not a checklist Corey works through — it's the agent's job.

### Why agent-led

Most of what a personal agent needs to know about its user — name, role, projects, contacts, working patterns — can be **pulled from the user's own tools** (Gmail profile, Calendar patterns, Drive/Notion activity, GitHub repos). Asking the user to type that out manually is friction. So the flow is **tools first, then context**.

### BOOTSTRAP phases (summary)

See `agent-files/onboarding/BOOTSTRAP.md` for the full script. Four phases:

**Phase 1 — Open.** Agent introduces itself: who it is (personal OpenClaw agent, distinct from Cosmo), what it can do, what it won't do without permission, and how the session will flow.

**Phase 2 — Wire the tools.** User-led tool authorisation, one tool at a time. Priority order: Gmail → Calendar → Drive → Slack → Notion → GitHub. Each wire-up is tested with a real action before moving on. `TOOLS.md` flips from `❌ Not connected` to `✅ Connected` per tool.

**Phase 3 — Pull the draft.** Agent reads the newly-connected tools and drafts `USER.md` with everything it could infer (name, role, projects, contacts, timezone, calendar patterns, communication style from recent mail). Every pulled field is annotated with its source.

**Phase 4 — Validate and fill the human gaps.** Agent walks the draft with the user, who corrects and extends. Then agent asks the handful of things data can't tell it: how the user thinks, what they want the agent to push back on, communication preferences, anything the agent should avoid.

**Close.** Agent sets its own `STATE_VERSION`, writes the first daily memory log, confirms next steps (morning brief tomorrow, heartbeat cadence). Commits and pushes.

### What "onboarded" means

After BOOTSTRAP completes, the agent has:
- `IDENTITY.md` — its name, vibe, emoji (user's choice).
- `USER.md` — filled from pulled data + user validation.
- `TOOLS.md` — flipped to `✅ Connected` for every wired tool, notes on scope.
- `MEMORY.md` — seeded with the essentials from the session.
- `memory/YYYY-MM-DD.md` — first daily log written.
- `STATE_VERSION` — set to the current framework version.

From here it runs the catch-up loop in `AGENTS.md` every subsequent session.

---

## What NOT to do during onboarding

- **Don't** have Corey (or anyone else) write the user's `USER.md` up-front. The agent fills it from tools + conversation. Pre-filling skips the real value of BOOTSTRAP.
- **Don't** let a central operator run BOOTSTRAP "on behalf of" the user. BOOTSTRAP is a conversation between the agent and its user. No intermediaries.
- **Don't** wire every tool before the user has said yes to each one. User-led authorisation matters.
- **Don't** skip the "test the connection" step after each wire-up. Auth handshake succeeded ≠ tool actually works.

---

## If BOOTSTRAP stalls

- **Tool wire-up fails:** leave the row as `❌` in `TOOLS.md`, capture the error, move on. Don't loop on retry. User can ask agent to wire it later.
- **User wants to stop partway:** fine. Agent saves progress (commits whatever's done), notes where it stopped, and picks up next session.
- **User skips Phase 4:** `USER.md` stays partial with explicit `[needs Phase 4]` markers. Agent operates with what it has and extends over time.

---

## References

- `agent-files/onboarding/BOOTSTRAP.md` — full agent-led script.
- `agent-files/AGENTS.md` — session boot + operational rules.
- `agent-files/TOOLS.md` — the per-user tool table that gets filled during BOOTSTRAP.
- `playbook.md` — what Personal Workspace is.

---

*Current version: beta (shipped 2026-04-23).*
