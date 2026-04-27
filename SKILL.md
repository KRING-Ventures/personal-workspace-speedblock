---
name: personal-workspace-setup
description: >
  Stand up a new Personal Workspace user — KRING-internal or venture
  deployment — by provisioning their accounts, creating their private
  personal-layer repo, seeding it from the shared agent-file blueprints,
  deploying their personal OpenClaw agent on Telegram, and handing off to the
  agent's own first-session BOOTSTRAP dialogue. Use when a new user joins (KRING
  team or a venture) and needs their full work environment (Google Workspace,
  Slack, Notion, GitHub, Telegram) plus their personal OpenClaw agent stood up.
  Reads `onboarding.md` for the human-led setup sequence and ships
  `agent-files/` as the payload deployed into the user's runtime. Does **not**
  handle ongoing operation or framework-version catch-ups — those are owned by
  each deployed agent's session-boot loop in `agent-files/AGENTS.md`. Does
  **not** run the user's first-session onboarding — that's a dialogue between
  the deployed agent and its user, scripted in
  `agent-files/onboarding/BOOTSTRAP.md`.
---

# Personal Workspace Setup

Use this skill to set up a new Personal Workspace user — KRING-internal or venture deployment.

## When to use

- A new user (KRING team, portfolio company, partner, or external venture) is joining and needs their full work environment + personal OpenClaw agent.
- An existing user needs a fresh agent instance (e.g. after losing access to their previous one).

## When NOT to use

- **Ongoing agent operation.** The deployed agent runs itself via `agent-files/AGENTS.md`.
- **Framework-version catch-ups for existing users.** Handled by the agent's session-boot catch-up loop against `CHANGELOG.md` + `agent-files/onboarding/MIGRATIONS/`.
- **Running the user's first-session onboarding.** That's a conversation between the deployed agent and its user, scripted in `agent-files/onboarding/BOOTSTRAP.md`. This skill ships the BOOTSTRAP file; it doesn't execute it.

## Core job

Deliver the two layers a new user needs, then get out of the way:

1. **The user's environment** — Google Workspace, Slack, Notion, GitHub, Telegram accounts wired against the relevant tenants. For KRING-internal users that's KRING's tenants; for venture deployments it's the venture's own tenants, which the venture must already have in place. KRING does not provision into a venture's accounts.
2. **The user's personal OpenClaw agent** — a deployed runtime on Telegram, pointed at the shared framework (this repo's `agent-files/`) and at the user's own private personal-layer repo (seeded from the per-user blueprints in `agent-files/`).

Once the agent sends its first Telegram message to the user, this skill's work is done. The agent owns the conversation from there.

## How to run it

Follow `onboarding.md` end-to-end. It carries the canonical setup sequence.

**Preconditions (don't start without these):**

- The venture's tenants are in place (Google Workspace, Slack, Notion, GitHub) — owned by the account provisioner. See `onboarding.md` § *Prerequisites*.
- The user has completed Step 0: sent their Telegram handle, the number of OpenClaw agents they need, and the chosen name for each agent. Without this, the operator has nothing to wire against.

**Operator steps:**

1. **Provision the user's workspace accounts** — Google Workspace, Slack, Notion, GitHub (if relevant), Telegram (user's existing). Issued by the account provisioner against the relevant tenants (KRING's, or the venture's).
2. **Create the user's private personal-layer repo** — seed from this repo's `agent-files/` per-user blueprints (`IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/AUTOMATIONS.md`, empty `MEMORY.md`, empty `memory/`, empty `STATE_VERSION`). Leave `{{FROM_BOOTSTRAP}}` markers in place — the agent fills them during its first session.
3. **Wire the OpenClaw runtime** — deploy a new OpenClaw instance for each agent the user requested, set its `{{AGENT_NAME}}` to the user's Step 0 choice, point it at both file layers (shared framework + user's private repo), and connect Telegram.
4. **Hand off to the agent** — send the user the Telegram handle. The agent runs `agent-files/onboarding/BOOTSTRAP.md` as a dialogue with its user.

Any time this skill would otherwise "do something for the user" beyond the user's Step 0 inputs — wiring their tools, filling their `USER.md`, choosing the agent's vibe — stop. That's the agent's job during BOOTSTRAP. Pre-filling beyond Step 0 breaks the relationship the first session is meant to build.

## Assets

`agent-files/` — the payload deployed into every personal OpenClaw agent.

- **Framework files** (identical for every agent): `SOUL.md`, `AGENTS.md`, `HEARTBEAT.md`, `KRING.md`, `MEMORY.md` template, `templates/` (daily / weekly / email-draft), `onboarding/BOOTSTRAP.md`, `onboarding/STATE_VERSION`, `onboarding/MIGRATIONS/`.
- **Per-user blueprints** (cloned into the user's private repo, filled by the agent during BOOTSTRAP): `IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/AUTOMATIONS.md`.

See `agent-files/README.md` for the full layout and the framework-vs-personal split.

## Human deliverables (read alongside this skill)

- **`playbook.md`** — Personal Workspace operating manual. What the user is stepping into: tool stack, four AI helpers, what their OpenClaw agent does, working rhythm. Read by the user; read by anyone orienting to how Personal Workspace works.
- **`onboarding.md`** — Setup flow in detail. The canonical reference for steps 1–4 above, written for whoever runs the setup.
- **`human-roles.md`** — Who operates what. Names the human roles this skill assumes (account provisioner, runtime operator, framework maintainer, user) and where each one's responsibility starts and ends.

## Version

Current framework version lives in `agent-files/onboarding/STATE_VERSION`. Each deployed agent tracks its own version in its private repo and catches up via the loop in `agent-files/AGENTS.md`. Shipping a new version: update `CHANGELOG.md`, bump `STATE_VERSION`, tag `v<x.y.z>`, push.

## Quality bar

A clean run leaves the user with:

- All five core accounts (Google Workspace, Slack, Notion, GitHub, Telegram) active.
- A private personal-layer repo they own, seeded with `{{FROM_BOOTSTRAP}}` markers in the right places.
- A running OpenClaw agent on Telegram (one per agent the user requested in Step 0) that has already pulled both layers and is waiting for the first message.
- The agent's `{{AGENT_NAME}}` set from the user's Step 0 choice — not invented by the operator. No pre-filled `USER.md`, no operator-imposed vibe, no wired tools other than Telegram. The agent starts BOOTSTRAP from a clean state.
