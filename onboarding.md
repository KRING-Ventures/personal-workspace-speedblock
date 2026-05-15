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

Requires a Google Workspace account (personal `@gmail.com` won't work). You also need permission to create projects in your Workspace org — if your admin has locked this, ask them to enable project creation for your user.

**1. Create a Google Cloud project**

- Go to [console.cloud.google.com](https://console.cloud.google.com) and sign in with your Workspace email.
- Top bar → project selector → **New Project**.
- Name: e.g. *Personal Workspace Agent*. Organization: your Workspace domain (e.g. `yourcompany.com`).
- Click **Create**, then switch into the new project.

**2. Enable the four APIs**

- Menu (☰) → **APIs & Services** → **Library**.
- Search and click **Enable** on each — one at a time:
  - **Gmail API**
  - **Google Calendar API**
  - **Google Drive API**
  - **Google Docs API**

*(Sheets, Slides, Contacts (People), Tasks, Meet are out of scope in this version — don't enable them. If we add them to the agent later, this list grows.)*

**3. Configure the OAuth consent screen**

- Menu → **APIs & Services** → **OAuth consent screen**.
- User Type: **Internal** → Create.
- App name, user support email, developer contact email → Save and Continue.
- **Scopes** → Add or remove scopes → tick:
  - `https://mail.google.com/` (Gmail — full mailbox, needed for read + draft + send-with-permission)
  - `https://www.googleapis.com/auth/calendar` (Calendar)
  - `https://www.googleapis.com/auth/drive` (Drive)
  - `https://www.googleapis.com/auth/documents` (Docs)
- Save and Continue → Back to Dashboard.

*(Internal apps skip Google's verification / CASA — that's only required for External apps.)*

**4. Create the OAuth client**

- Menu → **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth client ID**.
- Application type: **Web application**.
- Name: e.g. *Personal Workspace Agent*.
- **Authorized redirect URIs**: paste the callback URL the agent gives you on Telegram. Save.
- Copy the **Client ID** and **Client Secret** from the dialog.

**5. Hand off to the agent**

- Paste **Client ID** and **Client Secret** to the agent on Telegram.
- The agent returns an auth link. Click it → choose your Workspace account → **Allow**.
- The agent confirms by reading 3 recent emails and listing today's calendar back to you.

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
- Children inherit access by default — share a top-level page to give the agent everything under it.

*(If your workspace admin restricts integrations, they'll need to approve it from Settings → Connections.)*

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

## References

- `playbook.md` — Personal Workspace day-to-day.
- `best-practice.md` — the 4 AI Commandments and must-know git vocab.
