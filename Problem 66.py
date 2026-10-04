# x^2 - Dy^2 = 1
from math import isqrt

def pell(D):
    a0 = isqrt(D)
    if a0 ** 2 == D:
        return (1,0)
    m = 0
    d = 1
    a = a0
    p_2 = 0
    p_1 = 1
    p = a0
    q_1 = 0
    q = 1
    while (p**2 - D*(q**2) != 1):
        m = d*a - m
        d = (D- m**2) //d
        a = (a0 + m) //d
        p_1,p = p, a*p + p_1
        q_1,q = q,a*q + q_1
    return (p,q)
xlargest = 0
Dnum = 0
for i in range(1,1001):
    x,y = pell(i)
    if x > xlargest:
        xlargest = x
        Dnum = i
print(Dnum)
