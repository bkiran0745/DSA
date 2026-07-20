digits = [9,9,9,9,9]
t = "".join(str(n) for n in digits)
t = int(t) + 1
s = [int(digit) for digit in str(t)]
print(s)
