# Daily brief template

Used for {{AGENT_NAME}}'s morning brief to {{USER_FIRST_NAME}}. Default surface: Telegram.

Goal: one screen. Density over length. Skip anything not worth surfacing.

Placeholders the agent fills when generating each brief:

- `[weekday]` — today's weekday (e.g. *Monday*).
- `[date]` — today's date (e.g. *2026-04-27*).

The agent reads `USER.md` for the user's name and primary language and uses them naturally in the brief.

```
Morning, [user]. [weekday] [date].

📅 Calendar
- HH:MM — [event] [prep note if <2h]
- HH:MM — [event]

🎯 Top focus
1. [Priority 1 — why it matters today]
2. [Priority 2]
3. [Priority 3]

⏰ Commitments touching today
- [What] — [owner] — [deadline / context]

📥 Needs attention
- [Source] — [what, in one line]
```

Rules:
- Skip any section that's empty today. Don't fill for completeness.
- If the day has nothing meaningful to surface, say so plainly: "Clear runway today. Deep-work recommended."
- Use the user's primary language (from `USER.md`) for the user-facing text where sensible.
