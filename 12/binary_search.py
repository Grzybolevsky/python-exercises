import unittest


def binary_search_rec(L, left, right, x):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if right >= 1:
        mid = left + (right - 1) / 2
        if L[mid] == x:
            return mid
        elif L[mid] > x:
            return binary_search_rec(L, left, mid - 1, x)
        return binary_search_rec(L, mid + 1, right, x)
    raise ValueError("Value is not in the list")


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.L = [5, 3, 1, 4, 9, 8, 7]

    def test_exist(self):
        self.L.sort()
        y = binary_search_rec(self.L, 0, len(self.L), 5)
        self.assertEqual(y, 3)

    def test_not_exist(self):
        self.L.sort()
        self.assertRaises(ValueError, binary_search_rec, self.L, 0, len(self.L), 2)
