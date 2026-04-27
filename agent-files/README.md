# Personal Workspace — OpenClaw Agent File Set (shared layer)

The **shared framework layer** for every personal OpenClaw agent — KRING-internal users and venture deployments alike. Lives at `personal-workspace-speedblock/agent-files/` (this directory).

## What this is

The **shared** file set that ships identically with every personal OpenClaw agent — framework content (KRING context, SOUL, AGENTS, BOOTSTRAP, HEARTBEAT, memory templates, working templates) plus the per-user blueprint files (IDENTITY, USER, TOOLS, automations/) used when a new agent is instantiated.

**Personal context does not live here.** Each user's personal layer lives in their own private repo. The OpenClaw runtime assembles both layers — shared + personal — at session boot.

This is not the agent runtime. The runtime is OpenClaw; this is the file layer OpenClaw reads.

## Layout

One flat set of canonical templates. Files marked **(per-user)** are blueprints cloned into the user's private repo and personalised; everything else ships identically.

```
SOUL.md                # character, boundaries, voice
AGENTS.md              # session boot, memory, permissions, onboarding rule
HEARTBEAT.md           # proactive check-in protocol
KRING.md               # KRING org context (the entity)
MEMORY.md              # long-term memory template
IDENTITY.md            # name, role, vibe, emoji  (per-user)
USER.md                # user profile, filled during BOOTSTRAP  (per-user)
TOOLS.md               # what's actually wired up  (per-user)
onboarding/
├── BOOTSTRAP.md       # first-session dialogue (zeroth migration)
├── STATE_VERSION      # current framework version
└── MIGRATIONS/        # per-version per-user cleanup notes (empty unless a version changes per-user state)
memory/
└── 2026-04-22.md      # example daily log
templates/
├── daily.md           # morning brief
├── weekly.md          # Friday EOD brief
└── email-draft.md     # email drafting structure
automations/
└── AUTOMATIONS.md     # index of built automations  (per-user)
```

## Private per-user repos

Each user's **personal layer** — `IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/`, their own `MEMORY.md` + `memory/` — lives in an independent **private** repo they create themselves. Name it whatever you want; the OpenClaw runtime reads both layers regardless of repo name.

Personal context never sits alongside shared framework content.

## Agent layers

- **Personal OpenClaw agent** — one per user. Built on this framework + the user's private repo. Applies to KRING-internal users and venture deployments alike.
- **Cosmo** — the shared KRING-org OpenClaw agent. One instance for KRING the organisation. Runs in `/root/clawd/`. Not this file set. KRING-internal only — ventures don't get Cosmo.

## Skills

Not in this repo. Skills live in the shared KRING claw repo at https://github.com/KRING-Ventures/claw-shared (private). Each agent loads skills on demand; non-default scopes are recorded in that user's private `TOOLS.md`.

## GitHub is the source of truth

Both layers — shared framework and each user's personal repo — live in GitHub. Local filesystem state is a working mirror, not canonical.

- Agents **pull at session start** so they're running against the latest framework and latest personal state.
- Agents **push after every meaningful change** — memory logs, `MEMORY.md`, `USER.md`, `TOOLS.md`, automations. Never leave uncommitted work.
- GitHub is each agent's **cross-session continuity** mechanism — if it isn't pushed, the next session doesn't see it. *Not* a per-user backup story; Syncthing-to-local is on the roadmap for that.

See `AGENTS.md` for the operational rules.

## Instantiation flow (per agent)

At OpenClaw runtime, both layers are assembled:

1. Clone the `personal-workspace-speedblock` repo and read from `agent-files/` — all framework + blueprint files.
2. Clone the user's own private repo — personal files (already seeded with `{{FROM_BOOTSTRAP}}` markers).
3. **First live session:** the OpenClaw agent runs `onboarding/BOOTSTRAP.md` as a dialogue with its user. The agent fills its own `USER.md`, confirms its `IDENTITY.md` (agent name / vibe / emoji), and wires `TOOLS.md`. Seeds `MEMORY.md` and today's `memory/YYYY-MM-DD.md`. Sets its own `STATE_VERSION` to the framework's current value.
4. **Subsequent sessions:** the agent runs the onboarding catch-up loop in `AGENTS.md` — pulling framework + each subscribed Speedblock, comparing STATE_VERSION values, and running any MIGRATIONS for versions it's behind. BOOTSTRAP is the zeroth migration; the top-level `CHANGELOG.md` + `onboarding/MIGRATIONS/` handle every version after.

Placeholders (`{{AGENT_NAME}}`, `{{USER_FIRST_NAME}}`, etc.) use double curly braces. `{{FROM_BOOTSTRAP}}` markers are filled **by the OpenClaw agent, during its own first session** — never by a central operator.

## Licence

MIT. See `LICENSE` in the repo root if/when added.
