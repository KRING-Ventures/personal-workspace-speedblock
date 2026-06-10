# Migrating from Microsoft 365 to Google Workspace

For people moving onto Personal Workspace from a Microsoft 365 setup (Outlook mail, OneDrive/SharePoint files, Outlook calendar, Outlook contacts).

The goal isn't a hard cut-over. The goal is **Google is your daily driver from day one, Microsoft becomes a read-only backup** for anything older than the migration date.

---

## Principle: mirror, don't cut over

- **Google = daily driver.** All new mail, files, calendar events, and contacts live in Google from the migration date forward.
- **Microsoft = cold storage.** Keep the M365 licence active. Don't delete anything. You'll search it when you need something older than the cut-over date.
- **Overlap window = 30–60 days.** Auto-forward + auto-reply on the old address. After the window, the old address quietly goes dark; the licence stays so the archive remains searchable.

Your agent helps with both sides during the overlap — see the *Daily work after migration* section below.

---

## What gets migrated, and how

| What | Tool | Time | Result |
|---|---|---|---|
| Mail | Google Data Migration Service (DMS) | 1–48 h depending on mailbox size | Folders, flags, dates preserved in Gmail |
| Files | Google Migrate for Workspace (or manual upload for small sets) | Varies — hours to days | OneDrive/SharePoint tree mirrored into a Shared Drive |
| Calendar | `.ics` export → Google Calendar import | Minutes | Past and future events on Google Calendar |
| Contacts | CSV export → Google Contacts import | Minutes | Contacts in Google, including groups |

Run them in this order. Mail and files are the long-running ones — start those first, do calendar and contacts while they run.

---

## Step 1 — Mail (Google Data Migration Service)

Google ships a built-in tool for Exchange/Outlook → Gmail.

