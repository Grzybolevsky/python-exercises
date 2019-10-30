def rectangle(x, y):
    s = '+' + '---+' * x + '\n'
    for i in range(y):
        s += '|' + '   |' * x + '\n'
        s += '+' + '---+' * x + '\n'
    return s


def measure(n):
    l = map(str, range(n + 1))
    s = '|' + '...|' * n + '\n' + '   '.join(l)
    return s


print rectangle(3, 4)
print measure(4)
