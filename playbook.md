# Personal Workspace Speedblock — Playbook

Personal Workspace is the shared way of working we use across KRING and the ventures KRING builds: a standard set of tools, four AI helpers, and a personal AI assistant for every person.

This document explains what's in it and how to use it. Read it once top to bottom; come back to specific sections when you need them.

*Owned and maintained by KRING.*

---

## Principles

- **Same tools for everyone.** We all run on the same stack. Your personal AI assistant is the one layer that's specific to you.
- **AI first.** If an AI helper can do something for you, let it. You approve anything that gets sent, replied to, or changed for other people.
- **Write it down.** If it's not in the handbook, Notion, or GitHub, it doesn't exist.
- **Don't mix up the AI helpers.** Each one has a specific job. Using the wrong one in the wrong place creates friction.

---

## The Tool Stack

Every Personal Workspace user runs on these. We don't mix and match.

| For | We use | Your assistant reaches it? |
|---|---|---|
| Email, calendar, files, docs, meetings | **Google Workspace** (Gmail, Calendar, Drive, Docs, Meet) | ✅ Yes — wired during your first conversation |
| Your personal AI assistant | **Telegram** — you chat with your assistant there | ✅ Yes — primary surface |
| Project and task management | **Notion** — your venture's Notion workspace | ✅ Yes — wired during your first conversation |
| Team chat | **Slack** | ❌ No — humans only, your assistant doesn't read or post here |
| Code & engineering | **GitHub** | ❌ No — humans only |
| Help inside Google apps | **Gemini** — Google's AI inside Docs, Gmail, etc. | n/a — separate AI helper, see below |
| General-purpose AI | **Claude** — used for coding and individual projects | n/a — separate AI helper, see below |
| KRING's shared AI (Cosmo) | **Slack** — lives in KRING's Slack channels | n/a — *KRING-internal only; if you're at a venture, you don't have Cosmo* |

---

## The four AI helpers

Each does a different job. Pick the right one for what you're doing.

| AI | Where you find it | What it's for |
|---|---|---|
| **Gemini** | Inside Google apps | In-app help: summarising a doc, drafting a reply inside Gmail. Stays where it lives. |
| **Claude** | claude.ai | General thinking, writing, coding help. Doesn't remember between chats. |
| **Your OpenClaw assistant** | Telegram | Your personal assistant. Remembers you. Uses your tools. Drafts, briefs, and runs work on your behalf. |
| **Cosmo** | Slack | KRING's shared assistant. Knows the company. Helps with company-wide or cross-team work. *KRING-internal only — if you're at a venture, you don't have Cosmo.* |

Rule of thumb:

- Inside a Google Doc or Gmail? Use **Gemini**.
- One-off thinking or writing, not tied to anyone? Use **Claude**.
- Anything personal to you that needs memory or your inbox/calendar/etc? Use **your OpenClaw assistant**.
- Anything about KRING as a company, or across several people? Use **Cosmo**.

---

## Your personal AI assistant (OpenClaw)

Every Personal Workspace user gets their own AI assistant — a personal OpenClaw agent. You chat with it on Telegram. It's your partner for work.

### What it does for you

- **Remembers.** Keeps context about you — your role, projects, the people you work with, how you like things done. Memory carries between conversations.
- **Briefs you.** Each morning: your calendar, priorities, anything urgent. Each week: open commitments, things you're waiting on, patterns worth noticing.
- **Drafts for you.** Emails, messages, documents. Always drafts first — never sends without your OK.
- **Uses your tools.** Reads your Gmail, Calendar, Drive, Notion — plus any other tools you wire it to during onboarding.
- **Tracks commitments.** Notices when you've said you'll do something or are waiting on a reply.
- **Preps meetings.** For meetings that matter, pulls together who's there, what's relevant, and what you want to get out of it.
- **Builds automations.** If you want it to handle recurring work, you can ask it to set that up.

### What it asks you before doing

Your assistant drafts and researches freely. But it always asks first before anything leaves your account or changes things for other people.

| The assistant... | Asks first? |
|---|---|
| Reads, searches, drafts, or researches | No |
| Sends an email or replies to a message | **Yes** |
| Accepts or declines a calendar invite | **Yes** |
| Writes to someone else's Notion page | **Yes (every time)** |
| Does anything irreversible or visible to others | **Yes** |

### Day one vs. later

- **Day one** (after your first setup conversation with the assistant): it already knows your name, role, top projects, the people you work with, and your meeting patterns — pulled from your tools, not typed by you. Your tools are connected. It can draft, remember, and help.
- **Later**: it learns how you think and work — your preferences, your communication style, the things you want it to push back on.

---

## Working rhythm

- **Each day.** Morning brief from your assistant → use it throughout the day for drafting, research, and recall → it writes a short memory log at end of day.
- **Each week.** Friday evening or Monday morning: a weekly review — open commitments, things you're waiting on, calendar overview, patterns.

---

## Getting set up

Three steps, the same for everyone:

1. **Your venture activates the Speedblock.** Your venture sends KRING an intake — confirmation your accounts are set up (Google, Slack, Notion, GitHub), your Telegram handle, and the name you'd like for your assistant.
2. **KRING deploys your assistant.** When it's live, your venture passes you the assistant's Telegram handle.
3. **Your first conversation.** You open Telegram, find your assistant by the handle, and send the first message. Your assistant introduces itself and walks you through connecting your tools — Gmail, Calendar, Drive, Notion.

*One assistant per person* — that's the model. The name is decided in the intake; vibe and personality come out of your first conversation. Tools beyond the standard stack (e.g. Linear, Figma) are wired by you with your assistant after deployment.

Full step-by-step in `onboarding.md`.

---

## Don't mix up OpenClaw and Cosmo

- **Your OpenClaw assistant** is yours. On Telegram. Knows you. One per person.
- **Cosmo** is KRING's. On Slack. Knows the company. Shared across everyone.

Don't ask your OpenClaw assistant to do things for the whole company. Don't ask Cosmo to remember things that are personal to you. Different tools, different jobs.

---

## Glossary

- **Personal Workspace** — the shared way of working across KRING and the ventures KRING builds.
- **OpenClaw** — the AI assistant system. *Your* OpenClaw is your personal assistant; *Cosmo* is the shared, company-wide OpenClaw.
- **Cosmo** — KRING's shared AI in Slack.
- **Speedblock** — KRING's name for a focused project run in stages (Scope → Research → Solution → Build).
- **Brief** — the daily or weekly summary your assistant sends you.

---

*KRING owns this document. Anything unclear, off, or missing — tell us.*
