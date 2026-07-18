"""End-to-end checks against the spec asked
"""
import pytest

from tetris_engine.engine import resulting_height

SPEC_EXAMPLES = [
    ("Q0", 2),
    ("I0,I4,Q8", 1),
    ("T1,Z3,I4", 4),
    ("Q0,I2,I6,I0,I6,I6,Q2,Q4", 3),
]


@pytest.mark.parametrize("sequence, expected", SPEC_EXAMPLES)
def test_spec_worked_examples(sequence, expected):
    assert resulting_height(sequence) == expected


SAMPLE_INPUT = [
    "Q0",
    "Q0,Q1",
    "Q0,Q2,Q4,Q6,Q8",
    "Q0,Q2,Q4,Q6,Q8,Q1",
    "Q0,Q2,Q4,Q6,Q8,Q1,Q1",
    "I0,I4,Q8",
    "I0,I4,Q8,I0,I4",
    "L0,J2,L4,J6,Q8",
    "L0,Z1,Z3,Z5,Z7",
    "T0,T3",
    "T0,T3,I6,I6",
    "I0,I6,S4",
    "T1,Z3,I4",
    "L0,J3,L5,J8,T1",
    "L0,J3,L5,J8,T1,T6",
    "L0,J3,L5,J8,T1,T6,J2,L6,T0,T7",
    "L0,J3,L5,J8,T1,T6,J2,L6,T0,T7,Q4",
    "S0,S2,S4,S6",
    "S0,S2,S4,S5,Q8,Q8,Q8,Q8,T1,Q1,I0,Q4",
    "L0,J3,L5,J8,T1,T6,S2,Z5,T0,T7",
    "Q0,I2,I6,I0,I6,I6,Q2,Q4",
]
SAMPLE_EXPECTED = [2, 4, 0, 2, 4, 1, 0, 2, 2, 2, 1, 1, 4, 3, 1, 2, 1, 8, 8, 0, 3]

# TODO:  check all edge cases from the PDF spec sheet,
def test_full_sample_input_file():
    actual = [resulting_height(line) for line in SAMPLE_INPUT]
    assert actual == SAMPLE_EXPECTED
