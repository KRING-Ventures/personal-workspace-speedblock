# Human roles in Personal Workspace

The active human layer this Speedblock assumes — same shape whether the user is KRING-internal or being onboarded inside a venture. Each role has a narrow responsibility and a clean handoff — none of them overlap with the agent's job.

## Roles

### 1. Account provisioner

- **Who:** Whoever owns the user's tenants. For KRING-internal users, KRING ops/admin. For venture deployments, the venture itself (their ops/admin) — KRING does not provision into a venture's accounts.
- **Does:** Ensures all required user accounts exist *before* runtime wire-up — Google Workspace (or equivalent), Slack, Notion, GitHub (if role-relevant), plus any venture-specific tools the agent will need to reach. Issues invites, not credentials.
- **Hand-off:** Confirms to the runtime operator that the tenants and accounts are ready. If anything is missing, runtime wire-up doesn't start — it bounces back to this role until the environment is in place.

### 2. Runtime operator

- **Who:** Corey (KRING side, supports both KRING-internal and venture deployments today).
- **Does:** Deploys the OpenClaw runtime instance for each new user. Wires Telegram (bot token, chat binding). Points the runtime at both file layers — the shared framework (this repo's `agent-files/`) and the user's own private personal-layer repo. Confirms the agent is running and reachable on Telegram before handoff.
- **Does not:** Start wire-up before the account provisioner has confirmed accounts are ready. Pre-fill `USER.md`. Choose the agent's name or vibe. Wire any tools beyond Telegram. Those all belong to the agent's first session with the user.
- **Hand-off:** Tells the user the Telegram handle and that they can send the first message whenever they're ready.

### 3. Framework maintainer

- **Who:** August.
- **Does:** Owns the framework content — `agent-files/`, `playbook.md`, `onboarding.md`, this file. Ships versions (updates `CHANGELOG.md`, bumps `STATE_VERSION`, tags releases). Authors migrations when a version changes per-user state shape.
- **Does not:** Own each user's private personal-layer repo — that's the user's.

### 4. User

- **Who:** The person being onboarded.
- **Does:** Runs their own BOOTSTRAP conversation with their agent on Telegram — wires their tools one at a time, validates the draft `USER.md` the agent pulled from their tools, fills the human gaps (how they think, what they want the agent to push back on, etc.). Owns their private personal-layer repo after handoff.
- **Does not:** Need to know anything about the framework internals before starting. BOOTSTRAP orients them.

## The active human layer vs. the AI layer

Personal Workspace isn't fully autonomous — real humans do four things the AI does not:

1. **Provision accounts** inside third-party tenants (Google, Slack, Notion, GitHub).
2. **Deploy and wire runtimes** for each new agent instance.
3. **Author the framework** — the shared agent-files, the playbook, the onboarding protocol.
4. **Show up for the first conversation** — the user, on Telegram, starting BOOTSTRAP.

Everything else — memory, drafting, briefing, tool reach, commitment tracking, proactive check-ins, catch-up on new framework versions — the deployed agent handles itself.

## Future consolidation

When the account provisioner and runtime operator overlap with automated onboarding (e.g. SSO-driven provisioning, self-service runtime deployment), update this file to reflect what's actually still human. Don't leave stale role assignments here — they misrepresent who to go to when something breaks.
