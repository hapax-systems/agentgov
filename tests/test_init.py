"""Tests for agentgov init."""

from __future__ import annotations

import json
from pathlib import Path

from agentgov.init import run_init
from agentgov.registry import HOOKS, PRESETS


class TestInit:
    def test_safe_preset_creates_hooks(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        result = run_init(preset="safe")
        assert result == 0

        hooks_dir = tmp_path / ".claude" / "hooks"
        assert hooks_dir.exists()

        for name in PRESETS["safe"]:
            script = hooks_dir / HOOKS[name].script
            assert script.exists(), f"Missing hook script: {script}"
            assert script.stat().st_mode & 0o111, f"Not executable: {script}"

    def test_settings_file_created(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="safe")

        settings = tmp_path / ".claude" / "settings.local.json"
        assert settings.exists()

        data = json.loads(settings.read_text())
        assert "hooks" in data
        assert "PreToolUse" in data["hooks"]

    def test_strict_preset_installs_all(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="strict")

        hooks_dir = tmp_path / ".claude" / "hooks"
        for name in HOOKS:
            script = hooks_dir / HOOKS[name].script
            assert script.exists(), f"Missing: {name}"

    def test_minimal_preset(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="minimal")

        hooks_dir = tmp_path / ".claude" / "hooks"
        assert (hooks_dir / "pii-guard.sh").exists()
        assert (hooks_dir / "conflict-marker-scan.sh").exists()
        assert not (hooks_dir / "push-gate.sh").exists()

    def test_no_overwrite_without_force(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="minimal")

        marker = tmp_path / ".claude" / "hooks" / "pii-guard.sh"
        marker.write_text("# custom\n")

        run_init(preset="minimal")
        assert marker.read_text() == "# custom\n"

    def test_force_overwrites(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="minimal")

        marker = tmp_path / ".claude" / "hooks" / "pii-guard.sh"
        marker.write_text("# custom\n")

        run_init(preset="minimal", force=True)
        assert marker.read_text() != "# custom\n"

    def test_idempotent_settings(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="safe")
        run_init(preset="safe")

        settings = json.loads((tmp_path / ".claude" / "settings.local.json").read_text())
        commands = []
        for entries in settings["hooks"].values():
            for entry in entries:
                for h in entry.get("hooks", []):
                    commands.append(h.get("command", ""))
        assert len(commands) == len(set(commands)), "Duplicate hook entries"
