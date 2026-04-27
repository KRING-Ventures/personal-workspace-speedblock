# Human roles in Personal Workspace

The active human layer this Speedblock assumes. Each role has a narrow responsibility and a clean handoff to the next — none of them overlap with the agent's job.

## Roles

### 1. The venture

- **Who:** The venture activating Personal Workspace for its users.
- **Does:** Owns its own tenants — Google Workspace (or equivalent), Slack, Notion, GitHub, plus any venture-specific tools the assistants should reach. Provisions user accounts inside those tenants. Submits the intake to KRING (per-venture confirmation + per-user details: name, email, accounts ready, Telegram handle, assistant count, assistant name(s)). After deployment, runs the rollout — distributes the assistant Telegram handles to its users, points them at the playbook, and supports them through their first conversation.
- **Does not:** Wire OpenClaw runtimes (that's KRING). Run anyone's first conversation for them (that's between each user and their assistant).
- **Hand-offs:** Submits the intake to KRING. Receives deployed assistant handles from KRING. Hands each assistant handle to the user it belongs to.

### 2. KRING

- **Who:** KRING — the deploying party for Personal Workspace.
- **Does:** Receives the venture's intake. Deploys the OpenClaw runtime for each requested assistant. Creates the user's private settings repo, seeds it from the per-user blueprints, and points the runtime at both file layers (the shared framework + the user's private settings repo). Sets each assistant's name from the intake. Wires Telegram. Confirms each assistant is reachable before handing back. Owns and maintains the framework itself — ships versions, updates `CHANGELOG.md`, bumps `STATE_VERSION`, authors migration guidance when a version changes per-user file shapes.
- **Does not:** Provision into a venture's tenants. Pre-fill any per-user file beyond what comes from the intake (no operator-imposed `USER.md` content, no operator-invented vibe). Wire any tools beyond Telegram — that happens in each user's first conversation.
- **Hand-off:** Returns the deployed assistant Telegram handles to the venture.

### 3. The user

- **Who:** Each person being onboarded by the venture.
- **Does:** When their venture asks, provides the bits they own — confirming Telegram is installed on a device they use day-to-day, sharing their Telegram handle, and choosing a name for each assistant. After deployment, sends the first message to their assistant on Telegram and runs through the first conversation — connecting their tools, validating what their assistant pulled from those tools, and filling the gaps tools can't tell it (how they make decisions, what they want their assistant to push back on, etc.).
- **Does not:** Need to know anything about the framework internals beforehand. The first conversation orients them.

## The active human layer vs. the AI layer

Personal Workspace isn't fully autonomous — humans do four things the AI does not:

1. **Provision accounts** inside the venture's tenants (Google, Slack, Notion, GitHub).
2. **Deploy and wire runtimes** for each new assistant.
3. **Author and version the framework** — agent-files, playbook, onboarding, this file.
4. **Show up for the first conversation** — each user, on Telegram, starting their assistant's first session.

Everything else — memory, drafting, briefing, tool reach, commitment tracking, proactive check-ins, catch-up on new framework versions — the deployed assistant handles itself.

## Future consolidation

When parts of the venture or KRING side of the flow are replaced by automation (e.g. SSO-driven provisioning, self-service runtime deployment, intake submitted directly through Cosmica), update this file to reflect what's actually still human. Don't leave stale role assignments here — they misrepresent who to go to when something breaks.
