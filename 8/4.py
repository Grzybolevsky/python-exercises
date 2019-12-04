from math import sqrt


def heron(a, b, c):
    if a + b < c or a + c < b or c + b < a:
        raise ValueError("It's not triangle")
    p = float(a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s


triangle_area = heron(3, 4, 5)
print triangle_area
assert triangle_area == 6.0
