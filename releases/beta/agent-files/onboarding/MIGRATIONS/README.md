# MIGRATIONS

*Per-version migration notes. One file per version that requires per-pilot state changes when an OpenClaw agent catches up.*

**File name:** `<version>-<short-slug>.md` — e.g. `beta-2026-04-30-pa-hardcode.md`.

**Contents:** explicit instructions an OpenClaw agent can follow at session boot to bring its per-pilot state up to current — what to add, remove, rename, or restructure. Plain language, one action per bullet.

**When you need one:** any version ship that *changes the shape* of a per-pilot file (IDENTITY / USER / TOOLS / MEMORY / SPEEDBLOCKS / STATE_VERSION). Pure framework-only changes (SOUL / AGENTS / KRING / templates) don't need a migration file — pulling the framework is enough.

---

*[No migrations yet — pre-beta scaffolding.]*
