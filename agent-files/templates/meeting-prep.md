# Meeting prep template

Used by the **Meeting prep** job (`SCHEDULES.md`) ~30 min before a meeting, and for the one-line prep notes in the daily brief's *Calendar* section. Default surface: Slack.

Goal: everything {{USER_FIRST_NAME}} needs to walk in sharp, in well under a screen. Read-only — prep never schedules or sends anything.

Placeholders the agent fills:

- `[title]` — the meeting title.
- `[time]` — start time, user-local (e.g. *14:30*).
- `[attendees]` — who's in it (names; note anyone external).

```
🗓️ In ~30 min — [title] @ [time]

👥 Who: [attendees]

🧩 Context
- [Last thread / decision / where this stands — 1–2 lines]
- [Any open commitment or question tied to these people]

🎯 Your angle
- [What {{USER_FIRST_NAME}} likely wants out of this — the decision, the ask, the outcome]

📎 Handy
- [Doc / link / number worth having open, if any]
```

Rules:
- **Pull real context only.** Last email thread with the attendees, project status, open "waiting-on" items, the calendar description. If there's genuinely nothing to add, send a one-liner ("In ~30 min: [title] with [who] — no prior thread on file") rather than padding.
- **Name external attendees.** If someone outside the venture is on it, flag it — tone and prep differ.
- **One prep per meeting.** Log the event ID in today's `memory/YYYY-MM-DD.md` so the 15-min job doesn't re-send.
- **Morning-pass version is shorter.** In the daily brief, collapse this to a single line per meeting: `HH:MM — [title] ([who]) — [the one thing to know]`.
- Use the user's primary language (from `USER.md`) for user-facing prep text. Keep meeting titles, names, and source quotes in their original language when that is clearer.
- Never send a reply, accept/decline, or move the meeting from a prep — that's the calendar's job and follows the `## Action rules` permission model.
