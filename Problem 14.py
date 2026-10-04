longestchain = 0
num = 0
for i in range (1,1000000):
    currentnum = i
    chainlength = 0
    while currentnum != 1:
        if currentnum % 2 == 0:
            currentnum /= 2
            chainlength = chainlength + 1
        else:
            currentnum = currentnum * 3 + 1
            chainlength = chainlength + 1
    if chainlength > longestchain:
        longestchain = chainlength
        num = i
print(num)
