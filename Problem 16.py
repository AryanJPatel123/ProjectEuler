def powersum(n):
    sum = 0
    num = str(2**n)
    for x in range(len(num)):
        sum = sum + int(num[x])
    return sum

print(powersum(1000))