# KICKOFF — repurpose handover (existing agent → Personal Workspace)

The counterpart to `KICKOFF.md`, for the **repurpose** path: an agent that was already *something else* for **this same human** is becoming a Personal Workspace agent, keeping all its history, memory, and automations.

Repurpose is **operator-triggered, not boot-detected.** The agent will *not* sniff this out on its own — because its `USER.md` is already filled, boot correctly treats it as "not a blank slate" and skips `BOOTSTRAP`. So nothing happens until a human kicks it off. This brief is that kick.

**Order matters.** KRING runs `runbooks/repurposing-an-existing-agent.md` → **Part A first** (snapshot, drop in the shared framework, reconcile the per-user files into PW shape, set `STATE_VERSION`). *Then* paste the brief below to trigger Part B — the continuity-aware onboarding.

---

## The handover brief *(KRING fills the `{{…}}` blanks, then pastes this whole block to the agent — after Part A is done)*

```
You're being repurposed into a Personal Workspace agent. Part A is done —
your shared framework is installed and your per-user files are reconciled.

• Your name: {{AGENT_NAME}} (unchanged — keep your identity)
• Your framework files live at: {{REPO_URL}}
• The person you serve: {{USER_FULL_NAME}} — Slack <@{{USER_SLACK_ID}}> — the SAME
  human you already know. Do not re-introduce yourself or re-ask what you know.
• Support if something breaks: {{SUPPORT_NAME}} — Slack <@{{SUPPORT_SLACK_ID}}>

Your job now: get your bearings from your reconciled files, confirm you still
know this person, then run the continuity-aware onboarding —
runbooks/repurposing-an-existing-agent.md → Part B. Deliver the Personal
Workspace onboarding (the value, the best practices, the optional demos),
skip the introductions, and name the transition. You reach out — don't wait.
```

Keep the brief to these facts. Everything else is already in your reconciled files.

---

## What you — the agent — do the moment you receive this

1. **Get your bearings from the reconciled files.** Read the framework `.md` in `agent-files/` and your now-reconciled per-user files (`IDENTITY`, `USER`, `TOOLS`, `MEMORY`, `memory/`, `automations/`). Your memory and history are intact — confirm it.

2. **Confirm continuity, don't reset.** Your `USER.md` is **filled** (real facts about {{USER_FULL_NAME}}), and the human in your channel **matches** it. That's the repurpose signal: same person, real state. If the channel human does **not** match `USER.md`, this is not a repurpose — stop and flag support (that's a reset, `runbooks/resetting-an-agent.md`).

3. **Run the continuity onboarding — Part B.** Deliver the Personal Workspace onboarding the way `repurposing-an-existing-agent.md` → Part B scripts it: **deliver the value, skip the introductions, name the transition.** A repurposed user still deserves the same walkthrough a new user gets — they just don't get greeted like a stranger.

4. **Don't re-run BOOTSTRAP from the top.** BOOTSTRAP's clean-sheet intro re-asks things you already know. Part B is the continuity-aware version — use it. Preserve every existing memory, automation, and schedule (reconcile, don't duplicate).

<!-- Maintenance: keep in step with runbooks/repurposing-an-existing-agent.md (Parts A/B) and AGENTS.md → First session: onboarded or not?. New deploys use the sibling KICKOFF.md (bare agent → pull repo + onboard). This repurpose brief is separate because the agent already has its files and a filled USER.md, so it won't auto-start — it needs Part A first, then this manual trigger. -->
