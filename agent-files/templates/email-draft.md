# Email draft template

Used when {{AGENT_NAME}} drafts an email for {{USER_FIRST_NAME}} to review before sending. {{AGENT_NAME}} **never sends without explicit approval** — in both modes below, the output is a *draft*, never a sent message.

There are two modes:

- **Triage mode (scheduled, the default):** the *Inbox triage* job (`SCHEDULES.md`) drafts replies in bulk and stages them in the Gmail Drafts folder. {{USER_FIRST_NAME}} reviews and sends from Gmail. This is the ~95% path.
- **Interactive mode (on request):** {{USER_FIRST_NAME}} asks for a reply in chat; the agent presents the draft in Slack for live review (see *Presenting the draft*).

The *Draft structure* and *Drafting rules* below apply to both.

## Triage mode — staging drafts in Gmail

This is what the *Inbox triage* job runs every 30 minutes. For each unread email:

1. **Can I answer it well?** If yes — write the reply to the *Draft structure / Drafting rules* below and **save it as a draft in Gmail** (reply-draft on the thread, so it threads correctly). Aim to cover ~95% of mail; if a reply needs {{USER_FIRST_NAME}}'s judgment but is mostly there, draft what you can and flag it as *needs finishing touch*.
2. **Mark as read — only if drafted.** The moment a draft is staged for an email, mark that email read. This is the signal "handled, waiting on you." **Never mark an email read unless you've drafted a reply to it.**
3. **Leave the rest.** Anything you chose not to draft — a real decision, sensitive, missing information, or genuinely needs {{USER_FIRST_NAME}} — stays **unread**. Flag/label it so it stands out, and name it in the daily brief's *"Left for you"* list. Never bury it by marking it read.
4. **Don't re-draft.** Before drafting, check the thread doesn't already have a draft from a prior run. One draft per thread; update the existing one rather than stacking a second.
5. **Stay silent unless blocked.** Triage runs in the background. Only message {{USER_FIRST_NAME}} mid-day if a draft genuinely can't proceed without a decision now — otherwise everything is summarised in the 08:00 daily brief.

Invoices and similar actionables: if it's a "file / log / organise" item rather than a reply, handle per `playbook.md` (label, log, or route) and surface it under the brief's tasks/needs-attention — don't draft a reply that isn't needed.

## Draft structure

```
To: [recipient(s)]
Cc: [if any]
Subject: [concrete — not "following up"]

[Greeting — match {{USER_FIRST_NAME}}'s usual tone with this person]

[One-line context if needed — what this is about]

[The actual ask / update / response — direct, specific]

[Next step or call to action — who does what by when]

[Sign-off matching {{USER_FIRST_NAME}}'s style]
```

## Drafting rules

- **Match tone to relationship.** Check prior thread or recent correspondence. Don't default to formal.
- **Lead with the point.** No "I hope this email finds you well" unless {{USER_FIRST_NAME}} actually writes like that.
- **One ask per email.** If two things are needed, say so explicitly and number them.
- **Concrete subject lines.** "Carelog pricing — decision needed by Friday" beats "Following up".
- **Language.** Default to the user's primary language (from `USER.md`) unless the recipient writes in something else.
- **Attachments.** Name them in the body if relevant; never attach on {{USER_FIRST_NAME}}'s behalf without confirmation.

## Presenting the draft (interactive mode)

When {{USER_FIRST_NAME}} asked for a reply in chat, send the draft for review, wrapped like this:

```
Drafted reply to [recipient] — [one-line purpose]:

---
[full draft above]
---

Ready to send, or anything to change?
```

If multiple edits come back, re-present the clean version before sending — don't send a draft mid-revision.

## Never

- Send without explicit approval.
- Add recipients {{USER_FIRST_NAME}} didn't name.
- Fabricate context, deadlines, or commitments.
- Use "we" if {{USER_FIRST_NAME}} hasn't established it with this recipient.
