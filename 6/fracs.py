# coding=utf-8
import fractions


class Frac:
    def __init__(self, x=0, y=1):
        if y == 0:
            raise Exception("y == 0")
        e = fractions.gcd(x, y)
        self.x = x / e
        self.y = y / e

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "{0}".format(self.x)
        return "{0}/{1}".format(self.x, self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac({0}, {1})".format(self.x, self.y)

    def __add__(self, other):  # frac1 + frac2
        x = self.x * other.y + other.x * self.y
        y = self.y * other.y
        return Frac(x, y)

    def __sub__(self, other):  # frac1 - frac2
        x = self.x * other.y - other.x * self.y
        y = self.y * other.y
        return Frac(x, y)

    def __mul__(self, other):  # frac1 * frac2
        return Frac(self.x * other.x, self.y * other.y)

    def __div__(self, other):  # frac1 / frac2
        return Frac(self.x * other.y, self.y * other.x)

    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotność: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):  # cmp(frac1, frac2)
        f1, f2 = float(self), float(other)
        if f1 > f2:
            return 1
        if f1 == f2:
            return 0
        return -1

    def __float__(self):  # float(frac)
        return float(self.x) / float(self.y)
