# Personal Workspace — KRING Activation Guide

Internal setup guide for KRING. This covers everything KRING owns in Stages 2–3 of the activation flow — from agent build to access handover. The venture-facing view is in `activation.md`.

> This guide is under active refinement — steps and ownership are still being calibrated.

---

## Before you start

Confirm Stage 1 is complete:
- [ ] Speedblock activated in Cosmica (seat count set, terms accepted)
- [ ] Agreement signed
- [ ] Agent names received (one per seat)
- [ ] Google Workspace accounts confirmed (one per user)
- [ ] Slack workspace confirmed and user accounts in place

---

## Stage 2 — Setup (~3–4 days)

**These steps run in parallel, not in a strict line.** As soon as the agent names land (Stage 1), start building the agents — they can be ready and waiting while the venture sets up its tools. Wiring (Step 7) is the one step that *must* wait for the tools to exist. So: build agents ∥ venture sets up tools → wire once tools are ready → deploy.

### Step 4 — Agent build & files

Stand up one OpenClaw runtime per user. Install `agent-files/` as a **clean sheet**:
- Don't pre-fill `USER.md` — the agent builds this with the user in the first conversation.
- Don't invent the agent's personality beyond the framework defaults.
- Don't wire tools beyond Slack until Step 7.

Pre-filling breaks the relationship the first conversation is meant to create.

### Step 5 — Tech-stack confirmation

Confirm the venture has set up accounts for each user:
- [ ] Google Workspace (Gmail, Calendar, Drive, Docs, Meet) — Workspace account, not `@gmail.com`
- [ ] Slack — team workspace + user account
- [ ] ChatGPT — **Business (Team)** account, one seat per user (LLM the agent runs on, via the Codex CLI over the subscription)

If the venture is still setting up accounts, wait before proceeding to Step 6.

> **⚠️ ASK COREY — open item (placeholder).** We're standardising on the ChatGPT **Business (Team)** plan for now. Open question: is a base Business seat enough for an always-on agent running via the Codex CLI, or do we need to top up **credits** or move to a higher tier (Pro 5×/20×)? Codex runs on rolling 5-hour + weekly rate-limit windows, so a heavy agent can hit the ceiling. Confirm the right plan/credits setup with Corey before quoting usage to a venture.

#### How the venture provisions these accounts (one-time)

The venture sets these up itself — **it owns every account; logins and billing stay with the venture, nothing runs through KRING.** KRING only connects the agents to them (Steps 6–7). Done once per venture, plus one account per person.

| App | Plan | Where | How many | Time |
|---|---|---|---|---|
| **Google Workspace** | Business Standard | workspace.google.com | One per person | ~30–45 min + a few hrs for domain check |
| **Slack** | Pro | slack.com | One per person | ~10 min |
| **ChatGPT** | Business (Team) | chatgpt.com | One workspace, one member per person | ~10 min |

- **Google Workspace** — email, calendar, files; the core the agent works from. A personal `@gmail.com` won't work — it needs a Workspace account on the venture's own domain. At workspace.google.com → *Get started*: pick Business Standard, add (or buy) the company domain, verify it (a DNS record, a few hours to confirm), create one user per person.
- **Slack (Pro)** — where each person talks to their agent. Create the workspace, invite one account per person, choose **Pro** (it keeps full message history, which the agent relies on).
- **ChatGPT (Business / Team)** — the LLM the agent runs on, over the subscription (not metered API). Create a Business (Team) workspace and invite one member per person on the venture's own domain (that member becomes the agent's identity). KRING signs each agent into its seat at handover — no shared passwords.

Recommended extras (Notion, GitHub, Whispr Flow, Claude) are self-serve, set up later by each person — not part of activation. See the Playbook.

### Step 6 — Grant app access

The venture admin grants KRING the access needed to wire each agent. See "Wiring detail" below for exactly what each tool needs per user.

### Step 7 — Wire agent tools

Wire each agent's tools using the credentials from Step 6:
- ChatGPT (Codex CLI sign-in) — what the agent runs on; without it the runtime can't think
- Google Workspace (Gmail, Calendar, Drive, Docs, Meet, Tasks, People)
- Slack
- Microsoft 365 legacy data — **only if the venture is migrating from M365 (optional)**. See `agent-files/runbooks/migrations/ms-to-google.md`.

> Notion and GitHub are Recommended stack and are self-service — the user connects them in their own time after activation. Don't wait on these or wire them during setup.

Also set up the one-way local mirror (Syncthing, **Send Only**) on the runtime so the user can keep a read-only backup. The user finishes the Mac/PC side during onboarding. See `agent-files/runbooks/syncthing-local-mirror.md` → Part A.

---

## Stage 3 — Onboarding (~15 min per user)

### Step 8 — Access handover

Give each user access to their agent:
- [ ] Invite the user to the agent's Slack channel
- [ ] Send a verification step so they know it's their agent (not a generic bot)
- [ ] Confirm the agent's name matches what was submitted in Stage 1

### Step 9 — Hand off to the agent

