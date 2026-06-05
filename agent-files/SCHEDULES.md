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
| **Update check** | Weekly, Mondays ~09:00 user-local | Pulls the framework and compares its `STATE_VERSION` to your own. If the framework is ahead: tell {{USER_FIRST_NAME}} there's a new version and what it adds, in plain language, and **ask whether to apply it now**. Run catch-up only once they say yes. If they defer, leave their version untouched and re-offer next week. If you're already current, stay silent. | Telegram (only when there's a new version) |

All five run as **cron sessions** (isolated context — do the job, log, exit; see `AGENTS.md` → *Session types*).

The **update check** is the proactive trigger behind the "what's new" rule in `AGENTS.md`. Catch-up also runs at every session boot — but a user who hasn't opened a session in a while would otherwise never hear about a new version. This job guarantees they do: at most one message a week, only when something changed. It **notifies and asks before applying** — so no one is moved onto a version they didn't choose, and a freshly shipped update can't silently roll out across the whole fleet at once.

## How they get set up

- **The agent owns all of them.** During BOOTSTRAP, {{AGENT_NAME}} creates these five jobs with its `cron` capability. No deploy-time runtime setting, no manual step. The heartbeat is just an hourly cron that runs the `HEARTBEAT.md` protocol — same mechanism as the rest.
- **Timezone comes from `USER.md`** (pulled from Calendar in BOOTSTRAP Phase 3). The times above are sensible defaults — don't interview the user about them at onboarding. If {{USER_FIRST_NAME}} later says "move my brief to 8" or "skip weekends," adjust the job then.
- **The agent can list, change, or remove them on request** — "move my brief to 8am", "pause the Monday review", "stop the hourly checks".

## Rules

- **Never create a job that messages other humans.** These jobs only ever message {{USER_FIRST_NAME}} on Telegram. Anything outbound to other people still follows the `## Action rules` permission model in `AGENTS.md`.
- **One job per row above — no duplicates.** On boot, check what's already registered before creating. If a job already exists, leave it; don't stack a second copy.
- **Log every job to `automations/AUTOMATIONS.md`** when created or changed, using the entry template there. A schedule that fires invisibly and breaks silently is worse than none.
- **Respect "off".** If {{USER_FIRST_NAME}} pauses or removes a job, don't silently recreate it at the next boot — record the choice in `MEMORY.md` and leave it off.
