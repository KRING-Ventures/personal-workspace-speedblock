# Daily brief template

Used for {{AGENT_NAME}}'s morning brief to {{USER_FIRST_NAME}}. Default surface: Telegram.

Goal: one screen. Density over length. Skip anything not worth surfacing.

Placeholders the agent fills when generating each brief:

- `[weekday]` — today's weekday (e.g. *Monday*).
- `[day]` — today's day-of-month number only, no month or year and **not** the weekday (e.g. *8th*). With `[weekday]` this reads "Monday 8th".

The agent reads `USER.md` for the user's name and primary language and uses them naturally in the brief.

```
Good morning, [user] 🌞 It's [weekday] [day]

📅 Calendar
- HH:MM — [event] [prep note if <2h]
- HH:MM — [event]

🎯 Top focus
1. [Priority 1 — why it matters today]
2. [Priority 2]
3. [Priority 3]

✍️ Drafts ready to review ([N])
- [recipient] — [one-line purpose] [• needs your finishing touch, if partial]
→ All in your Gmail Drafts folder. Review and send when you're happy.

📨 Left for you ([M] — not drafted)
- [sender] — [why it needs you, in one line: judgment call / sensitive / missing info]

⏳ Still in Drafts from before
- [recipient] — [purpose] — drafted [when], not yet sent

⏰ Commitments touching today
- [What] — [owner] — [deadline / context]

✅ Tasks / reminders for today
- [Task or reminder]

📥 Other (messages, etc.)
- [Source] — [what, in one line]
```

Rules:
- Skip any section that's empty today. Don't fill for completeness.
- **Email is summarised, not pasted.** The drafts themselves live in the Gmail Drafts folder (per `templates/email-draft.md`) — the brief only *counts and names* them so {{USER_FIRST_NAME}} can go review and send. Never paste full draft bodies into the brief.
- **"Left for you" is the honesty check.** Every email the agent chose not to draft (judgment call, sensitive, missing info, needs {{USER_FIRST_NAME}}'s decision) is named here so nothing important hides. These stay unread/flagged in the inbox — they are never marked read.
- **"Still in Drafts from before"** surfaces any draft staged on a previous day that {{USER_FIRST_NAME}} hasn't sent yet — the day-after reminder so drafts don't rot unsent. Drop a draft from this list once it's sent or deleted.
- If the day has nothing meaningful to surface, say so plainly: "Clear runway today. Deep-work recommended."
- Use the user's primary language (from `USER.md`) for the user-facing text where sensible.
