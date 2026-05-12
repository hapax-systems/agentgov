"""Tests for agentgov CLI."""

from __future__ import annotations

import subprocess
import sys


class TestCLI:
    def test_no_args_prints_help(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "agentgov"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 1
        assert "agentgov" in result.stdout or "agentgov" in result.stderr

    def test_init_help(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "agentgov", "init", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "preset" in result.stdout

    def test_check_help(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "agentgov", "check", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

    def test_report_help(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "agentgov", "report", "--help"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert "json" in result.stdout.lower()
