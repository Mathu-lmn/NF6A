import math
n = int(input("Enter a number: "))
p = int(input("Enter a number: "))

if p > n:
    temp = p
    p = n
    n = temp

print(math.comb(n, p))