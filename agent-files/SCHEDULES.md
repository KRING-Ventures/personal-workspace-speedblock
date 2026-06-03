# SCHEDULES — {{AGENT_NAME}}'s Recurring Jobs

*The proactive layer only works if something fires it. This file is what fires it.*

Every capability in `playbook.md` that happens *without {{USER_FIRST_NAME}} asking* — the morning brief, the Monday review, the heartbeat checks on mail/calendar/commitments — depends on a scheduled trigger existing on this runtime. No trigger, no proactivity: the agent knows *how* to brief but is never *told to*. These are the triggers.

{{AGENT_NAME}} registers these during BOOTSTRAP (first session) and self-heals them at boot (see `AGENTS.md` → *Scheduled jobs*). They are set up with {{USER_FIRST_NAME}}'s real timezone and preferred times — never guessed.

## The standard jobs

| Job | Default cadence | What it runs | Surface |
|---|---|---|---|
| **Daily brief** | Weekdays, 07:30 user-local | A `cron` session that builds the brief from `templates/daily.md` and sends it | Telegram |
| **Weekly review** | Mondays, 07:30 user-local | A `cron` session that builds the review from `templates/weekly.md` | Telegram |
| **Heartbeat poll** | Hourly, 08:00–18:00 user-local, weekdays | A heartbeat session following `HEARTBEAT.md` (be useful or silent) | Telegram |
| **Memory distill** | Daily, end of day (~18:00 user-local) | A `cron` session that distills today's `memory/YYYY-MM-DD.md` into `MEMORY.md` | none (silent) |

Times are **defaults**. Ask {{USER_FIRST_NAME}} for their preferred brief time during BOOTSTRAP; if they don't care, use these. Always anchor to the timezone in `USER.md`.

## How they get set up

Two mechanisms, both needed:

1. **`cron` jobs — the agent owns these.** {{AGENT_NAME}} creates the daily brief, weekly review, and memory distill as scheduled wake events using its own `cron` capability. They run as **cron sessions** (isolated context — do the job, log, exit; see `AGENTS.md` → *Session types*). The agent can list, change, or remove them on request ("move my brief to 8am", "skip the weekend").

2. **Heartbeat poll — enabled at deploy.** The hourly heartbeat cadence is a runtime setting, not something the agent self-schedules. KRING enables it when standing up the runtime (`onboarding.md` Phase 2). A populated `HEARTBEAT.md` plus the poll cadence is what makes the reactive checks fire. If `HEARTBEAT.md` is empty or the cadence is off, no heartbeats run.

## Rules

- **Never create a job that messages other humans.** These jobs only ever message {{USER_FIRST_NAME}} on Telegram. Anything outbound to other people still follows the `## Action rules` permission model in `AGENTS.md`.
- **One job per row above — no duplicates.** On boot, check what's already registered before creating. If a job already exists, leave it; don't stack a second copy.
- **Log every job to `automations/AUTOMATIONS.md`** when created or changed, using the entry template there. A schedule that fires invisibly and breaks silently is worse than none.
- **Respect "off".** If {{USER_FIRST_NAME}} pauses or removes a job, don't silently recreate it at the next boot — record the choice in `MEMORY.md` and leave it off.
