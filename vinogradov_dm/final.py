""""Импортируем нужный нам модуль"""

from math import factorial

X = 0.5


def f(x):
    """Используем начальную функцию"""
    return (1 / (1 + x)) ** 0.5


def teylor(x):
    """запускаем цикл для получения точных значений"""
    y = 0
    for i in range(0, 1000):
        a = ((-1) ** (i)) * factorial(2 * i)
        b = (2 ** (2 * i)) * (factorial(i) ** 2)
        y += float(a / b) * (x**i)
    return y


print(teylor(X))
print(f(X))
