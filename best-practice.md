# Personal Workspace — Best Practice for working with agents

How to get good work out of your AI assistant — and not lose it.

These four practices apply across everything: drafting, planning, code, ops. Your assistant follows them too, and will nudge you when you're skipping one.

For the vocabulary used below (branch, pull request, etc.), see [`terms.md`](./terms.md).

---

## 1. Make the agent restate the prompt before it acts

When you ask for something non-trivial, ask the agent to describe back what you want before it starts. Read what comes back. If it's wrong, correct it now — not after work has been built on a misunderstanding.

> "Before you do this, describe back what I'm asking for so we're aligned."

This is the single biggest output-quality lever. It costs ten seconds and saves an hour of debugging the wrong thing.

---

## 2. Save what matters

The chat thread is not the record. It can be lost, scrolled past, or end up in someone else's window.

- Decisions, commitments, and anything load-bearing → write it down where it sticks: your assistant's memory, the project's docs, Notion, the repo.
- Your assistant logs daily and keeps long-term memory automatically — but tell it explicitly when something matters: *"log this."*
- If a decision happens in chat with another person, write it down somewhere both of you can find it later.

---

## 3. Lock work in as you go, in small chunks

Don't run a long stream of work without checkpointing.

- Pick the next small thing.
- Work on it.
- **Push and lock it in.** For code, that's a commit and a pull request merged to `main`. For docs, that's saved and shared. For decisions, that's written down where the team can see.
- Then move to the next thing.

Skip the lock-in step and work piles up — gets lost, gets overwritten, gets forgotten. Especially when more than one person (or agent) is in the same project.

---

## 4. Use branches and pull requests when others share the project

If you're sharing a project with other humans or agents, never edit directly on `main`.

- Make a **branch** for the change you're about to do.
- Push it as a **pull request** — that's the ledger of what you did and why.
- Get it reviewed (or at least seen) before merging to `main`.
- After merge, start fresh from updated `main` for the next thing.

This is true for code in GitHub. The same principle applies anywhere shared: copy, change, propose, merge — don't overwrite live shared state in place.

---

*Owned and maintained by KRING.*
