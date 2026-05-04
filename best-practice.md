# The 4 Commandments

Best practices for working with AI agents — plus the must-know vocabulary that goes with them.

The four practices below apply across everything: drafting, planning, code, ops. Your assistant follows them too, and will nudge you when you're skipping one. The glossary at the bottom is the shared vocabulary that makes the practices precise — most of it comes from software development but applies anywhere we treat work as versioned, reviewable changes.

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

## Glossary

The shared vocabulary for working with agents and with each other. If a teammate or your assistant uses one of these words, this is what they mean.

### Repository (repo)
A folder of files tracked by Git, usually living on GitHub. Code, docs, framework configs — anything shared across people or versions lives in a repo.

### Branch
A parallel copy of the repo where you can work without affecting what others see. You make a branch, do your changes, and either merge it back or throw it away. Like a draft on the side of the live document.

### Main branch
The branch everyone treats as the source of truth. Usually called `main`. Anything on `main` is real — shipped, agreed, in effect. You never edit it directly when working with others; you propose changes and merge them in.

### Commit
A saved snapshot of changes inside a branch. Each commit has a message describing what changed and why. Commits build up the history of a project — you can always go back to an earlier one.

### Pull request (PR)
A proposal to merge one branch into another (usually a feature branch into `main`). The PR is the place where the change is reviewed, discussed, and approved. When the PR is merged, the changes become part of `main`.

Pull request = "here's what I did, please review and merge."

### Merge
Combining one branch into another. After a PR is merged, the work is locked into `main` and visible to everyone.

### Work tree
Your local copy of the repo on disk — the actual files you're editing right now. You can have one work tree per branch you're working on. Useful when you want to work on two things in parallel without losing your place.

### Why these matter

Two reasons:

1. **You can ask your assistant for what you want, precisely.** "Open a PR" is unambiguous; "send me the change" is not.
2. **You can talk to your team without translation.** When someone says "I'll branch off main and PR it back," you know exactly what's happening.

---

*Owned and maintained by KRING.*
