# Personal Workspace — Onboarding

How your venture gets onto Personal Workspace.

Personal Workspace is a **Done with you** Speedblock — your admin does Phase 1, KRING does Phase 2, your team does Phase 3 with KRING's help.

## The three phases

1. **Admin setup** (you) — name each agent, submit Telegram handles, confirm tech-stack prereqs.
2. **KRING setup** (KRING) — we provision the agents and DM each user on Telegram.
3. **User setup** (you + KRING) — each user pairs with their agent, then the agent takes over for personal onboarding.

When Phase 3 is done for every user, your venture is running on Personal Workspace.

## What each user gets

A personal AI agent on Telegram — one per user, remembers across conversations. Capabilities (same list, same words as `playbook.md`):

- **Remembers** — role, projects, contacts, working preferences.
- **Briefs** — mornings on calendar, priorities, deadlines. Mondays on open commitments and what's outstanding.
- **Drafts** — emails, messages, docs. Never sent without approval.
- **Preps meetings** — attendees, context, intent.
- **Tracks commitments** — what the user has said they'll do, what they're waiting on.
- **Uses the tools** — Gmail, Calendar, Drive, Notion, GitHub, Telegram.
- **Builds automations** — on request.
- **4 AI Commandments walkthrough** — the agent teaches the user the four working practices and the must-know vocab in the first conversation. See `best-practice.md`.

## Phase 1 — Admin setup (you)

Three sub-steps, in the Cosmica Speedblock admin:

**1. Name each agent.** One name per seat (e.g. `Ida`). KRING needs the names to begin provisioning.

**2. Submit Telegram handles.** One personal Telegram handle per agent (e.g. `@maria`). Telegram must be installed on a device each user uses daily. KRING pairs the agent to the handle you submit.

**3. Confirm tech-stack prereqs.** Tick each tool once your venture has it in place. We don't provision into your tenants — that's on you.

| Tool | Required | Why |
|---|---|---|
| Google Workspace | Yes | Gmail, Calendar, Drive, Docs, Meet — the agent wires into this on the first conversation. |
| Slack | Yes | Team chat layer KRING expects every venture to operate on. |
| Notion | Optional | Wire up only if your venture uses it. |
| GitHub | Optional | Only if your venture writes code. |
| Claude | Optional | Each teammate uses Claude directly for coding and individual projects — the agent does not connect to it. |

KRING starts as soon as the required tools are ticked. *Anything beyond this stack* (Linear, Figma, etc.) — the user wires those with the agent after deployment, not at Phase 1.

## Phase 2 — KRING setup (KRING)

KRING provisions one agent per seat, then reaches each user directly on Telegram with their agent's username. Phase 3 opens automatically once every user has been DM'd.

## Phase 3 — User setup (you + KRING)

The Speedblock admin shows a per-seat pairing tracker — one row per user, with the user's Telegram handle and pairing status.

Each user pairs with their agent in four steps:

1. ✅ KRING provides the agent's username to the user directly on Telegram. *(Done by the end of Phase 2.)*
2. The user starts a new conversation with their agent on Telegram.
3. The agent provides the user with a code they must send back to KRING on Telegram.
4. KRING verifies and connects the user with their agent — they can now start the user onboarding with the agent.

Once a user is paired, the agent runs the first conversation — about ~20 minutes, real conversation, not a form. It walks the user through wiring up Gmail, Calendar, Drive, Notion, GitHub, and asks the few questions tools can't answer (how the user makes decisions, what to push back on, communication preferences).

Share the `Playbook` with your team before they start, so they know what Personal Workspace is.

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Share with your team in Phase 3.
- `agent-files/onboarding/BOOTSTRAP.md` — the script the agent follows in the first conversation.
- `agent-files/AGENTS.md` — operational rules (agent-side; useful if you want to understand how it works under the hood).

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
