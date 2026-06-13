# TOOLS — {{AGENT_NAME}}'s Tool Configuration

What this OpenClaw agent is connected to. Update as connections are wired.

## Standard tool set

| Tool | Status | Notes |
|---|---|---|
| Slack (primary surface) | ✅ Connected | Pre-wired at runtime. |
| Gmail | ❌ Not connected | |
| Google Calendar | ❌ Not connected | |
| Google Drive / Docs | ❌ Not connected | |
| Notion | ❌ Not connected | |
| GitHub | ❌ Not connected | Wireable with the user's permission for reading and working in their repos. |
| Web search | ✅ Available | Via OpenClaw harness. |
| Local files | ✅ Connected | The runtime's working directory; path set by the OpenClaw harness at deployment. |

## User-specific tools

Beyond the standard set above, {{USER_FIRST_NAME}} may use other tools the agent can wire to. Added here as they're connected.

| Tool | Status | Notes |
|---|---|---|

*`HEARTBEAT.md` checks this table to know what to scan.*

## Skills

Skills are collected from the shared KRING claw repo:

  https://github.com/KRING-Ventures/claw-shared

The OpenClaw agent loads skills on demand from this repo. Log non-default scopes here as they're granted.

| Skill | Granted | Scope / notes |
|---|---|---|

---

## Google Workspace

- **Account:** [email address]
- **Access:** OAuth via [skill / harness]
- **Surfaces:** Gmail · Calendar · Drive / Docs
- **Rules:**
  - Read freely.
  - Send mail, share files, accept/decline invites only with permission.
  - Drafting in Docs is fine; sharing externally requires permission.

## Slack

- **Account / chat:** [workspace + channel or DM]
- **Access:** bot token in harness config
- **Rules:**
  - Parse dictated / messy messages for intent — don't ask for rephrasing.
  - Never forward Slack content to other surfaces without explicit instruction.

## Notion

- **Workspace:** [workspace name]
- **Access:** [OAuth scope]
- **Rules:**
  - Read and search freely.
  - Modify pages only with explicit per-action permission.

## Web search

- **Access:** via OpenClaw harness (WebFetch, WebSearch, browser skill).
- **Rules:**
  - Search freely for research and context.
  - Don't fill forms, create accounts, or use {{USER_FIRST_NAME}}'s credentials without instruction.

## Local files

- **Workspace:** the runtime's working directory; path set by the OpenClaw harness at deployment.
- **Access:** local filesystem.
- **Rules:**
  - Organise freely within the workspace.
  - Ask before touching anything outside it.
  - Use `trash/` over `rm`.

## Local mirror (Syncthing)

If {{USER_FIRST_NAME}} set up the local mirror, this runtime's working directory is shared one-way (**Send Only**) to their Mac/PC as a read-only backup.

- **It is passive.** You don't manage it, write to it, or read from it — it mirrors your working directory automatically. Just know it exists.
- **You remain the sole writer of your files.** The mirror is receive-only on {{USER_FIRST_NAME}}'s side; their local edits never reach you. If {{USER_FIRST_NAME}} says "I changed X in my local copy," tell them that doesn't propagate — make the change here and it'll mirror to them.
- Setup and recovery steps: `runbooks/syncthing-local-mirror.md`.

| Tool | Status | Notes |
|---|---|---|
| Syncthing local mirror | ❌ Not set up | Flip to ✅ with device + folder once KRING/the user wire it (Part A + Part B of the runbook). |

## Microsoft 365 (legacy) — only if the user migrated from M365

Add this block during onboarding **only if** {{USER_FIRST_NAME}} confirmed they have legacy Microsoft 365 data. Otherwise delete this section.

- **Account:** [legacy email]
- **Cut-over date:** YYYY-MM-DD — date {{USER_FIRST_NAME}} switched onto Google Workspace as daily driver.
- **Access mode:** web-only (Outlook Web + OneDrive Web). No desktop clients.
- **Status:** read-only archive.
- **Auto-forward to Google:** active until YYYY-MM-DD, then off.
- **Rules:**
  - Search only; never send, never edit, never reply from this account.
  - Things older than the cut-over date live here; newer things live in Google.
  - If unsure where data lives, ask once: *"Is this before or after [cut-over date]?"* — then search the right system.
  - See `agent-files/runbooks/ms-to-google-overlap.md` for full overlap rules.
