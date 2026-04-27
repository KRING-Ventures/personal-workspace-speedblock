---
name: personal-workspace-setup
description: >
  Stand up the assistants for a venture activating Personal Workspace —
  receive the venture's intake, deploy one OpenClaw runtime per user
  (one assistant per user), create each user's private settings repo and
  seed it from the per-user blueprints, set each assistant's name from the
  intake, wire Telegram, confirm the assistants are reachable, and hand the
  assistant Telegram handles back to the venture for rollout. Use when a
  venture activates Personal Workspace and needs its assistants deployed.
  Reads `onboarding.md` for the canonical three-step flow (Activate →
  Build & deploy → Finish onboarding) and ships `agent-files/` as the payload
  deployed into each runtime. Does **not** provision into the venture's
  tenants — the venture owns its own accounts. Does **not** handle ongoing
  operation or framework-version catch-ups — those are owned by each deployed
  assistant's session-boot loop in `agent-files/AGENTS.md`. Does **not** run
  any user's first conversation — that's a dialogue between the deployed
  assistant and its user, scripted in `agent-files/onboarding/BOOTSTRAP.md`.
---

# Personal Workspace Setup

Use this skill to deploy the assistants for a venture that's activating Personal Workspace.

## When to use

- A venture has activated the Speedblock and submitted its intake — accounts confirmed, per-user details (name, email, Telegram handle, assistant name) provided.
- An existing user needs a fresh assistant instance (e.g. after losing access to their previous one).

## When NOT to use

- **Ongoing assistant operation.** The deployed assistant runs itself via `agent-files/AGENTS.md`.
- **Framework-version catch-ups for existing users.** Handled by each assistant's session-boot catch-up loop against `CHANGELOG.md` + `agent-files/onboarding/MIGRATIONS/`.
- **Running a user's first conversation.** That's a conversation between the deployed assistant and its user, scripted in `agent-files/onboarding/BOOTSTRAP.md`. This skill ships the BOOTSTRAP file; it doesn't execute it.

## Core job

Deliver one deployed assistant per user in the venture's intake, then hand back to the venture:

1. **The deployed runtime** — an OpenClaw runtime instance on Telegram, pointed at the shared framework (this repo's `agent-files/`) and at the user's own private settings repo, with the assistant's name set from the intake.
2. **The user's private settings repo** — a private GitHub repo holding the personal layer of this user's assistant, seeded from the per-user blueprints in `agent-files/`. Filled by the assistant itself during the user's first conversation.

Once the assistants are reachable on Telegram, this skill hands their Telegram handles back to the venture. The venture takes it from there.

## Preconditions

Don't start until both of these are in place:

- **The venture's tenants exist.** Google Workspace, Slack, Notion, GitHub — the fixed beta tech stack every Personal Workspace deployment runs on. Without these, there's nothing for the assistants to wire against. KRING does not provision into a venture's tenants.
- **The intake is complete.** Per-venture confirmation + per-user details (full name, primary email, accounts ready, Telegram handle, assistant name). See `onboarding.md` § *Step 1 — Activate the Speedblock*.

## How to run it

Follow `onboarding.md` end-to-end. The canonical sequence:

1. **Verify the intake.** Confirm everything in the *Preconditions* above is in place. If anything is missing, bounce it back to the venture before starting.
2. **For each user in the intake:**
   - Create the user's private settings repo. Seed it from this repo's `agent-files/` per-user blueprints (`IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/AUTOMATIONS.md`, empty `MEMORY.md`, empty `memory/`, empty `STATE_VERSION`). Leave `{{FROM_BOOTSTRAP}}` markers in place — the assistant fills them during the first conversation.
   - Deploy an OpenClaw runtime instance for this user.
   - Set the assistant's `{{AGENT_NAME}}` from the intake.
   - Point the runtime at both file layers (shared framework + user's private settings repo).
   - Wire Telegram (bot binding).
   - Confirm the assistant is reachable on Telegram.
3. **Hand back to the venture.** Return a list of assistant Telegram handles, one per user. The venture handles the rest of the rollout.

Any time this skill would otherwise "do something for the user" beyond what's in the intake — wiring their tools, filling their `USER.md`, inventing the assistant's vibe — stop. That's the assistant's job during the first conversation. Pre-filling beyond intake breaks the relationship the first conversation is meant to build.

## Assets

`agent-files/` — the payload deployed into every assistant.

- **Framework files** (identical for every assistant): `SOUL.md`, `AGENTS.md`, `HEARTBEAT.md`, `KRING.md`, `MEMORY.md` template, `templates/` (daily / weekly / email-draft), `onboarding/BOOTSTRAP.md`, `onboarding/STATE_VERSION`, `onboarding/MIGRATIONS/`.
- **Per-user blueprints** (cloned into each user's private settings repo, filled by the assistant during the first conversation): `IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/AUTOMATIONS.md`.

See `agent-files/README.md` for the full layout and the framework-vs-personal split.

## Human deliverables (read alongside this skill)

- **`playbook.md`** — Personal Workspace operating manual. What users are stepping into: tool stack, four AI helpers, what their assistant does, working rhythm. Read by users and by anyone orienting to how Personal Workspace works.
- **`onboarding.md`** — The three-step flow in detail (Activate → Build & deploy → Finish onboarding). Read by the venture and by whoever runs deployment.
- **`human-roles.md`** — Who does what across the three steps (the venture, KRING, each user).

## Version

Current framework version lives in `agent-files/onboarding/STATE_VERSION`. Each deployed assistant tracks its own version in its private settings repo and catches up via the loop in `agent-files/AGENTS.md`. Shipping a new version: update `CHANGELOG.md`, bump `STATE_VERSION`, tag `v<x.y.z>`, push.

## Quality bar

A clean run leaves the venture with:

- One deployed OpenClaw assistant on Telegram per user in their intake — already pulled both layers, named from the intake, waiting for the first message from its user.
- A private settings repo per user, seeded with `{{FROM_BOOTSTRAP}}` markers in the right places — owned by the user from this point on.
- No pre-filled `USER.md`. No invented vibe. No wired tools beyond Telegram. Each assistant starts the first conversation from a clean state.
- A list of assistant Telegram handles handed back, one per user, ready for the venture to distribute.
