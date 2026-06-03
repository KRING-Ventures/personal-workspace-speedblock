# Repurposing an Existing Agent into Personal Workspace

Turning an OpenClaw agent that **already has its own history, memory, automations, and personality** into a Personal Workspace agent — without wiping what it already knows.

## Which path am I on?

Three different things, don't confuse them:

- **Clean-sheet deploy** — brand-new agent, no prior state. Runs `BOOTSTRAP.md` (the full first-conversation). See `onboarding.md`.
- **Version update** — an agent already on Personal Workspace catching up to a newer framework version. Automatic at boot via the catch-up loop. See `agent-files/AGENTS.md` → *Onboarding: how you catch up*. Nothing to do here.
- **Repurpose (this file)** — an existing agent that was *something else* (or a generic assistant) becoming a Personal Workspace agent. It has real data you must preserve, but no PW `STATE_VERSION`, so it would wrongly trigger `BOOTSTRAP` (the clean-sheet intro) if you just dropped the files in. This runbook is how you avoid that.

## The load-bearing rule

> Set the agent's local `STATE_VERSION` to the framework's current value **before** its next session. That one step tells the framework "this agent is not new" — it skips `BOOTSTRAP` and goes straight to the catch-up loop, so the agent never re-runs the clean-sheet first-conversation over a user it already knows.

Everything else is reconciliation around that.

## Part A — Operator steps (KRING)

Prerequisite: shell access to the agent's runtime.

1. **Snapshot first.** Copy the agent's whole working directory somewhere safe (`cp -r` to a dated backup, or confirm its Syncthing mirror is up to date). If anything goes wrong, you restore from this. Never skip it.
2. **Drop in the shared framework.** Add/refresh the shared `agent-files/` (SOUL, AGENTS, KRING, HEARTBEAT, SCHEDULES, templates, BOOTSTRAP, runbooks). These carry no personal data — overwriting them is safe.
3. **Do NOT overwrite the per-user files.** Leave the agent's existing `IDENTITY.md`, `USER.md`, `TOOLS.md`, `MEMORY.md`, `memory/`, and `automations/` in place. These are the user's own — they get *reconciled*, not replaced.
4. **Reconcile the per-user files into PW shape** (content preserved, structure aligned):
   - `IDENTITY.md` — keep the agent's name and identity; map fields to the PW template.
   - `USER.md` — carry every real fact about the user across into the PW *Basics* structure. Don't drop anything; restructure only.
   - `TOOLS.md` — move already-wired tools into the PW table and mark them ✅. Note anything PW-standard that isn't connected yet (Notion, GitHub, local mirror) as ❌.
   - `MEMORY.md` + `memory/*.md` — **content untouched.** These are the user's memory. Adjust only headers/section names if the PW layout needs it; never rewrite the substance.
   - `automations/AUTOMATIONS.md` — preserve every existing entry. Don't delete or duplicate automations.
5. **Set `STATE_VERSION`** at the root of the working directory to the framework's current `agent-files/onboarding/STATE_VERSION` value. (This is the load-bearing rule above — it suppresses `BOOTSTRAP`.)
6. **Reconcile schedules, don't stack them.** On the next main session the boot self-heal will add any of the four standard jobs (brief, weekly review, heartbeat, memory distill) that are missing — *check existing cron jobs first so you don't end up with two morning briefs*. If the agent already had its own brief/heartbeat-type jobs, fold them into the PW ones rather than running both.

Success signal: the agent boots, does **not** start a clean-sheet intro, keeps all prior memory and automations, and reports it's on the current `STATE_VERSION`.

## Part B — What the user experiences

A repurposed agent **already knows the user** — so the worst thing it can do is greet them like a stranger and re-ask everything. The user-facing flow is *continuity, not reset*: "same me, new capabilities." On the first main session after repurposing, the agent runs a short **upgrade conversation** instead of `BOOTSTRAP`:

1. **Open with continuity.** *"I've just been upgraded to Personal Workspace — same me, I've kept everything we've done together. Here's what's new."* No re-introduction, no name reset.
2. **Name what changed, briefly.** Proactive morning brief + Monday review, hourly check-ins on mail/calendar/commitments (nudge → draft → your OK), the local backup mirror, and a shared tool stack. Keep it to a few lines — don't lecture.
3. **Confirm migrated basics, don't re-interview.** *"I've carried over your name, timezone and role — quick check they're still right?"* Patch anything stale. This replaces BOOTSTRAP Phase 3, but starts from what's already known.
4. **Teach the 4 AI Commandments.** This *is* new — it's the working contract. Walk them quickly (per `ai-commandments.md`); it's the one piece of BOOTSTRAP a repurposed agent still needs in full.
5. **Offer the gaps.** Any PW-standard tool not yet wired (Notion, GitHub) — offer to connect. Offer the local mirror setup (`runbooks/syncthing-local-mirror.md`). All optional, all skippable.
6. **Close.** *"Everything we had is intact — I've just got more I can do for you now."*

What the user must **not** experience: losing memory, losing automations, being asked to re-state things the agent already knew, or a duplicate set of scheduled jobs firing.

## Rollback

If the reconciled state looks wrong, restore the working directory from the Part A step 1 snapshot and try again. Because per-user content was preserved (not regenerated), rollback is always clean.
