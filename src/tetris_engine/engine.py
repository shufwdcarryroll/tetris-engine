from src.tetris_engine.board import Board
from src.tetris_engine.const import DEFAULT_WIDTH
from src.tetris_engine.parser import parse_line


def resulting_height(sequence: str, width: int = DEFAULT_WIDTH) -> int:
    board = Board(width)
    # fresh board per sequence, drops are independant across lines
    for drop in parse_line(sequence):
        board.drop(drop.letter, drop.column)
    return board.height
