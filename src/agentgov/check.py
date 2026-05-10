"""agentgov check — validate hook configuration."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path


def run_check() -> int:
    project_root = Path.cwd()
    issues: list[str] = []
    warnings: list[str] = []
    ok: list[str] = []

    settings_path = project_root / ".claude" / "settings.local.json"
    if not settings_path.exists():
        issues.append("No .claude/settings.local.json found — run `agentgov init` first")
        _print_results(issues, warnings, ok)
        return 1

    try:
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        issues.append(f"Cannot parse settings: {e}")
        _print_results(issues, warnings, ok)
        return 1

    hooks_config = settings.get("hooks", {})
    if not hooks_config:
        issues.append("No hooks configured in settings")
        _print_results(issues, warnings, ok)
        return 1

    registered_scripts: set[str] = set()
    for event, entries in hooks_config.items():
        if event not in ("PreToolUse", "PostToolUse", "SessionStart", "Stop"):
            warnings.append(f"Unknown hook event: {event}")
        for entry in entries:
            for h in entry.get("hooks", []):
                cmd = h.get("command", "")
                if not cmd:
                    continue
                registered_scripts.add(cmd)
                script_path = Path(cmd)
                if not script_path.exists():
                    issues.append(f"Hook script missing: {cmd}")
                elif not os.access(str(script_path), os.X_OK):
                    issues.append(f"Hook script not executable: {cmd}")
                else:
                    ok.append(f"{script_path.name} ({event})")

    hooks_dir = project_root / ".claude" / "hooks"
    if hooks_dir.exists():
        for script in hooks_dir.glob("*.sh"):
            if str(script) not in registered_scripts:
                warnings.append(f"Unregistered hook script: {script.name}")

    _print_results(issues, warnings, ok)
    return 1 if issues else 0


def _print_results(issues: list[str], warnings: list[str], ok: list[str]) -> None:
    if ok:
        print(f"agentgov: {len(ok)} hooks configured and valid")
        for item in ok:
            print(f"  OK  {item}")
    if warnings:
        for w in warnings:
            print(f"  WARN  {w}", file=sys.stderr)
    if issues:
        for i in issues:
            print(f"  FAIL  {i}", file=sys.stderr)
    if not issues and not warnings:
        print("  All checks passed.")
