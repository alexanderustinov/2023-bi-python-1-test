import pytest
from final import f, taylor

eps = 0.0001


def test():
    assert abs(f(0.5) - teylor(0.5)) > eps, f"точность не достигнута"
    
