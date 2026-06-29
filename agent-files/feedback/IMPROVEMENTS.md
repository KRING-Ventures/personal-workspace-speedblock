# IMPROVEMENTS — the feedback ledger

*When {{USER_FIRST_NAME}} corrects me, the fix shouldn't die in the chat. It gets noted here so it can later be promoted into the framework for every agent.*

## What this file is

A running log of **corrections, misses, and improvements** surfaced during real use. Whenever {{USER_FIRST_NAME}} points out something I got wrong or didn't do — *"why didn't you run my inbox triage?"* — I fix it in the moment **and** append an entry here.

This is the reverse of the update flow: framework updates travel repo → agent; these learnings travel agent → repo. KRING periodically harvests the `framework`-tagged entries across all agents and folds them into the template files so the same problem never reaches the next agent (see `runbooks/harvesting-improvements.md`).

## How this file is used — read the load rule

- **Write-mostly.** I append to it when a correction happens. I do **not** load it at boot and it is **not** part of the context bundle — it would only burn boot budget for entries I rarely need to re-read. (See `AGENTS.md` → *Where state lives* / *Capturing fixes*.)
- **Per-user and local.** It lives on this runtime, alongside `memory/` and `automations/`. It is **never overwritten by a framework update** — accumulated entries stay.
- **Read only at harvest** — by KRING (or me, when asked to review what's pending).

## When to log an entry

Log when {{USER_FIRST_NAME}}:
- points out something I should have done and didn't, or did wrong;
- corrects a default, a behaviour, or a piece of wording;
- asks for a fix to how I operate (not a one-off task).

Don't log: ordinary task requests, things already captured as automations (`automations/AUTOMATIONS.md`), or pure memory facts about the user (those go to `MEMORY.md`).

## Classify every entry — this is what makes the harvest work

- **`personal`** — specific to {{USER_FIRST_NAME}} (a preferred brief time, a tone, a named contact rule). **Stays here / in my own files. Never promoted.**
- **`framework`** — a gap or bug any agent would hit (a missing behaviour, a wrong default, a broken gate, unclear onboarding copy). **This is what KRING harvests upstream.**

If unsure, tag `framework` and add a note — better surfaced than lost. The harvest step makes the final call.

## Entry format

Append newest at the top, under *Entries*. One entry per correction:

```
## YYYY-MM-DD — short title
- **Trigger:** what {{USER_FIRST_NAME}} said / what went wrong
- **Root cause:** why it happened
- **Fix applied:** what I changed locally, right now
- **Type:** personal | framework
- **Maps to:** (framework only) template file + section — e.g. `HEARTBEAT.md → inbox triage`, `scripts/smart-trigger.py`
- **Status:** open | promoted <PR/commit> | wontfix <reason>
```

---

## Entries

<!-- Newest first. Nothing logged yet. -->
