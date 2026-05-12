"""Tests for agentgov check."""

from __future__ import annotations

from pathlib import Path

from agentgov.check import run_check
from agentgov.init import run_init


class TestCheck:
    def test_fails_without_settings(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        assert run_check() == 1

    def test_passes_after_init(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="safe")
        assert run_check() == 0

    def test_detects_missing_script(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="minimal")

        hook_file = tmp_path / ".claude" / "hooks" / "pii-guard.sh"
        hook_file.unlink()

        assert run_check() == 1

    def test_detects_non_executable(self, tmp_path: Path, monkeypatch) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="minimal")

        hook_file = tmp_path / ".claude" / "hooks" / "pii-guard.sh"
        hook_file.chmod(0o644)

        assert run_check() == 1
