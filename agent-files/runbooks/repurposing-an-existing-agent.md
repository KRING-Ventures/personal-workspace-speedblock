# Repurposing an Existing Agent into Personal Workspace

Turning an OpenClaw agent that **already has its own history, memory, automations, and personality** into a Personal Workspace agent — without wiping what it already knows.

## Which path am I on?

Three different things, don't confuse them:

- **Clean-sheet deploy** — brand-new agent, no prior state. Runs `BOOTSTRAP.md` (the full first-conversation). See `activation.md` → Part 2.
- **Version update** — an agent already on Personal Workspace catching up to a newer framework version. Automatic at boot via the catch-up loop. See `agent-files/AGENTS.md` → *Staying current* and `runbooks/updating-an-agent.md`. Nothing to do here.
- **Repurpose (this file)** — an existing agent that was *something else* (or a generic assistant) becoming a Personal Workspace agent **for the same human**. It has real data you must preserve. As long as its `USER.md` carries that real data (no `{{FROM_BOOTSTRAP}}` placeholders), boot will **not** run `BOOTSTRAP` — a filled `USER.md` is the "not a blank slate" signal. The only way to trip the clean-sheet intro is to drop in template files and leave the placeholders. **This path is operator-triggered, not boot-detected** — the agent doesn't sniff it out on its own. KRING runs Part A, then prompts the agent to run Part B. This runbook is how.
- **Reset / re-provision** — an agent whose state belongs to a *different* person, being handed to a **new** user. That is **not** a repurpose: the old user's data is archived, not inherited, and the new user gets a clean onboarding. See `runbooks/resetting-an-agent.md`. The tell: a repurpose keeps the same human; a reset changes who the user is.

## The load-bearing rule

> Make sure `USER.md` carries the user's real facts — **no `{{FROM_BOOTSTRAP}}` placeholders left** — before the agent's next session. A filled `USER.md` is what tells the framework "this agent is not a blank slate," so it skips `BOOTSTRAP` and never re-runs the clean-sheet first-conversation over a user it already knows. (Also set `STATE_VERSION` to current so the agent doesn't needlessly run version catch-up — but that's housekeeping, not what suppresses `BOOTSTRAP`.)

Everything else is reconciliation around that.

## Part A — Operator steps (KRING)

Prerequisite: shell access to the agent's runtime.

1. **Snapshot first.** Copy the agent's whole working directory somewhere safe (`cp -r` to a dated backup, or confirm its Syncthing mirror is up to date). If anything goes wrong, you restore from this. Never skip it.
2. **Drop in the shared framework.** Add/refresh the shared `agent-files/` (SOUL, AGENTS, KRING, HEARTBEAT, SCHEDULES, templates, BOOTSTRAP, runbooks). These carry no personal data — overwriting them is safe.
3. **Do NOT overwrite the per-user files.** Leave the agent's existing `IDENTITY.md`, `USER.md`, `TOOLS.md`, `MEMORY.md`, `memory/`, and `automations/` in place. These are the user's own — they get *reconciled*, not replaced.
4. **Reconcile the per-user files into PW shape** (content preserved, structure aligned):
   - `IDENTITY.md` — keep the agent's name and identity; map fields to the PW template.
   - `USER.md` — carry every real fact about the user across into the PW *Basics* structure. Don't drop anything; restructure only.
   - `TOOLS.md` — align to the PW standard table. The mandatory stack (Slack, Gmail, Calendar, Drive/Docs) is pre-wired at activation — mark it ✅. Web search and local files are ✅ by default. Carry any extra tools the agent already had into the *User-specific tools* table, marked with their real state. The recommended self-serve tools (GitHub, Notion, etc.) are **not** part of the standard set — leave them ❌/self-serve unless the agent genuinely already has them; the user wires those in their own time, so never mark them connected just because the template lists them. The local mirror stays ❌ until set up.
   - `MEMORY.md` + `memory/*.md` — **content untouched.** These are the user's memory. Adjust only headers/section names if the PW layout needs it; never rewrite the substance.
   - `automations/AUTOMATIONS.md` — preserve every existing entry. Don't delete or duplicate automations.
