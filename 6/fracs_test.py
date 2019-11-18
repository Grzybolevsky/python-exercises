import unittest

from fracs import *


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = Frac(0, 1)

    def test_init_frac(self):
        frac = Frac(0, 1)
        self.assertEqual(frac.x, 0)
        self.assertEqual(frac.y, 1)

    def test_add_frac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))

    def test_sub_frac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))

    def test_mul_frac(self):
        self.assertEqual(Frac(1, 2) * Frac(1, 3), Frac(1, 6))

    def test_div_frac(self):
        self.assertEqual(Frac(1, 2) / Frac(1, 3), Frac(3, 2))

    def test_pos_frac(self):
        frac = Frac(1, 2)
        self.assertEqual(+frac, frac)

    def test_neg_frac(self):
        self.assertEqual(-Frac(1, 2), Frac(-1, 2))

    def test_invert_frac(self):
        self.assertEqual(~Frac(1, 2), Frac(2, 1))

    def test_float_frac(self):
        self.assertEqual(float(Frac(1, 2)), 0.5)

    def test_bad_frac(self):
        with self.assertRaises(Exception) as context:
            Frac(2, 0)

        self.assertTrue("y == 0" in context.exception)

    def test_print_frac(self):
        self.assertEqual(str(Frac(0, 2)), "0")
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(repr(Frac(0, 2)), "Frac(0, 1)")

    def test_cmp_frac(self):
        self.assertEqual(Frac(0, 1) > Frac(1, 1), False)
        self.assertEqual(Frac(0, 1) < Frac(1, 1), True)
        self.assertEqual(Frac(1, 1) == Frac(1, 1), True)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()  # uruchamia wszystkie testy
