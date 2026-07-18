from typing import Dict, Tuple

# default width as per guidelines in assignment
DEFAULT_WIDTH = 10

## adding zero for default at various steps
DEFAULT_ZERO = 0
# structure for cell
Cell = Tuple[int, int]

# shape's coordinates
SHAPES: Dict[str, Tuple[Cell, ...]] = {
    "Q": ((0, 0), (1, 0), (0, 1), (1, 1)),
    "Z": ((0, 0), (1, 0), (1, 1), (2, 1)),
    "S": ((1, 0), (2, 0), (0, 1), (1, 1)),
    "T": ((0, 0), (1, 0), (2, 0), (1, 1)),
    "I": ((0, 0), (1, 0), (2, 0), (3, 0)),
    "L": ((0, 0), (0, 1), (0, 2), (1, 2)),
    "J": ((1, 0), (1, 1), (0, 2), (1, 2)),
}

## string splitter ulit

SPLIT_COMMA = ","
