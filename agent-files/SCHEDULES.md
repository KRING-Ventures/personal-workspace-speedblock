# SCHEDULES — {{AGENT_NAME}}'s Recurring Jobs

*The proactive layer only works if something fires it. This file is what fires it.*

Every capability in `playbook.md` that happens *without {{USER_FIRST_NAME}} asking* — the morning brief, the Monday review, the heartbeat checks on mail/calendar/commitments — depends on a scheduled trigger existing on this runtime. No trigger, no proactivity: the agent knows *how* to brief but is never *told to*. These are the triggers.

{{AGENT_NAME}} registers all of these itself with its `cron` capability — once, silently, during BOOTSTRAP — and self-heals them at boot (see `AGENTS.md` → *Scheduled jobs*). Nothing here needs a human to flip a switch on the runtime. Install the files, run the first session, and the rhythm sets itself up.

## The standard jobs

| Job | Default cadence | What it runs | Surface |
|---|---|---|---|
| **Daily brief** | Weekdays, 07:30 user-local | Builds the brief from `templates/daily.md` and sends it | Telegram |
| **Weekly review** | Mondays, 07:30 user-local | Builds the review from `templates/weekly.md` | Telegram |
| **Heartbeat check** | Hourly, 08:00–18:00 user-local, weekdays | Runs the `HEARTBEAT.md` protocol — be useful or stay silent | Telegram |
| **Memory distill** | Daily, ~18:00 user-local | Distills today's `memory/YYYY-MM-DD.md` into `MEMORY.md` | none (silent) |

All four run as **cron sessions** (isolated context — do the job, log, exit; see `AGENTS.md` → *Session types*).

## How they get set up

- **The agent owns all of them.** During BOOTSTRAP, {{AGENT_NAME}} creates these four jobs with its `cron` capability. No deploy-time runtime setting, no manual step. The heartbeat is just an hourly cron that runs the `HEARTBEAT.md` protocol — same mechanism as the rest.
- **Timezone comes from `USER.md`** (pulled from Calendar in BOOTSTRAP Phase 3). The times above are sensible defaults — don't interview the user about them at onboarding. If {{USER_FIRST_NAME}} later says "move my brief to 8" or "skip weekends," adjust the job then.
- **The agent can list, change, or remove them on request** — "move my brief to 8am", "pause the Monday review", "stop the hourly checks".

## Rules

- **Never create a job that messages other humans.** These jobs only ever message {{USER_FIRST_NAME}} on Telegram. Anything outbound to other people still follows the `## Action rules` permission model in `AGENTS.md`.
- **One job per row above — no duplicates.** On boot, check what's already registered before creating. If a job already exists, leave it; don't stack a second copy.
- **Log every job to `automations/AUTOMATIONS.md`** when created or changed, using the entry template there. A schedule that fires invisibly and breaks silently is worse than none.
- **Respect "off".** If {{USER_FIRST_NAME}} pauses or removes a job, don't silently recreate it at the next boot — record the choice in `MEMORY.md` and leave it off.
