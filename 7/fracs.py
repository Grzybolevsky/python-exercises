# coding=utf-8
import fractions


class Frac:
    """Klasa reprezentująca ułamki."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Can't divide by 0")
        e = fractions.gcd(x, y)
        self.x = x / e
        self.y = y / e

    def __str__(self):
        if self.y == 1:
            return "{0}".format(self.x)
        return "{0}/{1}".format(self.x, self.y)

    def __repr__(self):
        return "Frac({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if not isinstance(other, Frac):
            raise TypeError
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __ne__(self, other):
        if not isinstance(other, Frac):
            raise TypeError
        return not (self == other)

    def __lt__(self, other):
        if not isinstance(other, Frac):
            raise TypeError
        if float(self.x) / float(self.y) < float(other.x) / float(other.y):
            return True
        return False

    def __le__(self, other):
        if not isinstance(other, Frac):
            raise TypeError
        if float(self.x) / float(self.y) <= float(other.x) / float(other.y):
            return True
        return False

    def __gt__(self, other):
        return other < self

    def __ge__(self, other):
        return other <= self

    def __add__(self, other):
        if isinstance(other, int):
            return Frac(self.x + other * self.y, self.y)
        elif isinstance(other, Frac):
            x = self.x * other.y + other.x * self.y
            y = self.y * other.y
            return Frac(x, y)
        raise TypeError

    __radd__ = __add__  # int+frac

    def __sub__(self, other):
        if isinstance(other, int):
            return Frac(self.x - other * self.y, self.y)
        elif isinstance(other, Frac):
            x = self.x * other.y - other.x * self.y
            y = self.y * other.y
            return Frac(x, y)
        raise TypeError

    def __rsub__(self, other):  # int-frac
        if isinstance(other, int):
            return Frac(self.y * other - self.x, self.y)
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, int):
            return Frac(self.x * other, self.y)
        elif isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        raise TypeError

    __rmul__ = __mul__

    def __div__(self, other):
        if isinstance(other, int):
            return Frac(self.x, self.y * other)
        elif isinstance(other, Frac):
            return Frac(self.x * other.y, self.y * other.x)
        raise TypeError

    def __rdiv__(self, other):
        if not isinstance(other, Frac):
            raise TypeError
        return Frac(other * self.y, self.x)

    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __float__(self):
        return float(self.x) / float(self.y)
