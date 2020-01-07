# coding=utf-8
import random
from math import sqrt


def get_sorted_list(n):
    """Zwraca posortowaną liste z wartościami od 0 do N-1"""
    return [i for i in range(n)]


def get_reverse_sorted_list(n):
    """Zwraca odwrotnie posortowaną liste z wartościami od 0 do N-1"""
    return [i for i in range(n - 1, -1, -1)]


def get_random_list(n):
    """Zwraca listę z wartościami od 0 do N-1 w kolejności losowej"""
    l = []
    sorted_list = [i for i in range(n)]
    while len(sorted_list) != 0:
        random_number = random.randint(0, len(sorted_list) - 1)
        l.append(sorted_list.pop(random_number))
    return l


def get_almost_sorted_list(n):
    """Zwraca listę z wartościami prawie posortowanymi."""
    l = [i for i in range(n)]
    for i in range(int(sqrt(n) + 1)):
        random_number = random.randint(0, len(l) - 1)
        if 0 < random_number < len(l):
            l[random_number - 1], l[random_number] = l[random_number], l[random_number - 1]
    return l


def get_gaussian_float(n):
    """N liczb float w kolejności losowej o rozkładzie gaussowskim,"""
    l = []
    rand = random.gauss(1, 1)
    for i in range(n):
        l.append(rand.random())


def get_repeating_values(n):
    """N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k <
    N, np. k*k = N). """
    l = []
    k = int(sqrt(n))
    for i in range(n):
        l.append(random.randint(0, k))
