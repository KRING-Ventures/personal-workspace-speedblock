# Personal Workspace Speedblock — Playbook

Personal Workspace defines the best practices for how to work individually, across teams and AI agents. Aiming to make it more fun and frictionless to do everyday work.

---

## Principles

- **AI first.** If your agent can do something for you, let it. You approve anything that gets sent, replied to, or changed for other people.

---

## The Tool Stack

Every Personal Workspace user runs on these as the basics.

| For | We use | Your agent reaches it? |
|---|---|---|
| Email, calendar, files, docs, meetings | **Google Workspace** (Gmail, Calendar, Drive, Docs, Meet) | ✅ Yes — wired by KRING during activation |
| Your personal AI agent | **Telegram** — you chat with your agent there | ✅ Yes — primary surface |
| Meeting transcriptions & notes | **Notion** — your venture's Notion workspace | ✅ Yes — wired by KRING during activation |
| Code storage & access | **GitHub** | ✅ Yes — your agent can read and work in your repos with your permission |
| Team chat | **Slack** | ❌ Not yet — planned for a future version |
| Help inside Google apps | **Gemini** — Google's AI inside Docs, Gmail, etc. | n/a — you use this directly |
| General-purpose AI & Coding | **Claude** — for coding and individual projects | n/a — you use this directly |

---

## Your personal AI agent

You get your own personal AI agent for everyday work.

### What it does for you

- **Remembers.** Your role, projects, who you work with, how you like things done — across conversations.
- **Briefs you.** Every morning at 8: calendar, priorities, deadlines, plus what it drafted overnight and what it left for you. Mondays: the big-picture week — open commitments, what closed, what's ahead.
- **Triages your inbox.** All day, every 30 min: it drafts replies to almost everything (~95%) straight into your Gmail Drafts and marks only those as read — you open Drafts, review, and send. Anything it didn't touch stays unread and is called out in the brief. Never sent without your OK.
- **Preps meetings.** ~30 min before each one: who's in it, the context, what you want out of it — plus a heads-up on every meeting in the morning brief.
- **Manages your calendar.** Finds times, blocks your focus time, and schedules for you — including offering people a few slots to pick from and checking colleagues' availability across the venture workspace. It books your own time freely; anything involving other people, it asks first.
- **Tracks commitments.** Notices when you've said you'll do something or you're waiting on a reply.
- **Uses your tools.** Gmail, Calendar, Drive, Notion, etc.
- **Builds automations.** On request — recurring digests, deadline reminders, inbox rules, calendar reactions. Just describe what you want to happen automatically; it confirms the details, builds it, and shows you how to switch it off. Example asks: *"every Friday, summarise what I closed this week"* · *"remind me 3 days before any deadline"* · *"label anything from my accountant and file the receipts."*

### What it asks you before doing

Drafts and research are free. Anything that leaves your account or changes things for other people gets a check first.

| The agent... | Asks first? |
|---|---|
| Reads, searches, drafts, or researches | No |
| Blocks your own focus time / a solo event | No |
| Checks colleagues' free/busy in the venture workspace | No |
| Sends an email or replies to a message | **Yes** |
| Schedules, moves, or cancels a meeting with other people | **Yes** |
| Sends a booking invite to others | **Yes** |
| Accepts or declines a calendar invite | **Yes** |
| Writes to someone else's Notion page | **Yes** |
| Pushes to a shared GitHub branch / opens a PR | **Yes** |
| Does anything irreversible or visible to others | **Yes** |

---

## How to work with your agent — The 4 AI Commandments

Four practices that apply across everything — drafting, planning, code, ops:

1. **Make the agent repeat back your prompt.** *"Explain back to me what I just told you, so we are aligned."* Catches misunderstandings before they become rework.
2. **Work in small batches — and save as you go.** *"Commit and push this work."* Lock each piece in before starting the next; don't pile up large unsaved changes.
3. **KISS — keep it simple and understandable.** *"Avoid unnecessary words and fillers. Explain in a simple way."* Plain beats clever.
4. **In shared projects: work on a copy, then merge it.** *"Branch off main."* Don't edit `main` directly when other humans or agents share the repo — branch, PR, review, merge.

Full version, plus the vocabulary (branch, PR, merge, etc.): AI Commandments Guide.

Your agent follows these too, and will nudge you as you work together.

---

## Working rhythm

- **Each day (incl. weekends).** 8:00 brief → through the day it triages your inbox every 30 min so drafts are always waiting in Gmail → you review and send → it writes a short memory log at end of day. Drafts you leave unsent get re-surfaced in the next day's brief.
- **Each week.** Monday 8:00: a weekly review — the big picture, no email. Open commitments, what closed last week, the week's milestones, what you're waiting on.

---

## Migrations

- **Coming from Microsoft 365?** See the Microsoft to Google Workspace migration playbook. The short version: Google becomes your daily driver, M365 stays as a read-only backup for old data. Your agent knows the cut-over date and searches the right system.

---

## Your files, mirrored locally

Your agent's files — its memory, your profile, your notes — can be mirrored to a folder on your own Mac/PC, kept in sync automatically. It's **one-way**: the agent writes, your machine receives a read-only copy. So if the agent is ever down, you still have everything it knows in a folder you control. To change something you ask the agent — you don't edit the local copy. Setup is in the Syncthing local-mirror runbook.

---

## Staying up to date

Personal Workspace improves over time — new capabilities, better defaults. You don't have to manage any of it. About once a week your agent checks for a new version; if there is one, it tells you what's new in plain language and **asks before changing anything**. Nothing updates behind your back. Everything you've built up — its memory, your settings, how it knows you — carries over untouched. Say yes when you're ready, or "not now" and it'll ask again later.

---

## Glossary

- **Personal Workspace** — best practices for how work is done individually and across teams.
- **OpenClaw** — the AI agent system that powers your personal agent.
- **Speedblock** — KRING's name for a ready-to-implement product solving specific roadblocks.
