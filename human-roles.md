# Human roles in Personal Workspace

The active human layer this Speedblock assumes. Each role has a narrow responsibility and a clean handoff to the next — none of them overlap with the agent's job.

## Roles

### 1. The venture

- **Who:** The venture activating Personal Workspace for its users.
- **Does:** Owns its own tenants — Google Workspace, Slack, Notion, GitHub. Provisions user accounts inside those tenants. Submits the intake to KRING (per-venture confirmation + per-user details: name, email, accounts ready, Telegram handle, assistant name). After deployment, runs the rollout — distributes each assistant's Telegram handle to the corresponding user, points each user at the playbook, and supports each user through the first conversation.
- **Does not:** Wire OpenClaw runtimes (that's KRING). Run anyone's first conversation (that's between each user and the user's assistant).
- **Hand-offs:** Submits the intake to KRING. Receives deployed assistant handles from KRING. Hands each assistant handle to the user it belongs to.

### 2. KRING

- **Who:** KRING — the deploying party for Personal Workspace.
- **Does:** Receives the venture's intake. Deploys one OpenClaw runtime per user (one assistant per user). Loads the framework's onboarding templates so each assistant knows how to run the first conversation. Sets each assistant's name from the intake. Wires Telegram. Confirms each assistant is reachable before handing back. Owns and maintains the framework itself — ships versions, updates `CHANGELOG.md`, bumps `STATE_VERSION`, authors migration guidance when a version changes file shapes.
- **Does not:** Provision into a venture's tenants. Pre-fill any per-user file beyond what comes from the intake (no operator-imposed `USER.md` content, no operator-invented vibe). Wire any tools beyond Telegram — that happens in each user's first conversation.
- **Hand-off:** Returns the deployed assistant Telegram handles to the venture.

### 3. The user

- **Who:** Each person being onboarded by the venture.
- **Does:** When the venture asks, provides what the user owns — confirming Telegram is installed on a device the user uses day-to-day, sharing a Telegram handle, and choosing a name for the assistant. After deployment, sends the first message to the assistant on Telegram and runs through the first conversation — connecting tools, validating what the assistant pulled from those tools, and filling the gaps tools can't tell it (how the user makes decisions, what the user wants the assistant to push back on, etc.). Also wires any tools beyond the standard stack (e.g. Linear, Figma) with the assistant in conversation, post-deployment.
- **Does not:** Need to know anything about the framework internals beforehand. The first conversation handles orientation.

## The active human layer vs. the AI layer

Personal Workspace isn't fully autonomous — humans do four things the AI does not:

1. **Provision accounts** inside the venture's tenants (Google, Slack, Notion, GitHub).
2. **Deploy and wire runtimes** for each new assistant.
3. **Author and version the framework** — agent-files, playbook, onboarding, this file.
4. **Show up for the first conversation** — each user, on Telegram, starting their assistant's first session.

Everything else — memory, drafting, briefing, tool reach, commitment tracking, proactive check-ins, catch-up on new framework versions — the deployed assistant handles itself.

## Future consolidation

When parts of the venture or KRING side of the flow are replaced by automation (e.g. SSO-driven provisioning, self-service runtime deployment, self-service intake), update this file to reflect what's actually still human. Don't leave stale role assignments here — they misrepresent who to go to when something breaks.
