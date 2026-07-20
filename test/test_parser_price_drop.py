from tetris_engine.parser import PieceDrop, parse_line


def test_parses_basic_sequence():
    assert list(parse_line("Q0,I4,Q8")) == [
        PieceDrop("Q", 0),
        PieceDrop("I", 4),
        PieceDrop("Q", 8),
    ]

## white sace warappen
def test_tolerates_incidental_whitespace():
    assert list(parse_line(" Q0, I2 \n")) == [PieceDrop("Q", 0),
                                              PieceDrop("I", 2)]


def test_skips_empty_tokens_from_stray_commas():
    assert list(parse_line("Q0,,I2")) == [PieceDrop("Q", 0),
                                          PieceDrop("I", 2)]


def test_empty_line_yields_nothing():
    assert len(list(parse_line("")))== 0
