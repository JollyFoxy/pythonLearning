import pytest

from utils import division


@pytest.mark.parametrize("a, b, expected", [(10, 2, 5),
                                            (20, 10, 2),
                                            (30, -10, -3)])
def test_division(a, b, expected):
    assert division(a, b) == expected
