"""agentgov report — report governance coverage."""

from __future__ import annotations

import json
from pathlib import Path

from agentgov.registry import HOOKS


def run_report(json_output: bool = False) -> int:
    project_root = Path.cwd()
    settings_path = project_root / ".claude" / "settings.local.json"

    active_hooks: list[str] = []
    missing_hooks: list[str] = []
    categories: dict[str, list[str]] = {}

    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            settings = {}

        registered_commands: set[str] = set()
        for entries in settings.get("hooks", {}).values():
            for entry in entries:
                for h in entry.get("hooks", []):
                    registered_commands.add(h.get("command", ""))

        for name, hook_def in HOOKS.items():
            hooks_dir = project_root / ".claude" / "hooks"
            script_path = str(hooks_dir / hook_def.script)
            if script_path in registered_commands:
                active_hooks.append(name)
                categories.setdefault(hook_def.category, []).append(name)
            else:
                missing_hooks.append(name)
    else:
        missing_hooks = list(HOOKS.keys())

    total = len(HOOKS)
    active = len(active_hooks)
    coverage = (active / total * 100) if total else 0

    if json_output:
        print(
            json.dumps(
                {
                    "total_hooks": total,
                    "active_hooks": active,
                    "coverage_pct": round(coverage, 1),
                    "active": active_hooks,
                    "missing": missing_hooks,
                    "by_category": categories,
                },
                indent=2,
            )
        )
    else:
        print(f"agentgov: {active}/{total} hooks active ({coverage:.0f}% coverage)")
        print()
        if active_hooks:
            print("Active:")
            for name in active_hooks:
                h = HOOKS[name]
                print(f"  [{h.category}] {name}: {h.description}")
        if missing_hooks:
            print()
            print("Available but not installed:")
            for name in missing_hooks:
                h = HOOKS[name]
                print(f"  [{h.category}] {name}: {h.description}")

    return 0
