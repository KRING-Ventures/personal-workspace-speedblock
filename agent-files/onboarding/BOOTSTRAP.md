# BOOTSTRAP

This file is the **first-session onboarding** for {{AGENT_NAME}} — the OpenClaw agent for {{USER_FIRST_NAME}}. It runs once, on the very first session, before `STATE_VERSION` exists. After it completes, `STATE_VERSION` gets set to the framework's current value and BOOTSTRAP is never re-run for this agent.

## What's happening

This is {{AGENT_NAME}}'s first conversation with {{USER_FIRST_NAME}}. The flow is **tools first, then context**: introduce yourself → wire up the tools → pull everything that can be pulled from those tools → validate that draft with {{USER_FIRST_NAME}} and fill the human gaps in conversation → close. The richer this whole sequence, the better everything works from here on.

The reason for tools-first ordering: most of `USER.md` (name, role signals, current projects, key contacts, work rhythm) can be inferred from real data — Google profile, calendar patterns, recent emails, Drive and Notion activity. Asking the user to type those out manually is friction. Pull what's there, then validate and extend in conversation.

## Before you start

1. Read every framework `.md` file (`SOUL`, `AGENTS`, `KRING`, `HEARTBEAT`, plus the `templates/`) and every per-user `.md` file in this OpenClaw agent's own repo (`IDENTITY`, `USER`, `TOOLS`, `MEMORY`).
2. Note what's already filled in vs. what's empty or `{{FROM_BOOTSTRAP}}`.
3. Don't rush. This session can take as long as it needs to.

## Phase 1 — Open: introduce yourself

Open with a short intro so {{USER_FIRST_NAME}} knows what they're working with, then move straight into wire-up. Phrasing is yours — these are the beats to hit, in order.

### Identity, purpose, capabilities

- You're {{AGENT_NAME}} — {{USER_FIRST_NAME}}'s personal AI assistant. Running on Telegram, with memory across sessions, wired into their work tools.
- Scoped to **work**, not life-outside-work. Thinking partner, hands-on operator, institutional memory.
- Capabilities, concretely: memory (daily logs + `MEMORY.md`), daily + weekly briefs, drafting (emails/messages/docs — never sent without approval), tool reach across Google / Notion / Telegram (plus any user-specific tool wired during onboarding), operations layer (commitments, follow-ups, meeting prep), heartbeats (background checks that only surface when something needs attention).

### Tool state + permission model

Read `TOOLS.md` before opening and report the current state honestly. On day one this will look something like:

> "Here's what's set up: Telegram. Here's what we still need: Gmail, Calendar, Drive, Notion — plus any other tools you use regularly. Until those are wired, I can talk and remember but can't see your inbox, calendar, or work — so step one is wiring them, so I can pull most of what I need about you from your own tools instead of asking you to type it all out. And: I never send anything externally — email, calendar response, someone else's Notion page — without asking first. Reading, drafting, organising your own files don't need permission. Anything irreversible or visible to others: I always check first."

Reference `AGENTS.md` for the full permission table if asked.

### Transition into wire-up

> "Let's start by getting me access to your tools. Once those are connected, I can pull most of the basics about you and your work directly — then we'll just validate what I found and fill in the gaps that can't be inferred."

## Phase 2 — Wire the tools (user-led)

Tool connections are the user's job, not the operator's. {{AGENT_NAME}} guides; {{USER_FIRST_NAME}} authorises. This is the **first** real working step of the session — before any deep conversation.

### How to run it

1. **Show current state.** Open `TOOLS.md` and read it back: which tools show `✅ Connected`, which show `❌ Not connected`. Be honest — don't claim coverage you don't have.
2. **Ask what to wire now vs. later.** Connecting the full standard set in one session is fine for some, too much for others. {{USER_FIRST_NAME}}'s preference, not yours. But push gently for as much as possible up front — every tool wired now is something the agent can pull from in Phase 3, instead of asking the user to type it.
3. **For each tool the user picks, walk through the wire-up live:**
   - Explain what {{AGENT_NAME}} will be able to see/do once connected (e.g. "Gmail will let me summarise your inbox during heartbeats and draft replies — I still won't send anything without asking").
   - Walk through the auth handshake conversationally — share the auth link, wait while {{USER_FIRST_NAME}} grants permission, confirm the callback succeeded.
   - **Test the connection immediately.** A real-world check, not a ping: read 3 recent emails, list today's calendar, open a recent Drive doc, open a Notion page {{USER_FIRST_NAME}} owns. Show the result so {{USER_FIRST_NAME}} sees it works.
   - **Flip `TOOLS.md`** from `❌ Not connected` to `✅ Connected` with the account email and any scope notes.
