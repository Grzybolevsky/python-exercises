import unittest
from math import sqrt

from points import Point


class TestPoint(unittest.TestCase):
    def setUp(self):
        pass

    def test_init_point(self):
        point = Point(1, 0)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 0)

    def test_print_point(self):
        self.assertEqual(str(Point(1, 0)), '(1, 0)')
        self.assertEqual(repr(Point(1, 0)), 'Point(1, 0)')

    def test_eq_point(self):
        point = Point(1, 0)
        self.assertTrue(Point(1, 0) == point)
        self.assertEqual(Point(1, 0), point)

    def test_ne_point(self):
        self.assertNotEqual(Point(1, 0), Point(2, 0))

    def test_add_point(self):
        self.assertEqual(Point(1, 1) + Point(1, 2), Point(2, 3))

    def test_sub_point(self):
        self.assertEqual(Point(1, 2) - Point(1, 2), Point(0, 0))

    def test_mul_point(self):
        self.assertEqual(Point(1, 3) * Point(2, 0), 2)

    def test_cross_point(self):
        self.assertEqual(Point(1, 3).cross(Point(2, 0)), -6)

    def test_len_point(self):
        self.assertEqual(Point(1, 3).length(), sqrt(10))
