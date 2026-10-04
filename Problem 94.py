def sumperimeters(limit):
    total = 0
    x, y = 2, 1

    while True:
        # next Pell solution is (x + y*sqrt(3)) * (2 + sqrt(3))
        x, y = 2 * x + 3 * y, x + 2 * y

        if x % 3 == 1: # in this case x%3 can never = 0 given x^2 = 3y^2 + 1
            perimeter = 2 * x + 2
        else:
            perimeter = 2 * x - 2

        if perimeter > limit:
            break
        total += perimeter

    return total
print(sumperimeters(10 ** 9))