Kick the agent off with the **deployment handover**: open `agent-files/onboarding/KICKOFF.md`, fill in the brief (agent name, repo URL, the user's full name + **Slack ID**, venture, and the support contact + Slack ID), and **paste that block into the agent's Slack channel as its first message.** That single paste gives the agent its bearings and the Slack identities it can't infer — then it proactively tags the user and runs the first conversation using `agent-files/onboarding/BOOTSTRAP.md`. KRING's job is done.

Monitor: the agent should complete `STATE_VERSION` and finalize `USER.md` by the end of that first session. If something breaks, the user will surface it via Slack.

---

## Wiring detail

### ChatGPT (Codex CLI) — ~10 min per user

What the agent runs on. It signs in to the venture's **ChatGPT Business (Team)** subscription through the **Codex CLI** — no OpenAI API key, no pay-per-use billing. Do this as part of standing up the runtime; the agent can't run without it.

Requires: one ChatGPT Team **member seat per agent** (created by the venture, on a domain email), and that seat's sign-in.

**1. Confirm the Codex CLI** is installed on the agent's runtime.

**2. Sign in with ChatGPT**
- Run `codex login` and complete the **"Sign in with ChatGPT"** flow using the agent's Team seat (the venture-domain email).
- This authenticates the agent against the subscription — not an API key.

**3. Verify**
- Run a quick `codex` prompt; confirm it responds with **no API-key prompt** and no per-token charge.
- The seat is now the agent's identity; it draws on the subscription's rolling usage allowance.

> **⚠️ ASK COREY (see Step 5).** Open question on whether a base Team seat's allowance covers an always-on agent, or whether we need credits / a higher tier. Confirm before quoting usage.

---

### Google Workspace — ~15 min per user

Requires a Google Workspace account (not `@gmail.com`) and permission to create projects in the Workspace org.

**1. Create a Google Cloud project**
- [console.cloud.google.com](https://console.cloud.google.com) → sign in with the Workspace email.
- Top bar → project selector → **New Project**.
- Name: e.g. *Personal Workspace Agent*. Organization: the Workspace domain.
- Click **Create**, then switch into the new project.

**2. Enable the nine APIs**
- Menu (☰) → **APIs & Services** → **Library**.
- Enable each one:
  - Gmail API · Google Calendar API · Google Drive API · Google Docs API · Google Sheets API · Google Slides API · People API · Google Meet API · Google Tasks API

**3. Configure the OAuth consent screen**
- Menu → **APIs & Services** → **OAuth consent screen**.
- User Type: **Internal** → Create.
- App name, support email, developer contact → Save and Continue through the remaining panels.

**4. Create the OAuth client**
- Menu → **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth client ID**.
- Application type: **Web application**.
- **Authorized redirect URIs**: paste the callback URL for this runtime.
- Copy **Client ID** and **Client Secret**.

**5. Complete the auth handshake**
- Use the Client ID + Secret to authenticate against the user's Workspace account.

---

### Notion — ~10 min per user *(self-serve)*

> Recommended stack — the **user** connects this themselves after activation, not KRING. Kept here as reference KRING can hand over if asked.

**1. Create an internal integration**
- [notion.so/profile/integrations](https://www.notion.so/profile/integrations) → **New integration**.
- Name: e.g. *Personal Workspace Agent*. Workspace: the venture's. Type: **Internal**.

**2. Set capabilities**
- Content: Read · Update · Insert. Comments: Read · Insert. Users: Read with email.

**3. Copy the secret**
- **Secrets** → copy the Internal Integration Secret (`secret_…`).

**4. Share pages with the integration**
- Each page or database → **•••** → **Connections** → add the integration.
- Share a top-level page to give access to everything below it.

---

### GitHub — ~10 min per user *(self-serve)*

> Recommended stack — the **user** connects this themselves after activation, not KRING. Kept here as reference KRING can hand over if asked.

**1. Create a fine-grained personal access token**
- [github.com/settings/tokens](https://github.com/settings/tokens) → **Fine-grained tokens** → **Generate new token**.
- Token name: *Personal Workspace Agent*. Expiration: 1 year.

**2. Resource owner and repos**
- Personal repos: user. Org repos: the org (org owner must approve after creation).
- Repository access: *Only select repositories* (recommended).

**3. Permissions**
- Contents: Read and write. Issues: R/W. Pull requests: R/W. Metadata: Read-only. Workflows: R/W *(only if agent edits Actions files)*.

**4. Copy the token**
- Generate → copy the token (`github_pat_…`) — shown once.

*(Fallback if org disables fine-grained tokens: classic PAT with `repo` + `workflow` scopes.)*

---

### Microsoft 365 legacy data — only if migrating from M365

Full step-by-step in `agent-files/runbooks/migrations/ms-to-google.md`. Short version:

1. **Mail** — Google Data Migration Service imports Outlook/Exchange into Gmail.
2. **Files** — Google Migrate for Workspace mirrors OneDrive/SharePoint into a Shared Drive.
3. **Calendar** — Publish Outlook calendar as `.ics`, add to Google Calendar from URL.
4. **Contacts** — Export CSV from Outlook → import into Google Contacts.
5. **Cut-over day** — set auto-forward + out-of-office on the M365 mailbox.
6. **Tell the agent** the cut-over date so it writes a `## Microsoft 365 (legacy)` block into `TOOLS.md`.

After 30 days the forward goes off; the M365 licence stays so the archive remains searchable.

---

### Local backup mirror (Syncthing) — ~10 min per user, optional

A read-only copy of the agent's files on the user's Mac/PC, kept in sync automatically. KRING sets up the runtime (Send Only) side in Step 7; the user finishes their Mac/PC side during onboarding using the Syncthing **Device ID**. Full step-by-step: `agent-files/runbooks/syncthing-local-mirror.md`.

---

## References

- `buy-in.md` — the value case for Personal Workspace (venture-facing).
- `activation.md` — the venture-facing journey: getting set up (Stages 1–2) **and** the user's first conversation (Stage 3).
- `agent-files/onboarding/BOOTSTRAP.md` — the agent-side onboarding script.
- `playbook.md` — Personal Workspace day-to-day.
- `agent-files/runbooks/migrations/ms-to-google.md` — Microsoft 365 → Google Workspace migration.
- `agent-files/runbooks/syncthing-local-mirror.md` — one-way local mirror setup.
