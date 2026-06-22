# SCHEDULES — {{AGENT_NAME}}'s Recurring Jobs

*The proactive layer only works if something fires it. This file is what fires it.*

Every capability in `playbook.md` that happens *without {{USER_FIRST_NAME}} asking* — the morning brief, the Monday review, the heartbeat checks on mail/calendar/commitments — depends on a scheduled trigger existing on this runtime. No trigger, no proactivity: the agent knows *how* to brief but is never *told to*. These are the triggers.

{{AGENT_NAME}} registers all of these itself with its `cron` capability — once, silently, during BOOTSTRAP — and self-heals them at boot (see `AGENTS.md` → *Scheduled jobs*). Nothing here needs a human to flip a switch on the runtime. Install the files, run the first session, and the rhythm sets itself up.

## The standard jobs

There are three job types. This distinction is load-bearing:

- **Visible jobs** are allowed to message {{USER_FIRST_NAME}} when they run.
- **Prefiltered jobs** must pass through a hard, token-free gate before the agent wakes. If the gate finds no signal, the job exits silently.
- **Silent jobs** do internal work and never message unless something is broken and needs human action.

| Job (`id`) | Type | When — cron, user-local | What it runs | Surface |
|---|---|---|---|---|
| **Daily brief** (`daily-brief`) | Visible | `0 8 * * 1-5` (weekdays 08:00) | Morning inbox sweep (see *Inbox triage*), then build + send the brief from `templates/daily.md` — today's calendar, focus, commitments, and what was drafted / left for {{USER_FIRST_NAME}}. | Slack |
| **Inbox triage** (`inbox-triage`) | Prefiltered | smart trigger every 30 min | Token-free gate checks Gmail first (see `runbooks/smart-triggers.md` and `scripts/smart-trigger.py`). Only wake the agent when there is unhandled unread inbox mail that may need drafting or a same-day human decision. If woken, run `templates/email-draft.md`: draft ~95% into Gmail Drafts, mark **only drafted** emails read, leave the rest flagged. | Slack only if the user needs to act now |
| **Weekly review** (`weekly-review`) | Visible | `0 8 * * 1` (Mon 08:00) | Build + send from `templates/weekly.md` — open commitments, what closed last week, the week's milestones, direction. **No email.** | Slack |
| **Meeting prep** (`meeting-prep`) | Visible | `*/15 8-17 * * *` (every 15 min, 08:00–18:00) | For any meeting starting in **~15 min** with other attendees (skip solo/focus blocks), send a prep from `templates/meeting-prep.md` **once** — attendees, recent context, what {{USER_FIRST_NAME}} wants from it. Track prepped meetings so it never double-fires. | Slack |
| **Heartbeat check** (`heartbeat`) | Prefiltered | `0 8-18 * * *` (hourly 08:00–18:00) | Run a cheap signal check first (see `runbooks/smart-triggers.md`), then the `HEARTBEAT.md` protocol only when needed. Covers commitment slips, deadlines, and calendar-load. General email and meeting prep have their own jobs. | Slack only if useful now |
| **Memory distill** (`memory-distill`) | Silent | `0 18 * * *` (daily ~18:00) | Distill today's `memory/YYYY-MM-DD.md` into `MEMORY.md`. | none |
| **Update check** (`update-check`) | Silent unless action needed | `0 9 * * 1` (Mon ~09:00) | Pull the framework, compare `STATE_VERSION`; if it's ahead, tell {{USER_FIRST_NAME}} what's new in plain language and **ask before applying**. Also run `openclaw doctor`; if a boot file is truncated, move detail to `runbooks/` (see `AGENTS.md` → *Keep the boot bundle lean*) — never let `MEMORY.md` be the file that drops. | Slack only when there's a new version or a budget action |
| **Agent hygiene** (`agent-hygiene`) | Silent unless action needed | `30 9 * * 1` (Mon ~09:30) | Run `runbooks/agent-hygiene.md`: check boot budget, root clutter, oversized files, and memory bloat; compact/archive obvious bloat; explain recommendations when a decision is needed. | Slack only when the user needs to decide |

### Creating them correctly
- **Use the `id` as the job name** when you create or self-heal a job — that's how the boot check finds an existing one and avoids stacking duplicates.
- **Anchor to the user's timezone** (`USER.md`). The cron times above are user-local: pass the `USER.md` timezone to your cron tool (or convert before scheduling), then confirm the first fire lands at the right local hour. **No timezone yet? Get one before registering** (BOOTSTRAP Step 1) — don't guess.
- **Do not register prefiltered jobs as normal agent crons.** High-frequency jobs like inbox triage must use a hard gate before the agent wakes. Prompt instructions like "stay silent" are not enough; final assistant text can leak into Slack/Telegram. The gate contract lives in `runbooks/smart-triggers.md`.
- **The behaviour guards live in the job, not the schedule.** The cron only controls *when it runs*; things like inbox triage's 18:00–08:00 silence, "draft never send," and meeting prep's once-per-meeting must be encoded in the job's own logic.

Visible and silent jobs run as **cron sessions** (isolated context — do the job, log, exit; see `AGENTS.md` → *Session types*). Prefiltered jobs run their gate first and wake an agent session only after a real signal.

A few things the table doesn't make obvious:

- **Brief + triage are one rhythm.** Triage prefilter runs every 30 min round the clock, every day, so the 08:00 brief already reflects everything that landed. The brief itself goes out on weekdays. The weekly review is the only Monday-only job, and the only one that leaves email out.
- **Meeting prep is its own job, not a heartbeat check** — the heartbeat's "skip routine standups" filter used to swallow it. The daily brief covers the morning's meetings in one line each; this job fires the fuller ~30-min-before prep.
- **Update check notifies and asks before applying** — at most one message a week, only when there's a new version, so no one is moved onto a version they didn't choose.
- **Agent hygiene explains best practice when it needs a choice** — most users do not know which agent files should be compacted, archived, or left alone. Silent cleanup is fine for obvious generated clutter; judgment calls get a recommendation plus the reason.

## How they get set up

- **The agent owns all of them.** During BOOTSTRAP, {{AGENT_NAME}} creates these jobs with the trigger type shown above. No deploy-time runtime setting, no manual step. Visible and silent jobs can be normal agent cron jobs; prefiltered jobs must be wired through their gate.
- **Timezone comes from `USER.md`** (pulled silently from Calendar in BOOTSTRAP Step 1). The times above are sensible defaults — don't interview the user about them at onboarding. If {{USER_FIRST_NAME}} later says "move my brief to 8" or "skip weekends," adjust the job then.
- **The agent can list, change, or remove them on request** — "move my brief to 8am", "pause the Monday review", "stop the hourly checks".

## Rules

- **Never create a job that messages other humans.** These jobs only ever message {{USER_FIRST_NAME}} on Slack. Anything outbound to other people still follows the `## Action rules` permission model in `AGENTS.md`.
- **One job per row above — no duplicates.** On boot, check what's already registered before creating. If a job already exists, leave it; don't stack a second copy.
- **Never "fix" a missing prefiltered job by creating a direct agent cron.** Recreate the gate, not a noisy shortcut.
- **Log every job to `automations/AUTOMATIONS.md`** when created or changed, using the entry template there. A schedule that fires invisibly and breaks silently is worse than none.
- **Respect "off".** If {{USER_FIRST_NAME}} pauses or removes a job, don't silently recreate it at the next boot — record the choice in `MEMORY.md` and leave it off.
