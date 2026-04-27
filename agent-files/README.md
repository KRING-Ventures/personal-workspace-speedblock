# Personal Workspace — OpenClaw Agent File Set (shared layer)

The **shared framework layer** for every personal OpenClaw assistant. Lives at `personal-workspace-speedblock/agent-files/` (this directory).

## What this is

The **shared** file set that ships identically with every personal OpenClaw agent — framework content (KRING context, SOUL, AGENTS, BOOTSTRAP, HEARTBEAT, memory templates, working templates) plus the per-user blueprint files (IDENTITY, USER, TOOLS, automations/) used when a new agent is instantiated.

**Personal context does not live here.** Each user's personal layer lives on their own runtime's local filesystem — not in a separate GitHub repo. The OpenClaw runtime assembles both layers — shared (this set, read from GitHub) + personal (local files) — at session boot.

This is not the agent runtime. The runtime is OpenClaw; this is the file layer OpenClaw reads.

## Layout

One flat set of canonical templates. Files marked **(per-user)** are blueprints seeded into each runtime's local working directory at deployment and filled by the assistant during the first conversation; everything else ships identically.

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
templates/
├── daily.md           # morning brief
├── weekly.md          # Monday morning brief
├── email-draft.md     # email drafting structure
└── example-daily.md   # example shape for a memory/YYYY-MM-DD.md daily log
automations/
└── AUTOMATIONS.md     # index of built automations  (per-user)
```

## Where state lives

- **Shared framework** — this directory, in GitHub at `KRING-Ventures/personal-workspace-speedblock`. The agent reads from it at session boot to pick up template content and version updates.
- **Per-user state** — `IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/`, the user's own `MEMORY.md` and `memory/` — lives on the OpenClaw runtime's local filesystem, seeded from the per-user blueprints in this set at deployment. The agent writes there freely; it does **not** push back to a per-user GitHub repo.

There is no per-user GitHub repo for state. Cross-session continuity is handled by the runtime's durable filesystem.

Personal context never sits alongside shared framework content.

## Agent layers

- **Personal OpenClaw assistant** — one per user. Built on this framework + the runtime's local per-user state.

## Skills

Not in this repo. Skills live in the shared KRING claw repo at https://github.com/KRING-Ventures/claw-shared (private). Each agent loads skills on demand; non-default scopes are recorded in that user's local `TOOLS.md`.

## GitHub access

The agent reaches GitHub for two distinct things:

- **Reading the framework** at `KRING-Ventures/personal-workspace-speedblock` — for templates and version catch-up. This is read-only.
- **Reading and working in the user's own code repos** — with the user's permission, the agent can act as a tool surface here (open PRs, read code, draft changes). Granted via `TOOLS.md`.

The agent does *not* push per-user state to GitHub. State is local. See `AGENTS.md` § *Where state lives* for the operational rules.

## Instantiation flow (per agent)

At deployment:

1. The OpenClaw runtime reads the shared framework from `personal-workspace-speedblock/agent-files/`.
2. The runtime seeds its local working directory with the per-user blueprints (`IDENTITY.md`, `USER.md`, `TOOLS.md`, `automations/AUTOMATIONS.md`, empty `MEMORY.md`, empty `memory/`, `STATE_VERSION`). Blueprints carry `{{FROM_BOOTSTRAP}}` markers — the assistant fills those during the first conversation.
3. **First live session:** the assistant runs `onboarding/BOOTSTRAP.md` as a dialogue with its user. The assistant fills its own `USER.md`, confirms its `IDENTITY.md` (agent name / vibe / emoji), and wires `TOOLS.md`. Seeds `MEMORY.md` and today's `memory/YYYY-MM-DD.md`. Sets its own `STATE_VERSION` to the framework's current value.
4. **Subsequent sessions:** the assistant runs the onboarding catch-up loop in `AGENTS.md` — reading the framework, comparing `STATE_VERSION` values, and reading any `MIGRATIONS/` notes for versions it's behind. BOOTSTRAP is the zeroth migration; the top-level `CHANGELOG.md` + `onboarding/MIGRATIONS/` cover every version after.

**Placeholders.** Two kinds, both written as double curly braces:

- `{{AGENT_NAME}}` and `{{USER_FIRST_NAME}}` — filled by the OpenClaw runtime at deployment from the venture's intake. Already in place by the time the assistant boots.
- `{{FROM_BOOTSTRAP}}` — filled by the assistant itself during its first conversation with the user. Never by a central operator. Anywhere a per-user file says `{{FROM_BOOTSTRAP}}`, that's the assistant's job to fill in BOOTSTRAP.

Templates (`templates/daily.md`, `templates/weekly.md`) use `[bracketed]` lowercase tokens (e.g. `[weekday]`, `[date]`, `[iso week]`) — those are filled by the assistant when it generates each brief, drawing on what it knows from the runtime, the user's `USER.md`, and the current date.

## Licence

MIT. See `LICENSE` in the repo root if/when added.
