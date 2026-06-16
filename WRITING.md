# Writing Standard

Every user-facing page in this repo must pass this test before it ships.

## The test

1. **One job.** Can the reader tell what to *do* after 10 seconds of scanning?
2. **Plain.** Would someone outside KRING understand every sentence? No jargon.
3. **Selective.** Can any line be cut without losing the reader's job? If yes — cut it.
4. **One screen.** Does it fit without scrolling?

If any answer is *no*, it's not ready.

## The rule behind it

Write for the reader's *one job* — not to cover everything. Detail lives one click away in its own file, never dumped on the page.

KISS means: say the one thing clearly, in the fewest words that still land. Short but unclear fails too.

**When you ask someone to *do* something, give them enough to finish it** — where to go, what to get, how long it takes. Lean isn't starved. If those steps run long, keep the overview page short and move the detail into the relevant detail guide (e.g. the app-provisioning steps live inside `activation-kring.md`, not on the one-screen `activation.md`).

## Applies to

**First-read pages** — `buy-in.md`, `activation.md`. All four rules; keep each section to one screen (activation.md now carries two short parts — setup, then first conversation).

**Reference pages** — `playbook.md`. Rules 1–3 per section; you consult it, so it can run long, but every section must be scannable and answer one question fast.

**Internal guides** — `activation-kring.md`, runbooks. Built for precision during setup, not a first read. Rules 2–3 only.
