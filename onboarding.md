# Personal Workspace — User Onboarding

The agent-led first conversation. It starts the moment KRING hands the user access to their agent (Stage 3 of `activation.md`) and runs entirely through the agent.

**~16 min** for the core flow. The two optional steps — a first real task and a first automation — add up to ~30 min if the user wants them; either can be picked up later instead.

By the time onboarding starts, the agent's tools are already wired (KRING did this during activation). So this conversation is about the *relationship*, not setup: who the agent is, who the user is, how they'll work together.

The agent-side script for this flow is `agent-files/onboarding/BOOTSTRAP.md` — keep the two in step. A change here is a change there, and vice versa.

---

## 1. Welcome & intro *(agent, ~5 min)*

The agent introduces itself in one short, conversational message:

- **Who it is** — the user's personal AI agent, with memory across conversations.
- **What it can do** — brief, draft, prep meetings, track commitments, use the user's tools, build automations.
- **How to talk to it** — plain language; ask it to repeat back anything important.
- **What it won't do / its limits** — scoped to work; nothing sent or changed for other people without the user's OK.
- **When to use it** — day to day, for anything in the list above.

## 2. Gets to know you *(agent + user)*

The agent learns the basics and starts building the user's profile:

- Name and how to address them.
- Role and what they actually work on.
- Preferred wording / comms style — tone, length, formality.

It pulls what it can from the already-wired tools (name, email, timezone, title) and confirms rather than interrogates. Everything deeper builds over time from real work, not a day-one questionnaire.

## 3. Maps your needs *(agent + user, ~10 min)*

The agent maps how the user wants it to operate:

- **Proactivity & check-ins** — how forward it should be, when it should reach out.
- **Working hours & days** — so briefs, triage, and nudges land at the right times.
- **Biggest pains** — the recurring friction worth solving first (feeds step 5).
- **Any extra tools** the user wants wired beyond the standard stack.

This is where the agent quietly sets up the user's rhythm — morning brief, inbox triage, weekly review, meeting prep, heartbeat checks — anchored to the working hours mapped here.

## 4. First real task *(optional, agent + user, ~6 min)*

The agent walks the user through one real task, end to end — a showcase of a core capability. Pull a data point, answer a question from the user's own tools, draft something. One task, start to finish, so the user sees it work. Can always be done later.

## 5. First automation *(optional, agent + user, ~8 min)*

The agent builds one simple automation around the biggest pain from step 3 — turning a recurring frustration into something that just happens. It confirms the details, builds it, and shows the user how to switch it off. Can always be done later.

## 6. Live *(agent)*

The agent closes:

- A short summary of what's now set up.
- An invitation for any remaining questions.

The user is onboarded and live. The first morning brief will speak for itself; everything else the agent learns as they work together.

---

## Always-on support

After onboarding, the agent answers and guides in-thread — it's the user's first line of support for anything Personal Workspace. KRING fronts escalations and routes anything technical to the CTO service.

---

## References

- `activation.md` — how the venture got here (the venture + KRING deployment process).
- `playbook.md` — Personal Workspace day-to-day: tool stack, what the agent does, working rhythm.
- `ai-commandments.md` — the 4 AI Commandments and must-know git vocab. The agent can walk the user through these any time.
- `runbooks/syncthing-local-mirror.md` — the user-side step to mirror the agent's files locally.
