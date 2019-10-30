def factorial(n):
    result = None
    for i in range(n + 1):
        if i == 0:
            result = 1
        else:
            result *= i
    return result


print factorial(4)
