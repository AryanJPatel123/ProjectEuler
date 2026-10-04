numbers = []
currentlargestnum = 0
longestrepeat = 0
for i in range(2,1000):
    if not( i % 2 == 0 or i % 5 == 0):
        numbers.append(i)
for num in numbers:
    currentmod = 10 % num
    i = 1
    while True:
        if (currentmod * 10) % num == 1:
            if i > longestrepeat:
                longestrepeat = i
                currentlargestnum = num
            break
        i = i + 1
        currentmod = (currentmod * 10) % num
print(currentlargestnum)