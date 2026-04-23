# CHANGELOG

Versioned deliverables for the Personal Workspace Speedblock.

Each release is a milestone snapshot under `releases/<version>/`. The root directory is always the living latest state.

---

## v0.1-beta  ·  shipped 2026-04-23

First packaged release. Deliverables: playbook, onboarding, and the shared OpenClaw agent file set.

**What shipped**
- `playbook.md` — the Personal Workspace operating manual: locked tech stack (Google Workspace, Telegram, Notion, GitHub, Claude, Slack), four AI layers (Gemini / Claude / OpenClaw / Cosmo), OpenClaw purpose and capabilities, working rhythm.
- `onboarding.md` — human setup (Google/Slack/Notion/GitHub accounts, user's private personal-layer repo, OpenClaw runtime deployment) + agent-led BOOTSTRAP conversation.
- `agent-files/` — shared OpenClaw framework: SOUL, AGENTS, KRING, HEARTBEAT, IDENTITY/USER/TOOLS per-user blueprints, MEMORY templates, working templates (daily/weekly/email-draft), BOOTSTRAP script, CHANGELOG, STATE_VERSION.

**Frozen snapshot**
- `releases/beta/` — frozen copy of the above, cut at ship.

**Product rename**
- This version reflects the rename from "Workspace Beta" to "Personal Workspace" (2026-04-23).
- Shared framework moved from `workspace-beta-agent-files` (deleted) to `personal-workspace-speedblock/agent-files/`.
- KRING-managed per-pilot repos (`op-august`, `op-jesper`, `op-johan`) deleted. Each user now creates their own private personal-layer repo with a name of their choice.

**Pilots shipped to**
- August Kring, Jesper Kring, Johan Rishede Duus.
