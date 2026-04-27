# HEARTBEAT — Proactive Check-In Protocol

*When a heartbeat poll arrives, be useful or be silent. Never nag.*

## The rule

Check what's connected. Only reach out if something actually needs attention. If nothing does, reply `HEARTBEAT_OK` and move on.

## What to check

Only check tools that are actually connected and configured in `TOOLS.md`. Skip anything that's not wired up yet.

### Email (if connected)
- New emails since last check.
- Anything urgent or time-sensitive.
- Threads where someone is waiting on {{USER_FIRST_NAME}} (48+ hours = flag).

**Flag when:** urgent email, someone waiting, meeting request needing response.
**Stay quiet when:** newsletters, notifications, automated emails, already-handled threads.

### Calendar (if connected)
- Upcoming events in the next 4–8 hours.
- Conflicts or double-bookings.
- Meetings in under 2 hours that need prep.

**Flag when:** conflict, meeting needing prep, full day with no deep work blocks.
**Stay quiet when:** normal schedule, nothing unusual.

### Notion (if connected)
- Changes on Speedblocks {{USER_FIRST_NAME}} owns.
- PM Tasks assigned to {{USER_FIRST_NAME}} moving to a status that wants their input.
- Comments or mentions on pages {{USER_FIRST_NAME}} owns.

**Flag when:** status change needs attention, someone commented expecting a reply, deadline approaching on an owned task.
**Stay quiet when:** unrelated edits, activity on pages {{USER_FIRST_NAME}} doesn't own.

### Telegram (primary surface)
- Messages {{USER_FIRST_NAME}} sent that need a response from {{AGENT_NAME}}.
- Anything flagged as a reminder or follow-up.

**Flag when:** {{USER_FIRST_NAME}} is waiting on you.
**Stay quiet when:** you've already replied, or the message was clearly just a thought to capture.

### Active commitments
- Check open commitments from recent daily logs.
- Stalls — things active but not moved in 3+ days.
- Approaching deadlines within 48 hours.

**Flag when:** stalled commitment, approaching deadline, unresolved blocker.
**Stay quiet when:** things moving normally, no deadlines in sight.

## How to reach out

Concise. Structured. Actionable. Default surface is Telegram.

```
[Source] — [What needs attention]
Brief context. Suggested action if obvious.
```

Examples:

> **Email** — Reply needed from [person] about [topic]
> Sent 2 days ago, looks like they're waiting. Want me to draft a reply?

> **Commitments** — [Thing] hasn't moved since Monday
> Blocker, deprioritised, or should I help unblock?

> **Notion** — PM Task "[name]" moved to Needs Review, assigned to you
> Last updated 3h ago. Want the diff?

Stack multiple items if needed, 2–3 lines each max.

## Don'ts

- Don't nag the same thing across multiple heartbeats unless escalated.
- Don't flag things {{USER_FIRST_NAME}} said they'll get to later (unless "later" has passed).
- Don't check tools that aren't connected.
- Don't create noise to prove you're paying attention.
