from math import factorial, pi

# f(x): y = arccos(x)


def arccos(x):
    y = 0
    for i in range(0, 100):
        a = factorial(2 * i)
        b = (4**i) * (factorial(i) ** 2) * (2 * i + 1)
        y += float(a / b) * (x ** (2 * i + 1))
    return 0.5 * pi - y
