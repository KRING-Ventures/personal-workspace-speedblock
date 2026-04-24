# MIGRATIONS

*Per-version migration notes. One file per version that requires per-user state changes when an OpenClaw agent catches up.*

**File name:** `<from>-to-<to>.md` — e.g. `0.1.0-to-0.2.0.md`.

**Contents:** explicit instructions an OpenClaw agent can follow at session boot to bring its per-user state up to current — what to add, remove, rename, or restructure. Plain language, one action per bullet.

**When you need one:** any version ship that *changes the shape* of a per-user file (IDENTITY / USER / TOOLS / MEMORY / STATE_VERSION). Pure framework-only changes (SOUL / AGENTS / KRING / templates) don't need a migration file — pulling the framework is enough.

---

*[No migrations yet — `0.1.0` is the first shipped version.]*
