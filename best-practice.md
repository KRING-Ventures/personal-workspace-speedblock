# The 4 AI Commandments

Best practices for working with AI agents. Apply across drafting, planning, code, ops. Your agent follows them too, and will nudge you when you skip one.

**1. Make the agent repeat back your prompt.** *"Explain back to me what I just prompted, so we are aligned."* — Catches misunderstandings before they become rework.

**2. Work in small batches — save as you go.** *"Save and commit this work."* — Lock each piece in before starting the next; don't pile up large unsaved changes.

**3. KISS — keep it simple and understandable.** *"Avoid unnecessary words and fillers. Explain in a simple way."* — Plain beats clever. If you can't follow it on the first read, neither can the next person.

**4. In shared projects: work on a copy, then merge.** *"Branch off main."* — Don't edit `main` directly when others share the repo. Branch, change, propose, merge.

## Must-know vocabulary

- **Repo** — folder of files tracked by Git, usually on GitHub.
- **Branch** — a parallel copy of the repo where you can work without affecting others.
- **Main** — the source-of-truth branch. Anything on `main` is real; never edit directly when sharing.
- **Commit** — a saved snapshot of changes inside a branch.
- **Pull request (PR)** — proposal to merge one branch into another. Reviewed first, then merged.
- **Merge** — combining one branch into another. After merge, the work is on `main`.
- **Work tree** — your local copy of the repo on disk. One per branch you're working on.
