# Personal Workspace — Onboarding

How a venture gets onto Personal Workspace — from agent names submitted to KRING to every employee having their first conversation with their agent.

Personal Workspace is a **Done with you** Speedblock. The venture admin gathers a few details, KRING sets the agents up, then each employee pairs with their agent on Telegram. Activation happens once in Cosmica before phase 1 begins.

## Phase 1 — Admin (venture)

1. The admin provides the names of the personal agents to KRING.
2. The admin gets the employees to set up a Telegram account.
3. The admin provides the employees' Telegram usernames to KRING.

## Phase 2 — KRING

1. KRING sets up the personal agents.
2. KRING sends a message to each employee on Telegram with their specific agent username.

## Phase 3 — User (employee)

1. The user starts a new conversation with the provided agent username on Telegram and sends a `Hi`.
2. The user receives a verification code from the agent.
3. The user sends the verification code back to KRING on Telegram. KRING verifies.
4. The user can now talk with the agent — Phase 4 begins.

## Phase 4 — Agent onboarding (agent-led)

Once verified, the agent runs the user through the first conversation. Six short stages:

1. **Intro.** The agent introduces itself — **states its name** (the name KRING set during provisioning — no rename offered), explains what it does, where it lives (Telegram), what tools it'll use, and the permission rule (its own files: no asking; anything that touches others: always asks first).
2. **Tech-stack map.** Before wiring anything, the agent walks the user through the **whole** Personal Workspace tech stack so they leave the first conversation knowing what they're running on — Google Workspace, Telegram, Notion, GitHub (agent-wired), plus Slack (not yet), Gemini (used directly inside Google apps), and Claude (general-purpose AI). Four are agent-connected, three the user uses themselves.
3. **Wire the tools.** The user sets up each agent-wired tool themselves, in their own accounts. KRING is out of the loop — Personal Workspace is the agent; everything it plugs into lives in the user's own consoles. The agent guides each setup step-by-step in chat, the user clicks through their own admin panels, and the agent tests every connection live before moving on. Order and what's involved per tool is in **Phase 4 — Wiring detail** below. Wiring now is optional — the user can skip any tool and the agent will remind them later.
4. **Confirm the basics.** With tools connected, the agent pulls name, email, timezone, and role from the user's own data, reads it back, and the user corrects anything wrong and adds their preferred name. Everything else — contacts, projects, communication style — builds up naturally in memory as the agent works alongside the user.
5. **The 4 AI Commandments.** The agent walks the user through the four practices that keep agent work on the rails: ask the agent to repeat the prompt back, work in small saved batches, keep it simple, and branch off main in shared projects. Plus the must-know git vocabulary (repo, branch, commit, PR, merge).
6. **Close.** The agent confirms onboarding is complete. From here, memory builds with every conversation — the relationship starts compounding.

When every employee has finished phase 4, your venture is fully running on Personal Workspace.

## Phase 4 — Wiring detail

What the user actually does to wire each agent-connected tool. All three are done by the user, in their own accounts — no KRING involvement. The agent guides every step inside Telegram.

### Google Workspace — ~15 min, first time

Done once in the venture's own **Google Cloud Console**. Uses the **Internal** OAuth consent screen — restricted to the venture's own Workspace domain — which skips Google's CASA verification entirely. Requires a Google Workspace account (a personal `@gmail.com` cannot use Internal).

1. Create a Google Cloud project (e.g. `personal-workspace-agent`) at [console.cloud.google.com](https://console.cloud.google.com).
2. Enable APIs: **Gmail**, **Google Calendar**, **Google Drive**, **Google Docs**.
3. Configure the **OAuth consent screen** → user type **Internal**. Add the agent's scopes (the agent gives you the exact list in chat).
4. Create an **OAuth 2.0 Client ID** (Web application). Add the agent's callback URL — the agent provides this.
5. Paste the **Client ID** and **Client Secret** to the agent on Telegram.
6. Click the auth link the agent returns, grant access. The agent confirms by reading your inbox, calendar, and a Drive doc back.

### Notion — ~10–15 min

Done once in the user's own Notion workspace as an **Internal integration**.

1. Go to [notion.so/profile/integrations](https://www.notion.so/profile/integrations) → **New integration**.
2. Name it (the agent's name), pick the workspace, grant **Read content**, **Update content**, **Insert content**.
3. Copy the **Internal Integration Secret** and paste it to the agent on Telegram.
4. In each Notion page or database the agent should access, click **••• → Connections → Add** the integration.
5. The agent reads back one connected page to confirm.

### GitHub — ~10–15 min

Done once with a **fine-grained personal access token** in the user's own GitHub account.

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens) → **Fine-grained tokens** → **Generate new token**.
2. Select the repos the agent should work in (or **All repositories** if the user prefers).
3. Set permissions: **Contents** (read/write), **Issues** (read/write), **Pull requests** (read/write), **Metadata** (read).
4. Copy the token and paste it to the agent on Telegram.
5. The agent lists one repo and reads a recent commit to confirm.

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Share with your team before phase 3.
- `best-practice.md` — the 4 AI Commandments and the must-know vocab the agent walks each user through.
- `agent-files/onboarding/BOOTSTRAP.md` — the script the agent follows in the first conversation.
- `agent-files/AGENTS.md` — operational rules (agent-side).

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
