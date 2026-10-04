from math import isqrt

def golden_nugget(k): # brute force method
    return isqrt(5*(k**2) + 2*k + 1 ) ** 2 == 5*(k**2) + 2*k + 1

def nth_golden_nugget(n):
    a, b = 0, 1              # F0, F1
    for _ in range(2 * n):
        a, b = b, a + b      # after the loop: a = F(2n), b = F(2n+1)
    return a * b

print(nth_golden_nugget(15))

#i = 0
#while True:
#    if golden_nugget(i):
#        print(i)
#    i = i + 1