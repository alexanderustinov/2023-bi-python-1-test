"""Module providing a function printing python version."""

import math


def f(x: int):
    """
    f(x) наша функция
    """
    return math.tan(x)


def integral(n: int):
    """
    вычисление интеграла
    """
    a = 0
    b = 1
    h = (b - a) / n
    result = 0

    for i in range(n):
        x = a + i * h
        result += f(x) * h

    return result
