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
- [ ] ChatGPT — user account (LLM the agent system runs on)

If the venture is still setting up accounts, wait before proceeding to Step 6.

### Step 6 — Grant app access

The venture admin grants KRING the access needed to wire each agent. See "Wiring detail" below for exactly what each tool needs per user.

### Step 7 — Wire agent tools

Wire each agent's tools using the credentials from Step 6:
- Google Workspace (Gmail, Calendar, Drive, Docs, Meet, Tasks, People)
- Slack
- Notion *(if the venture uses it — recommended stack)*
- GitHub *(if the user has repos to connect — optional)*
- Any Microsoft 365 legacy data if migrating — see `runbooks/migrations/ms-to-google.md`

Also set up the one-way local mirror (Syncthing, **Send Only**) on the runtime so the user can keep a read-only backup. The user finishes the Mac/PC side during onboarding. See `runbooks/syncthing-local-mirror.md` → Part A.

---

## Stage 3 — Onboarding (~15 min per user)

### Step 8 — Access handover

Give each user access to their agent:
- [ ] Invite the user to the agent's Slack channel
- [ ] Send a verification step so they know it's their agent (not a generic bot)
- [ ] Confirm the agent's name matches what was submitted in Stage 1

### Step 9 — Hand off to the agent

From here the agent leads. It runs the first conversation with the user using `agent-files/onboarding/BOOTSTRAP.md`. KRING's job is done.

Monitor: the agent should complete `STATE_VERSION` and finalize `USER.md` by the end of that first session. If something breaks, the user will surface it via Slack.

---

## Wiring detail

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

### Notion — ~10 min per user *(if used)*

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

### GitHub — ~10 min per user *(if used)*

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

Full step-by-step in `runbooks/migrations/ms-to-google.md`. Short version:

1. **Mail** — Google Data Migration Service imports Outlook/Exchange into Gmail.
2. **Files** — Google Migrate for Workspace mirrors OneDrive/SharePoint into a Shared Drive.
3. **Calendar** — Publish Outlook calendar as `.ics`, add to Google Calendar from URL.
4. **Contacts** — Export CSV from Outlook → import into Google Contacts.
5. **Cut-over day** — set auto-forward + out-of-office on the M365 mailbox.
6. **Tell the agent** the cut-over date so it writes a `## Microsoft 365 (legacy)` block into `TOOLS.md`.

After 30 days the forward goes off; the M365 licence stays so the archive remains searchable.

---

### Local backup mirror (Syncthing) — ~10 min per user, optional

A read-only copy of the agent's files on the user's Mac/PC, kept in sync automatically. KRING sets up the runtime (Send Only) side in Step 7; the user finishes their Mac/PC side during onboarding using the Syncthing **Device ID**. Full step-by-step: `runbooks/syncthing-local-mirror.md`.

---

## References

- `activation.md` — the venture-facing activation overview.
- `onboarding.md` — the user-facing onboarding flow (Stage 3).
- `agent-files/onboarding/BOOTSTRAP.md` — the agent-side onboarding script.
- `playbook.md` — Personal Workspace day-to-day.
- `runbooks/migrations/ms-to-google.md` — Microsoft 365 → Google Workspace migration.
- `runbooks/syncthing-local-mirror.md` — one-way local mirror setup.
