# Updating an Agent to the Latest Version

The standard way to bring an **existing Personal Workspace agent** up to the current framework version — activate any new core capabilities, preserve everything personal, and tell the user what changed. This replaces the ad-hoc "you must update to the latest version…" message written by hand each time.

## Which path am I on?

- **Update (this file)** — an agent that is *already* Personal Workspace, on an older version, catching up to current. It has a PW `STATE_VERSION`; you're moving it forward.
- **First boot** — no `STATE_VERSION` at all → run `agent-files/onboarding/BOOTSTRAP.md`.
- **Repurpose** — real state but *never* was PW (no `STATE_VERSION`) → run `repurposing-an-existing-agent.md`.

## The load-bearing rule

**Preserve all per-user state. Activate the framework deltas. Tell the user what's new.** An update is *continuity plus new capability* — never a reset. Memory, `USER.md`, `automations/`, personality: untouched. Only the framework layer moves.

## Part A — Shipping the update (KRING, once per version)

A version only reaches agents if the trigger is real. When you ship:

1. **Finalise `CHANGELOG.md`** — move `[Unreleased]` into a dated `[x.y.z]` entry.
2. **Bump `agent-files/onboarding/STATE_VERSION`** to `x.y.z`. *This is the trigger.* If it stays behind, every agent compares its version to an unchanged number, sees no delta, and silently skips the whole update — the most common reason an update "didn't land."
3. **Update `README.md`** "Current version".
4. **Write a `MIGRATIONS/<from>-to-<to>.md`** only if per-user state shape changed (most updates don't need one).
5. **Tag** `git tag vx.y.z` and push the tag.

## Part B — The standard update prompt

Send this to an existing agent (or let it run at boot). It's the consistent version of the hand-written message — fill the two blanks:

> You're running an older version of the Personal Workspace framework. Pull the latest from `KRING-Ventures/personal-workspace-speedblock`, read your own `STATE_VERSION` against the framework's `agent-files/onboarding/STATE_VERSION`, and run the catch-up loop in `agent-files/AGENTS.md` for every version in between.
>
> Bring yourself fully current: read the `CHANGELOG.md` entries from your version onward, apply what's relevant to this user, and **actually register the jobs — don't just confirm you've read about them.** Use your `cron` capability to create or update all seven scheduled jobs (daily brief, inbox triage, weekly review, meeting prep, hourly heartbeat check, memory distill, weekly update check) and make sure the `HEARTBEAT.md` protocol is live. Reading the changelog is not the same as the job existing — if a job isn't in your actual `cron` list, create it now.
>
> **Preserve everything personal** — memory, `USER.md`, automations, our history. This is an upgrade, not a reset.
>
> When you're current, set your `STATE_VERSION` to the framework's value, log what you caught up to in today's memory, then reply with two things: (1) **what's new in plain language** — the capabilities I now have that I didn't before; and (2) **proof it's actually wired** — the list of `cron` jobs you now have registered, each with its schedule, plus confirmation the heartbeat is live. Don't tell me it's done until those jobs actually exist in your `cron` list.

## Part C — What the agent does

On the update session, the agent:

1. **Pulls** the latest framework.
2. **Runs catch-up** per `agent-files/AGENTS.md` → *How catch-up works*: reads `CHANGELOG.md` from its version onward, applies what fits this user, ignores cosmetic-only changes.
3. **Verifies core capabilities are active, not just described.** Checks its five `cron` jobs exist (self-heals missing ones per `AGENTS.md` → *Scheduled jobs*) and that the heartbeat is registered. A capability the framework documents but the runtime never scheduled is not a real capability.
4. **Preserves per-user state.** No re-interviewing, no clean-sheet intro, no duplicate jobs.
5. **Sets `STATE_VERSION`** to current and logs the catch-up in today's `memory/YYYY-MM-DD.md`.
6. **Tells the user what's new** — a short, feature-level "here's what I can now do" message, in the continuity tone from `repurposing-an-existing-agent.md` Part B. Cosmetic/wording updates stay silent; capability-level updates get one short message. *(This Part-C flow is the operator-triggered push — KRING already chose to ship it, so the agent applies and explains. The **weekly automatic check** instead asks before applying — see "The weekly update check" below.)* Required by the *"what's new" rule* in `agent-files/AGENTS.md` → *How catch-up works*.

## Verification checklist

After an update session, confirm:

- [ ] Agent's `STATE_VERSION` == framework `STATE_VERSION`.
- [ ] Five `cron` jobs present **in the runtime's actual `cron` list** (not just mentioned) and logged in `automations/AUTOMATIONS.md`.
- [ ] Agent reported that list back as proof — job names + schedules — rather than a bare "done".
- [ ] Heartbeat protocol active.
- [ ] Memory, `USER.md`, automations intact — nothing reset or duplicated.
- [ ] User received a short "what's new" message for capability-level changes.
- [ ] Today's memory log notes the version caught up to.

## The weekly update check (notify, then ask)

Catch-up runs at every session boot — but an agent only boots when the user opens a session, so a quiet user could go weeks without their agent ever noticing a new version. The **update check** job (`SCHEDULES.md`, Mondays ~09:00) closes that: once a week the agent pulls the framework on its own. If there's a new version, it does **not** silently apply it — it tells the user there's an update and what it adds, in plain language, and **asks whether to apply it now**. It only catches up once the user says yes; if they defer, it leaves their version untouched and re-offers next week.

This is deliberate. A version that auto-rolls out to everyone the moment it ships can put a whole fleet onto an unevaluated change at once — and the user never got to decide whether now is the right time to take that risk. The weekly check makes every update a *choice*: explained first, applied on consent.

The operator-sent prompt in Part B is the manual half — for when KRING has evaluated a version and wants to push it to a specific agent immediately rather than wait for that agent's weekly check.

## How the "what's new" rule is wired

Catch-up used to be fully silent (`agent-files/AGENTS.md`: *"Don't announce it. Just do it."*) — right for wording/cosmetic updates, wrong for capability-level ones, which is why a user could gain a morning brief and never be told. As of `1.0.0`, `AGENTS.md` → *How catch-up works* keeps silent auto-apply for cosmetic/mechanical changes, but for any change a user can see or use it **explains the update and asks before applying** — at boot and via the weekly check alike. Cosmetic stays invisible; capability-level changes are always a user choice.
