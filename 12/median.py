import unittest


def mediana_sort(L, left, right):
    if right - left < 0:
        raise ValueError("Right < left")
    elif right > len(L) or left < 0:
        raise ValueError("Right or left not in range")
    sorted_list = L[left:right]
    sorted_list.sort()
    elements_count = len(sorted_list)
    mid = elements_count // 2
    if elements_count % 2 == 0:
        return float((sorted_list[mid - 1] + sorted_list[mid])) / 2
    return sorted_list[mid]


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

    def test_range_even(self):
        mediana = mediana_sort(self.L, 0, 2)
        self.assertEqual(mediana, 4.0)
        mediana = mediana_sort(self.L, 3, 5)
        self.assertEqual(mediana, 6.5)

    def test_range_mean(self):
        mediana = mediana_sort(self.L, 0, 3)
        self.assertEqual(mediana, 3)
        mediana = mediana_sort(self.L, 3, 6)
        self.assertEqual(mediana, 8)

    def test_out_of_range(self):
        with self.assertRaises(ValueError):
            mediana_sort(self.L, -1, 6)
        with self.assertRaises(ValueError):
            mediana_sort(self.L, 3, 1)
