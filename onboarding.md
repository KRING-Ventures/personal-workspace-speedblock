# Personal Workspace — Onboarding

A walk-through from the moment you activate Personal Workspace in Cosmica to the moment every teammate is using their agent.

Each step below tells you **when** it happens, **who's doing it**, and **what you see**. Personal Workspace is a **Done with you** Speedblock — you do a couple of small things, KRING provisions, your agent runs the conversations.

## Timeline at a glance

| # | Step | When | Who | What happens |
|---|------|------|-----|--------------|
| 1 | Activate | ~5 min | You | Confirm scope and billing in the Cosmica marketplace. |
| 2 | Name your agent | ~2 min | You | Pick a name in the Onboarding tab. |
| 3 | KRING provisions your agent | ~1 business day | KRING | We wire it up and confirm it's ready to talk. |
| 4 | First conversation with your agent | ~20 min | You + your agent | Open the chat — your agent captures your team list and tenant info. |
| 5 | KRING provisions each teammate's agent | ~1 business day | KRING | One agent per teammate, reached on Telegram. |
| 6 | Each teammate's first conversation | ~20 min per person | Each teammate + their agent | The agent walks them through tools, working practices, and personal setup. |

When step 6 is done for every teammate, your venture is running on Personal Workspace.

---

## Step 1 — Activate (~5 min, you)

**Where:** Cosmica → Speedblocks → Personal Workspace → **Activate**.

You'll go through two short screens:

1. **Scope.** A summary of what Personal Workspace delivers and the timeline. Hit *Continue to billing*.
2. **Billing.** Personal Workspace is free during beta — no charges to confirm. Tick the activation terms, hit *Confirm & activate*.

Cosmica then shows a green success screen. Personal Workspace moves to your **Active Speedblocks** list, and KRING is notified to start onboarding.

## Step 2 — Name your agent (~2 min, you)

**Where:** the same Speedblock panel → **Onboarding** tab.

You'll see three milestones. The first is unlocked: *Name your agent*. You'll get a single input — pick anything (`Mira`, `Otto`, your team mascot). You can change it later.

> **Heads-up.** Cosmica's Onboarding tab names *one* agent per activation today. This first agent is the one you talk to — it captures your team list in step 4. Each teammate gets their own personal agent later, in step 5.

Hit *Save name*. The milestone marks complete and KRING starts provisioning.

## Step 3 — KRING provisions your agent (~1 business day, KRING)

**What you see:** the Onboarding tab switches to a blue card — *"[name] is being built"*. The milestone shows "owned by KRING".

**What KRING is doing:** spinning up the runtime, wiring the agent to Telegram, loading the Personal Workspace skill bundle, and confirming the agent is reachable.

You don't need to do anything here. When the agent is ready, the milestone flips green and a **Talk to [name]** button appears. You'll also get a heads-up from KRING.

## Step 4 — First conversation with your agent (~20 min, you + your agent)

**Where:** click **Talk to [name]** in the Onboarding tab — it opens the agent's chat.

The agent will:

- Introduce itself and confirm what Personal Workspace is. Want your team oriented first? Share `playbook.md` before they meet their agents.
- Ask you to list the teammates who get an agent. For each: full name, primary email, Telegram handle (e.g. `@maria`), and the name they'd like for their agent.
- Confirm your tenants are in place. Required: Google Workspace, Slack. Optional: Notion, GitHub. KRING doesn't provision into your tenants — that's on you.
- Hand the list to KRING ops to provision each teammate's agent.

No forms. Real conversation, in chat. If something's missing, the agent asks for it.

## Step 5 — KRING provisions each teammate's agent (~1 business day, KRING)

KRING provisions one personal agent per teammate, wires each one to the Telegram handle you submitted, and reaches each teammate on Telegram with their agent's username.

You can track progress by asking your agent — it knows where each teammate is in the pairing process.

## Step 6 — Each teammate's first conversation (~20 min per person, each teammate + their agent)

For each teammate, in any order:

1. KRING messages the teammate on Telegram with their agent's username. *(Done by the end of step 5.)*
2. The teammate opens Telegram, finds the agent, and sends any message.
3. The agent introduces itself and runs the first conversation — about ~20 minutes, real conversation, not a form.

In that first conversation, the agent walks them through:

- Wiring up Gmail, Calendar, Drive, Notion, and GitHub.
- The **4 AI Commandments** and the must-know vocab (branch, pull request, merge, etc.). See `best-practice.md`.
- The few questions tools can't answer — how they make decisions, what to push back on, communication preferences.

When every teammate has finished that first conversation, your venture is fully on Personal Workspace.

## What each teammate gets

A personal AI agent on Telegram — one per teammate, remembers across conversations:

- **Remembers** — role, projects, contacts, working preferences.
- **Briefs** — mornings on calendar, priorities, deadlines. Mondays on open commitments and what's outstanding.
- **Drafts** — emails, messages, docs. Never sent without approval.
- **Preps meetings** — attendees, context, intent.
- **Tracks commitments** — what they've said they'll do, what they're waiting on.
- **Uses the tools** — Gmail, Calendar, Drive, Notion, GitHub, Telegram.
- **Builds automations** — on request.
- **4 AI Commandments walkthrough** — the agent teaches the four working practices and the must-know vocab in the first conversation.

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Share with your team before step 6.
- `best-practice.md` — the 4 AI Commandments and must-know vocab.
- `agent-files/onboarding/BOOTSTRAP.md` — the script the agent follows in the first conversation.
- `agent-files/AGENTS.md` — operational rules (agent-side; useful if you want to understand how it works under the hood).

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
