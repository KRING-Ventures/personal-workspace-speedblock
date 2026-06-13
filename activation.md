# Personal Workspace — Activation

How a venture gets deployed onto Personal Workspace. Roughly **~5 business days** end to end.

Three stages: **you set things up** → **KRING builds and wires the agents** → **each user gets onboarded by their agent in ~15 minutes**.

> This flow is under active refinement — treat the lane split as a working draft.

---

## Stage 1 — Provisioning (~1 day, venture-led)

**1. Speedblock activation**
Set the seat count in Cosmica and accept the terms and pricing.

**2. Invoicing & agreement**
KRING invoices the venture and the agreement is signed.

**3. Provide agent names**
Name each agent — one per seat — and submit to KRING. One name per user; that becomes the agent's identity throughout the product.

---

## Stage 2 — Setup (~3–4 days, KRING-led)

KRING builds and wires each agent during this stage. You don't need to manage the technical steps — your job here is to set up the accounts and grant KRING the access needed to wire everything in.

**4. Set up the mandatory tech stack**
Subscribe to the required tools and create user accounts before KRING can wire the agents. See "Required tech stack" below.

**5. Grant KRING access**
Give KRING the credentials and permissions needed per tool. KRING will specify exactly what's needed when they start setup.

---

## Stage 3 — Onboarding (~15 min per user, agent-led)

**6. Access handover**
KRING gives each user access to their agent — the Slack channel plus a verification step to confirm identity.

**7. User onboarding**
Each agent runs its own first conversation with the user. No KRING involvement needed from here. Full flow in `onboarding.md`.

---

## Required tech stack

Each user needs these in place before Stage 2 can complete:

- **Google Workspace** (Gmail, Calendar, Drive, Docs, Meet) — one Workspace account per user; personal `@gmail.com` won't work.
- **Slack** — team communication and the surface each user talks to their agent on.
- **ChatGPT** — the LLM OpenClaw runs on.

See `playbook.md` for the full recommended tech stack.

---

## References

- `onboarding.md` — the agent-led first conversation each user goes through (Stage 3).
- `playbook.md` — Personal Workspace day-to-day: tool stack, working rhythm.
- `activation-kring.md` — KRING-internal setup guide with the full wiring detail for Stages 2–3.
- `ai-commandments.md` — the 4 AI Commandments and must-know git vocab.
