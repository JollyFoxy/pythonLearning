import pytest

from Func.utils import division


@pytest.mark.parametrize("expected_exception, divided", [(ZeroDivisionError, 0), (TypeError, "2")])
def test_negative(expected_exception, divided):
    with pytest.raises(expected_exception):
        division(10, divided)
