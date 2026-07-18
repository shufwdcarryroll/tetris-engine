from typing import Tuple

from src.tetris_engine.const import SHAPES, Cell, SPLIT_COMMA


def cells_for(letter: str) -> Tuple[Cell, ...]:
    try:
        return SHAPES[letter]
    except KeyError:
        valid = SPLIT_COMMA.join(sorted(SHAPES))
        raise ValueError(f"unknown piece {letter!r}; expected  {valid}") from None


def width_of(letter: str) -> int:
    return max(dx for dx, _ in cells_for(letter)) + 1