# TOOLS — {{AGENT_NAME}}'s Tool Configuration

What this OpenClaw agent is connected to. Update as connections are wired.

## Standard tool set

| Tool | Status | Notes |
|---|---|---|
| Telegram (primary surface) | ✅ Connected | Pre-wired at runtime. |
| Gmail | ❌ Not connected | |
| Google Calendar | ❌ Not connected | |
| Google Drive / Docs | ❌ Not connected | |
| Slack | ❌ Not connected | KRING workspace. |
| Notion | ❌ Not connected | KRING Ventures workspace. |
| GitHub | ❌ Not connected | |
| Web search | ✅ Available | Via OpenClaw harness. |
| Local files | ✅ Connected | `{{WORKSPACE_PATH}}` |

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

## Telegram

- **Account / chat:** [@handle or chat ID]
- **Access:** bot token in harness config
- **Rules:**
  - Parse dictated / messy messages for intent — don't ask for rephrasing.
  - Never forward Telegram content to other surfaces without explicit instruction.

## Slack

- **Workspace:** KRING Ventures
- **Access:** [OAuth scope]
- **Rules:**
  - Read and search freely.
  - Posting to channels or replying in threads requires permission.

## Notion

- **Workspace:** KRING Ventures
- **Access:** [OAuth scope]
- **Rules:**
  - Read and search freely.
  - Modify pages only with explicit per-action permission.

## GitHub

- **Account:** [username]
- **Access:** [token / OAuth]
- **Rules:**
  - Read repos freely.
  - Pushing, PRs, or issue comments require permission.

## Web search

- **Access:** via OpenClaw harness (WebFetch, WebSearch, browser skill).
- **Rules:**
  - Search freely for research and context.
  - Don't fill forms, create accounts, or use {{USER_FIRST_NAME}}'s credentials without instruction.

## Local files

- **Workspace:** `{{WORKSPACE_PATH}}`
- **Access:** local filesystem
- **Rules:**
  - Organise freely within the workspace.
  - Ask before touching anything outside it.
  - Use `trash/` over `rm`.
