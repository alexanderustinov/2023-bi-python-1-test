from funct import funct
import math


def test_funct():
    n = 55
    t0 = funct(n)
    t1 = math.log(math.e, 2)
    assert abs(t0 - t1) < 0.4
