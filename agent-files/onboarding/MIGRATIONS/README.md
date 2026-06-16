# MIGRATIONS

*Per-version migration **guidelines**. One file per version where a deployed OpenClaw agent should know about a change in its private files when it catches up. Guidance, not a script.*

**File name:** `<from>-to-<to>.md` (e.g. for a hypothetical 0.3.0 ship that renames a section in `USER.md`, the file would be `0.2.x-to-0.3.0.md`).

**Contents:** describe *what's changing and why* — fields renamed, sections restructured, files moved — in plain language, like a note from a colleague reviewing a PR. The agent reads it, decides what's relevant to its user's state, and applies only the parts that fit. The agent doesn't execute these mechanically.

**When you need one:** any version ship where a deployed agent should be aware that its private files (IDENTITY / USER / TOOLS / MEMORY / STATE_VERSION) need to know about a change. Pure framework-only updates (SOUL / AGENTS / KRING / templates) don't need a migration file — pulling the framework is enough.

**What migrations don't touch:** `memory/*.md` daily logs, `MEMORY.md` content, and `automations/AUTOMATIONS.md` content are the user's own — guidelines describe structural changes (file paths, naming) but never rewrite the user's actual content.

---

*Migrations on file:*
- `1.0.1-to-1.0.2.md` — boot-budget restructure (lean `AGENTS.md`, procedures → plain habits, `KRING.md` read on demand). Framework-only; the one action is re-applying any local edits to `AGENTS.md`/`SOUL.md` on top of the new lean structure.
