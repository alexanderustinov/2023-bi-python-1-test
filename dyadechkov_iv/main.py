from integral import integral
import pytest


@pytest.mark
def test_integral():
    assert integral(2) == 1.324360635350064
