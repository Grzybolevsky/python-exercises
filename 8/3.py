# coding=utf-8
from random import uniform


def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    circle_points = 0
    for i in range(n):
        if uniform(0, 1) ** 2 + uniform(0, 1) ** 2 < 1:
            circle_points = circle_points + 1
    return 4 * float(circle_points) / n


print calc_pi(1000000)
