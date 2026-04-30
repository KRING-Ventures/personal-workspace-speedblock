# Personal Workspace — Terms

The shared vocabulary for working with agents and with each other. Most of these come from software development but apply anywhere we treat work as versioned, reviewable changes.

If a teammate or your assistant uses one of these words, this is what they mean.

---

## Repository (repo)
A folder of files tracked by Git, usually living on GitHub. Code, docs, framework configs — anything shared across people or versions lives in a repo.

## Branch
A parallel copy of the repo where you can work without affecting what others see. You make a branch, do your changes, and either merge it back or throw it away. Like a draft on the side of the live document.

## Main branch
The branch everyone treats as the source of truth. Usually called `main`. Anything on `main` is real — shipped, agreed, in effect. You never edit it directly when working with others; you propose changes and merge them in.

## Commit
A saved snapshot of changes inside a branch. Each commit has a message describing what changed and why. Commits build up the history of a project — you can always go back to an earlier one.

## Pull request (PR)
A proposal to merge one branch into another (usually a feature branch into `main`). The PR is the place where the change is reviewed, discussed, and approved. When the PR is merged, the changes become part of `main`.

Pull request = "here's what I did, please review and merge."

## Merge
Combining one branch into another. After a PR is merged, the work is locked into `main` and visible to everyone.

## Work tree
Your local copy of the repo on disk — the actual files you're editing right now. You can have one work tree per branch you're working on. Useful when you want to work on two things in parallel without losing your place.

---

## Why these matter

Two reasons:

1. **You can ask your assistant for what you want, precisely.** "Open a PR" is unambiguous; "send me the change" is not.
2. **You can talk to your team without translation.** When someone says "I'll branch off main and PR it back," you know exactly what's happening.

For how to use these in practice, see [`best-practice.md`](./best-practice.md).

---

*Owned and maintained by KRING.*
