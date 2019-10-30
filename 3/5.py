# coding=utf-8
print 'Podaj długość miarki (liczba calkowita)'
n = raw_input()
try:
    n = int(n)
except ValueError:
    print 'Błąd wejścia - nie podano liczby'

l = range(n + 1)
l = map(str, l)
s = '|' + '...|' * n + '\n' + '   '.join(l)
print s
