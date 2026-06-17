# Using shared skills (claw-shared)

How a Personal Workspace (PA) agent reaches the fleet's shared skill library and
pulls full skill instructions **on demand**. This is the concrete wiring behind
the `## Skills` section in `TOOLS.md`.

## The idea

Skills live in one shared repo — **`KRING-Ventures/claw-shared`** — not inside
each agent. A PA agent doesn't carry the skill bodies around; it carries a local
clone and lets OpenClaw load each skill **on demand**:

- At boot, the agent sees only every skill's **name + description**.
- The full `SKILL.md` body is read **the moment the agent decides a skill is
  relevant** to the task in front of it — never preloaded.

So the library can hold dozens of skills (growth + personal + fleet) and the
agent's context stays lean. New skills reach every PA agent by being merged to
`claw-shared` `master` and pulled — no agent change, no redeploy.

The `personal/` category in claw-shared is the one built for PA agents (daily
brief, meeting prep, inbox triage, …). The agent can also reach the growth and
fleet skills when a task genuinely calls for them.

## Where the index lives (and why not in agent files)

There are two indexes, and **neither is copied into the agent's own files** —
that would just drift:

1. **The live index** is automatic. OpenClaw exposes every shared skill's name +
   description to the agent at boot, straight from the local clone. This is what
   the agent actually scans to decide what to fetch — it's always exactly in sync
   with the clone, no daily copy job needed.
2. **The human-readable catalog** is `claw-shared/skills/INDEX.md`, generated
   from frontmatter. The agent reads it *from its clone* (`~/claw-shared/skills/
   INDEX.md`) when it wants the full browsable list.

Both stay current by the same one mechanism: the nightly `git pull`. We
deliberately **don't** maintain a second copy of the index inside the agent's
workspace — one source of truth (the clone), pulled daily, beats two that
disagree.

## One-time wiring (per PA agent host)

KRING sets this up when the agent is provisioned (PA agents are KRING-assisted,
not self-serve).

1. **Clone the library** next to the agent's workspace, on stable storage:

   ```bash
   git clone https://github.com/KRING-Ventures/claw-shared.git ~/claw-shared
   ```

2. **Point the skill loader at it** in `openclaw.json` (`skills.load.extraDirs`):

   ```json
   "skills": {
     "load": {
       "extraDirs": ["/root/claw-shared/skills"]
     }
   }
   ```

   The loader exposes every `SKILL.md` by its flat frontmatter `name`, at any
   folder depth — so `skills/personal/daily-brief/SKILL.md` is just the
   `daily-brief` skill. No per-skill config.

3. **Restart the gateway** so the skills register.

4. **Verify**: ask the agent "what skills do you have?" — `daily-brief` and the
   shared catalog should appear. The `fleet-test` skill exists to confirm shared
   loading works.

## Keeping it fresh

A nightly `git pull` in `~/claw-shared` keeps the agent current; a merge to
`master` ships a skill to every PA agent on its next pull. Wire it as a cron /
automation (see `building-automations.md`):

```bash
cd ~/claw-shared && git pull --ff-only
```

## Adding or changing a skill

Don't edit skills inside an agent. Propose them in `claw-shared` — branch, PR,
Corey reviews, merge to `master`. See `claw-shared/CONTRIBUTING.md` for the
authoring rules and `skills/INDEX.md` for the catalog.

## Boundaries

- Treat `~/claw-shared` as **read-only** from the agent's side — pull, never
  push local edits. Changes go through the claw-shared PR flow.
- A PA agent loads shared skills; it does not get write access to other people's
  workspaces or data through them.
