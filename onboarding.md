# Personal Workspace — Onboarding

How your venture gets onto Personal Workspace.

## The three steps

1. **Activate** — you send us the intake.
2. **Build & deploy** — we set up one agent per user.
3. **Finish onboarding** — you hand each agent to its user; each user runs a first conversation on Telegram.

When step 3 is done, your venture is running on Personal Workspace.

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

## Step 1 — Activate (you)

Send us one intake with everything we need.

**Once, for your venture:**

- Confirm your tenants are in place: Google Workspace, Slack, Notion, GitHub. These are the required tools. We don't provision into your tenants — that's on you.

**For each user:**

- Full name and primary email of the user.
- The user's Telegram handle (e.g. `@maria`). Telegram must be installed on a device the user uses daily.
- The name the user wants for the agent (e.g. `Ida`).

**Send it** when activating the Speedblock in Cosmica. We'll come back if anything is missing.

*Anything beyond the standard stack* (Linear, Figma, etc.) — the user wires those with the agent after deployment, not at intake.

## Step 2 — Build & deploy (KRING)

We deploy one agent per user, wire each to Telegram, and confirm each is reachable. Then we send you the list of Telegram handles — one per user — through the same channel you used for the intake.

## Step 3 — Finish onboarding (you)

For each user, in any order:

1. **Share the `Playbook`** so the user knows what Personal Workspace is before starting.
2. **Tell the user to open Telegram, find the agent, and send any message.** The agent introduces itself and runs the first conversation — about ~20 minutes, real conversation, not a form. It walks the user through wiring up Gmail, Calendar, Drive, Notion, GitHub, and asks the few questions tools can't answer (how the user makes decisions, what to push back on, communication preferences).

## References

- `playbook.md` — what Personal Workspace is and how it works day-to-day. Share with your team in Step 3.
- `agent-files/onboarding/BOOTSTRAP.md` — the script the agent follows in the first conversation.
- `agent-files/AGENTS.md` — operational rules (agent-side; useful if you want to understand how it works under the hood).

---

*Current framework version is in `agent-files/onboarding/STATE_VERSION`. Per-version history is in `CHANGELOG.md`.*
