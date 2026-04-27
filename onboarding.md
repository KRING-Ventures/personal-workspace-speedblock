# Personal Workspace — Onboarding

How a venture activates Personal Workspace and gets running.

This document is read by two people:

- **The venture** activating the Speedblock — for *what to send us in the intake* (Step 1) and *how to roll out* (Step 3).
- **The user** being onboarded — for *what to expect when your assistant says hello* (Step 3).

The flow has three steps:

1. **Activate the Speedblock** *(you, the venture)* — send us the intake.
2. **Build & deploy** *(KRING)* — we deploy one assistant per user.
3. **Finish onboarding** *(you, the venture, with each of your users)* — roll out and let each user's first conversation happen.

When Step 3 wraps, you have a fully functioning Personal Workspace.

---

## What this version ships

- **A personal AI assistant on Telegram** for each user — remembers them across conversations, scoped to their work.
- **Daily brief** (morning) — calendar, top priorities, anything urgent.
- **Weekly brief** (Monday morning) — open commitments, things they're waiting on, patterns worth noticing.
- **Heartbeats** — periodic background check-ins; only surface things when they actually need attention.
- **Tool reach** — Gmail, Calendar, Drive, Notion, GitHub, plus any other tools wired during the first conversation.
- **Drafting** — emails, messages, documents. Always drafts first; never sends without the user's OK.
- **Automations** — built on request.

Source of truth for what's in each version: `CHANGELOG.md`.

---

## Step 1 — Activate the Speedblock (you, the venture)

To activate, send us one intake with everything we need to deploy.

Once for your venture as a whole:

- Confirm your tenants are in place — Google Workspace, Slack, Notion, GitHub. These are the fixed beta tech stack: every Personal Workspace deployment runs on these. We don't provision into your tenants; that's on you.

For each user you're onboarding, send us:

- Their full name and primary email.
- Confirmation their accounts are live in your tenants (Google Workspace, Slack, Notion, GitHub if it's relevant to their role).
- Their Telegram handle (e.g. `@august`). They need to have Telegram installed on a device they use day-to-day.
- The name they want for their assistant (e.g. `Ida`, `Kerstin`). One assistant per user. Vibe and personality come out of their first conversation; only the name is decided up front.

We don't start deployment until the intake is complete. If anything's missing, we'll bounce it back.

*Tools beyond the standard stack* — anything venture-specific a user wants their assistant to reach (e.g. Linear, Figma) — get wired by the user with their assistant after deployment, not at intake.

---

## Step 2 — Build & deploy (KRING)

We use your intake to deploy one assistant per user. For each:

- Spin up an OpenClaw runtime instance.
- Set up the assistant's local working files from the framework's per-user blueprints (`IDENTITY`, `USER`, `TOOLS`, `automations/`, empty `MEMORY`, empty `memory/`, `STATE_VERSION`). The blueprints carry `{{FROM_BOOTSTRAP}}` markers — the assistant fills those in during the first conversation.
- Set the assistant's name from your intake.
- Wire Telegram (bot binding).
- Confirm the assistant is reachable on Telegram.

When all the assistants are live, we hand you back a list of assistant Telegram handles — one per user.

From there, the rest is yours.

---

## Step 3 — Finish onboarding (you, the venture, with each of your users)

Now you roll the assistants out to your users. For each one:

- Hand them their assistant's Telegram handle.
- Point them at the playbook so they know what they're getting.
- Tell them to send the first message — their assistant will guide them through the rest.

When a user sends the first message, their assistant runs a structured first conversation:

- Introduces itself.
- Walks the user through connecting their tools one at a time (Gmail → Calendar → Drive → Notion → GitHub, plus any other tools they use).
- Reads what it can from each.
- Asks a few questions to fill in the parts tools can't tell it (how the user makes decisions, what they want their assistant to push back on, how they communicate, etc.).

This is a real conversation, not a form. The user takes their time. You support the rollout — coordinating who goes first, fielding questions — but you don't run the first conversation yourself; that's between each user and their assistant.

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
