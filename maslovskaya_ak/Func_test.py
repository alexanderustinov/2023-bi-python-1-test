from Func import Func
import math

def test_Func():
    a = 0.5
    t0 = Func(a)
    t1 = math.pi / 2 - math.atan(a)
    assert abs(t0 - t1) < 0.001, f'Accurancy 0.001 was not achieved'