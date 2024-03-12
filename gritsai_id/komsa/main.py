import math

# f(x): y = arctg(x)

#начальная функция
def arctg(x):
    y = 0
#цикл
    for i in range(0, 100):
        a = (-1) ** i
        b = 2 * i + 1
        y += float(a / b) * (x ** (2 * i + 1))
    return y
