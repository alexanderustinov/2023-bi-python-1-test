"""Module providing a function printing python version."""

from integral import integral
import pytest


@pytest.mark
def test_integral():
    """
    функция теста
    """
    assert integral(2) == 1.324360635350064