5. **Set `STATE_VERSION`** at the root of the working directory to the framework's current `agent-files/onboarding/STATE_VERSION` value — so the agent isn't flagged as behind on the framework. (`BOOTSTRAP` is already suppressed by the filled `USER.md` from step 4 — that's the load-bearing rule above.)
6. **Reconcile schedules, don't stack them.** On the next main session the boot self-heal will add any of the standard jobs/triggers (see `SCHEDULES.md`) that are missing — *check existing schedules first so you don't end up with two morning briefs*. Preserve job type: visible jobs may be normal agent crons, prefiltered jobs must keep their hard gate, and silent/silent-unless-action-needed jobs must not post unless broken or a user decision is needed. If the agent already had its own brief/heartbeat-type jobs, fold them into the PW ones rather than running both.

Success signal: the agent boots, does **not** start a clean-sheet intro, keeps all prior memory and automations, and reports it's on the current `STATE_VERSION`.

## Part B — The continuity-aware onboarding (agent-followed script)

A repurposed agent **already knows the user** — so the worst thing it can do is greet them like a stranger and re-ask everything. But it must **not** skip the onboarding either: a repurposed user still deserves the same Personal Workspace onboarding a new user gets — the value, the best practices, the optional demos. The rule is: **deliver the onboarding, skip the introductions, and name the transition.**

This is the script the agent runs on the first main session after repurposing — *instead of* clean-sheet `BOOTSTRAP`. It is the same flow as `onboarding/BOOTSTRAP.md` with three deliberate differences:

1. **It opens by naming the transition** — what the agent is becoming, what's **new**, and what **stays** — instead of a cold "hi, I'm your new assistant."
2. **It confirms identity, it doesn't collect it** — name, language, role and projects are already known, so Steps 1 and 4 become a single quick confirm, not an interview.
3. **Everything else is BOOTSTRAP, unchanged** — the teaching copy (core features, best practices) and the optional demos are delivered from BOOTSTRAP's *locked blocks*, word-for-word.

> This same continuity-aware flow is what `runbooks/updating-an-agent.md` → Part C reaches for when an agent was updated/repurposed *before* the onboarding existed and the user never got it. One script, both paths.

### The flow at a glance

| # | Step | Source | Optional |
|---|------|--------|----------|
| R1 | Welcome back & what's changing | this file (new copy) | — |
| 2 | Core features | BOOTSTRAP Step 2 (verbatim, two greeting-line swaps) | — |
| 3 | How to work with me | BOOTSTRAP Step 3 (verbatim) | — |
| R4 | Confirm migrated basics | this file (new copy) | — |
| 5 | See a feature in action | BOOTSTRAP Step 5 (verbatim) | optional |
| 6 | Build your first automation | BOOTSTRAP Step 6 (verbatim) | optional |
| R7 | Live | this file (new copy) | — |

**Wording rules carry over from BOOTSTRAP.** The blocks below (and the BOOTSTRAP blocks you reuse) are **locked, scripted copy — send each word-for-word**, filling only the `{{…}}` placeholders. Deliver in the language you *already know* this user speaks (from your history / `USER.md`) — you do **not** re-ask for it. If that language isn't English, translate every block faithfully (same wording, structure, bullets, emojis, tone), including the *"next"* cue. The same **answer-then-bridge** rule and **completion checklist** from BOOTSTRAP apply here — let them wander, never lose the place, and only close at R7 once every mandatory step (R1 · 2 · 3 · R4 · R7) and the *After the conversation* finalisation are done. There is **no hard gate** here (BOOTSTRAP's one gate was name + language — you already have both).

---

### Step R1 — Welcome back & what's changing *(Agent)*

**Goal:** the user understands, in one breath, that this is the same agent (nothing lost), that it's becoming their Personal Workspace assistant, and that what's new is what it can now *do* for them.

**Send this exactly** (fill the `{{…}}` placeholders — change nothing else):

```
Quick heads-up, {{USER_FIRST_NAME}} — I've just become your Personal Workspace assistant 🌞

*Same me — nothing's lost.* Everything we've built together stays: what I know about you, our history, your memory, and every automation you've set up. This is an upgrade, not a reset.

*What's new is what I can now do for you.* I've gained a set of built-in features and ways of working designed to take more of the boring, heavy, repetitive work off your plate — proactively, every day.

Let me give you the quick tour so you know what's now possible. Just say "next" when you're ready 🚀
```

**Capture:** nothing — delivery only. (You already have name, language, timezone.)

**Then:** when they're ready — or with a light nudge if they go quiet (you lead; see BOOTSTRAP → *Carrying the conversation*) — move into Step 2.

---

### Step 2 — Core features *(Agent)*

**Goal:** the user sees what comes built in, and that it's extendable to their own needs.

**Send BOOTSTRAP Step 2 verbatim, with exactly two line swaps** so it doesn't read as if you'd never met this user. BOOTSTRAP Step 2 opens with a *first-introduction* greeting and a *just-born* framing — both contradict R1 ("same me, nothing's lost"). Swap only these two lines; change nothing else:

1. The greeting line `Great to meet you, {{USER_FIRST_NAME}}! 🫶🏼` → becomes:

```
Here's the quick tour, {{USER_FIRST_NAME}} 🫶🏼
```

2. The core-features header line `*I'm already born with core features:*` → becomes:

```
*Here are the core features I now run for you:*
```

Everything else in the BOOTSTRAP Step 2 block — the feature bullets, the "you can personalize me…" paragraph, and the closing *"next"* line — is sent **unchanged, word-for-word**.

**Capture:** nothing — delivery only.

**Silent (no message):** do **not** blindly register fresh jobs — a repurposed agent may already have schedules. The Part A step 6 reconcile (and the boot self-heal) handles this: add only the standard jobs that are *missing*, preserve each job's type, and fold any pre-existing brief/heartbeat jobs into the PW ones rather than running duplicates. Verify against `SCHEDULES.md`; log to `automations/AUTOMATIONS.md`.

