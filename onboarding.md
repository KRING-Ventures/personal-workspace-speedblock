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
3. **Wire the tools.** The agent guides the user through connecting the four agent-wired tools — Google Workspace (Gmail, Calendar, Drive, Docs), then Notion, then GitHub. The user authorises each one; the agent tests every connection live and confirms it works. Wiring now is optional — the user can skip any tool and the agent will remind them later.
4. **Confirm the basics.** With tools connected, the agent pulls name, email, timezone, and role from the user's own data, reads it back, and the user corrects anything wrong and adds their preferred name. Everything else — contacts, projects, communication style — builds up naturally in memory as the agent works alongside the user.
5. **The 4 AI Commandments.** The agent walks the user through the four practices that keep agent work on the rails: ask the agent to repeat the prompt back, work in small saved batches, keep it simple, and branch off main in shared projects. Plus the must-know git vocabulary (repo, branch, commit, PR, merge).
6. **Close.** The agent confirms onboarding is complete. From here, memory builds with every conversation — the relationship starts compounding.

When every employee has finished phase 4, your venture is fully running on Personal Workspace.

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Share with your team before phase 3.
- `best-practice.md` — the 4 AI Commandments and the must-know vocab the agent walks each user through.
- `agent-files/onboarding/BOOTSTRAP.md` — the script the agent follows in the first conversation.
- `agent-files/AGENTS.md` — operational rules (agent-side).

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
