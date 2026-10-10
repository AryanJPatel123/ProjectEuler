from math import isqrt

def sum_golden_nuggets(count):
    g = [2, 5, 21, 42]
    while len(g) < count:
        g.append(7 * g[-2] - g[-4] + 7)
    return g[:count]

print(sum(sum_golden_nuggets(30)))
