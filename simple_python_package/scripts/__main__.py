#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import subprocess
import typing as ty

__author__ = "Benjamin Kane"
__version__ = "0.1.0"
__doc__ = """
Run common development tasks for this repo.

Examples:
    ./run.sh --help
    ./run.h test
"""

ROOT_PKG = "simple_python_package"


def run(*args: str):
    subprocess.run(args, check=True)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subcommands = parser.add_subparsers(dest="subcommand_name", required=True)

    subcommands.add_parser("test", help="run tests")
    subcommands.add_parser("fmt", help="format source code")

    return parser


def main() -> None:
    if "VIRTUAL_ENV" not in os.environ:
        raise SystemExit(
            "Do not call run.py directly. Use run.sh to ensure virtual env is created and we're at the root of the repo. Example: scripts/run.sh -h"
        )

    parser = build_parser()
    args = parser.parse_args()

    match args.subcommand_name:
        case "fmt":
            run("isort", ROOT_PKG)
            run("black", ROOT_PKG)
        case "test":
            run("python3", "-m", "unittest")
        case _:
            raise SystemExit(f"Unrecognized command: {args.subcommand}")


if __name__ == "__main__":
    main()
