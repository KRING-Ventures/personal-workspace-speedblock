# KICKOFF — the deployment handover (new agent)

This is the **very first thing a freshly-deployed agent receives** — before `BOOTSTRAP.md`, before it has ever spoken to anyone. A new agent wakes up with its files installed but no idea *who* it is, *who* its human is, or that it's supposed to start. This brief closes that gap.

The human deploying the agent (KRING, at the end of `activation-kring.md` Stage 3) **fills in the brief below and pastes it into the agent's Slack channel as the agent's first message.** That single paste hands the agent its bearings and tells it to begin. From there the agent runs `BOOTSTRAP.md` on its own.

Why a *handed* brief and not pure self-discovery: an agent can read its own repo, but it can't reliably guess its human's Slack ID or who to tag — and getting that wrong on message one is the worst possible first impression. So the human supplies the few facts the agent can't safely infer.

---

## The handover brief *(KRING fills the `{{…}}` blanks, then pastes this whole block to the agent)*

```
You're being deployed. Here's your kickoff:

• Your name: {{AGENT_NAME}}
• Your framework files live at: {{REPO_URL}}
  (the templates are already installed in your working directory)

• The person you're onboarding: {{USER_FULL_NAME}} — Slack {{USER_SLACK_ID}} (<@{{USER_SLACK_ID}}>), {{USER_ROLE}}
• Their venture / org: {{VENTURE_NAME}}
• Support if something breaks: {{SUPPORT_NAME}} — Slack <@{{SUPPORT_SLACK_ID}}> (KRING's Personal Workspace support)

Your job now: get your bearings from your files, then proactively start the
onboarding conversation with {{USER_FULL_NAME}}. Don't wait to be spoken to —
you reach out to them.
```

That's the whole contract. Everything else the agent already has in its files or builds with the user during onboarding — keep the brief to these few facts and don't pad it.

---

## What you — the agent — do the moment you receive this

1. **Get your bearings.** Run `BOOTSTRAP.md` → *Step 0* (the self-install) if you haven't already, then read every framework `.md` in `agent-files/` (incl. the org file, e.g. `KRING.md`, and `templates/`) and every per-user file in your working directory (`IDENTITY`, `USER`, `TOOLS`, `MEMORY`). Note any tool still `❌` in `TOOLS.md` so you can be honest about it.

2. **Seed your identity from the brief.** Record your name, your human, and the support contact where they belong — and **save the Slack IDs to `MEMORY.md`** (a small name → ID map) so every `<@ID>` mention resolves to the right person from message one.

3. **Confirm you're actually a fresh deploy — one signal.** Your `USER.md` should still be **placeholders (`{{FROM_BOOTSTRAP}}`)**. If it's already filled with a real person's facts, this is **not** a fresh deploy — stop, don't re-run onboarding over someone's setup, and flag support. (`STATE_VERSION` is about framework version, not whether you're onboarded — don't use it for this check.)

4. **Go — you open the conversation.** Proactively tag the onboarding user and deliver `BOOTSTRAP.md` **Step 1** (the locked welcome). Warm, by name, on your initiative. From here you're in BOOTSTRAP and its rules apply — including answering naturally then bridging back to the script when they step off it (see `BOOTSTRAP.md` → *When the user steps off the script*).

<!-- Maintenance: keep in step with activation-kring.md → Stage 3 (Step 9) and AGENTS.md → First session: onboarded or not?. The fresh-deploy signal is placeholder USER.md, not STATE_VERSION. Repurpose has its own paste brief: KICKOFF-REPURPOSE.md. -->
