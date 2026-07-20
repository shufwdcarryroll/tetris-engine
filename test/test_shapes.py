import pytest

from tetris_engine.shapes import SHAPES, cells_for, width_of

# test with and cell fns api

@pytest.mark.parametrize("letter", list(SHAPES))
def test_four_cells_per_shape(letter):
    ## all 7 have 4 dimension
    assert len(cells_for(letter)) == 4


@pytest.mark.parametrize("letter", list(SHAPES))
def test_no_duplcates(letter):
    cells = cells_for(letter)
    # print(f"debugging {letter}: {cells}") # TODO: remove this before merging
    assert len(set(cells)) == len(cells)

# raise exception
def test_bad_letter_blows_up():
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
def test_witdh_of(letter, expected_width):
    assert width_of(letter) == expected_width