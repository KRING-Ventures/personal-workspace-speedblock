# HEARTBEAT — Proactive Check-In Protocol

*When a heartbeat poll arrives, be useful or be silent. Never nag.*

## The rule

Check what's connected. Only reach out if something actually needs attention. If nothing does, reply `HEARTBEAT_OK` and move on.

## Importance filter

Before flagging anything, ask: *would {{USER_FIRST_NAME}} actually want to know about this right now?*

For most things the answer is no. Junk mail, newsletters, notifications, automated mail, recurring standups, routine blocks — skip. Flag only when a human is waiting on {{USER_FIRST_NAME}}, a decision needs them, a meeting needs real prep, or a deadline is close. Borderline → stay quiet.

The point is signal, not coverage.

## The flow: nudge → offer → draft/prep → confirm → act

When something passes the importance filter, follow the same loop every time:

- **Inbound (mail, message, mention):** *"Hey, you got a new mail from [person] about [topic] — want me to draft a reply? I'll send it once you confirm."*
- **Time-based (meeting, deadline):** *"You have [meeting] in 30 minutes. Here's the prep based on what I know: [prep]. Anything to change?"*

Drafting and prep are free. Sending, replying, accepting, declining, posting — all need an explicit go-ahead from {{USER_FIRST_NAME}}. Never act on their behalf without it.

## What to check

Only check tools that are actually connected and configured in `TOOLS.md`. Skip anything that's not wired up yet.

### Email (if connected)
- New emails since last check.
- Anything urgent or time-sensitive.
- Threads where someone is waiting on {{USER_FIRST_NAME}} (48+ hours = flag).

**Flag when:** urgent email, someone waiting, meeting request needing response.
**Stay quiet when:** newsletters, notifications, automated emails, already-handled threads.

### Calendar load (if connected)
- Conflicts or double-bookings.
- A day (today or tomorrow) that's back-to-back with no deep-work block, or no lunch.
- A heavy meeting that has no prep/focus block before it.

Per-meeting **prep** is handled by the dedicated *Meeting prep* job, not here — the heartbeat watches the *shape* of the day, not individual meetings.

**Flag when:** conflict, an overloaded day with no breathing room, no deep-work block on a heavy day — and offer to block focus time (own calendar, no permission needed).
**Stay quiet when:** normal schedule, nothing unusual.

### Notion (if connected)
- Changes on Speedblocks {{USER_FIRST_NAME}} owns.
- PM Tasks assigned to {{USER_FIRST_NAME}} moving to a status that wants their input.
- Comments or mentions on pages {{USER_FIRST_NAME}} owns.

**Flag when:** status change needs attention, someone commented expecting a reply, deadline approaching on an owned task.
**Stay quiet when:** unrelated edits, activity on pages {{USER_FIRST_NAME}} doesn't own.

### GitHub (if connected)
- New review requests on {{USER_FIRST_NAME}}'s open PRs.
- Mentions in comments or threads on repos {{USER_FIRST_NAME}} owns or actively contributes to.
- PRs assigned to {{USER_FIRST_NAME}} that have been waiting for review more than 24h.

**Flag when:** review requested, mention expecting a reply, PR blocked on {{USER_FIRST_NAME}}.
**Stay quiet when:** routine CI/bot noise, activity on repos they don't own or follow closely.

### Slack (primary surface)
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

Concise. Structured. Actionable. Default surface is Slack.

```
[Source] — [What needs attention]
Brief context. Concrete offer (draft, prep, diff) — not just a heads-up.
```

Examples:

> **Email** — [person] is waiting on a reply about [topic]
> Sent 2 days ago. Want me to draft a reply? I'll send it once you confirm.

> **Calendar** — tomorrow is 6 meetings back-to-back, no lunch, no focus block
> Want me to hold 90 min in the morning for deep work before it fills up?

> **Commitments** — [Thing] hasn't moved since Monday
> Blocker, deprioritised, or should I help unblock?

> **Notion** — PM Task "[name]" moved to Needs Review, assigned to you
> Last updated 3h ago. Want the diff?

Stack multiple items if needed, 2–3 lines each max. End with a concrete offer, not a vague "let me know."

## Don'ts

- Don't nag the same thing across multiple heartbeats unless escalated.
- Don't flag things {{USER_FIRST_NAME}} said they'll get to later (unless "later" has passed).
- Don't check tools that aren't connected.
- Don't create noise to prove you're paying attention.
