# Harvesting Improvements into the Framework

How KRING turns real-use corrections — logged by agents in their `feedback/IMPROVEMENTS.md` ledgers — into permanent fixes in the template files. This is the **agent → repo** channel: the counterpart to the update flow that pushes the framework repo → agent.

## Why this exists

Every agent collects corrections as it runs (see `agent-files/feedback/IMPROVEMENTS.md` and `AGENTS.md` → *Capturing fixes*). A fix made on one agent helps that user immediately — but the *next* agent deployed still ships with the same gap unless the learning is promoted into the template. This runbook is that promotion step. Without it, the same bug gets re-fixed by hand on every agent forever.

## Cadence

Operator-run, not a per-agent cron — the harvest reads *across* agents, which no single agent can do. Run it on a regular beat (e.g. with each version cycle, or monthly), and any time you're already shipping a framework update.

## The loop

1. **Collect.** Gather each agent's `feedback/IMPROVEMENTS.md`. (Pull from each runtime, or read via its Syncthing mirror.) You only care about entries with **`Type: framework`** and **`Status: open`** — skip `personal` (those belong to that user alone) and anything already `promoted`.

2. **Cluster.** Group the open `framework` entries by what they touch — several agents reporting "didn't surface my calendar invite" is **one** framework fix, not five. The cluster size is also the signal: the same gap hit by many agents is high-priority.

3. **Decide.** For each cluster, make the call the agent couldn't:
   - **Promote** — a genuine framework gap/bug → fix the template.
   - **Reclassify as personal** — on review it's really one user's preference → leave it local, mark the entry so it isn't re-surfaced.
   - **Wontfix** — intentional behaviour or out of scope → record why.

4. **Apply to the templates.** Make the fix in the real files (`BOOTSTRAP.md`, `HEARTBEAT.md`, `runbooks/`, `scripts/`, etc.), guided by each entry's **Maps to** field. Add a `CHANGELOG.md` entry. If the change alters per-user state shape, write a `MIGRATIONS/<from>-to-<to>.md`. Follow `runbooks/updating-an-agent.md` → Part A to ship it (bump `STATE_VERSION`, tag).

5. **Close the loop.** Mark the harvested entries `Status: promoted <PR/commit>` so they aren't picked up again. The fix now reaches every agent the normal way — via catch-up (`updating-an-agent.md`) — including, eventually, the agents that reported it.

## Rules

- **`personal` never gets promoted.** The classification is the firewall between "this user likes X" and "the framework should do X." If a `personal` entry looks like it should be framework, reclassify it deliberately in step 3 — don't promote it silently.
- **Cluster before fixing.** One template change per real gap, however many agents reported it.
- **Always leave a trail** — `CHANGELOG.md` entry + the entries marked `promoted`. A fix that lands in the templates with no record is how the same thing gets "fixed" twice.
- **Don't edit an agent's ledger beyond status.** It's that agent's record; you update `Status` (and reclassify `Type` with a note), nothing else.

## Surfacing (optional)

To keep ledgers from rotting unharvested, an agent's weekly `agent-hygiene` job (`SCHEDULES.md`) may note when it's accumulated several open `framework` entries — a quiet "ready to harvest" signal to whoever's running this loop. Keep it light; the harvest itself stays operator-driven.
