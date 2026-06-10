# Personal Workspace — Activation

How a venture gets deployed onto Personal Workspace — from activating the Speedblock to a live, onboarded user. Roughly **5 business days** end to end.

This is the venture-and-KRING process. The agent-led part that each *individual* user goes through is a separate flow — see `onboarding.md`.

Three lanes run through this: **Venture** (the company adopting Personal Workspace), **KRING** (sets the agents up and wires them), **User** (the employee who ends up with an agent). KRING runs an orchestration layer across the whole thing — it collects every input, tracks what's outstanding, chases what's missing, and supports the venture at each step.

> The exact split of who does what across Venture / KRING / User is still being calibrated — treat the lanes below as the working draft.

---

## Stage 1 — Provisioning (~1 day, venture-led)

**1. Speedblock activation** *(Venture)*
Set the seat count in Cosmica (e.g. 3 users) and accept the terms and pricing.

**2. Invoicing & agreement** *(Venture · KRING)*
KRING invoices the venture through the Data Room and the agreement is signed.

**3. Provide agent names** *(Venture)*
Name each agent — one per seat — and submit the names to KRING. KRING's orchestration layer collects each name as it comes in, tracks which seats are still unnamed, and chases the rest.

---

## Stage 2 — Setup (~3–4 days, KRING-led)

**4. Agent build & files** *(KRING)*
KRING stands up one OpenClaw runtime per user and installs `agent-files/` as a **clean sheet** — don't pre-fill `USER.md`, don't invent the agent's personality, don't wire tools beyond the chat surface. The agent builds all of that *with* the user in the first conversation (see `onboarding.md`). Pre-filling breaks the relationship that first conversation is meant to create.

**5. Tech-stack setup** *(Venture)*
The venture subscribes to the required apps and creates the user accounts — Google Workspace, Notion, GitHub. (See "Required tech stack" below.)

**6. Grant app access** *(Venture)*
The venture admin grants KRING the access needed to wire each agent — see "Wiring detail" for exactly what each tool needs.

**7. Wire agent tools** *(KRING)*
KRING wires each agent's tools: Google Workspace, Notion, GitHub, and any legacy Microsoft 365 data — APIs, credentials, permissions. KRING also sets up the one-way local mirror (Syncthing, **Send Only**) on the runtime so the user can keep a read-only backup; the user finishes the Mac/PC side during onboarding. See `runbooks/syncthing-local-mirror.md` → Part A.

---

## Stage 3 — Onboarding (~16 min, agent-led)

**8. Access handover** *(KRING)*
KRING gives the user access to their agent — the chat handle plus a verification step to confirm it's really them.

**9. User onboarding** *(Agent-led)*
The agent runs the first conversation with the user — introduces itself, gets to know them, maps their needs, and goes live. Full flow in `onboarding.md`. This is the hand-off point: everything before it is venture + KRING; from here the agent leads.

---

## Required tech stack

The venture sets these up in Stage 2 so the agents have something to wire into. `playbook.md` is the source of truth for the full stack and what each tool is for.

- **Google Workspace** (Gmail, Calendar, Drive, Docs, Meet) — a Workspace account per user; personal `@gmail.com` won't work.
- **Telegram** — the surface each user talks to their agent on.
- **Notion** — the venture's project workspace.
- **GitHub** — the user's code repos.

---

## Wiring detail

What each tool needs in Stage 2. The venture admin creates the credentials (Step 6) and KRING wires them into each agent (Step 7).

### Google Workspace — ~15 min

