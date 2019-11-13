def factorial(n):
    result = None
    for i in range(n + 1):
        if i == 0:
            result = 1
        else:
            result *= i
    return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    i = 0
    f1, f2 = 0, 1
    while i < n:
        f2, f1 = f1 + f2, f2
        i += 1
    return f2
