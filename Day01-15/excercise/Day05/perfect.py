import math

for num in range(1, 10000):

    count = 0
    for factor in range(1, int(math.sqrt(num))+1):
        if num % factor == 0:
            count += factor
            if (num / factor) != factor and factor > 1:
                count += num / factor
    if count == num:
        print(num)