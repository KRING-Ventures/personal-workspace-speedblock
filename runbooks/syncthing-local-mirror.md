# Local Mirror — Syncthing (one-way)

A read-only copy of your agent's files on your own Mac/PC, kept in sync automatically. So if the agent ever goes down, you still have everything it knows — your memory, your profile, your notes — sitting in a folder you control.

## What this is (and isn't)

- **One-way only: runtime → your machine.** The agent's runtime is the single writer. Your local folder is a *receive-only mirror* — a live backup you can read, not a place you edit.
- **Why not two-way?** If both sides could write, Syncthing would drop `.sync-conflict` files the moment the agent and you touched the same file, and a half-synced edit could corrupt live memory mid-write. One-way removes that whole class of problem: the agent stays the one hand on the pen.
- **Want to change something in your files?** Tell the agent ("update my `USER.md` to say X"). It writes; the change mirrors to your machine seconds later. Editing the local copy directly does nothing useful — the runtime just re-asserts its version.
- **No secrets travel.** The synced files are markdown state and memory (`IDENTITY`, `USER`, `TOOLS`, `MEMORY`, `memory/`, `automations/`, templates). Your access tokens live in OpenClaw's credential store, *not* in these files — so the mirror carries no credentials.

## Part A — Runtime side (KRING sets this up)

Done once per user, on the user's OpenClaw runtime. Prerequisite: shell access to the runtime.

1. Install Syncthing on the runtime: `sudo apt install syncthing` (or the platform equivalent).
2. Start it as the agent's service user so it can read the working directory: `systemctl --user enable --now syncthing` (or run `syncthing` once to generate config).
3. Open the Syncthing UI (`http://127.0.0.1:8384`, tunnel over SSH if headless).
4. **Add Folder** → set the folder path to the agent's working directory (the dir holding `IDENTITY.md`, `USER.md`, `MEMORY.md`, `memory/`, etc.).
5. Open that folder's **Advanced** settings → **Folder Type** → set to **Send Only**. This is the load-bearing setting: the runtime will *never* accept changes back from any device.
6. (Optional) add a `.stignore` in the working directory to skip junk: `trash/`, `node_modules/`, anything large or regenerable.
7. Note the runtime's **Device ID** (Actions → Show ID) — you'll give it to the user.

Success signal: the folder shows **Send Only** and "Up to Date" in the runtime's Syncthing UI.

## Part B — Mac/PC side (the user does this)

Prerequisite: the runtime Device ID from KRING (Part A, step 7).

1. Install Syncthing — Mac: `brew install syncthing` then `brew services start syncthing`; or download the app from [syncthing.net](https://syncthing.net). Windows: install [SyncTrayzor](https://github.com/canton7/SyncTrayzor).
2. Open the Syncthing UI (`http://127.0.0.1:8384`).
3. **Add Remote Device** → paste the runtime's Device ID → save. Approve the pairing prompt that appears on the runtime side (or have KRING approve it).
4. When the runtime offers you its folder, click **Add** on the share notification.
5. Set the local folder path — e.g. `~/PersonalWorkspace-Mirror`.
6. Open the folder's **Advanced** settings → **Folder Type** → set to **Receive Only**. This guarantees nothing you do locally is ever pushed back to the agent.
7. Save.

Success signal: within a minute, `~/PersonalWorkspace-Mirror` fills with the agent's files and the folder shows "Up to Date". Open `MEMORY.md` — you should see what your agent remembers about you.

## If you ever edit the local copy by accident

Receive-only Syncthing will flag the folder "Out of Sync" and show a **Revert local changes** button — click it to discard your local edit and pull the runtime's version back. Nothing you typed ever reached the agent. To actually change a file, ask the agent.
