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

Now you roll the assistants out to your team. For each user:

- Give them their assistant's Telegram handle.
- Send them the message below so they know exactly what to do.

### Hand-off message (paste-ready)

Copy and send this to each user (in Slack, email, or however you communicate with your team — just fill in their name, the handle, and the link):

```
Hi [name] — your AI assistant is ready.

It's on Telegram at @<handle>. Send it any message to get started.

Your assistant will introduce itself and walk you through connecting your
tools (Gmail, Calendar, Drive, Notion, GitHub) — one at a time, with
permission for each — then ask you a few questions tools can't tell it
(how you make decisions, what you want it to push back on, how you
communicate). Block 30–45 minutes when you're ready; it's a real
conversation, not a form.

For context on what Personal Workspace is, read the playbook:
<link to your shared playbook copy, or to the public repo>
```

### What happens in the user's first conversation

For your reference, so you can field questions:

- The assistant introduces itself.
- Walks the user through connecting their tools one at a time (Gmail → Calendar → Drive → Notion → GitHub, plus any other tools they use).
- Reads what it can from each.
- Asks a few questions to fill in the parts tools can't tell it (how they make decisions, what they want their assistant to push back on, how they communicate, etc.).

This is a real conversation, not a form. The user takes their time. You coordinate the rollout — who goes first, fielding questions — but the first conversation itself is between each user and their assistant.

---

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Read this if you're new.
- `human-roles.md` — who does what in the three steps above.
- `agent-files/onboarding/BOOTSTRAP.md` — the full script each assistant follows in the first conversation.
- `agent-files/AGENTS.md` — session boot and operational rules (assistant-side; useful if you want to understand how it works under the hood).
- `agent-files/TOOLS.md` — per-user tool table; filled in during the first conversation.

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
