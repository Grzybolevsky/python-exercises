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


print fibonacci(6)
