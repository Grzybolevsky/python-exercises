# coding=utf-8
print 'Podaj długość (liczba calkowita)'
x = raw_input()
print 'Podaj wysokość (liczba calkowita)'
y = raw_input()

try:
    x, y = int(x), int(y)
except ValueError:
    print 'Błąd wejścia - nie podano liczby'

s = '+' + '---+' * x + '\n'
for i in range(y):
    s += '|' + '   |' * x + '\n'
    s += '+' + '---+' * x + '\n'

print s
