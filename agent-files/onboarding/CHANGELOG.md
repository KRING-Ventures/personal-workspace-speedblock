# CHANGELOG — Personal Workspace Framework

*One dated entry per version ship. Each entry tells an OpenClaw agent what changed and — if any personal-layer state cleanup is required — points at the migration file that walks through it.*

The current framework version lives in `onboarding/STATE_VERSION`. Each OpenClaw agent's repo records its last-synced version in its own `STATE_VERSION` file at the repo root. The session-boot rule in `AGENTS.md` describes how the comparison and catch-up runs.

## Entry format

```
## <version>  ·  shipped <YYYY-MM-DD>

**What shipped:**
- short bullet
- short bullet

**Personal-layer state changes required:** yes | no
- If yes: see `MIGRATIONS/<version>-<slug>.md` for the explicit cleanup steps.
```

---

## 0.1-beta  ·  shipped 2026-04-23

**What shipped:**
- Initial beta framework: SOUL, AGENTS, KRING, HEARTBEAT, IDENTITY, USER, TOOLS, MEMORY, templates, BOOTSTRAP.
- Tools-first BOOTSTRAP ordering (wire tools → pull drafts → validate with user).
- Renamed product "Workspace Beta" → "Personal Workspace".
- Shared framework now lives at `personal-workspace-speedblock/agent-files/`.
- Personal layer is each user's own private repo (name of their choice) — no KRING-managed per-pilot repos.

**Personal-layer state changes required:** no
- No prior beta versions existed; this is the first shipped version.
