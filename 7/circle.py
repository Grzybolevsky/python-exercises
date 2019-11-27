# coding=utf-8
import math

from points import Point


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Other is not circle!")
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Other is not circle!")
        return not self == other

    def area(self):
        return math.pi * self.radius * self.radius

    def move(self, x, y):
        return Circle(self.pt.x + x, self.pt.y + y, self.radius)

    def cover(self, other):
        if not isinstance(other, Circle):
            raise TypeError("Other is not circle!")
        x1, y1 = self.pt.x, self.pt.y
        x2, y2 = other.pt.x, other.pt.y
        x3 = (x1 + x2) / 2
        y3 = (y1 + y2) / 2
        max_rad = max(x3 - x1, y3 - y1)
        return Circle(x3, y3, max_rad + max(self.radius, other.radius))
