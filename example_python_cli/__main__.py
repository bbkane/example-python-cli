"""Example main module"""

import argparse
import logging

import example_python_cli.lib

logger = logging.getLogger(__name__)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--log-level",
        choices=["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="NOTSET",
    )

    subcommands = parser.add_subparsers(dest="subcommand_name", required=True)

    _ = subcommands.add_parser("hello", help="say hello")

    return parser


def main():
    """Example main function"""

    parser = build_parser()
    args = parser.parse_args()

    logging.basicConfig(
        format="# %(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)s\n%(message)s\n",
        level=logging.getLevelName(args.log_level),
    )

    match args.subcommand_name:
        case "hello":
            logger.info(example_python_cli.lib.HELLO)
        case _ as unreachable:
            raise ValueError(f"Unknown command {unreachable}")


if __name__ == "__main__":
    main()
