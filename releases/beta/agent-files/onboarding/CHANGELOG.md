# CHANGELOG — Workspace Framework

*One dated entry per version ship. Each entry tells an OpenClaw agent what changed and — if any per-pilot state cleanup is required — points at the migration file that walks through it.*

The current framework version lives in `onboarding/STATE_VERSION`. Each OpenClaw agent's repo records its last-synced version in its own `STATE_VERSION` file at the repo root. The session-boot rule in `AGENTS.md` describes how the comparison and catch-up runs.

## Entry format

```
## <version>  ·  shipped <YYYY-MM-DD>

**What shipped:**
- short bullet
- short bullet

**Per-pilot state changes required:** yes | no
- If yes: see `MIGRATIONS/<version>-<slug>.md` for the explicit cleanup steps.
```

---

*[No entries yet — pre-beta scaffolding. First entry lands when Workspace Beta ships, with the full set of beta deliverables and any per-pilot migrations needed to come up from pre-beta.]*