1. In the Google Admin console: **Apps → Google Workspace → Gmail → Data migration**.
2. Source: **Microsoft Exchange / Microsoft 365**. Auth with the M365 admin account (or per-user app password if you don't have admin).
3. Pick the date range. Default is everything; tighten if the mailbox is huge.
4. Pick users (you can run it per user or in batch).
5. Start. Folder structure, flags, read/unread state, and original dates are preserved.

**Verify when done:**
- Spot-check 5 recent and 5 old messages — same content, same date, same folder?
- Search for one attachment by name — does it open?
- Filters/rules don't migrate; rebuild any important ones in Gmail directly.

## Step 2 — Files (OneDrive / SharePoint → Drive)

Use **Google Migrate for Workspace** (the supported successor to Mover). It moves OneDrive and SharePoint into Drive.

1. In Admin console: **Apps → Google Workspace → Drive and Docs → Migrate data**.
2. Source: OneDrive or SharePoint. Auth with M365.
3. **Destination:** a Shared Drive, not "My Drive". Mirror the original folder tree so permissions stay manageable and it's findable.
4. Set conflict policy (recommend: skip duplicates by content hash).
5. Start. You'll get an email when it's done.

**Don't:** bulk-dump everything into "My Drive". Personal Drives don't share well and you'll regret it the first time someone needs access.

**Verify when done:**
- Pick three files: do they open in Docs/Sheets/Slides without formatting damage?
- Check sharing on a folder you'd expect to be team-visible — does it match the M365 ACL?
- Office files (.docx, .xlsx, .pptx) open in Google as-is. Convert them in-place when you next edit them; don't batch-convert.

## Step 3 — Calendar

Outlook → `.ics` → Google Calendar.

1. In Outlook Web (`outlook.office.com`): **Calendar → Settings → View all Outlook settings → Calendar → Shared calendars → Publish a calendar**. Pick *Can view all details*, copy the ICS URL.
2. In Google Calendar: **Settings → Add calendar → From URL** and paste it. Imports past + future events.
3. **Re-share recurring meetings from Google.** Anything you organise that repeats — re-create or re-share from Google so future edits propagate to attendees. Imported events are read-only copies; they don't sync changes back to Outlook.

**Verify:**
- Open three recent and three future events — attendees, times, video links present?
- For any event with a Teams link: replace with Google Meet on the next occurrence.

## Step 4 — Contacts

1. In Outlook Web: **People → Manage → Export contacts** → CSV.
2. In Google Contacts: **Import** → upload the CSV.
3. Re-create labels (Google's name for contact groups) — they don't import cleanly.

---

## Cut-over day

A short checklist for the day Google becomes your default.

- [ ] All four migrations above run and verified.
- [ ] Update your email signature in Gmail.
- [ ] Set up an auto-forward on the M365 mailbox: forward all to your Google address.
- [ ] Set an out-of-office on the M365 mailbox: *"I've moved to <new address>. This inbox is no longer monitored after [date]. Mail is being forwarded for the next 30 days."*
- [ ] Update your address in places that send you mail: bank, calendar invitees, tools you log into with email.
- [ ] Set Google Calendar as default in your phone calendar app; sign out of Outlook on mobile if you only used it for calendar.
- [ ] Pin `outlook.office.com` as a bookmark on the laptop. **Don't** keep the Outlook desktop client open — it'll fight you for notifications.

---

## Daily work after migration

**The rule of thumb:** anything from before the cut-over date → search Microsoft. Anything from after → search Google.

Your agent knows the cut-over date (it's logged in `TOOLS.md` when you set this up). When you ask *"find that contract from Jens last year"*, the agent picks the right system based on the date.

**Microsoft access during the overlap window:**
- Outlook Web (`outlook.office.com`) — bookmarked, used for search only.
- OneDrive Web (`onedrive.live.com`) — same.
- Don't reinstall the desktop apps. They'll re-sync and re-notify and you'll lose the clean break.

**After 30 days:**
- Turn off the auto-forward.
- Update the auto-reply to a final *"this inbox is closed, reach me at <new>"*.
- Keep the M365 licence. The archive remains searchable; cancelling deletes it.

**After 60 days:**
- The auto-reply stays on indefinitely (cheap insurance).
- Consider archiving the M365 tenant if it's a personal cost (export full mailbox + Drive to a local backup first).

---

## Common gotchas

- **"Where's my folder structure?"** Gmail uses labels, not folders. The DMS converts each Outlook folder to a label with the same name. They look like folders in the sidebar but a message can carry multiple labels — that's normal.
- **Shared mailboxes.** DMS doesn't do shared mailboxes natively; run them as separate user migrations or use a third-party tool (CloudMigrator, BitTitan) for a clean job.
- **Distribution lists / Groups.** Recreate in Google Groups; they don't migrate.
- **Power Automate / Outlook rules.** Don't migrate. Rebuild as Gmail filters or as agent automations (talk to your agent about it).
- **Encrypted (IRM/AIP) mail.** Doesn't decrypt on migration — those messages arrive as locked. Either decrypt before migrating or accept that some archive items stay readable only via M365.
- **Microsoft Teams chat history.** Not in scope here. Teams chats don't migrate to Slack/Meet/anything cleanly; export what matters as a text archive before tenancy decommission.

---

## When to ask your agent

- *"Set up the overlap auto-forward for me."* — agent guides you through the M365 settings page.
- *"Find the invoice from Q1 — I think it was Outlook."* — agent searches the right system based on date.
- *"What's still on OneDrive that I haven't touched in 6 months?"* — agent helps you audit what to clean up before closing the tenant.
- *"Rebuild this Outlook rule as a Gmail filter."* — agent translates and sets it up.

---

## Related

- `playbook.md` — Personal Workspace top-level playbook
- `agent-files/runbooks/ms-to-google-overlap.md` — agent-side rules for the overlap window
- `activation.md` — legacy MS data is handled during activation (Stage 2 wiring); that routes you here
