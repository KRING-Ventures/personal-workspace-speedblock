# Personal Workspace — Playbook

Your day-to-day guide to Personal Workspace: the tools you'll use, what your agent does for you, and the rhythm you'll settle into. The goal is simple — make everyday work faster, calmer, and more fun.

> New here, or want the case for why this is worth it? Start with `buy-in.md`.

---

## The one principle

**AI first.** If your agent can do something for you, let it. The only thing it checks with you on is anything that gets sent, replied to, or changed for other people — that always gets your OK.

---

## The Tool Stack

### Mandatory tech stack

The apps required to use Personal Workspace. These are set up during activation.

| App | What it's for | Your agent reaches it? |
|---|---|---|
| **Google Workspace** (Gmail, Calendar, Drive, Docs, Meet) | Default workspace and file storage — email, calendar, files, docs, meetings | ✅ Yes — wired by KRING during activation |
| **Slack** | Team and agent communication — where you talk to your agent | ✅ Yes — primary surface |
| **ChatGPT** | The LLM OpenClaw runs on | n/a — infrastructure |

### Recommended tech stack

Apps we recommend for other tasks. Not required — you set these up yourself after activation.

| App | What it's for | Your agent reaches it? |
|---|---|---|
| **Notion** | Notes and meeting transcriptions — your venture's project workspace | ✅ Yes — connect it yourself after activation |
| **GitHub** | Code repositories and version control | ✅ Yes — connect it yourself after activation |
| **Whispr Flow** | Fast speech-to-text — dictate messages and notes | n/a — you use this directly |
| **Claude** | Everyday AI tasks and vibe coding | n/a — you use this directly |

---

## Your personal AI agent

You get your own personal AI agent for everyday work.

### What it does for you

| What it does | How it works |
|---|---|
| **Remembers you** | Your role, projects, who you work with, how you like things done — across every conversation. |
| **Briefs you** | Every morning at 8: calendar, priorities, deadlines, and what it drafted overnight. Mondays: the week ahead. |
| **Triages your inbox** | All day, it drafts ~95% of replies straight into your Gmail Drafts — you review and send. Never sent without your OK. |
| **Preps your meetings** | ~30 min before each: who's in it, the context, and what you want out of it. |
| **Manages your calendar** | Finds times, blocks focus time, schedules for you. Your own time freely; anything with other people, it asks first. |
| **Tracks commitments** | Notices what you've promised and what you're waiting on. |
| **Uses your tools** | Gmail, Calendar, Drive, Notion, and more. |
| **Builds automations** | On request — describe what should happen automatically and it builds it, then shows you how to switch it off. |

*Automation examples: "every Friday, summarise what I closed this week" · "remind me 3 days before any deadline" · "label anything from my accountant and file the receipts."*

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

- **Coming from Microsoft 365?** Optional. If your venture runs on M365, KRING can migrate your email, calendar, and files to Google Workspace during setup — just flag it at activation. Google becomes your daily driver; M365 stays as a read-only backup. Your agent knows the cut-over date and searches the right system.

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
