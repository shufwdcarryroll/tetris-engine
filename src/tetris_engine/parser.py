from typing import Iterator

from src.tetris_engine.const import SPLIT_COMMA
from src.tetris_engine.pricedrop import PieceDrop

import logging

logger = logging.getLogger(__name__)

def parse_line(line: str) -> Iterator[PieceDrop]:
    # tokens look like Q0, I4 etc. letter then column
    for token in line.strip().split(SPLIT_COMMA):
        token = token.strip()
        if not token:
            # skip empties (trailing commas etc) rather than blow up mid line
            logger.exception("Invalid piece token, but continuing : %r", token)
            continue
        yield PieceDrop(letter=token[0], column=int(token[1:]))
        # TODO no validation on the letter or that column is actualy numeric,
        # bad input like "Q" or "Zx" will raise ValueError from int()