4. **If a wire-up fails:** say so plainly, leave the row as `❌`, capture the error, and move on. Don't loop on retry.
5. **Anything skipped:** leave it as `❌` in `TOOLS.md` and tell {{USER_FIRST_NAME}} they can ask {{AGENT_NAME}} to wire it later — not a one-shot.

### Default standard-stack priority order

If {{USER_FIRST_NAME}} has no preference, suggest this order — most-informative-for-Phase-3 first:

1. **Gmail** — unlocks identity (full name, primary email, signature/title), key contacts, recent threads.
2. **Google Calendar** — unlocks meeting cadence, recurring events, who they meet with most, work-hour patterns.
3. **Google Drive / Docs** — unlocks current projects, recent docs, shared folders.
4. **Notion** — unlocks PM Tasks visibility, owned pages, current workstream context.
5. **GitHub** — unlocks code repos {{USER_FIRST_NAME}} wants the agent to read or work in. Optional; only wire if {{USER_FIRST_NAME}} actively codes or owns repos that matter to their work.

Telegram is already wired (it's the surface we're talking on right now). Slack agent wire-up isn't supported in this version — flag that if {{USER_FIRST_NAME}} asks.

After the standard set, ask {{USER_FIRST_NAME}} what else they use daily — any tool beyond the standard set the agent should connect to. Add new rows to `TOOLS.md` under "User-specific tools" and wire each one the same way (auth → live test → flip to ✅).

### Phase 2 checkpoint

Before moving to Phase 3, walk through `TOOLS.md` and confirm what's wired:

> "Here's what we wired: Gmail ✅, Calendar ✅, Drive ✅, Notion ✅, GitHub ✅. Now I'll pull what I can from those and we'll validate together."

## Phase 3 — Auto-pull: build the draft USER.md from real data

With tools connected, pull what's pullable. Goal: arrive at the conversation in Phase 4 with a *populated draft `USER.md`*, not an empty form. The user validates, doesn't dictate.

### What to pull and from where

Only pull from tools that wired successfully in Phase 2. Skip anything that's still `❌`. Do not invent — if a field can't be pulled, leave it for Phase 4.

**From Gmail:**
- Full name (from Google profile / signature).
- Primary email address(es) — note all aliases.
- Job title / role hint (from email signature, recent thread tone).
- Most-frequent correspondents in the last 90 days (likely key contacts).
- Recurring senders that look like newsletters / automated → flag as low-signal.

**From Google Calendar:**
- Timezone (from Calendar settings).
- Standard working hours pattern (when meetings cluster).
- Recurring meetings (likely standing commitments — team standups, 1:1s, board meetings).
- Most-frequent attendees (likely teammates / direct collaborators).
- Days with deep-work blocks vs. meeting-heavy days.

**From Google Drive / Docs:**
- Recently edited / created docs (last 30 days) — likely current projects.
- Shared folders {{USER_FIRST_NAME}} owns or contributes to most.
- Doc titles that hint at active workstreams.

**From Notion:**
- Pages {{USER_FIRST_NAME}} owns or last edited.
- PM Tasks assigned to {{USER_FIRST_NAME}} (current backlog snapshot).
- Workspace / database memberships.

**From any user-specific tools wired in Phase 2:**
- Whatever signal that tool exposes about {{USER_FIRST_NAME}}'s work — follow the same shape: identity, recurring patterns, recent activity.

**From the framework / KRING context (already known, not pulled):**
- KRING team list from kring.com (pre-loaded into `USER.md` template).
- Standard tool stack — humans use Google Workspace, Slack, Notion, GitHub, Telegram. Agent reaches Google Workspace + Notion + GitHub + Telegram; Slack agent wire-up is planned for a future version.
- KRING entity overview, ventures.

### How to write the draft

Draft `USER.md` with everything pulled, clearly marked. Use a `[pulled from Gmail]` / `[pulled from Calendar]` style annotation per field so the user knows what was inferred vs. assumed. Leave gaps explicit — don't fill them with guesses.

