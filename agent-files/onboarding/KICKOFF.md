# KICKOFF — the deployment handover

This is the **very first thing a freshly-deployed agent receives** — before `BOOTSTRAP.md`, before it has ever spoken to anyone. A new agent wakes up with its files installed but no idea *who* it is, *who* its human is, or that it's supposed to start. This brief closes that gap.

The human deploying the agent (KRING, at the end of `activation-kring.md` Stage 3) **fills in the brief below and pastes it into the agent's Slack channel as the agent's first message.** That single paste hands the agent its bearings and tells it to begin. From there the agent runs `BOOTSTRAP.md` on its own.

Why a *handed* brief and not self-discovery: an agent can read its own repo, but it can't reliably guess its human's Slack ID or who to tag — and getting that wrong on message one is the worst possible first impression. So the human supplies the few facts the agent can't safely infer.

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

1. **Get your bearings.** Read every framework `.md` in `agent-files/` (incl. the org file, e.g. `KRING.md`, and `templates/`) and every per-user file in your working directory (`IDENTITY`, `USER`, `TOOLS`, `MEMORY`). Confirm the templates are actually installed and note any tool still `❌` in `TOOLS.md` so you can be honest about it. This is the same pre-read `BOOTSTRAP.md` → *Before you start* expects — do it now.

2. **Seed your identity from the brief.** Record your name, your human, and the support contact where they belong — and **save the Slack IDs to `MEMORY.md`** (a small name → ID map) so every `<@ID>` mention resolves to the right person from message one. This is the exact context KRING would otherwise have to hand you by hand mid-conversation.

3. **Confirm you're actually a fresh deploy.** `STATE_VERSION` at your repo root should be absent or empty. If it's already set, this is **not** a first deploy — stop, don't re-run onboarding, and flag it to support rather than restarting someone's setup.

4. **Go — you open the conversation.** Proactively tag the onboarding user in the channel and deliver `BOOTSTRAP.md` **Step 1** (the locked welcome). Warm, by name, on your initiative. From here you're in BOOTSTRAP and its rules apply — including *answer-then-bridge* when they step off the script.

<!-- Maintenance: keep in step with activation-kring.md → Stage 3 (Step 9) and BOOTSTRAP.md → Before you start. A change here is a change there. -->
