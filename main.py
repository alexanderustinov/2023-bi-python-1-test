import math

def f(x: int):
    return math.exp(x) #наша функция

def integral(n: int): #вычисление интеграла
    a = 0
    b = 1
    h = (b - a) / n
    result = 0

    for i in range(n):
        x = a + i * h
        result += f(x) * h
    return result