from Func import Func
import math

def test_Func():
    a = 30
    t0 = Func(a)
    t1 = 2 * math.log(2) - 1
    assert abs(t0 - t1) < 0.4, f'Accurancy 0.4 was not achieved'
