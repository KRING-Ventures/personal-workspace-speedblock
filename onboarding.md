# Personal Workspace — Onboarding

How your venture gets onboarded onto Personal Workspace.

Throughout this doc:

- **You / your venture** — the venture activating Personal Workspace and rolling it out to its team. The reader.
- **KRING / we** — the deploying party. We build and deploy one assistant per person at your venture, then hand them back to you.
- **Your team / your users** — the people at your venture being onboarded, one personal AI assistant each.

Three steps:

1. **Activate** — you send us the intake.
2. **Build & deploy** — we deploy one assistant per user.
3. **Finish onboarding** — you roll the assistants out to your team; each team member runs a first conversation with their own assistant on Telegram.

When Step 3 is done, your venture is running on Personal Workspace.

---

## What this version ships

For each person at your venture, after Step 3:

- **A personal AI assistant on Telegram** — remembers the user across conversations, scoped to the user's work.
- **Daily brief** (morning) — calendar, top priorities, anything urgent.
- **Weekly brief** (Monday morning) — open commitments, what the user is waiting on, patterns worth noticing.
- **Heartbeats** — periodic background check-ins; only surface things when something actually needs attention.
- **Tool reach** — Gmail, Calendar, Drive, Notion, GitHub, plus any other tools the user wires during the first conversation.
- **Drafting** — emails, messages, documents. Always drafts first; never sends without the user's OK.
- **Automations** — built on request.

Source of truth for what's in each version: `CHANGELOG.md`.

---

## Step 1 — Activate (you)

Send us one intake with everything we need to deploy.

**Once for your venture as a whole:**

- Confirm your tenants are in place — Google Workspace, Slack, Notion, GitHub. These are the fixed beta tech stack. We don't provision into your tenants; that's on you.

**For each user at your venture being onboarded:**

- Their full name and primary email.
- Confirmation the user's accounts are live in your tenants (Google Workspace, Slack, Notion, GitHub if relevant to the user's role).
- The user's Telegram handle (e.g. `@maria`). Telegram must be installed on a device the user uses day-to-day.
- The name the user wants for the assistant (e.g. `Ida`, `Kerstin`). One assistant per user. Vibe and personality come out of the first conversation; only the name is decided up front.

**How to send it.** Email or message the intake to your KRING contact — the person at KRING you've been coordinating with. One document or message with one section per user works fine. We don't start until the intake is complete; if anything's missing, we'll tell you what we still need.

*Tools beyond the standard stack* — anything venture-specific (e.g. Linear, Figma) — get wired by each user with the assistant *after* deployment, not at intake.

---

## Step 2 — Build & deploy (us — KRING)

We take your intake and deploy one assistant per user. For each:

- Spin up an OpenClaw runtime for the user.
- Load the framework's onboarding templates so the assistant knows how to run the first conversation.
- Set the assistant's name from your intake.
- Wire Telegram.
- Confirm the assistant is reachable.

When all the assistants are live, we send you a list of Telegram handles — one per user — back through the same channel you used for the intake.

From there, the rest is yours.

---

## Step 3 — Finish onboarding (you)

You roll the assistants out to your team, one user at a time. For each user at your venture:

1. **Send the user the assistant's Telegram handle** (e.g. `@ida_kring`). Use Slack, email, or whatever channel you normally use with your team — we don't prescribe a format.
2. **Share `playbook.md` with the user** so the user knows what Personal Workspace is before starting. Send the link from this repo, or a copy your team mirrors internally.
3. **Tell the user to open Telegram, find the assistant by the handle, and send any message to start.** The assistant introduces itself and runs the first conversation from there — about 30–45 minutes, real conversation, not a form. The assistant walks the user through wiring up tools (Gmail, Calendar, Drive, Notion, GitHub) one at a time, and asks the few questions tools can't answer (how the user makes decisions, what to push back on, communication preferences).

That's your part. The first conversation runs between the user and the assistant directly — you're not in it. You coordinate the rollout (who goes first, fielding questions on the side) but the conversation itself is between the user and the assistant.

---

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Read this if you're new, or share it with your team in Step 3.
- `human-roles.md` — who does what in the three steps above (the venture, KRING, the user).
- `agent-files/onboarding/BOOTSTRAP.md` — the full script each assistant follows in the first conversation.
- `agent-files/AGENTS.md` — session boot and operational rules (assistant-side; useful if you want to understand how it works under the hood).
- `agent-files/TOOLS.md` — per-user tool table; filled in during the first conversation.

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
