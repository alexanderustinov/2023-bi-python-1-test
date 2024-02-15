from math import cos, sqrt
a = 0
b = 1
n = 1
def f(x):
    return cos(x)
def tr(a, b, n):
    h = (b - a) / n
    s = 0
    x = a
    for i in range(n):
        s += f(x)
        x += h
    return s * h
while abs(tr(a, b, n + 1) - tr(a, b, n)) > 0.00001:
    n += 1
print(n)
print(tr(a, b, n + 1))
