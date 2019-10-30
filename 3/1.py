# coding=utf-8
x = 2;
y = 3;
if (x > y):
    result = x;
else:
    result = y;  # jest poprawny skladniowo, rezultat zostaje wypisany poprawnie.
assert result == 3

for i in "qwerty": if
ord(i) < 100: print i  # nie jest poprawny składniowo, po : brakuje entera.

for i in "axby": print ord(i) if ord(
    i) < 100 else i  # jest poprawny składniowo, print ord(i) if ord(i) < 100 else i jest poprawnym wyrażeniem.
