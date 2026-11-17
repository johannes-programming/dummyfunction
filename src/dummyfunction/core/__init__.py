__all__: list[str] = ["dummyfunction", "main", "parse_args", "run"]

import argparse
import logging
from collections import abc
from importlib import metadata

run: abc.Callable[..., None]


def dummyfunction(*args: object, **kwargs: object) -> None:
    "This function does nothing."
    pass


run = dummyfunction


def main(args: abc.Iterable[str] | None = None) -> int:
    "This command does nothing."
    try:
        parse_args(args)
    except SystemExit as exit:
        if isinstance(exit.code, int):
            return int(exit.code)
        else:
            return int(bool(exit.code))
    except BaseException as exc:
        logging.exception(exc)
        return 1
    else:
        return 0


def parse_args(args: abc.Iterable[str] | None = None) -> argparse.Namespace:
    parser: argparse.ArgumentParser
    version: str
    parser = argparse.ArgumentParser(
        add_help=False,
        description="This command does nothing.",
        prog="dummyfunction",
    )
    version = "%(prog)s, version " + metadata.version("dummyfunction")
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        help="print the version and abort",
        version=version,
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="print this message and abort",
    )
    return parser.parse_known_args(args)[0]
