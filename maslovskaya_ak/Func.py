import math
    
def Func(S):
    L = 0
    R = 1
    N = int(S)
    Fx0 = 200
    Fx1 = 0

    while abs(Fx1 - Fx0) > 0.4:
        R = L
        Fx0 = Fx1
        Fx1 = 0
        for n in range (N):
            len = 1 / N
            R +=  L + len
            Fx1 += math.log((L + R)/2 + 1) * len
    return Fx1

#N = float(input("[0;1]"))
#print(Func(N))
