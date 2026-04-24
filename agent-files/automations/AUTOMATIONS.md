# AUTOMATIONS — {{AGENT_NAME}}

Index of automations built for {{USER_FIRST_NAME}}. One entry per automation. Built as requested, run inside the Basis stack.

## Standing rules

- **Every automation has a named owner** (typically {{USER_FIRST_NAME}}). If it breaks, someone is accountable.
- **Every automation has a rollback.** Reversibility before ship.
- **Every automation logs to MEMORY.md when built and when meaningfully changed.** Invisible automations that break silently are worse than no automation.
- **No automation sends messages to other humans without per-send confirmation** unless {{USER_FIRST_NAME}} explicitly grants standing permission and it's logged in `TOOLS.md` → Standing permissions.

## Automation index

*[None yet — populate as automations are built. Use the template below.]*

---

## Entry template

```markdown
### [Automation name]

- **What it does:** [one-line purpose]
- **Owner:** {{USER_FIRST_NAME}}
- **Built:** YYYY-MM-DD
- **Trigger:** [cron schedule / event / manual]
- **Surfaces touched:** [Gmail / Calendar / Drive / Notion / ...]
- **Human-in-loop:** [yes / no — if yes, at what step]
- **Rollback:** [how to disable or reverse]
- **Known failure modes:** [what breaks it, what to watch]
- **Last reviewed:** YYYY-MM-DD
```
