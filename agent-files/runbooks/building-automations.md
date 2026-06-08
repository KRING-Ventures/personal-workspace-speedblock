# Building automations

How {{AGENT_NAME}} turns "can you make X happen automatically?" into a running, logged, reversible automation. This is the *how-to*; `automations/AUTOMATIONS.md` is the *record* of what's been built.

The standing rules (owner, rollback, logging, no outbound-without-permission) live at the top of `automations/AUTOMATIONS.md` — they bind every automation built here.

## What "an automation" is

Anything that runs **without {{USER_FIRST_NAME}} asking each time** — on a schedule or on an event. The standard PW stack can build, roughly:

- **Scheduled digests / reports** — e.g. a Friday summary of the week's closed commitments; a Monday list of invoices due. (A `cron` job that reads + messages.)
- **Time-based reminders & escalations** — e.g. nudge me 3 days before any deadline in my notes; re-surface a draft that's been unsent 48h.
- **Inbox rules beyond triage** — e.g. auto-label anything from the accountant; route receipts to a Drive folder.
- **Calendar reactions** — e.g. when a meeting with an external is booked, draft a prep doc; block 30 min of buffer after any 2h+ meeting (own calendar only).
- **Document / Notion triggers** — e.g. when a PM task moves to *Needs Review* and is assigned to me, ping me with the diff.

If a request needs a tool that isn't in `TOOLS.md`, say so and stop — don't pretend the integration exists.

## The build process

Five steps, every time. Don't skip the boring ones — they're what makes an automation safe to leave running.

1. **Confirm scope back.** One line: *"So: every weekday at 17:00, you want a list of any commitment due tomorrow — Telegram only, no emails to anyone. Right?"* Lock trigger, action, surface, and who (if anyone) it touches **before** building. (This is the `clear-and-complete-instructions` procedure applied to automations.)
2. **Check the permission line.** If the automation would ever **message or change things for other people**, it needs standing permission logged in `TOOLS.md` → Standing permissions, or it asks per-send. Default: automations message **only {{USER_FIRST_NAME}}**. Never build one that emails other humans on a schedule without explicit, logged sign-off.
3. **Build it as a `cron` job** (or event hook), anchored to the timezone in `USER.md`. Reuse the patterns in `SCHEDULES.md`. Keep the job's logic in one place; if it builds a message, point it at a template.
4. **Log it in `automations/AUTOMATIONS.md`** using the entry template there — purpose, owner, trigger, surfaces, human-in-loop, **rollback**, failure modes, date. An automation that fires invisibly and breaks silently is worse than none.
5. **Test once, then confirm.** Trigger it manually (or wait for the first real fire) and show {{USER_FIRST_NAME}} the result. *"Built and tested — here's what tomorrow's 17:00 run will look like. Disable any time by telling me to stop it."*

## When to act vs ask

- **Act** (then confirm) when the automation only ever reads and messages {{USER_FIRST_NAME}} — that's the same bar as a draft.
- **Ask first** when it sends to / changes things for other people, spends money, or is hard to reverse. Same permission model as `AGENTS.md` → *Action rules*.
- **Push back** when an automation would hide something important (e.g. auto-archiving mail it didn't truly handle) or fire so often it becomes noise. Better automation, not more.

## Changing or removing one

- To change: update the `cron` job and the `AUTOMATIONS.md` entry together. Note what changed and when.
- To remove: disable the job, mark the entry removed (don't delete the history), and tell {{USER_FIRST_NAME}} it's off. Respect "off" — don't recreate it at the next boot (record the choice in `MEMORY.md`, same as paused schedules).
