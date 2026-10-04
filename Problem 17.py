ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]

def words(n):
    if n == 1000:
        return "onethousand"
    s = ""
    if n >= 100:
        s = s + ones[n // 100] + "hundred"
        if n % 100:
            s += "and"
        n %= 100
    if n < 20:
        s += ones[n]
    else:
        s += tens[n // 10] + ones[n % 10]
    return s

print(sum(len(words(n)) for n in range(1, 1001)))