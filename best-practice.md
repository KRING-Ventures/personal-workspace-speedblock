# The 4 Commandments

Best practices for working with AI agents.

These four apply across everything: drafting, planning, code, ops. Your assistant follows them too, and will nudge you when you're skipping one.

For the vocabulary used below (branch, pull request, etc.), see [`terms.md`](./terms.md).

---

## 1. Make the agent repeat back your prompt

When you ask for something non-trivial, have the agent restate what you want before it starts. Read what comes back. If it's wrong, correct it now — not after work has been built on a misunderstanding.

> "Explain back to me what I just prompted, so we are aligned."

This is the single biggest output-quality lever. Ten seconds up front saves an hour of debugging the wrong thing.

---

## 2. Work in small batches — and save as you go

Don't let work pile up unsaved. Pick the next small thing, do it, lock it in, then move on.

> "Save and commit this work."

For code, that means a commit pushed to a branch. For docs, that means saved and shared where it sticks. For decisions, that means written down where the team can find it later. Skip the lock-in step and work gets lost, gets overwritten, gets forgotten.

---

## 3. KISS — keep it simple and understandable

Ask for plain, simple work. Tell the agent when you don't want it to over-explain or pad output with filler. The same goes for what you write in chat: less context-stuffing, clearer asks.

> "Avoid unnecessary words and fillers. Explain in a simple way."

Simple beats clever. If you can't follow it on the first read, neither can the next person.

---

## 4. In shared projects: work on a copy, then merge it

If you're sharing a project with other humans or agents, don't edit the live shared state in place. Make a copy, change the copy, propose the merge.

> "Branch off main."

In code, that's a branch + pull request into `main`. The same principle applies anywhere shared: copy, change, propose, merge — never overwrite live shared state without a review step.

---

*Owned and maintained by KRING.*
