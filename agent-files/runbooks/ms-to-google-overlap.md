# MS → Google Overlap — Agent Rules

How {{AGENT_NAME}} handles a user with a Microsoft 365 archive sitting behind their primary Google Workspace.

**When this applies:** during onboarding the user said *yes, I have legacy MS data*. `TOOLS.md` then carries a Microsoft 365 entry with a **cut-over date** and **access mode** (web-only / read-only / decommissioned).

If `TOOLS.md` has no Microsoft 365 entry, none of this applies — skip the file.

---

## The rule of thumb

- **Newer than the cut-over date** → it lives in Google. Search Gmail, Calendar, Drive directly.
- **Older than the cut-over date** → it lives in Microsoft. Search via the M365 web surfaces (`outlook.office.com`, `onedrive.live.com`) or ask the user to fetch it.
- **Spans both** → search Google first, then M365 if not found; tell the user where you found it.

Do not guess. If the user asks for something and you don't know the date, ask once: *"Is this before or after [cut-over date]?"* — then search the right system.

---

## During the overlap window (first 30–60 days)

While auto-forward is still active on the M365 mailbox, new mail can appear in **both** systems. Treat Google as canonical. If the user mentions a recent message and you find it only in M365, surface that explicitly — it usually means the forward hasn't caught up, or the message is internal-only to the M365 tenant.

If the user asks to reply to something arriving via the forward, reply from the Google account (never from M365).

---

## After the overlap window

- Auto-forward is off.
- M365 mailbox is a read-only archive — never send from it, never reply from it.
- Old contacts, old files, old calendar events: searchable but not editable. If the user needs to edit an old M365 file, copy it into Drive first, then edit.

---

## What to never do

- Don't suggest the user re-install Outlook or OneDrive desktop clients. The clean break is the point.
- Don't propose deleting the M365 tenant unless the user explicitly asks. Cancelling = archive gone.
- Don't try to bridge — no agent-side syncing between the two systems. Use whichever is canonical for that data and tell the user where you looked.
- Don't bother the user with "I checked Google and didn't find it, checking M365 now" unless the search takes real time. Silent fallback is fine for one-shot lookups.

---

## Logging in `TOOLS.md`

When the user goes through migration, `TOOLS.md` gets a Microsoft 365 entry that looks like this:

```markdown
## Microsoft 365 (legacy)

- **Account:** [legacy email]
- **Cut-over date:** YYYY-MM-DD
- **Access mode:** web-only (Outlook Web + OneDrive Web)
- **Status:** read-only archive
- **Auto-forward to Google:** active until YYYY-MM-DD (then off)
- **Rules:**
  - Search only; never send, never edit.
  - Surface to user when answering questions about anything older than the cut-over date.
```

If you set this up with the user during onboarding, write that block into `TOOLS.md` and date it.

---

## Related

- `runbooks/migrations/ms-to-google.md` — the human-facing migration playbook
- `TOOLS.md` template — `## Microsoft 365 (legacy)` section
