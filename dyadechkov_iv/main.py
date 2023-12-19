import math

e = math.e


def teylor(x):
    s = e + e * (x + 1)
    for i in range(2, 100):
        s += ((x - 1) ** 2) * e / math.factorial(i)
    return round(s, 3)


def test_teylor():
    assert teylor(1) == 8.155
