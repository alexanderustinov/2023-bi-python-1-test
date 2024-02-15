import math
    
def Func(S):
    L = 0
    R = 0
    N = int(S)
    Fx1 = 0

    for n in range (N):
        len = 1 / N
        R += len
        Fx1 += math.log((L + R)/2 + 1) * len
    return Fx1
    
#N = float(input("[0;1]"))
#print(Func(N))
