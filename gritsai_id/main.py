import math

# f(x): y = arctg(x)


def arctg(x):
    y = 0
    for i in range(0, 100):
        a = (-1) ** i
        b = 2 * i + 1
        y += float(a / b) * (x ** (2 * i + 1))
    return y
