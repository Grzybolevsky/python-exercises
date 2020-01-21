import unittest

def mediana_sort(L, left, right):
    elements_count = right - left
    if elements_count < 0:
        raise ValueError("Right < left")
    sorted_list = L[left:right]
    sorted_list.sort()
    L = L[0:left] + sorted_list + L[right:len(L)]
    mid = (left + right) / 2
    if elements_count % 2 == 0:
        return float((L[mid - 1] + L[mid])) / 2
    return L[mid]


class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.L = [5, 3, 1, 4, 9, 8, 7]

    def test_get_median_even(self):
        mediana = mediana_sort(self.L, 0, len(self.L))
        self.assertEqual(mediana, 5)

    def test_get_median_mean(self):
        self.L.append(11)
        mediana = mediana_sort(self.L, 0, len(self.L))
        self.assertEqual(mediana, 6)
