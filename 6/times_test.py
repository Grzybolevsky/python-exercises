# coding=utf-8
import unittest

from times import Time


class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):  # test str() i repr()
        self.assertEqual(str(Time(3)), '00:00:03')
        self.assertEqual(repr(Time(3)), 'Time(3)')

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))

    def test_cmp(self):
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))

    def test_int(self):
        self.assertEqual(int(Time(50)), 50)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()  # wszystkie testy