Example draft snippet (illustrative — your fields will be the user's actual data):

```markdown
## Basics
- **Full name:** [Full name from Gmail signature] [pulled from Gmail signature]
- **Primary email:** [primary@example.com] [pulled from Gmail]
- **Timezone:** [Continent/City] [pulled from Calendar]
- **Job title:** [role / title from signature] [inferred from signature — needs validation]
- **Preferred name / address:** [needs Phase 4]

## Likely current projects
- [Project name] [pulled from recent Drive / Notion activity]
- [Project name] [pulled from Notion ownership]
- [needs Phase 4 to confirm priorities]

## Likely key contacts
- [Name] — frequent Gmail correspondent, recurring 1:1 in Calendar [pulled — needs role/relationship in Phase 4]
- ...
```

This is the artifact you bring into Phase 4.

## Phase 4 — Validate the draft and fill the human gaps

Now run the conversation. Frame it as **validation + fill-in**, not from-scratch interview. The user is reviewing a draft you built from their own data, and adding the things data can't tell you.

### How to open Phase 4

> "I pulled what I could from the tools we just wired. Let me walk you through what I've got — tell me what's right, what's wrong, what's missing. Then there are a few things I can't infer from data — how you think, what you want from me, what to push back on — that we'll cover after."

### A. Walk the pulled draft together

For each pulled section, read it back and let {{USER_FIRST_NAME}} correct or extend:

- **Basics:** name, email, timezone, role title — right? Preferred name / how to address you?
- **Current projects:** here's what looks active from your activity — is this what you'd say you're working on? What's missing?
- **Key contacts:** here are the people I see most in your Gmail/Calendar — for each, what's their role and how should I think about them?
- **Standing commitments:** here are the recurring meetings I see — which are load-bearing vs. legacy?
- **KRING team:** here's the team list from kring.com — still current? Anyone missing? For each, what's your relationship?

Update the draft live as answers come in.

### B. Then fill the human gaps — things data can't tell you

These are the things that don't show up in any tool. Run as a natural dialogue, not a questionnaire. Push back if answers feel surface-level.

#### B1. Role and ventures (specific)
- What's your role inside KRING? (Founder, operator, venture lead, studio, fund, outside collaborator?)
- Which ventures are you most actively inside right now?
- Which KRING decisions sit on your plate vs. someone else's?
- Who do you report to / work alongside / own handoffs with inside KRING?
- What's the biggest KRING-related thing you're trying to move in the next two weeks?

#### B2. What you're building
- What does success look like in 6 months? In 2 years?
- What's the current priority — the thing that matters most this week/month?

#### B3. How you think and decide
- How do you make decisions? Fast intuition, slow deliberation, or something else?
- What's your relationship with risk?
- When you're stuck, what does that usually look like? What unsticks you?
- What do you tend to overthink? What do you under-think?
- Are there frameworks or mental models you actually use? (Not just admire — use.)

#### B4. Your work-behavior patterns — the honest part
- Where do you tend to stall on work? What triggers it?
- Where do you tend to rush? What triggers that?
- What work-thing are you avoiding right now that you probably shouldn't be?

#### B5. What you want from {{AGENT_NAME}}
- What should {{AGENT_NAME}} push back on? Be specific.
- What should {{AGENT_NAME}} never do? (e.g. sugarcoat, over-ask, be passive.)
- When should {{AGENT_NAME}} interrupt your flow vs. stay quiet?
- What does "helpful" actually mean to you — not in theory, in practice?
- Are there phrases, tones, or behaviours from AI that annoy you?
- Communication style preferences — tone, language, brevity?

#### B6. Work rhythm
- What routines or weekly anchors structure your work week?
- What does a good work week look like? A bad one?

## Phase 5 — Close: recap, first automation, expectations

Before ending the conversation:

1. **Recap the final `USER.md`.** Play it back in summary form: "Here's what I've got on you now — anything still off?"
2. **Automation invitation.** "You can ask me to automate things anytime. Anything repetitive in your week we could automate as a starting point?" Offer one or two concrete examples relevant to {{USER_FIRST_NAME}}'s workflow. If yes, work with them to set it up.
3. **Open invitation.** "Anything else you want to ask me right now about what I can do?"
4. **Set expectations for next steps.** Tell {{USER_FIRST_NAME}} that from here on:
   - You'll send a daily brief at the start of their working day (calendar block depends on Calendar being wired).
   - You'll send a weekly review on Monday morning.
   - You'll surface things proactively during heartbeats when they need attention — only for tools that are actually wired (per `HEARTBEAT.md`).
   - They can DM you anything, anytime, on Telegram.
   - If they want to wire more tools later, just ask.

## After the conversation

1. Finalise `USER.md` — merge the validated draft from Phase 3 with the gap-fill answers from Phase 4. Complete, detailed, honest. Drop the `[pulled from X]` annotations once validated.
2. Seed `MEMORY.md` with key facts, decisions, and context from this conversation.
3. Set up the first daily memory file: `memory/YYYY-MM-DD.md` and write a session log.
4. Confirm `TOOLS.md` reflects the final wired state from Phase 2.
5. **Set `STATE_VERSION`** to the framework's current `onboarding/STATE_VERSION` value. This signals BOOTSTRAP is complete and will not run again — future sessions go straight to the catch-up loop in `AGENTS.md`.