Requires a Google Workspace account (personal `@gmail.com` won't work) and permission to create projects in the Workspace org — if the admin has locked this, enable project creation for the user first.

**1. Create a Google Cloud project**

- Go to [console.cloud.google.com](https://console.cloud.google.com) and sign in with the Workspace email.
- Top bar → project selector → **New Project**.
- Name: e.g. *Personal Workspace Agent*. Organization: the Workspace domain (e.g. `yourcompany.com`).
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
- **Authorized redirect URIs**: paste the callback URL KRING provides. Save.
- Copy the **Client ID** and **Client Secret** from the dialog.

**5. Hand off to KRING**

- Provide **Client ID** and **Client Secret** to KRING.
- KRING completes the auth handshake against the user's Workspace account.

### Notion — ~10 min

**1. Create an internal integration**

- Go to [notion.so/profile/integrations](https://www.notion.so/profile/integrations) → **New integration**.
- Name: e.g. *Personal Workspace Agent*. Associated workspace: the venture's workspace. Type: **Internal**.

**2. Set capabilities**

- **Content Capabilities**: Read content · Update content · Insert content.
- **Comment Capabilities**: Read comments · Insert comments.
- **User Capabilities**: Read user information (with email — needed to tag owners).
- Save.

**3. Copy the secret**

- Under **Secrets** → copy the **Internal Integration Secret** (`secret_…`).
- Provide it to KRING.

**4. Share pages with the integration**

- Open each page or database the agent should access → **•••** (top right) → **Connections** → **Add connections** → pick the integration.
- Share a top-level page to give the agent access to everything under it.

### GitHub — ~10 min

**1. Create a fine-grained personal access token**

- Go to [github.com/settings/tokens](https://github.com/settings/tokens) → **Fine-grained tokens** → **Generate new token**.
- Token name: e.g. *Personal Workspace Agent*. Expiration: 1 year (or longer if the org allows).

**2. Pick resource owner and repos**

- **Resource owner**: the user for personal repos, or the org for org repos. If org, the org owner must approve the token after creation (Org Settings → Personal access tokens → Pending requests).
- **Repository access**: *Only select repositories* (recommended — pick what the agent needs) or *All repositories*.

**3. Set repository permissions**

- **Contents**: Read and write.
- **Issues**: Read and write.
- **Pull requests**: Read and write.
- **Metadata**: Read-only (auto-granted).
- **Workflows**: Read and write *(only if the agent should edit GitHub Actions files)*.

**4. Hand off to KRING**

- Click **Generate token** → copy the token (`github_pat_…`) — shown only once.
- Provide it to KRING.

*(If the org disables fine-grained tokens, fall back to a classic PAT with scopes `repo` and `workflow`.)*

### Microsoft 365 legacy data — only if migrating from M365

If the venture is coming from a Microsoft 365 setup (Outlook mail, OneDrive/SharePoint files, Outlook calendar/contacts), don't do a hard cut-over. Mirror the data into Google and keep M365 as a read-only backup.

Full step-by-step in `runbooks/migrations/ms-to-google.md`. Short version:

1. **Mail** — Google Data Migration Service (Admin console) imports Outlook/Exchange into Gmail with folders, flags, dates preserved.
2. **Files** — Google Migrate for Workspace mirrors OneDrive/SharePoint into a **Shared Drive** (not "My Drive").
3. **Calendar** — Publish the Outlook calendar as `.ics`, add it to Google Calendar from URL.
4. **Contacts** — Export CSV from Outlook → import into Google Contacts.
5. **Cut-over day** — set auto-forward + out-of-office on the M365 mailbox; pin Outlook Web (`outlook.office.com`) as a bookmark only.
6. **Tell the agent** the cut-over date. It writes a `## Microsoft 365 (legacy)` block into `TOOLS.md` so it knows when to search the old system vs the new.

After 30 days the forward goes off; the M365 licence stays so the archive remains searchable.

### Local backup mirror (Syncthing) — ~10 min, optional but recommended

A read-only copy of the agent's files on the user's own Mac/PC, kept in sync automatically — so if the agent is ever down, everything it knows is still in a folder the user controls. It's **one-way**: the agent writes, the user's machine receives. KRING sets up the runtime (Send Only) side in Stage 2; the user finishes the Mac/PC side during onboarding using the runtime's Syncthing **Device ID**. Full step-by-step in `runbooks/syncthing-local-mirror.md`.

---

## References

- `onboarding.md` — the agent-led first conversation each user goes through (Stage 3).
- `playbook.md` — Personal Workspace day-to-day.
- `ai-commandments.md` — the 4 AI Commandments and must-know git vocab.
- `runbooks/migrations/ms-to-google.md` — Microsoft 365 → Google Workspace migration playbook.
- `runbooks/syncthing-local-mirror.md` — one-way local mirror of the agent's files (backup / visibility).
- `runbooks/repurposing-an-existing-agent.md` — converting an existing agent into Personal Workspace without losing its data or automations.
