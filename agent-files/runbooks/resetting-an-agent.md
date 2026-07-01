# Resetting an Agent for a New User

Re-provisioning an OpenClaw agent that **already carries a previous person's state** so it can serve a **different** human — cleanly, with the old user's data archived, not silently inherited.

This is the path the framework was missing. Deleting `STATE_VERSION` alone does **not** reset an agent: the per-user files (`USER.md`, `MEMORY.md`, `memory/`, `IDENTITY.md`, `automations/`) still describe the previous person, so on next boot the agent reads a **filled `USER.md`**, concludes "already set up," and just carries on as the old user — greeting the new human as them. The reset is what gets `USER.md` back to placeholders so boot sees a blank slate. That is the exact failure this runbook fixes.

## Which path am I on?

Don't confuse the four:

- **Clean-sheet deploy** — brand-new runtime, no prior state at all → `onboarding/BOOTSTRAP.md`.
- **Version update** — already PW, catching up to a newer framework version → automatic at boot; `runbooks/updating-an-agent.md`.
- **Repurpose** — an agent that was *something else* for **this same user** becoming PW, keeping its history → `runbooks/repurposing-an-existing-agent.md`.
- **Reset / re-provision (this file)** — an agent that held **another person's** state being handed to a **new** user. The old user's data must be preserved out-of-band and removed from the live workspace, then the new user gets a genuine clean-sheet onboarding.

The tell: **a reset changes *who the user is*.** A repurpose and an update keep the same human; a reset does not. If the person in the 1:1 channel is not the person in `USER.md`, you are resetting — not repurposing.

## The load-bearing rule

> A reset is a **clean start for a new person, with the old person's state archived first.** When it's done correctly the per-user files are back to template placeholders (`USER.md` = `{{FROM_BOOTSTRAP}}`) — so the normal boot logic sees a blank slate and runs `BOOTSTRAP` clean. (Clearing `STATE_VERSION` too is housekeeping, not the trigger.) The whole job is getting to that empty-slate state safely, without losing the previous user's data and without the new user ever being mistaken for the old one.

## The guard — what the agent does on its own

Even before an operator runs the steps below, the agent must not silently inherit a stranger's identity. Per `AGENTS.md` → *First session: onboarded or not?*: when `USER.md` is filled but the human in its 1:1 channel doesn't match it, the agent **stops and confirms intent** rather than greeting them as the old user or running anything:

> *"Heads up — I still have {old user}'s setup on disk, but you look new here. Should I start fresh for you, or am I picking up where {old user} left off?"*

- **"Start fresh"** → this is a reset. If an operator hasn't already archived/cleared the old state, the agent must not just plough ahead destructively — it flags that the prior user's files are still present and either (a) waits for the operator to run Part A, or (b) with explicit confirmation, archives them itself (Part B) before running `BOOTSTRAP`.
- **"Picking up where they left off"** → not a reset after all (e.g. same user, display-name confusion); fall back to repurpose/update.

This guard is the safety net for a half-done reset (someone archived the old user but left the filled per-user files in place) — it converts the old silent-wrong-identity behaviour into one explicit question.

## Part A — Operator steps (KRING)

Prerequisite: shell access to the agent's runtime, and confirmation the previous user is genuinely off this agent.

1. **Snapshot the whole workspace first.** `cp -r` the agent's working directory to a dated backup outside the workspace (or confirm its Syncthing mirror is current). Never skip — this is the previous user's data and the only undo.
2. **Archive the previous user's state out of the live workspace.** Move — don't just delete — the per-user files to the backup so they're preserved but no longer read at boot:
   - `USER.md`, `MEMORY.md`, `memory/`, `IDENTITY.md`, `automations/`, `feedback/`, and any user-specific `TOOLS.md` entries.
3. **Reset the per-user files to template state.** Restore the blank PW templates (from `agent-files/templates/` and the seed copies) so the files exist but carry no prior-user content — `USER.md` back to `{{FROM_BOOTSTRAP}}` placeholders, an empty `MEMORY.md`, a fresh `IDENTITY.md`, no daily memory files, no automations. If provisioning seeds the new user's Slack member ID, set that one field; leave the rest blank.
4. **De-register the previous user's scheduled jobs.** The old `automations/` jobs (briefs, triage, heartbeat, anything custom) were anchored to the old person — remove them so they don't fire for the new user or against the old user's calendar. The standard jobs get re-created fresh during BOOTSTRAP.
5. **Clear `STATE_VERSION`.** Delete the repo-root `STATE_VERSION` file (or confirm it's already gone) — housekeeping. The template reset in step 3 (`USER.md` back to `{{FROM_BOOTSTRAP}}`) is what re-arms `BOOTSTRAP`.
6. **Hand over.** On the next session the agent sees a placeholder `USER.md` → it runs a clean `BOOTSTRAP` and onboards the new user from scratch.

Success signal: the agent boots, does **not** know the previous user, introduces itself to the new human, runs the full first-conversation, and ends on the current `STATE_VERSION` with a fresh `USER.md`/`MEMORY.md`.

## Part B — If the agent does the archiving itself

When there's no operator on the shell and the new user confirms "start fresh", the agent may perform the reset itself — but only with explicit confirmation, because it is destructive to the live workspace (the data survives in the archive):

1. **Confirm once, in plain words** — *"Got it. I'll archive {old user}'s setup to a backup and start completely fresh for you. Nothing of theirs is deleted, it just moves out of my active workspace. Go ahead?"*
2. **Archive, don't delete** — move the Part A step 2 files into a dated `trash/`- or `archive/`-style folder inside the workspace (per file-hygiene: `trash/` over `rm`). Never hard-delete the previous user's memory.
3. **Reset to template** (Part A steps 3–4) and **clear `STATE_VERSION`** (step 5).
4. **Then run `onboarding/BOOTSTRAP.md`** from the top as a genuine cold start for the new user.

If anything is ambiguous — you're not sure the old user is really gone, or whether this is a reset vs. a repurpose — **stop and ask the operator/KRING** rather than archiving. Safety over completion.

## Rollback

Restore the workspace from the Part A step 1 snapshot (or the Part B archive folder). Because the previous user's state was archived rather than deleted, a reset is always reversible.

<!-- Maintenance: the boot-time guard lives in AGENTS.md → First session: onboarded or not?; keep the mismatch-stop wording in step with it. Sibling paths: repurposing-an-existing-agent.md, updating-an-agent.md. -->
