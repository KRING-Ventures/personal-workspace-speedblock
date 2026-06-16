# SCHEDULES — {{AGENT_NAME}}'s Recurring Jobs

*The proactive layer only works if something fires it. This file is what fires it.*

Every capability in `playbook.md` that happens *without {{USER_FIRST_NAME}} asking* — the morning brief, the Monday review, the heartbeat checks on mail/calendar/commitments — depends on a scheduled trigger existing on this runtime. No trigger, no proactivity: the agent knows *how* to brief but is never *told to*. These are the triggers.

{{AGENT_NAME}} registers all of these itself with its `cron` capability — once, silently, during BOOTSTRAP — and self-heals them at boot (see `AGENTS.md` → *Scheduled jobs*). Nothing here needs a human to flip a switch on the runtime. Install the files, run the first session, and the rhythm sets itself up.

## The standard jobs

| Job (`id`) | When — cron, user-local | What it runs | Surface |
|---|---|---|---|
| **Daily brief** (`daily-brief`) | `0 8 * * 1-5` (weekdays 08:00) | Morning inbox sweep (see *Inbox triage*), then build + send the brief from `templates/daily.md` — today's calendar, focus, commitments, and what was drafted / left for {{USER_FIRST_NAME}}. | Slack |
| **Inbox triage** (`inbox-triage`) | `*/30 * * * *` (every 30 min, 24/7) | `templates/email-draft.md` loop: draft ~95% into the Gmail Drafts folder, mark **only the drafted** emails read, leave the rest flagged. **Job logic must stay silent 18:00–08:00** (stage drafts, no Slack ping) and only message mid-day if a draft needs a decision now. | Slack (daytime, only if input needed) |
| **Weekly review** (`weekly-review`) | `0 8 * * 1` (Mon 08:00) | Build + send from `templates/weekly.md` — open commitments, what closed last week, the week's milestones, direction. **No email.** | Slack |
| **Meeting prep** (`meeting-prep`) | `*/15 6-21 * * *` (every 15 min, 06:00–22:00) | For any meeting starting in **~15 min** with other attendees (skip solo/focus blocks), send a prep from `templates/meeting-prep.md` **once** — attendees, recent context, what {{USER_FIRST_NAME}} wants from it. Track prepped meetings so it never double-fires. | Slack |
| **Heartbeat check** (`heartbeat`) | `0 8-18 * * *` (hourly 08:00–18:00) | Run the `HEARTBEAT.md` protocol — be useful or stay silent. Covers commitment slips, deadlines, calendar-load (email and meeting prep have their own jobs). | Slack |
| **Memory distill** (`memory-distill`) | `0 18 * * *` (daily ~18:00) | Distill today's `memory/YYYY-MM-DD.md` into `MEMORY.md`. | none (silent) |
| **Update check** (`update-check`) | `0 9 * * 1` (Mon ~09:00) | Pull the framework, compare `STATE_VERSION`; if it's ahead, tell {{USER_FIRST_NAME}} what's new in plain language and **ask before applying**. Also run `openclaw doctor`; if a boot file is truncated, move detail to `runbooks/` (see `AGENTS.md` → *Keep the boot bundle lean*) — never let `MEMORY.md` be the file that drops. | Slack (only when there's a new version or a budget action) |

### Creating them correctly
- **Use the `id` as the job name** when you create or self-heal a job — that's how the boot check finds an existing one and avoids stacking duplicates.
- **Anchor to the user's timezone** (`USER.md`). The cron times above are user-local: pass the `USER.md` timezone to your cron tool (or convert before scheduling), then confirm the first fire lands at the right local hour. **No timezone yet? Get one before registering** (BOOTSTRAP Step 1) — don't guess.
- **The behaviour guards live in the job, not the schedule.** The cron only controls *when it runs*; things like inbox triage's 18:00–08:00 silence, "draft never send," and meeting prep's once-per-meeting must be encoded in the job's own logic.

All seven run as **cron sessions** (isolated context — do the job, log, exit; see `AGENTS.md` → *Session types*).

A few things the table doesn't make obvious:

- **Brief + triage are one rhythm.** Triage runs every 30 min round the clock, every day (silent overnight), so the 08:00 brief already reflects everything that landed. The brief itself goes out on weekdays. The weekly review is the only Monday-only job, and the only one that leaves email out.
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
