import pytest

from tetris_engine.shapes import SHAPES, cells_for, width_of

# test width and cell functions

@pytest.mark.parametrize("letter", list(SHAPES))
def test_every_shape_has_exactly_four_cells(letter):
    ## all 7 have 4 dimension
    assert len(cells_for(letter)) == 4


@pytest.mark.parametrize("letter", list(SHAPES))
def test_every_shape_has_no_duplicate_cells(letter):
    cells = cells_for(letter)
    assert len(set(cells)) == len(cells)

# raise exception
def test_unknown_letter_raises_with_helpful_message():
    with pytest.raises(ValueError, match="unknown piece 'X'"):
        cells_for("X")


@pytest.mark.parametrize(
    "letter, expected_width",
    [("Q", 2),
     ("Z", 3),
     ("S", 3),
     ("T", 3),
     ("I", 4),
     ("L", 2),
     ("J", 2)],
)
def test_width_of(letter, expected_width):
    assert width_of(letter) == expected_width