**Then:** move into Step 3.

---

### Step 3 — How to work with me *(Agent)*

**Goal:** the user picks up a few best practices, understands agents are still early, and knows when to use a personal vs. a shared agent. This is genuinely **new** to a repurposed user — don't shortcut it.

**Send BOOTSTRAP Step 3 verbatim.** No changes — the copy already fits a returning user.

**Capture:** nothing — delivery only.

**Then:** move into Step R4. (The full **AI Commandments** stay available on demand — see BOOTSTRAP → on-demand walkthroughs.)

---

### Step R4 — Confirm migrated basics *(Agent + user)*

**Goal:** confirm what you already know instead of re-interviewing. Replaces BOOTSTRAP Steps 1 + 4 — you carried this over in Part A, so you're checking it's current, not asking from scratch.

**Send this exactly** (fill every `{{…}}` from the migrated `USER.md` / `MEMORY.md` — if a field is genuinely blank, ask only for that one):

```
One quick check before we move on 👀

I've kept everything I already know about you, so I won't re-interview you — just a quick confirm that it's still current:
• Name: {{PREFERRED_NAME}}
• Language: {{LANGUAGE}}
• Role: {{ROLE}}
• Working on: {{PROJECTS}}

Anything there changed, or good as-is?
```

**Capture:** patch anything stale into `USER.md` (name, language, role) and `MEMORY.md` (projects). Don't expand into a fresh interview — confirm and move on. See BOOTSTRAP → *Carrying the conversation* (don't re-ask what you already know).

**Then:** thank them, then move into Step 5.

---

### Step 5 — See a feature in action *(Agent + user · optional)*

**Send BOOTSTRAP Step 5 verbatim** — the "draft a reply to a recent email" showcase, exactly as a new user gets it. The draft stays in Drafts; never sent.

**Then:** if they skip, *"no problem — we can do this any time."* Move on to Step 6.

---

### Step 6 — Build your first automation *(Agent + user · optional)*

**Send BOOTSTRAP Step 6 verbatim** — find their biggest recurring pain, turn it into a working automation, log it in `automations/AUTOMATIONS.md`, show them how to switch it off.

**Then:** move to Step R7.

---

### Step R7 — Live *(Agent)*

**Goal:** close cleanly — recap that everything carried over and the agent simply does more now.

**Send this exactly** (fill the `{{…}}` placeholders — change nothing else):

```
That's it — you're all set on Personal Workspace 🫶🏼

To recap:
• Everything we had together is intact — I've just got more I can do for you now.
• I'll start running my core features and automations from here on, to make your workday lighter.
• If anything ever looks off — a brief that didn't arrive, a draft not written — just tell me and I'll fix it fast.
• And whenever something keeps eating your time, point me at it and we'll automate it together.

Do you have any final questions, or anything you want me to know? 🌞
```

---

### Optional — offer the extras

Not a scripted step; offer these naturally if they fit, after R7 or whenever relevant:

- **Local mirror (Syncthing)** — a real opt-in backup of the agent's working directory to the user's Mac/PC. Offer to set it up: `runbooks/syncthing-local-mirror.md`. Optional.
- **Recommended self-serve tools** (GitHub, Notion, etc.) — these are the user's own to connect in their own time and are **not** part of the standard PW stack (see `playbook.md` → Recommended stack). Mention they exist if useful, but don't wire them during onboarding and don't imply the agent will.

## After the conversation

Same finalisation as BOOTSTRAP, minus the identity collection (you already had it):

1. **Patch `USER.md`** with anything R4 corrected — name, language, role. Keep it lean.
2. **Top up `MEMORY.md`** — current projects, the automation built (if any), any fresh personalization signals. Don't overwrite existing memory.
3. **Log today's session** in `memory/YYYY-MM-DD.md` — note that the continuity-aware onboarding ran, so a future update doesn't re-deliver it (`updating-an-agent.md` → Part C checks for this).
4. **Confirm `TOOLS.md`** reflects the real wired state.
5. **Confirm the schedule** — all standard jobs/triggers present with the correct type, no duplicates, logged in `automations/AUTOMATIONS.md`. This is the one piece that, if missing, silently kills all proactivity.
6. **Confirm `STATE_VERSION`** equals the framework's current value (set in Part A step 5). The continuity onboarding is now complete and won't run again — future sessions go straight to the catch-up loop in `AGENTS.md`.

What the user must **not** experience: losing memory, losing automations, being asked to re-state things the agent already knew, a duplicate set of scheduled jobs firing — or, the failure this fixes, being quietly dropped onto Personal Workspace and **never shown the onboarding at all**.

## Rollback

If the reconciled state looks wrong, restore the working directory from the Part A step 1 snapshot and try again. Because per-user content was preserved (not regenerated), rollback is always clean.
