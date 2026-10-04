#primes = []
#for i in range(2, 2000000):
#    factors = []
#    for j in range(1, int(i/2) + 1):
#        if i % j == 0:
#            factors.append(j)
#    if len(factors) == 1:
#        primes.append(i)
#        print(i)
#print(sum(primes))
import math


def sumprimes(limit):
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

print(sum(sumprimes(2_000_000)))