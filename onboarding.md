# Personal Workspace — Onboarding

How a venture gets onto Personal Workspace.

## Phase 1 — Admin (venture)

1. Submit your agent names to KRING.
2. Have each employee set up a Telegram account.
3. Submit each employee's Telegram username to KRING.

## Phase 2 — KRING

1. KRING sets up the agents — one OpenClaw runtime per employee, seeded with `agent-files/` as-is. Deploy each as a **clean sheet**: don't pre-fill `USER.md`, don't invent the agent's personality, don't wire tools beyond Telegram. The agent builds all of that *with* the user in the first conversation (Phase 4). Pre-filling breaks the relationship that first conversation is meant to create. (The agent sets up its own brief / review / heartbeat schedule in Phase 4 — no runtime step needed; see `agent-files/SCHEDULES.md`.)
2. Set up the one-way local mirror on the runtime (Syncthing, **Send Only**) so the employee can keep a read-only backup of their agent's files. Runtime side only here; the employee finishes the Mac/PC side in Phase 4. See `runbooks/syncthing-local-mirror.md` → Part A.
3. KRING messages each employee on Telegram with their agent's username, plus the runtime's Syncthing **Device ID** (needed for the mirror in Phase 4).

## Phase 3 — User (employee)

1. Message your agent on Telegram with `Hi`.
2. You receive a verification code.
3. Send the code back to KRING on Telegram.
4. You can now talk to your agent — Phase 4 begins.

## Phase 4 — Agent onboarding (agent-led)

In your first conversation, the agent:

1. Introduces itself and the tools you'll use together.
2. Helps you connect Google Workspace, Notion, and GitHub (skip and come back later if you want — wiring detail below).
3. Asks if you have legacy Microsoft 365 data to migrate. If yes, routes you into `runbooks/migrations/ms-to-google.md` and logs a Microsoft 365 (legacy) entry in `TOOLS.md` so it can search the right system later.
4. Confirms the basics about you and closes onboarding.

## Phase 4 — Wiring detail (the agent will guide you set-by-step)

### Google Workspace — ~15 min

