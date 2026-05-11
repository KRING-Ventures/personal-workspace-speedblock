# Personal Workspace — Onboarding

How your venture gets onto Personal Workspace, following the Cosmica Speedblock flow.

Personal Workspace is a **Done with you** Speedblock — you do a couple of small things in Cosmica, KRING provisions, and your agent does the rest with you in chat.

## The three steps in Cosmica

After you activate Personal Workspace in the Cosmica marketplace, the Speedblock opens an **Onboarding** tab with three milestones:

1. **Name your agent** *(you)* — pick a name in Cosmica.
2. **Provision the agent** *(KRING)* — we wire it up; you see status update.
3. **Walk through the rest** *(your agent)* — open the chat, the agent runs the conversation.

When step 3 is done for every teammate, your venture is running on Personal Workspace.

## What each user gets

A personal AI agent on Telegram — one per user, remembers across conversations. Same list, same words as `playbook.md`:

- **Remembers** — role, projects, contacts, working preferences.
- **Briefs** — mornings on calendar, priorities, deadlines. Mondays on open commitments and what's outstanding.
- **Drafts** — emails, messages, docs. Never sent without approval.
- **Preps meetings** — attendees, context, intent.
- **Tracks commitments** — what the user has said they'll do, what they're waiting on.
- **Uses the tools** — Gmail, Calendar, Drive, Notion, GitHub, Telegram.
- **Builds automations** — on request.
- **4 AI Commandments walkthrough** — the agent teaches the user the four working practices and the must-know vocab in the first conversation. See `best-practice.md`.

## Step 1 — Name your agent

**Where:** Cosmica → Speedblocks → Personal Workspace → Onboarding tab.

You'll see a single input: *Pick a name for your agent*. This first agent is your venture's onboarding lead — it talks to you (the admin) and captures everything KRING needs to set up the rest of your team.

Pick anything — `Mira`, `Otto`, your team mascot. You can change it later. Hit **Save name** and the milestone marks complete.

> **Note:** Cosmica's onboarding tab today names *one* agent per Speedblock activation. Your per-teammate agents come in step 3, when this first agent walks you through who's on the team. You don't have to fill in a list of users or Telegram handles upfront.

## Step 2 — KRING provisions

**What you'll see:** the panel switches to *"[name] is being built"* with a blue card. KRING is provisioning the agent and connecting it to your venture.

**What KRING does:** spins up the runtime, wires Telegram, loads the Personal Workspace skill, and confirms the agent is reachable.

You don't need to do anything in this step. When the agent is ready, the milestone flips and a **Talk to [name]** button appears.

## Step 3 — Walk through the rest in chat

**Where:** click **Talk to [name]** in the Onboarding tab — it opens the conversation surface for your agent.

In chat, the agent will:

- Greet you and confirm what Personal Workspace is (≈5 min — point your team at `playbook.md` first if you want them oriented).
- Ask you to list the teammates who get an agent (full name, primary email, Telegram handle, and the name they'd like for their agent).
- Confirm your tenants are in place: Google Workspace, Slack, Notion (optional), GitHub (optional). We don't provision into your tenants — that's on you.
- Hand the list back to KRING ops, who provisions one personal agent per teammate and DMs each user on Telegram with their agent's username.

**Then, for each teammate:**

1. KRING DMs the teammate on Telegram with their agent's username. *(Done by KRING.)*
2. The teammate opens Telegram, finds the agent, sends any message.
3. The agent introduces itself and runs the first conversation — about ~20 minutes, real conversation, not a form. It walks them through wiring up Gmail, Calendar, Drive, Notion, GitHub, and the 4 AI Commandments, and asks the few questions tools can't answer (how the user makes decisions, what to push back on, communication preferences).

When every teammate has finished that first conversation, your venture is fully on Personal Workspace.

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Share with your team before they pair with their agent.
- `best-practice.md` — the 4 AI Commandments + must-know vocab.
- `agent-files/onboarding/BOOTSTRAP.md` — the script the agent follows in the first conversation.
- `agent-files/AGENTS.md` — operational rules (agent-side; useful if you want to understand how it works under the hood).

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
