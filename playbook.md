# Personal Workspace Speedblock — Playbook

Personal Workspace is the shared way of working we use across KRING and the ventures KRING builds: a standard set of tools and a personal AI assistant for every person.

This document explains what's in it and how to use it. Read it once top to bottom; come back to specific sections when you need them.

*Owned and maintained by KRING.*

---

## Principles

- **AI first.** If your assistant can do something for you, let it. You approve anything that gets sent, replied to, or changed for other people.
- **Write it down.** If it's not in Notion or GitHub, it doesn't exist.

---

## The Tool Stack

Every Personal Workspace user runs on these. We don't mix and match.

| For | We use | Your assistant reaches it? |
|---|---|---|
| Email, calendar, files, docs, meetings | **Google Workspace** (Gmail, Calendar, Drive, Docs, Meet) | ✅ Yes — wired during your first conversation |
| Your personal AI assistant | **Telegram** — you chat with your assistant there | ✅ Yes — primary surface |
| Project and task management | **Notion** — your venture's Notion workspace | ✅ Yes — wired during your first conversation |
| Code & engineering | **GitHub** | ✅ Yes — your assistant can read and work in your repos with your permission |
| Team chat | **Slack** | ❌ Not yet — planned for a future version |
| Help inside Google apps | **Gemini** — Google's AI inside Docs, Gmail, etc. | n/a — you use this directly |
| General-purpose AI | **Claude** — for coding and individual projects | n/a — you use this directly |

---

## Your personal AI assistant

You get your own AI assistant — powered by OpenClaw, running on Telegram. It's your partner for work.

### What it does for you

- **Remembers.** Keeps context about you — your role, projects, the people you work with, how you like things done. Memory carries between conversations.
- **Briefs you.** Each morning: your calendar, priorities, anything urgent. Each week: open commitments, things you're waiting on, patterns worth noticing.
- **Drafts for you.** Emails, messages, documents. Always drafts first — never sends without your OK.
- **Uses your tools.** Reads your Gmail, Calendar, Drive, Notion, GitHub — plus any other tools you wire it to.
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
| Writes to someone else's Notion page | **Yes** |
| Pushes to a shared GitHub branch / opens a PR | **Yes** |
| Does anything irreversible or visible to others | **Yes** |

---

## How to work with your assistant — The 4 Commandments

Four practices that apply across everything — drafting, planning, code, ops:

1. **Make the agent repeat back your prompt.** *"Explain back to me what I just prompted, so we are aligned."* Catches misunderstandings before they become rework.
2. **Work in small batches — and save as you go.** *"Save and commit this work."* Lock each piece in before starting the next; don't pile up large unsaved changes.
3. **KISS — keep it simple and understandable.** *"Avoid unnecessary words and fillers. Explain in a simple way."* Plain beats clever.
4. **In shared projects: work on a copy, then merge it.** *"Branch off main."* Don't edit `main` directly when other humans or agents share the repo — branch, PR, review, merge.

Full version: [`best-practice.md`](./best-practice.md). Vocabulary (branch, PR, merge, etc.): [`terms.md`](./terms.md).

Your assistant follows these too, and will nudge you when you're skipping one.

---

## Working rhythm

- **Each day.** Morning brief from your assistant → use it throughout the day for drafting, research, and recall → it writes a short memory log at end of day.
- **Each week.** Monday morning: a weekly review — open commitments, things you're waiting on, calendar overview, patterns worth noticing.

---

## Glossary

- **Personal Workspace** — the shared way of working across KRING and the ventures KRING builds.
- **OpenClaw** — the AI assistant system that powers your personal assistant.
- **Speedblock** — KRING's name for a focused project run in stages (Scope → Research → Solution → Build).
- **Brief** — the daily or weekly summary your assistant sends you.

---

*KRING owns this document. Anything unclear, off, or missing — tell us.*
