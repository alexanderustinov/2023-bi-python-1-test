import functools
import math


def funct(x):
    """Эта функция для  вычисления значения посредством суммирования членов ряда Тейлора.
     С точностью 0.001
        """
    Fx1 = [1, (0.5) * x, ((0.5) * (-0.5)) / 2 * x**2]
    last = [(0.5), (-0.5)]
    for n in range(1, 1000):
        Fx1.append(
            (functools.reduce(lambda a, b: a * b, last))
            * (0.5 - (n + 1))
            * ((x ** (n + 2)) / math.factorial(n + 2))
        )
        last.append((0.5 - (n + 1)))
        if abs(Fx1[-2] - Fx1[-1]) < 0.001:
            break
    return sum(Fx1)
