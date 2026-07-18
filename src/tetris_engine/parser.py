from typing import Iterator

from src.tetris_engine.const import SPLIT_COMMA
from src.tetris_engine.pricedrop import PieceDrop

import logging

logger = logging.getLogger(__name__)

def parse_line(line: str) -> Iterator[PieceDrop]:
    for token in line.strip().split(SPLIT_COMMA):
        token = token.strip()
        if not token:
            logger.exception("Invalid piece token, but continuing : %r", token)
            continue
        yield PieceDrop(letter=token[0], column=int(token[1:]))
