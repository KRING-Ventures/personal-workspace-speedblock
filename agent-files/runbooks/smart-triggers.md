# Smart triggers

Use smart triggers for high-frequency jobs where "no signal" must cost zero tokens and send no user-facing message.

## Contract

The architecture is:

```text
schedule -> smart trigger -> agent only if signal -> user channel only if useful
```

Never use this architecture for high-frequency silent work:

```text
schedule -> agent -> prompt says "stay silent"
```

Prompt-based silence is not a safety boundary. If the agent produces final text, the runtime may deliver it.

## Inbox triage gate

Runs every 30 minutes.

The gate may wake the agent only when at least one unread inbox thread is likely to need drafting or a same-day decision.

Gate checks:

1. Gmail unread inbox, excluding spam/trash and already-flagged/no-reply labels.
2. Skip threads that already have a draft.
3. Skip obvious newsletters, automated notices, product updates, and service announcements unless they match an urgent condition.
4. Wake the agent with `INBOX_TRIAGE_FIRE` only when there is real work.

No signal means:

```text
exit 0
```

No agent call. No Slack/Telegram message. No summary.

## Heartbeat gate

Runs during working hours.

The gate may wake the agent only for:

- commitment/deadline signal that needs attention now
- calendar-load issue such as conflict or heavy day with no focus/lunch
- email only if immediate and high-consequence: same-day human decision, deadline within 24 hours, account lockout/security compromise, payment failure, or today's calendar impact

Heartbeat must not wake for general unread email. General email belongs to inbox triage and the daily brief.

## Output rule

If a smart trigger wakes the agent and the agent later finds the signal is no longer useful, the agent returns:

```text
HEARTBEAT_OK
```

The runtime wrapper must treat that as no visible user message.

## Logging

Log internally:

- when a signal was found
- when the same signal is skipped because of cooldown
- errors that need operator attention

Do not log empty "nothing happened" summaries to the user channel.
