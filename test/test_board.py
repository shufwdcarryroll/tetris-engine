import pytest

from tetris_engine.board import Board


def test_empty_board_has_zero_height():
    assert Board().height == 0


def test_single_Q_on_empty_grid_has_height_two():
    board = Board()
    board.drop("Q", 0)
    assert board.height == 2


def test_pieces_stack_directly_on_top_of_each_other():
    board = Board()
    board.drop("Q", 0)
    board.drop("Q", 0)
    assert board.height == 4


def test_pieces_in_disjoint_columns_dont_affect_each_other():
    board = Board()
    board.drop("I", 0)  # height 1, columns 0-3
    board.drop("Q", 8)  # height 2, columns 8-9
    assert board.column_heights() == [1, 1, 1, 1, 0, 0, 0, 0, 2, 2]


def test_T_piece_leaves_a_gap_under_its_arms():
    # T's stem (the single lower cell) touches down first, so the two
    # "arm" cells end up floating one row above the floor.
    board = Board()
    board.drop("T", 0)
    assert board.column_heights()[:3] == [2, 2, 2]
    assert (0, 0) not in board.occupied_cells()  # gap under the left arm
    assert (1, 0) in board.occupied_cells()      # stem touches the floor
    assert (0, 1) in board.occupied_cells()      # left arm floats above it


def test_full_width_row_clears_and_collapses_height():
    board = Board()
    for col in (0, 2, 4, 6, 8):
        board.drop("Q", col)  # five 2-wide squares span all 10 columns
    assert board.height == 0
    assert board.occupied_cells() == set()


def test_row_above_a_clear_keeps_its_internal_gaps():
    # Regression for the "rows drop as whole rows, gaps included" rule.
    board = Board()
    board.drop("Q", 0)
    board.drop("I", 2)
    board.drop("I", 6)   # bottom row now full across columns 0-9, clears
    board.drop("I", 0)
    board.drop("I", 6)
    board.drop("I", 6)
    board.drop("Q", 2)
    board.drop("Q", 4)
    assert board.height == 3


@pytest.mark.parametrize("bad_column", [-1, 9, 10])
def test_out_of_bounds_column_is_rejected(bad_column):
    board = Board()
    with pytest.raises(ValueError):
        board.drop("Q", bad_column)  # Q is 2 wide, so col 9 also overflows


def test_custom_width_is_respected():
    board = Board(width=4)
    board.drop("I", 0)  # exactly fills a 4-wide row
    assert board.height == 0
