# SCHEDULES — {{AGENT_NAME}}'s Recurring Jobs

*The proactive layer only works if something fires it. This file is what fires it.*

Every capability in `playbook.md` that happens *without {{USER_FIRST_NAME}} asking* — the morning brief, the Monday review, the heartbeat checks on mail/calendar/commitments — depends on a scheduled trigger existing on this runtime. No trigger, no proactivity: the agent knows *how* to brief but is never *told to*. These are the triggers.

{{AGENT_NAME}} registers all of these itself with its `cron` capability — once, silently, during BOOTSTRAP — and self-heals them at boot (see `AGENTS.md` → *Scheduled jobs*). Nothing here needs a human to flip a switch on the runtime. Install the files, run the first session, and the rhythm sets itself up.

## The standard jobs

| Job | Default cadence | What it runs | Surface |
|---|---|---|---|
| **Daily brief** | Every day, 08:00 user-local | Runs the morning inbox sweep (see *Inbox triage*), then builds the brief from `templates/daily.md` and sends it — today's calendar, focus, commitments, plus what the agent drafted and what it left for {{USER_FIRST_NAME}} | Slack |
| **Inbox triage** | Every 30 min, 24/7 | Runs the `templates/email-draft.md` triage loop: read new mail, draft everything it can answer (~95%) **into the Gmail Drafts folder**, mark **only the drafted emails** as read, leave the rest unread and flagged for {{USER_FIRST_NAME}}. Runs round the clock so drafts are ready whenever mail lands — but **stays silent outside waking hours** (no Slack pings 18:00–08:00; just stage drafts). Only ever messages mid-day if a draft genuinely needs a human decision now. | Slack (daytime only, when input is needed) |
| **Weekly review** | Mondays, 08:00 user-local | Builds the review from `templates/weekly.md` — the big-picture week. **No email triage in this one**: open commitments, what closed last week, the week's milestones/events, direction. | Slack |
| **Meeting prep** | Every 15 min, 06:00–22:00 user-local, every day | Checks the calendar for any meeting starting in ~30 min that has other attendees (skips solo/focus blocks). For each, sends a prep from `templates/meeting-prep.md` **once** — who's in it, recent context, what {{USER_FIRST_NAME}} wants from it. Tracks which meetings it's already prepped so it never double-fires. | Slack |
| **Heartbeat check** | Hourly, 08:00–18:00 user-local, every day | Runs the `HEARTBEAT.md` protocol — be useful or stay silent. Email is owned by *Inbox triage* and meeting prep by its own job; the heartbeat covers everything else (commitment slips, deadlines, calendar-load nudges). | Slack |
| **Memory distill** | Daily, ~18:00 user-local | Distills today's `memory/YYYY-MM-DD.md` into `MEMORY.md` | none (silent) |
| **Update check** | Weekly, Mondays ~09:00 user-local | Pulls the framework and compares its `STATE_VERSION` to your own. If the framework is ahead: tell {{USER_FIRST_NAME}} there's a new version and what it adds, in plain language, and **ask whether to apply it now**. Run catch-up only once they say yes. If they defer, leave their version untouched and re-offer next week. If you're already current, stay silent. **Also run a context-budget check:** `openclaw doctor`. If it reports any boot file truncated, move detail out to `runbooks/` (see `AGENTS.md` → *Keep the boot bundle lean*) — never let `MEMORY.md` be the file that gets dropped. | Slack (only when there's a new version, or when the budget check needs action) |

All seven run as **cron sessions** (isolated context — do the job, log, exit; see `AGENTS.md` → *Session types*).

A few things the table doesn't make obvious:

- **Brief + triage are one rhythm.** Triage runs every 30 min round the clock (silent overnight) so the 08:00 brief already reflects everything that landed. Both run every day; the weekly review is the only Monday-only job and the only one that leaves email out.
- **Meeting prep is its own job, not a heartbeat check** — the heartbeat's "skip routine standups" filter used to swallow it. The daily brief covers the morning's meetings in one line each; this job fires the fuller ~30-min-before prep.
- **Update check notifies and asks before applying** — at most one message a week, only when there's a new version, so no one is moved onto a version they didn't choose.

## How they get set up

- **The agent owns all of them.** During BOOTSTRAP, {{AGENT_NAME}} creates these seven jobs with its `cron` capability. No deploy-time runtime setting, no manual step. The heartbeat is just an hourly cron that runs the `HEARTBEAT.md` protocol — same mechanism as the rest.
- **Timezone comes from `USER.md`** (pulled silently from Calendar in BOOTSTRAP Step 1). The times above are sensible defaults — don't interview the user about them at onboarding. If {{USER_FIRST_NAME}} later says "move my brief to 8" or "skip weekends," adjust the job then.
- **The agent can list, change, or remove them on request** — "move my brief to 8am", "pause the Monday review", "stop the hourly checks".

## Rules

- **Never create a job that messages other humans.** These jobs only ever message {{USER_FIRST_NAME}} on Slack. Anything outbound to other people still follows the `## Action rules` permission model in `AGENTS.md`.
- **One job per row above — no duplicates.** On boot, check what's already registered before creating. If a job already exists, leave it; don't stack a second copy.
- **Log every job to `automations/AUTOMATIONS.md`** when created or changed, using the entry template there. A schedule that fires invisibly and breaks silently is worse than none.
- **Respect "off".** If {{USER_FIRST_NAME}} pauses or removes a job, don't silently recreate it at the next boot — record the choice in `MEMORY.md` and leave it off.
