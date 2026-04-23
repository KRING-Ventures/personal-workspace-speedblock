# Email draft template

Used when {{AGENT_NAME}} drafts an email for {{USER_FIRST_NAME}} to review before sending. {{AGENT_NAME}} never sends without explicit approval.

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
- **Language.** Default to {{USER_PRIMARY_LANGUAGE}} unless the recipient writes in something else.
- **Attachments.** Name them in the body if relevant; never attach on {{USER_FIRST_NAME}}'s behalf without confirmation.

## Presenting the draft

Send the draft to {{USER_FIRST_NAME}} for review, wrapped like this:

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
