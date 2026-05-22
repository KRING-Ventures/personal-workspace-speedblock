# Personal Workspace — Onboarding

How a venture gets onto Personal Workspace.

## Phase 1 — Admin (you)

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

## Phase 4 — Agent/user onboarding (employee)

In your first conversation, the agent:

1. Introduces itself and the tools you'll use together.
2. Helps you connect Google Workspace, Notion, and GitHub (skip and come back later if you want — wiring detail below).
3. Asks if you have legacy Microsoft 365 data to migrate. If yes, walks you through the *Microsoft 365 legacy data* section below and logs a Microsoft 365 (legacy) entry in `TOOLS.md` so it can search the right system later.
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

If you're coming from a Microsoft 365 setup (Outlook mail, OneDrive/SharePoint files, Outlook calendar/contacts), don't try a hard cut-over.

**The principle: mirror, don't cut over.** Google becomes your daily driver from day one. Microsoft stays as a read-only backup for anything older than the cut-over date. Auto-forward + auto-reply on the old address for 30–60 days, then it goes dark; the M365 licence stays so the archive remains searchable.

Run the four steps in this order. Mail and files are long-running — start those first, do calendar and contacts while they run.

**1. Mail — Google Data Migration Service**

In the Google Admin console: **Apps → Google Workspace → Gmail → Data migration**.

- Source: **Microsoft Exchange / Microsoft 365**. Auth with the M365 admin account (or per-user app password if no admin).
- Pick a date range (default = everything) and the users to migrate.
- Start. Folder structure, flags, read/unread state, and original dates are preserved.

Verify: spot-check 5 recent and 5 old messages (content, date, folder match); open one attachment by name. Rules/filters don't migrate — rebuild any important ones in Gmail directly.

**2. Files — OneDrive / SharePoint → Drive**

In Admin console: **Apps → Google Workspace → Drive and Docs → Migrate data**. Tool is **Google Migrate for Workspace** (successor to Mover).

- Source: OneDrive or SharePoint. Auth with M365.
- **Destination:** a **Shared Drive**, not "My Drive". Mirror the original folder tree.
- Conflict policy: skip duplicates by content hash.
- Start. You'll get an email when it's done.

Verify: three files open in Docs/Sheets/Slides without formatting damage; sharing on a folder matches the M365 ACL. Office files open as-is — convert in-place when you next edit, don't batch-convert.

Don't bulk-dump into "My Drive" — personal Drives don't share well.

**3. Calendar — `.ics` export → Google Calendar**

In Outlook Web (`outlook.office.com`): **Calendar → Settings → View all Outlook settings → Calendar → Shared calendars → Publish a calendar**. Pick *Can view all details*, copy the ICS URL.

In Google Calendar: **Settings → Add calendar → From URL** and paste it. Imports past + future events.

**Re-share recurring meetings from Google.** Anything you organise that repeats — re-create or re-share from Google so future edits propagate to attendees. Imported events are read-only copies.

**4. Contacts — CSV export → Google Contacts**

In Outlook Web: **People → Manage → Export contacts** → CSV. In Google Contacts: **Import** → upload the CSV. Re-create labels (Google's name for contact groups) — they don't import cleanly.

**Cut-over day checklist**

- [ ] All four migrations above run and verified.
- [ ] Update your email signature in Gmail.
- [ ] Auto-forward on the M365 mailbox → your Google address.
- [ ] Out-of-office on the M365 mailbox: *"I've moved to <new>. This inbox is no longer monitored after [date]. Mail is forwarded for the next 30 days."*
- [ ] Update your address in places that send you mail: bank, calendar invitees, login emails.
- [ ] Set Google Calendar as default in your phone calendar app; sign out of Outlook on mobile if you only used it for calendar.
- [ ] Pin `outlook.office.com` as a bookmark on the laptop. **Don't** keep the Outlook desktop client open — it'll fight you for notifications.
- [ ] Tell your agent the cut-over date. It writes a `## Microsoft 365 (legacy)` block into `TOOLS.md` so it knows when to search the old system vs the new.

After 30 days the forward goes off; the M365 licence stays so the archive remains searchable.

**Common gotchas**

- **"Where's my folder structure?"** Gmail uses labels, not folders. DMS converts each Outlook folder to a label with the same name. A message can carry multiple labels — that's normal.
- **Shared mailboxes.** DMS doesn't do them natively — run as separate user migrations or use CloudMigrator / BitTitan.
- **Distribution lists / Groups.** Recreate in Google Groups; don't migrate.
- **Power Automate / Outlook rules.** Don't migrate. Rebuild as Gmail filters or as agent automations.
- **Encrypted (IRM/AIP) mail.** Doesn't decrypt on migration — arrives locked. Decrypt before migrating or leave it readable only via M365.
- **Microsoft Teams chat history.** Not in scope. Export what matters as a text archive before tenancy decommission.

## References

- `playbooks/playbook.md` — Personal Workspace day-to-day.
- `playbooks/the-4-ai-commandments.md` — the 4 AI Commandments and must-know git vocab.
- `playbooks/update-onboarding.md` — for existing users: what's shipped since you onboarded.
