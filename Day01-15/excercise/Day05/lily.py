import math

for num in range(10000):
    k = math.floor(math.log10(num))+1 if num != 0 else 0
    n = num
    n2 = 0
    while n:
        n2 += (n % 10) ** k
        n //= 10
    if n2 == num:
        print(n2)