# Personal Workspace — Onboarding

How you activate Personal Workspace and get your team running.

Three steps:

1. **Activate** — you send us the intake.
2. **Build & deploy** — we deploy one assistant per user.
3. **Finish onboarding** — you roll out to your users, each one runs their first conversation.

When Step 3 is done, you have a fully functioning Personal Workspace.

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

## Step 1 — Activate

Send us one intake with everything we need to deploy.

Once for your venture as a whole:

- Confirm your tenants are in place — Google Workspace, Slack, Notion, GitHub. These are the fixed beta tech stack. We don't provision into your tenants; that's on you.

For each user:

- Their full name and primary email.
- Confirmation their accounts are live in your tenants (Google Workspace, Slack, Notion, GitHub if relevant to their role).
- Their Telegram handle (e.g. `@maria`). They need Telegram installed on a device they use day-to-day.
- The name they want for their assistant (e.g. `Ida`, `Kerstin`). One assistant per user. Vibe and personality come out of the first conversation; only the name is decided up front.

**How to send it.** Email or message the intake to your KRING contact (the person you've been coordinating with). One document or message with one section per user works fine. We don't start until the intake is complete — if anything's missing, we'll let you know what's still needed.

*Tools beyond the standard stack* — anything venture-specific (e.g. Linear, Figma) — get wired by the user with their assistant after deployment, not at intake.

---

## Step 2 — Build & deploy (KRING)

We take your intake and deploy one assistant per user. For each:

- Spin up an OpenClaw runtime.
- Load the framework's onboarding templates so the assistant knows how to run the first conversation.
- Set the assistant's name from your intake.
- Wire Telegram.
- Confirm the assistant is reachable.

When all the assistants are live, we send you a list of Telegram handles — one per user — back through the same channel you used for the intake.

From there, the rest is yours.

---

## Step 3 — Finish onboarding

You roll the assistants out to your team, one user at a time. For each user:

1. **Send them their assistant's Telegram handle** (e.g. `@ida_kring`). Use Slack, email, or whatever channel you normally use with your team — we don't prescribe a format.
2. **Share `playbook.md` with them** so they know what Personal Workspace is before they start. Send the link from this repo, or a copy your team mirrors internally.
3. **Tell them to open Telegram, find the assistant by the handle, and send any message to start.** Their assistant introduces itself and runs the first conversation from there — about 30–45 minutes, real conversation, not a form. The assistant walks them through wiring up their tools (Gmail, Calendar, Drive, Notion, GitHub) one at a time, and asks the few questions tools can't answer (how they make decisions, what to push back on, how they communicate).

That's your part. The first conversation runs between the user and their assistant directly — you're not in it. You coordinate the rollout (who goes first, field questions on the side) but the conversation itself is between the two of them.

---

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Read this if you're new.
- `human-roles.md` — who does what in the three steps above.
- `agent-files/onboarding/BOOTSTRAP.md` — the full script each assistant follows in the first conversation.
- `agent-files/AGENTS.md` — session boot and operational rules (assistant-side; useful if you want to understand how it works under the hood).
- `agent-files/TOOLS.md` — per-user tool table; filled in during the first conversation.

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
