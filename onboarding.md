# Personal Workspace — Onboarding

How a new user gets set up on Personal Workspace.

This document is read by two people:

- **The user joining** — for "what you do first" (Step 0) and what to expect when your assistant says hello (Part 2).
- **The runtime operator** (Corey, today) — for the technical setup (Part 1).

The flow goes in three phases:

0. **What you do first** *(you, the user)* — install Telegram, pick a name for your assistant, send the details to Corey.
1. **Setup** *(Corey)* — provision your accounts, create your private space, deploy your assistant on Telegram.
2. **First conversation** *(your assistant + you)* — your assistant introduces itself on Telegram and walks you through connecting your tools.

---

## What this version ships

- **Your own AI assistant on Telegram** — remembers you across conversations, scoped to your work.
- **Daily brief** (morning) — calendar, top priorities, anything urgent.
- **Weekly brief** (Friday) — open commitments, things you're waiting on, patterns worth noticing.
- **Heartbeats** — periodic background check-ins; only surfaces things when they actually need your attention.
- **Tool reach** — Gmail, Calendar, Drive, Notion, plus any other tools you wire during onboarding.
- **Drafting** — emails, messages, documents. Always drafts first; never sends without your OK.
- **Automations** — built on request.

Source of truth for what's in each version: `CHANGELOG.md`.

---

## Step 0 — what you do first (you, the user)

Before anything else can happen, there are a few things only you can do. Without these, your assistant can't be set up.

1. **Install Telegram** on your phone or laptop, and make sure you can receive messages on it.
2. **Decide how many assistants you want.** Default is **one**. Some people want more — for example, one for your KRING work and a separate one for a venture role you hold. Most people only need one.
3. **Pick a name** for each assistant. Whatever you'd like to call it (e.g. `Ida`, `Kerstin`). The vibe and personality come later in your first conversation — only the *name* is decided up front.
4. **Send Corey** (the person who deploys your assistant) three things:
   - Your Telegram handle, e.g. `@august`.
   - How many assistants you want.
   - The name(s) you've chosen.

Once Corey has that — and your accounts are ready (see *Accounts must already exist* below) — they'll set up the rest.

---

## Accounts must already exist

Before Corey can set anything up, your accounts have to be in place: Google Workspace (or whatever email/calendar your venture uses), Slack, Notion, GitHub, plus any venture-specific tools your assistant should be able to reach.

Who handles this depends on which side you're on:

- **If you're a KRING-internal user**, KRING ops/admin sets up your accounts in KRING's tenants.
- **If you're being onboarded inside a venture**, the venture itself sets up your accounts in its own tenants. KRING does not create accounts inside a venture's systems.

If any of those accounts aren't ready, setup waits until they are.

---

## Part 1 — Setup (Corey, one-time)

Done once per new user, before they talk to their assistant.

### 1. Provision the user's accounts

Issued by the account provisioner against the relevant tenants (KRING's, or the venture's):

- **Google Workspace** account on the relevant domain (e.g. `@kringventures.com` for KRING-internal users; the venture's own domain otherwise).
- **Slack** invite to the relevant workspace.
- **Notion** invite to the relevant workspace.
- **GitHub** invite to the relevant org (if it's relevant to the user's role).
- **Telegram** — the user has already installed this in Step 0; they'll authorise the assistant's bot during wire-up.
- Any **venture-specific tools** the user needs day-to-day that the assistant should be able to reach.

### 2. Create the user's private settings repo

Each user has their own **private GitHub repo** holding the personal layer of their assistant (IDENTITY, USER, TOOLS, automations, memory). It's separate from the shared framework — only the user's own settings live here.

- The user (or Corey) creates the repo. Name it whatever makes sense — no mandated convention.
- Seed it from this repo's `agent-files/` per-user blueprints (`IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/AUTOMATIONS.md`, empty `MEMORY.md`, empty `memory/`, empty `STATE_VERSION`). Leave `{{FROM_BOOTSTRAP}}` markers in place — the assistant fills these in during the first conversation.

### 3. Deploy the OpenClaw runtime on Telegram

One runtime per assistant the user requested in Step 0. For each:

- Deploy a new OpenClaw instance scoped to this user.
- Set the assistant's name from the user's Step 0 choice (e.g. `Ida`).
- Point it at both file-layer sources: the shared framework (`KRING-Ventures/personal-workspace-speedblock/agent-files/`) and the user's private settings repo.
- Connect Telegram (bot token, chat binding).
- Confirm the assistant is reachable on Telegram before handing off.

### 4. Hand off to the user

Send the user the assistant's Telegram handle and tell them: **start the first conversation**. The assistant takes it from here.

---

## Part 2 — First conversation with your assistant

You open Telegram, find your assistant by the handle Corey sent you, and send the first message.

Your assistant runs a structured first session — it introduces itself, walks you through connecting your tools one at a time (Gmail → Calendar → Drive → Notion, plus any other tools you use), reads what it can from each, and asks you a few questions to fill in the parts tools can't tell it (how you make decisions, what you want it to push back on, how you communicate, etc.).

This is a real conversation, not a form. Take your time.

The full script your assistant follows: `agent-files/onboarding/BOOTSTRAP.md`.

---

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Read this if you're new.
- `human-roles.md` — who's responsible for what in the setup.
- `agent-files/onboarding/BOOTSTRAP.md` — the full script your assistant follows in your first conversation.
- `agent-files/AGENTS.md` — session boot and operational rules (assistant-side; read if you're curious how it works under the hood).
- `agent-files/TOOLS.md` — per-user tool table; filled in during your first conversation.

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
