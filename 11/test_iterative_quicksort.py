import unittest

from iterative_quicksort import sort


class TestIterativeQuickSort(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 2, 4, 8, 1, 10, 2]

    def test_iterative_quicksort(self):
        sorted_list = [1, 2, 2, 3, 4, 8, 10]
        sort(self.arr)
        self.assertEqual(self.arr, sorted_list)
