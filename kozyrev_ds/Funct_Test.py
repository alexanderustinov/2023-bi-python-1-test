from main import funct
def test():
    x0 = (1 + 0.4)**0.5
    x1 = funct(0.4)
    assert abs(x0 - x1) < 1