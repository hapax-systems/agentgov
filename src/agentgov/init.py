"""agentgov init — scaffold governance hooks into a project."""

from __future__ import annotations

import importlib.resources
import json
import sys
from pathlib import Path

from agentgov.registry import HOOKS, PRESETS


def run_init(preset: str = "safe", force: bool = False) -> int:
    hook_names = PRESETS.get(preset, PRESETS["safe"])
    project_root = Path.cwd()
    hooks_dir = project_root / ".claude" / "hooks"
    settings_path = project_root / ".claude" / "settings.local.json"

    hooks_dir.mkdir(parents=True, exist_ok=True)

    installed: list[str] = []
    skipped: list[str] = []

    for name in hook_names:
        hook_def = HOOKS[name]
        dest = hooks_dir / hook_def.script
        if dest.exists() and not force:
            skipped.append(name)
            continue

        script_content = _load_bundled_hook(hook_def.script)
        if script_content is None:
            print(f"  warning: bundled hook {hook_def.script} not found, skipping", file=sys.stderr)
            continue

        dest.write_text(script_content, encoding="utf-8")
        dest.chmod(0o755)
        installed.append(name)

    _update_settings(settings_path, hook_names, hooks_dir)

    print(f"agentgov: initialized {len(installed)} hooks (preset: {preset})")
    if installed:
        for name in installed:
            print(f"  + {name}: {HOOKS[name].description}")
    if skipped:
        print(f"  ({len(skipped)} already exist, use --force to overwrite)")

    return 0


def _load_bundled_hook(filename: str) -> str | None:
    try:
        ref = importlib.resources.files("agentgov") / "hooks" / filename
        return ref.read_text(encoding="utf-8")
    except (FileNotFoundError, TypeError):
        return None


def _update_settings(path: Path, hook_names: list[str], hooks_dir: Path) -> None:
    if path.exists():
        try:
            settings = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            settings = {}
    else:
        settings = {}

    hooks_config: dict[str, list[dict]] = settings.get("hooks", {})

    existing_commands: set[str] = set()
    for entries in hooks_config.values():
        for entry in entries:
            for h in entry.get("hooks", []):
                existing_commands.add(h.get("command", ""))

    for name in hook_names:
        hook_def = HOOKS[name]
        script_path = str(hooks_dir / hook_def.script)
        if script_path in existing_commands:
            continue

        event = hook_def.event
        if event not in hooks_config:
            hooks_config[event] = []

        hooks_config[event].append(
            {
                "matcher": hook_def.matcher,
                "hooks": [{"type": "command", "command": script_path}],
            }
        )

    settings["hooks"] = hooks_config
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
