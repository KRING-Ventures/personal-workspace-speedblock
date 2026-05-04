# Human roles in Personal Workspace

The humans this Speedblock relies on. Each role has a narrow responsibility and a clean handoff to the next — none of them overlap with the agent's job.

## Roles

### 1. The venture

**Who:** The venture activating Personal Workspace for its users.

**Does:**
- Owns its own tenants (Google Workspace, Slack, Notion, GitHub) and provisions user accounts inside them.
- Submits the intake to KRING — per-venture confirmation plus per-user details (name, email, accounts ready, Telegram handle, assistant name).
- Runs the rollout after deployment — hands each assistant's Telegram handle to the right user, points each user at the playbook, and supports them through the first conversation.

**Does not:** Wire OpenClaw runtimes (that's KRING). Run anyone's first conversation (that's between each user and the user's assistant).

**Hand-offs:** Submits the intake to KRING. Receives deployed assistant handles back. Hands each handle to the user it belongs to.

### 2. KRING

**Who:** KRING — the deploying party for Personal Workspace.

**Does:**
- Receives the venture's intake.
- Deploys one OpenClaw runtime per user (one assistant per user) — loads the onboarding templates, sets each assistant's name from the intake, wires Telegram, and confirms each assistant is reachable before handing back.
- Owns and maintains the framework — ships versions, updates `CHANGELOG.md`, bumps `STATE_VERSION`, and writes migration guidance when a version changes file shapes.

**Does not:** Provision into a venture's tenants. Pre-fill any per-user file beyond what's in the intake (no operator-imposed `USER.md` content, no operator-invented vibe). Wire any tools beyond Telegram — that happens in each user's first conversation.

**Hand-off:** Returns the deployed assistant Telegram handles to the venture.

### 3. The user

**Who:** Each person being onboarded by the venture.

**Does:**
- When the venture asks, provides what only the user can give — confirms Telegram is installed on a daily-driver device, shares the Telegram handle, and picks a name for the assistant.
- Sends the first message to the assistant on Telegram after deployment and runs through the first conversation — connects tools, validates what the assistant pulled from them, and fills the gaps tools can't (how the user makes decisions, what the user wants the assistant to push back on, etc.).
- Wires any extra tools beyond the standard stack (e.g. Linear, Figma) with the assistant later, in conversation.

**Does not:** Need to know anything about the framework internals beforehand. The first conversation handles orientation.

## The active human layer vs. the AI layer

Personal Workspace isn't fully autonomous — humans do four things the AI does not:

1. **Provision accounts** inside the venture's tenants (Google, Slack, Notion, GitHub).
2. **Deploy and wire runtimes** for each new assistant.
3. **Author and version the framework** — agent-files, playbook, onboarding, this file.
4. **Show up for the first conversation** — each user, on Telegram, starting their assistant's first session.

Everything else — memory, drafting, briefing, tool reach, commitment tracking, proactive check-ins, catch-up on new framework versions — the deployed assistant handles itself.

## Future consolidation

When parts of the venture or KRING side of the flow are replaced by automation (e.g. SSO-driven provisioning, self-service runtime deployment, self-service intake), update this file to reflect what's actually still human. Don't leave stale role assignments here — they misrepresent who to go to when something breaks.
