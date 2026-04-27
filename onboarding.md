# Personal Workspace — Onboarding

How a venture activates Personal Workspace and gets running.

The flow has three steps:

1. **Activate the Speedblock** *(venture)* — the venture provides KRING with the information needed to deploy the agents.
2. **Build & deploy** *(KRING)* — KRING builds and deploys the agents to the venture.
3. **Finish onboarding** *(venture)* — the venture distributes the agents to its users; each user has a first conversation with their assistant; setup completes inside that conversation.

When Step 3 wraps, the venture has a fully functioning Personal Workspace.

---

## What this version ships

- **A personal AI assistant on Telegram** for each user — remembers them across conversations, scoped to their work.
- **Daily brief** (morning) — calendar, top priorities, anything urgent.
- **Weekly brief** (Friday) — open commitments, things they're waiting on, patterns worth noticing.
- **Heartbeats** — periodic background check-ins; only surface things when they actually need attention.
- **Tool reach** — Gmail, Calendar, Drive, Notion, plus any other tools wired during the first conversation.
- **Drafting** — emails, messages, documents. Always drafts first; never sends without the user's OK.
- **Automations** — built on request.

Source of truth for what's in each version: `CHANGELOG.md`.

---

## Step 1 — Activate the Speedblock (venture)

To activate, the venture submits one intake to KRING with everything needed to deploy.

Once for the venture as a whole:

- Confirmation that the venture's tenants are in place — Google Workspace (or equivalent), Slack, Notion, GitHub, plus any venture-specific tools the assistants should be able to reach. KRING does not provision into a venture's tenants; that's the venture's responsibility.

For each user being onboarded:

- Full name and primary email.
- Confirmation that the user's accounts are live in the venture's tenants (Google Workspace, Slack, Notion, GitHub if relevant, plus any venture-specific tools the user needs day-to-day).
- The user's Telegram handle (e.g. `@august`). They need to have Telegram installed on a device they use day-to-day.
- How many assistants this user needs. Default is one. Some users may want more — e.g. one for one role and a separate one for another.
- The chosen name for each assistant (e.g. `Ida`, `Kerstin`). Vibe and personality come out of each user's first conversation; only the name is decided up front.

KRING doesn't start deployment until the intake is complete. If anything is missing, that's the venture's job to fix before the next step.

---

## Step 2 — Build & deploy (KRING)

KRING uses the intake to deploy the assistants. For each one:

- Creates the user's private settings repo — a private GitHub repo holding the personal layer of the assistant (`IDENTITY`, `USER`, `TOOLS`, `automations/`, `MEMORY`, `memory/`).
- Seeds the repo from this Speedblock's `agent-files/` per-user blueprints.
- Deploys an OpenClaw runtime instance.
- Sets the assistant's name from the intake.
- Wires Telegram (bot binding).
- Confirms the assistant is reachable on Telegram.

When all the assistants are live, KRING hands the venture a list of assistant Telegram handles — one per user.

From here, the rest is in the venture's hands.

---

## Step 3 — Finish onboarding (venture)

The venture rolls the assistants out to its users. For each user:

- Hand them their assistant's Telegram handle.
- Point them at the playbook so they understand what they're getting.
- Tell them to send the first message — their assistant will guide them through connecting their tools.

When a user sends the first message, their assistant runs a structured first conversation:

- Introduces itself.
- Walks the user through connecting their tools one at a time (Gmail → Calendar → Drive → Notion, plus any other tools they use).
- Reads what it can from each.
- Asks a few questions to fill in the parts tools can't tell it (how the user makes decisions, what they want the assistant to push back on, how they communicate, etc.).

This is a real conversation, not a form. The user takes their time. The venture supports the rollout — coordinating who goes first, fielding questions — but doesn't run the first conversation itself; that's between each user and their assistant.

The full script the assistant follows: `agent-files/onboarding/BOOTSTRAP.md`.

---

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Read this if you're new.
- `human-roles.md` — who does what in the three steps above.
- `agent-files/onboarding/BOOTSTRAP.md` — the full script each assistant follows in the first conversation.
- `agent-files/AGENTS.md` — session boot and operational rules (assistant-side; useful if you want to understand how it works under the hood).
- `agent-files/TOOLS.md` — per-user tool table; filled in during the first conversation.

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
