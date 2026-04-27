# Personal Workspace Speedblock — Playbook

Personal Workspace is the shared way of working we use across KRING and the ventures KRING builds: a standard set of tools, four AI helpers, and a personal AI assistant for every person.

This document explains what's in it and how to use it. Read it once top to bottom; come back to specific sections when you need them.

*Owner: August Kring.*

---

## Principles

- **Same tools for everyone.** We all run on the same stack. Your personal AI assistant is the one layer that's specific to you.
- **AI first.** If an AI helper can do something for you, let it. You approve anything that gets sent, replied to, or changed for other people.
- **Write it down.** If it's not in the handbook, Notion, or GitHub, it doesn't exist.
- **Don't mix up the AI helpers.** Each one has a specific job. Using the wrong one in the wrong place creates friction.

---

## The Tool Stack

Every Personal Workspace user runs on these. We don't mix and match.

| For | We use |
|---|---|
| Email, calendar, files, docs, meetings | **Google Workspace** (Gmail, Calendar, Drive, Docs, Meet) |
| Your personal AI assistant | **Telegram** — you chat with your assistant there |
| KRING's shared AI (Cosmo) | **Slack** — Cosmo lives in the KRING channels *(KRING-internal only; ventures don't get Cosmo)* |
| Help inside Google apps | **Gemini** — Google's AI inside Docs, Gmail, etc. |
| General-purpose AI | **Claude** — used for coding and individual projects |
| Project and task management | **Notion** — your venture's Notion workspace |
| Team chat | **Slack** |

---

## The four AI helpers

Each does a different job. Pick the right one for what you're doing.

| AI | Where you find it | What it's for |
|---|---|---|
| **Gemini** | Inside Google apps | In-app help: summarising a doc, drafting a reply inside Gmail. Stays where it lives. |
| **Claude** | claude.ai | General thinking, writing, coding help. Doesn't remember between chats. |
| **Your OpenClaw assistant** | Telegram | Your personal assistant. Remembers you. Uses your tools. Drafts, briefs, and runs work on your behalf. |
| **Cosmo** | Slack | KRING's shared assistant. Knows the company. Helps with company-wide or cross-team work. |

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

Three phases:

0. **What you do first.** Install Telegram on your phone or laptop. Decide how many assistants you want (usually one) and what to call each one. Send your Telegram handle, the count, and the chosen names to the runtime operator (Corey, today). That's what unblocks the rest.
1. **Setup.** Someone on the team provisions your accounts (Google, Slack, Notion, GitHub, Telegram), creates a private space for your personal assistant's settings, and starts the assistant on Telegram with the name you picked.
2. **First conversation with your assistant.** You open Telegram and send the first message. The assistant runs a guided setup: introduces itself, connects to your tools one at a time (Gmail → Calendar → Drive → Notion, plus any other tools you use), reads what it can from them, then asks you a few questions to fill in the things tools can't tell it.

*One per person* is the default. If you need more than one — e.g. one for KRING work and a separate one for a venture role — just ask for that in Step 0. Vibe and personality still come from your first conversation; only the *name* is decided up front.

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

*August owns this document. Anything unclear, off, or missing — tell him.*
