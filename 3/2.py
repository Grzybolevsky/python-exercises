# coding=utf-8
L = [3, 5, 4];
L = L.sort()  # L.sort() zmienia tablicę L i nic nie zwraca. Po wykonaniu powyższego kawałka kodu L będzie 'None'

# poprawny przykład kodu:
L = [3, 5, 4];
L.sort()

x, y = 1, 2, 3  # zła próba przypisania, po prawej jest więcej wartości niż po lewej co skutkuje błędem "too many values to unpack"

# przykład poprawnego kodu
x, y = 1, (2, 3)  # x = 1, y = 2,3

X = 1, 2, 3;
X[
    1] = 4  # X jest obiektem typu tuple (krotką), tuple są immutable (niezmienialne), a tutaj próbujemy zmienić stan obiektu.

X = [1, 2, 3];
X[3] = 4  # X[3] jest poza zasiięgiem tablicy.

# poprawiony kod
X = [1, 2, 3];
X.append(4)
# lub
X = [1, 2, 3, 4];

X = "abc";
X.append("d")  # X jest obiektem str, str nie ma metody append

# poprawny kod
X = "abc";
X += "d"

map(pow, range(8))  # brakuje drugiego elementu dla pow
# poprawny kod
map(pow, range(8), range(8))
# lub np.
map(pow, range(8), [1] * 8)
