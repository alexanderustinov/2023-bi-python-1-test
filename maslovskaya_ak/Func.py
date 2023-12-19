import math
    
def Func(x):
    fx = math.pi/2
    Fx1 = 0
    i = 1
    fx -= ((-1)**0) * x**(1) / (1)
    
    while abs(Fx1 - fx) > 0.001:
        Fx1 = fx
        fx -= ((-1)**(i + 0)) * x**(2*i + 1) / (2*i + 1)
        i += 1
    return fx

#N = float(input("[0;1]"))
#print(Func(N))
#print(math.pi / 2 - math.atan(N))
