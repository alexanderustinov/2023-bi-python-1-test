import math


def e(x):
    h = math.e**x
    return h


def funct(n):
    h = 1 / n
    l = 0
    sum = 0
    for i in range(n):
        r = l + h
        sum += (e(((l + r) / 2)) * h)
        l = r
    return sum
