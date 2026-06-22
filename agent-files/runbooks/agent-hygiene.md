# Agent hygiene

Run this weekly to keep the agent's files small, readable, and reliable.

The goal is not to "delete old stuff." The goal is to keep boot files lean, memory curated, raw history archived, and generated files out of the root workspace.

## When it runs

Default schedule: weekly, after the update check.

Run silently unless:

- `openclaw doctor` reports truncation or another boot-budget problem
- a cleanup decision needs the user's judgment
- the cleanup changes something the user can see or use
- the agent cannot safely continue without help

## Best-practice rules

1. **Boot files stay essential-only.** `AGENTS.md`, `SOUL.md`, `HEARTBEAT.md`, and `SCHEDULES.md` should contain only what the agent needs every session. Long procedures go in `runbooks/`.
2. **`MEMORY.md` is curated.** Keep long-term facts, decisions, patterns, preferences, and open threads. Do not let raw logs, transcript fragments, or repeated summaries accumulate there.
3. **Daily logs are raw, then distilled.** `memory/YYYY-MM-DD.md` can be detailed. The daily/weekly distill should promote the useful parts and leave the raw log as history.
4. **Generated files do not live in the root.** Audio, screenshots, exports, one-off outputs, and scratch files go in `out/`, `logs/`, or `trash/`.
5. **Archive, don't destroy.** Use `trash/` with dated names for old versions or uncertain cleanup. Never hard-delete personal state during hygiene.
6. **One home per rule.** If a rule appears in multiple boot files, keep the canonical version and replace duplicates with a pointer.
7. **Recommendations explain the standard.** Users are not expected to know agent-file best practice. When asking for a decision, state the recommended action and why.

## Weekly checklist

1. Run:

```bash
openclaw doctor
```

2. Check the largest files:

```bash
du -ah . | sort -h | tail -40
```

3. Check root clutter:

```bash
find . -maxdepth 1 -type f | sort
```

4. Inspect `MEMORY.md` for raw fragments, repeated promoted-memory blocks, stale open threads, and outdated decisions.

5. Inspect today's and yesterday's daily logs only when needed to confirm whether memory was already distilled.

6. Move long procedures from boot files into `runbooks/`, then leave short pointers in the boot files.

7. Move generated/scratch files out of the root:

- `out/` for exports and generated deliverables
- `logs/` for operational logs
- `trash/YYYY-MM-DD-...` for old versions or uncertain cleanup

8. Record meaningful cleanup in today's daily log. If an automation entry exists for agent hygiene, update its `Last reviewed` date.

## What the agent may do without asking

- run diagnostics and size checks
- move obvious generated/scratch files from root into `out/`, `logs/`, or dated `trash/`
- compact `MEMORY.md` when the raw material is already represented in daily logs or runbooks
- move duplicated procedure detail from boot files into a runbook, preserving the rule as a pointer
- update today's daily log with a short record of the cleanup

## What requires asking first

- deleting anything permanently
- removing information when there is no obvious surviving source
- changing scheduled-job behavior beyond self-healing the standard jobs
- editing files outside the agent workspace
- changing user-visible behavior or recommendations

## User-facing wording when action is needed

Use this shape:

```text
I found [specific issue]. Recommended fix: [action]. Reason: [one sentence best-practice rule]. Good to apply?
```

Example:

```text
I found raw transcript fragments accumulating in MEMORY.md. Recommended fix: move the raw block to a dated archive runbook and keep only the durable decisions in MEMORY.md. Reason: MEMORY.md should be curated long-term memory, not raw history. Good to apply?
```

## Success state

- `openclaw doctor` is clean, or any warning has a clear next action
- boot files contain rules, not long procedures
- `MEMORY.md` is readable and curated
- raw logs remain available in `memory/`
- generated files are not cluttering the root workspace
- no permanent deletion happened
