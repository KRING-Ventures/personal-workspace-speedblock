# Personal Workspace — Onboarding

How a venture gets onto Personal Workspace.

## Phase 1 — Admin (venture)

1. Submit your agent names to KRING.
2. Have each employee set up a Telegram account.
3. Submit each employee's Telegram username to KRING.

## Phase 2 — KRING

1. KRING sets up the agents.
2. KRING messages each employee on Telegram with their agent's username.

## Phase 3 — User (employee)

1. Message your agent on Telegram with `Hi`.
2. You receive a verification code.
3. Send the code back to KRING on Telegram.
4. You can now talk to your agent — Phase 4 begins.

## Phase 4 — Agent onboarding (agent-led)

In your first conversation, the agent:

1. Introduces itself and the tools you'll use together.
2. Helps you connect Google Workspace, Notion, and GitHub (skip and come back later if you want — wiring detail below).
3. Confirms the basics about you and closes onboarding.

## Phase 4 — Wiring detail

### Google Workspace — ~15 min

Requires a Google Workspace account (personal `@gmail.com` won't work).

1. Create a project at [console.cloud.google.com](https://console.cloud.google.com).
2. Enable APIs: Gmail, Calendar, Drive, Docs.
3. Configure the OAuth consent screen → user type **Internal**.
4. Create an OAuth 2.0 Client ID (Web application) using the callback URL the agent gives you.
5. Paste the Client ID and Secret to the agent on Telegram.
6. Click the auth link the agent returns and grant access.

### Notion — ~10 min

1. Go to [notion.so/profile/integrations](https://www.notion.so/profile/integrations) → **New integration**.
2. Name it, pick the workspace, grant Read / Update / Insert content.
3. Paste the Internal Integration Secret to the agent.
4. In each page or database the agent should access: **••• → Connections → Add**.

### GitHub — ~10 min

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens) → Fine-grained tokens → **Generate new token**.
2. Select the repos (or All repositories).
3. Permissions: Contents, Issues, Pull requests (read/write); Metadata (read).
4. Paste the token to the agent.

## References

- `playbook.md` — Personal Workspace day-to-day.
- `best-practice.md` — the 4 AI Commandments and must-know git vocab.
