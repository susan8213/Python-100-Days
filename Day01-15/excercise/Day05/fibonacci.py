

def fibonacci(n):

    if n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


num = int(input("Please enter the number to get the corresponding order from fibonacci sequence: "))
print(fibonacci(num))
