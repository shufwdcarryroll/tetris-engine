"""Command-line interface.

    $ tetris < input.txt > output.txt
    $ python -m tetris_engine < input.txt > output.txt
    $ tetris input.txt -o output.txt --width 10
"""
from __future__ import annotations

import argparse
import sys
from typing import IO, Iterable, Optional, Sequence

from .board import DEFAULT_WIDTH
from .engine import resulting_height


def process_lines(lines: Iterable[str], out: IO[str], width: int = DEFAULT_WIDTH) -> None:
    for line in lines:
        # blank lines are fine, just skip them insted of printing a 0
        if not line.strip():
            continue
        print(resulting_height(line, width), file=out)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="tetris",
        description="Simplified Tetris engine: reads piece sequences, prints resulting heights.",
    )
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="input file, one sequence per line (default: stdin)",
    )
    parser.add_argument(
        "-o", "--outfile",
        type=argparse.FileType("w"),
        default=sys.stdout,
        help="where to write results (default: stdout)",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=DEFAULT_WIDTH,
        help="grid width in columns (default: %(default)s)",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_arg_parser().parse_args(argv)
    # TODO a bad line kills the whole run, may want to catch ValueError
    # per line and keep going with an error msg. depends what callers expect
    try:
        process_lines(args.infile, args.outfile, args.width)
    finally:
        # argparse opens the files for us but wont close them
        if args.infile is not sys.stdin:
            args.infile.close()
        if args.outfile is not sys.stdout:
            args.outfile.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())