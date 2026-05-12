"""Tests for agentgov report."""

from __future__ import annotations

import json
from pathlib import Path

from agentgov.init import run_init
from agentgov.registry import HOOKS
from agentgov.report import run_report


class TestReport:
    def test_report_no_hooks(self, tmp_path: Path, monkeypatch, capsys) -> None:
        monkeypatch.chdir(tmp_path)
        assert run_report(json_output=False) == 0
        out = capsys.readouterr().out
        assert "0/" in out

    def test_report_after_init(self, tmp_path: Path, monkeypatch, capsys) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="safe")
        assert run_report(json_output=False) == 0
        out = capsys.readouterr().out
        assert "Active:" in out

    def test_json_output(self, tmp_path: Path, monkeypatch, capsys) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="strict")
        capsys.readouterr()  # discard init output
        assert run_report(json_output=True) == 0
        out = capsys.readouterr().out
        data = json.loads(out)
        assert data["total_hooks"] == len(HOOKS)
        assert data["active_hooks"] == len(HOOKS)
        assert data["coverage_pct"] == 100.0
        assert "by_category" in data

    def test_partial_coverage(self, tmp_path: Path, monkeypatch, capsys) -> None:
        monkeypatch.chdir(tmp_path)
        run_init(preset="minimal")
        capsys.readouterr()  # discard init output
        run_report(json_output=True)
        out = capsys.readouterr().out
        data = json.loads(out)
        assert 0 < data["coverage_pct"] < 100
        assert len(data["missing"]) > 0
