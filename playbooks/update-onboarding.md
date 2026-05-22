# Update Onboarding

For people who are already onboarded onto Personal Workspace and want to catch up on what's shipped since.

**How to read this file.** A menu, not a checklist. Each version section lists what shipped, who it's relevant for, and how to adopt it if you want. Nothing here is mandatory — your agent will surface the deltas that fit your situation and let you decide.

Newest version on top. The agent knows your current version (in your local `STATE_VERSION`) and walks you through sections newer than that.

For new users: skip this file. `onboarding.md` is the full setup from zero on the latest version.

---

## beta → v1.0

Shipped: 2026-05-22.

### Microsoft 365 → Google Workspace migration

**What shipped.** A migration path for people coming onto Personal Workspace from a Microsoft 365 setup. Google becomes the daily driver, M365 becomes a read-only backup. Your agent learns the cut-over date and searches the right system based on the date of what you're asking for.

**Who it's relevant for.** Anyone with legacy Microsoft 365 data — Outlook mail, OneDrive/SharePoint files, Outlook calendar/contacts — that still matters to you. Skip if you've never used M365, or if you've already cleaned out your old tenant.

**How to adopt it.**

1. Open the *Microsoft 365 legacy data* section in `onboarding.md` — that's the full setup (4 migration steps + cut-over checklist + gotchas). Same content new users get.
2. Tell your agent: *"I'm migrating my old Microsoft 365 data — let's run the steps in onboarding."*
3. Your agent walks the steps with you and writes a `## Microsoft 365 (legacy)` block into your `TOOLS.md` with the cut-over date so it knows when to search M365 vs Google going forward.

**Skip if.** You don't have legacy M365 data, or you've already cut over your own way and just want the agent to know the cut-over date — in which case ask your agent to add the `TOOLS.md` block directly.
