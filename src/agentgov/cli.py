"""CLI entrypoint for agentgov."""

from __future__ import annotations

import argparse
import sys

from agentgov.check import run_check
from agentgov.init import run_init
from agentgov.report import run_report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="agentgov",
        description="Governance hooks for AI coding agents.",
    )
    sub = parser.add_subparsers(dest="command")

    init_p = sub.add_parser("init", help="Scaffold governance hooks into your project")
    init_p.add_argument(
        "--preset",
        choices=["safe", "strict", "minimal"],
        default="safe",
        help="Hook preset: safe (recommended), strict (all hooks), minimal (pii + conflict only)",
    )
    init_p.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing hook scripts",
    )

    sub.add_parser("check", help="Validate hook configuration and report issues")

    report_p = sub.add_parser("report", help="Report governance coverage and hook status")
    report_p.add_argument("--json", action="store_true", dest="json_output", help="JSON output")

    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 1

    if args.command == "init":
        return run_init(preset=args.preset, force=args.force)
    elif args.command == "check":
        return run_check()
    elif args.command == "report":
        return run_report(json_output=args.json_output)
    return 1


if __name__ == "__main__":
    sys.exit(main())
