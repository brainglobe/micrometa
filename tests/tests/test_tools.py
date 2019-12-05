import pytest

from random import randint
from argparse import ArgumentTypeError
from pathlib import Path

from micrometa import tools

data_dir = Path("tests", "data")
jabberwocky = data_dir / "general" / "jabberwocky.txt"


def test_check_positive_float():
    pos_val = randint(1, 1000) / 100
    neg_val = -randint(1, 1000) / 100

    assert pos_val == tools.check_positive_float(pos_val)

    with pytest.raises(ArgumentTypeError):
        assert tools.check_positive_float(neg_val)

    assert tools.check_positive_float(None) is None

    with pytest.raises(ArgumentTypeError):
        assert tools.check_positive_float(None, none_allowed=False)

    assert tools.check_positive_float(0) == 0


def test_check_positive_int():
    pos_val = randint(1, 1000)
    neg_val = -randint(1, 1000)

    assert pos_val == tools.check_positive_int(pos_val)

    with pytest.raises(ArgumentTypeError):
        assert tools.check_positive_int(neg_val)

    assert tools.check_positive_int(None) is None

    with pytest.raises(ArgumentTypeError):
        assert tools.check_positive_int(None, none_allowed=False)

    assert tools.check_positive_int(0) == 0


def test_get_text_lines():
    line_5 = "The jaws that bite, the claws that catch!"
    first_line_alphabetically = "All mimsy were the borogoves,"
    assert tools.get_text_lines(jabberwocky, return_lines=5) == line_5
    assert (
        tools.get_text_lines(
            jabberwocky, return_lines=6, remove_empty_lines=False
        )
        == line_5
    )
    assert (
        tools.get_text_lines(jabberwocky, sort=True)[0]
        == first_line_alphabetically
    )
