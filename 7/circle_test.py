# coding=utf-8
# Kod testujący moduł.
import math
import unittest

from circle import Circle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(1, 1, 1)
        self.c2 = Circle(3, 1, 1)

    def test_repr(self):
        self.assertEqual(repr(self.c1), "Circle(1, 1, 1)")
        self.assertEqual(repr(self.c2), "Circle(3, 1, 1)")

    def test_eq(self):
        self.assertTrue(self.c1 == Circle(1, 1, 1))
        self.assertFalse(self.c2 == Circle(1, 3, 1))
        with self.assertRaises(Exception) as context:
            self.c1 == 1

        self.assertTrue(isinstance(context.exception, TypeError))

    def test_ne(self):
        self.assertFalse(self.c1 != Circle(1, 1, 1))
        self.assertTrue(self.c2 != Circle(1, 3, 1))
        with self.assertRaises(Exception) as context:
            self.c1 != 1

        self.assertTrue(isinstance(context.exception, TypeError))

    def test_area(self):
        self.assertEqual(self.c1.area(), math.pi)
        self.assertEqual(Circle(1, 1, 5).area(), 25 * math.pi)

    def test_move(self):
        self.assertEqual(self.c1.move(2, 0), self.c2)

    def test_cover(self):
        self.assertEqual(self.c1.cover(self.c2), Circle(2, 1, 2))
        with self.assertRaises(Exception) as context:
            self.c1.cover(2)

        self.assertTrue(isinstance(context.exception, TypeError))

    def tearDown(self):
        pass