Requires a Google Workspace account (personal `@gmail.com` won't work). You also need permission to create projects in your Workspace org — if your admin has locked this, ask them to enable project creation for your user.

**1. Create a Google Cloud project**

- Go to [console.cloud.google.com](https://console.cloud.google.com) and sign in with your Workspace email.
- Top bar → project selector → **New Project**.
- Name: e.g. *Personal Workspace Agent*. Organization: your Workspace domain (e.g. `yourcompany.com`).
- Click **Create**, then switch into the new project.

**2. Enable the nine APIs**

- Menu (☰) → **APIs & Services** → **Library**.
- Search and click **Enable** on each — one at a time:
  - **Gmail API**
  - **Google Calendar API**
  - **Google Drive API**
  - **Google Docs API**
  - **Google Sheets API**
  - **Google Slides API**
  - **People API**
  - **Google Meet API**
  - **Google Tasks API**

**3. Configure the OAuth consent screen**

- Menu → **APIs & Services** → **OAuth consent screen**.
- User Type: **Internal** → Create.
- App name, user support email, developer contact email → Save and Continue.
- Click through the remaining panels (Scopes, Summary) without changes — the agent requests the scopes it needs at auth time.

**4. Create the OAuth client**

- Menu → **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth client ID**.
- Application type: **Web application**.
- Name: e.g. *Personal Workspace Agent*.
- **Authorized redirect URIs**: paste the callback URL the agent gives you on Telegram. Save.
- Copy the **Client ID** and **Client Secret** from the dialog.

**5. Hand off to the agent**

- Paste **Client ID** and **Client Secret** to the agent on Telegram.
- The agent returns an auth link. Click it → choose your Workspace account → **Allow**.

### Notion — ~10 min

**1. Create an internal integration**

- Go to [notion.so/profile/integrations](https://www.notion.so/profile/integrations) → **New integration**.
- Name: e.g. *Personal Workspace Agent*. Associated workspace: pick your workspace. Type: **Internal**.

**2. Set capabilities**

- **Content Capabilities**: Read content · Update content · Insert content.
- **Comment Capabilities**: Read comments · Insert comments.
- **User Capabilities**: Read user information (with email — needed to tag owners).
- Save.

**3. Copy the secret**

- Under **Secrets** → copy the **Internal Integration Secret** (`secret_…`).
- Paste it to the agent on Telegram.

**4. Share pages with the integration**

- Open each page or database the agent should access → **•••** (top right) → **Connections** → **Add connections** → pick the integration.
- Share a top-level page to give the agent access to everything under it.

### GitHub — ~10 min

**1. Create a fine-grained personal access token**

- Go to [github.com/settings/tokens](https://github.com/settings/tokens) → **Fine-grained tokens** → **Generate new token**.
- Token name: e.g. *Personal Workspace Agent*. Expiration: 1 year (or longer if your org allows).

**2. Pick resource owner and repos**

- **Resource owner**: yourself for personal repos, or your org for org repos. If org, the org owner must approve the token after you create it (Org Settings → Personal access tokens → Pending requests).
- **Repository access**: *Only select repositories* (recommended — pick what the agent needs) or *All repositories*.

**3. Set repository permissions**

- **Contents**: Read and write.
- **Issues**: Read and write.
- **Pull requests**: Read and write.
- **Metadata**: Read-only (auto-granted).
- **Workflows**: Read and write *(only if you want the agent to edit GitHub Actions files)*.

**4. Hand off to the agent**

- Click **Generate token** → copy the token (`github_pat_…`) — shown only once.
- Paste it to the agent on Telegram.

*(If your org disables fine-grained tokens, fall back to a classic PAT with scopes `repo` and `workflow`.)*

### Microsoft 365 legacy data — only if you said yes above

If you're coming from a Microsoft 365 setup (Outlook mail, OneDrive/SharePoint files, Outlook calendar/contacts), don't try a hard cut-over. Mirror your data into Google and keep M365 as a read-only backup.

Full step-by-step in `runbooks/migrations/ms-to-google.md`. Short version:

1. **Mail** — Google Data Migration Service (Admin console) imports Outlook/Exchange into Gmail with folders, flags, dates preserved.
2. **Files** — Google Migrate for Workspace mirrors OneDrive/SharePoint into a **Shared Drive** (not "My Drive").
3. **Calendar** — Publish your Outlook calendar as `.ics`, add it to Google Calendar from URL.
4. **Contacts** — Export CSV from Outlook → import into Google Contacts.
5. **Cut-over day** — set auto-forward + out-of-office on the M365 mailbox; pin Outlook Web (`outlook.office.com`) as a bookmark only.
6. **Tell your agent** the cut-over date. It writes a `## Microsoft 365 (legacy)` block into `TOOLS.md` so it knows when to search the old system vs the new.

After 30 days the forward goes off; the M365 licence stays so the archive remains searchable.

### Local backup mirror (Syncthing) — ~10 min, optional but recommended

A read-only copy of your agent's files on your own Mac/PC, kept in sync automatically — so if the agent is ever down, you still have everything it knows in a folder you control. It's **one-way**: the agent writes, your machine receives. You read the mirror; to change anything you ask the agent.

You'll need the runtime's Syncthing **Device ID** from KRING (sent with your agent username in Phase 2). Full step-by-step in `runbooks/syncthing-local-mirror.md` → Part B.

## References

- `playbook.md` — Personal Workspace day-to-day.
- `ai-commandments.md` — the 4 AI Commandments and must-know git vocab.
- `runbooks/migrations/ms-to-google.md` — Microsoft 365 → Google Workspace migration playbook.
- `runbooks/syncthing-local-mirror.md` — one-way local mirror of your agent's files (backup / visibility).
- `runbooks/repurposing-an-existing-agent.md` — converting an existing agent into Personal Workspace without losing its data or automations.
