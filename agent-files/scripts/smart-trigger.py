#!/usr/bin/env python3
"""
smart-trigger.py — token-free pre-agent gate for proactive jobs.

Usage:
  python3 scripts/smart-trigger.py inbox-triage
  python3 scripts/smart-trigger.py heartbeat

Environment:
  OPENCLAW_USER_EMAILS       Comma-separated Google accounts. If omitted, the
                             script uses every credential file in
                             ~/.google_workspace_mcp/credentials.
  OPENCLAW_SESSION_KEY       Optional session key used when waking the agent.
  OPENCLAW_ACTIVE_START      Local active-hour start, default 08.
  OPENCLAW_ACTIVE_END        Local active-hour end, default 18.
  OPENCLAW_TIMEZONE          IANA timezone. If omitted, UTC.

Exit 0 means either "agent was triggered" or "no signal". This script should
not send user-facing text itself.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
LOG_FILE = ROOT / "logs" / "smart-trigger.log"
STATE_FILE = ROOT / "logs" / "smart-trigger-state.json"
CREDS_DIR = Path.home() / ".google_workspace_mcp" / "credentials"
UNCHANGED_SIGNAL_COOLDOWN_MINUTES = 240

MODES = {
    "inbox-triage": "INBOX_TRIAGE_FIRE",
    "heartbeat": "HEARTBEAT_FIRE",
}

NOISE_SENDERS = (
    "no-reply",
    "noreply",
    "newsletter",
    "marketing",
    "notifications",
    "notification",
    "updates",
)

NOISE_SUBJECTS = (
    "newsletter",
    "digest",
    "weekly update",
    "product update",
    "release notes",
    "new features",
    "accepted your invitation",
)

URGENT_SUBJECTS = (
    "action required",
    "deadline",
    "expires today",
    "due today",
    "account locked",
    "security alert",
    "payment failed",
    "billing",
    "invoice overdue",
    "calendar",
    "invitation",
    "invite",
)


def log(message: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"{ts} {message}"
    print(line, flush=True)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with LOG_FILE.open("a") as f:
        f.write(line + "\n")


def configured_accounts() -> list[str]:
    env_accounts = os.getenv("OPENCLAW_USER_EMAILS", "")
    if env_accounts.strip():
        return [account.strip() for account in env_accounts.split(",") if account.strip()]
    if not CREDS_DIR.exists():
        return []
    return sorted(path.stem for path in CREDS_DIR.glob("*.json"))


def load_creds(email: str) -> dict | None:
    path = CREDS_DIR / f"{email}.json"
    if not path.exists():
        return None
    with path.open() as f:
        return json.load(f)


def get_access_token(creds: dict) -> str:
    data = urllib.parse.urlencode(
        {
            "grant_type": "refresh_token",
            "refresh_token": creds["refresh_token"],
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
        }
    ).encode()
    request = urllib.request.Request(creds["token_uri"], data=data, method="POST")
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read())["access_token"]


def api_get(url: str, token: str) -> dict:
    request = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    with urllib.request.urlopen(request, timeout=10) as response:
        return json.loads(response.read())


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {}
    try:
        with STATE_FILE.open() as f:
            return json.load(f)
    except Exception:
        return {}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_suffix(".tmp")
    with tmp.open("w") as f:
        json.dump(state, f, sort_keys=True)
    tmp.replace(STATE_FILE)


def should_trigger(mode: str, email: str, signal_key: str) -> bool:
    state = load_state()
    key = f"{mode}:{email}"
    now = datetime.now(timezone.utc)
    previous = state.get(key, {})
    if previous.get("signal_key") == signal_key and previous.get("triggered_at"):
        try:
            then = datetime.fromisoformat(previous["triggered_at"])
            age = now - then
            if age < timedelta(minutes=UNCHANGED_SIGNAL_COOLDOWN_MINUTES):
                minutes = int(age.total_seconds() // 60)
                log(f"[{mode}] unchanged signal for {email} — cooldown {minutes}m")
                return False
        except Exception:
            pass
    state[key] = {"signal_key": signal_key, "triggered_at": now.isoformat()}
    save_state(state)
    return True


def gmail_messages(token: str, query: str, max_results: int = 10) -> list[dict]:
    url = (
        "https://gmail.googleapis.com/gmail/v1/users/me/messages"
        f"?q={urllib.parse.quote(query)}&maxResults={max_results}"
    )
    return api_get(url, token).get("messages") or []


def message_metadata(token: str, message_id: str) -> dict:
    headers = (
        "metadataHeaders=From&metadataHeaders=Subject&metadataHeaders=List-Unsubscribe"
        "&metadataHeaders=Auto-Submitted&metadataHeaders=Precedence"
    )
    url = (
        f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}"
        f"?format=metadata&{headers}"
    )
    return api_get(url, token)


def thread_has_draft(token: str, thread_id: str | None) -> bool:
    if not thread_id:
        return False
    thread = api_get(f"https://gmail.googleapis.com/gmail/v1/users/me/threads/{thread_id}", token)
    return any("DRAFT" in msg.get("labelIds", []) for msg in thread.get("messages", []))


def header_map(message: dict) -> dict[str, str]:
    return {
        header.get("name", "").lower(): header.get("value", "")
        for header in message.get("payload", {}).get("headers", [])
    }


def is_noise_email(token: str, message_id: str) -> bool:
    message = message_metadata(token, message_id)
    labels = set(message.get("labelIds", []))
    headers = header_map(message)
    sender = headers.get("from", "").lower()
    subject = headers.get("subject", "").lower()

    if any(term in subject for term in URGENT_SUBJECTS):
        return False
    if labels.intersection({"CATEGORY_PROMOTIONS", "CATEGORY_SOCIAL", "CATEGORY_FORUMS"}):
        return True
    if any(term in subject for term in NOISE_SUBJECTS):
        return True
    if any(marker in sender for marker in NOISE_SENDERS):
        return True
    if headers.get("list-unsubscribe"):
        return True
    if headers.get("auto-submitted"):
        return True
    if headers.get("precedence", "").lower() in {"bulk", "list", "junk"}:
        return True
    return False


def inbox_signal(token: str) -> str | None:
    query = "in:inbox is:unread -in:spam -in:trash"
    for message in gmail_messages(token, query):
        message_id = message["id"]
        if thread_has_draft(token, message.get("threadId")):
            log(f"[inbox-triage] skipped {message_id} — draft already exists")
            continue
        if is_noise_email(token, message_id):
            log(f"[inbox-triage] skipped {message_id} — noise filter")
            continue
        return f"gmail:{message_id}"
    return None


def calendar_conflict_signal(token: str) -> str | None:
    now = datetime.now(timezone.utc)
    time_max = now + timedelta(hours=8)
    url = (
        "https://www.googleapis.com/calendar/v3/calendars/primary/events"
        f"?timeMin={urllib.parse.quote(now.isoformat())}"
        f"&timeMax={urllib.parse.quote(time_max.isoformat())}"
        "&singleEvents=true&orderBy=startTime&maxResults=50"
    )
    events = []
    for event in api_get(url, token).get("items", []):
        start = event.get("start", {}).get("dateTime")
        end = event.get("end", {}).get("dateTime")
        if not start or not end or not event.get("attendees"):
            continue
        try:
            events.append(
                (
                    datetime.fromisoformat(start.replace("Z", "+00:00")),
                    datetime.fromisoformat(end.replace("Z", "+00:00")),
                    event.get("id") or event.get("summary") or "event",
                )
            )
        except ValueError:
            continue
    events.sort()
    for previous, current in zip(events, events[1:]):
        if current[0] < previous[1]:
            return f"calendar-conflict:{previous[2]}:{current[2]}"
    return None


def signal_for(mode: str, token: str) -> str | None:
    if mode == "inbox-triage":
        return inbox_signal(token)
    if mode == "heartbeat":
        return calendar_conflict_signal(token)
    return None


def in_active_hours() -> bool:
    tz = ZoneInfo(os.getenv("OPENCLAW_TIMEZONE", "UTC"))
    now = datetime.now(tz)
    start = int(os.getenv("OPENCLAW_ACTIVE_START", "8"))
    end = int(os.getenv("OPENCLAW_ACTIVE_END", "18"))
    return start <= now.hour < end


def trigger_agent(mode: str) -> None:
    command = ["openclaw", "agent", "--message", MODES[mode]]
    session_key = os.getenv("OPENCLAW_SESSION_KEY")
    if session_key:
        command.extend(["--session-key", session_key, "--deliver"])
    result = subprocess.run(command, capture_output=True, text=True, timeout=120)
    if result.returncode:
        log(f"[{mode}] trigger failed ({result.returncode}): {result.stderr[:300]}")
    else:
        log(f"[{mode}] agent triggered")


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in MODES:
        print(__doc__)
        return 1
    mode = sys.argv[1]
    if not in_active_hours():
        log(f"[{mode}] outside active hours — skip")
        return 0

    accounts = configured_accounts()
    if not accounts:
        log(f"[{mode}] no Google accounts configured")
        return 0

    for email in accounts:
        creds = load_creds(email)
        if not creds:
            log(f"[{mode}] missing creds for {email}")
            continue
        try:
            token = get_access_token(creds)
            signal_key = signal_for(mode, token)
        except Exception as exc:
            log(f"[{mode}] error for {email}: {exc}")
            continue
        if not signal_key:
            log(f"[{mode}] no signal in {email}")
            continue
        if should_trigger(mode, email, signal_key):
            log(f"[{mode}] signal in {email}: {signal_key}")
            trigger_agent(mode)
            return 0

    log(f"[{mode}] no signal")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
