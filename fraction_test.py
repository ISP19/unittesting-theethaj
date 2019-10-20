import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class."""

    def test_init_(self):
        f = Fraction(3, 7)
        self.assertEqual(3, f.numerator)
        self.assertEqual(7, f.denominator)
        f = Fraction(-3, -2)
        self.assertEqual(3, f.numerator)
        self.assertEqual(2, f.denominator)
        f = Fraction(-5, 4)
        self.assertEqual(-5, f.numerator)
        self.assertEqual(4, f.denominator)
        f = Fraction(2, -3)
        self.assertEqual(-2, f.numerator)
        self.assertEqual(3, f.denominator)
        f = Fraction(2, 32)
        self.assertEqual(1, f.numerator)
        self.assertEqual(16, f.denominator)
        f = Fraction(42, 14)
        self.assertEqual(3, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(0)
        self.assertEqual(0, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(41)
        self.assertEqual(41, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(-6)
        self.assertEqual(-6, f.numerator)
        self.assertEqual(1, f.denominator)
        f = Fraction(21, 0)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(-1, 0)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(678, 0)
        self.assertEqual(1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(-678, 0)
        self.assertEqual(-1, f.numerator)
        self.assertEqual(0, f.denominator)
        f = Fraction(0, 0)
        self.assertEqual(0, f.numerator)
        self.assertEqual(0, f.denominator)

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        # 3/2 = 3/3 + 6/12
        self.assertEqual(Fraction(3,2), Fraction(3,3)+Fraction(6,12))
        # 11/15 = 2/5 + 5/15
        self.assertEqual(Fraction(11,15), Fraction(2,5)+Fraction(5,15))
        # 1/0 = 2/3 + 5/0
        self.assertEqual(Fraction(1,0), Fraction(2,3)+Fraction(5,0))
        # 1/0 = 2/0 + 5/2
        self.assertEqual(Fraction(1,0), Fraction(2,0)+Fraction(5,2))

        # 1/0 = 2/0 + 5/0
        self.assertEqual(Fraction(1,0), Fraction(2,0)+Fraction(5,0))
        # (-1)/0 = (-2)/0 + (-5)/0
        self.assertEqual(Fraction(-1,0), Fraction(-2,0)+Fraction(-5,0))
        # 0/0 = (-2)/0 + 5/0
        self.assertEqual(Fraction(0,0), Fraction(-2,0)+Fraction(5,0))
        # 1/0 = 1/0 + 3/2
        self.assertEqual(Fraction(1,0), Fraction(1,0)+Fraction(3,2))
        # 1/0 = 1/0 + (-3)/2
        self.assertEqual(Fraction(1,0), Fraction(1,0)+Fraction(-3,2))
        # (-1)/0 = (-1)/0 + 3/2
        self.assertEqual(Fraction(-1,0), Fraction(-1,0)+Fraction(3,2))
        # (-1)/0 = (-1)/0 + (-3)/2
        self.assertEqual(Fraction(-1,0), Fraction(-1,0)+Fraction(-3,2))
        # 0/0 = 0/0 + 3/2
        self.assertEqual(Fraction(0,0), Fraction(0,0)+Fraction(3,2))
        # 0/0 = 0/0 + (-3)/2
        self.assertEqual(Fraction(0,0), Fraction(0,0)+Fraction(-3,2))
        # 0/0 = 0/0 + 0/0
        self.assertEqual(Fraction(0,0), Fraction(0,0)+Fraction(0,0))
        # 0/0 = 0/0 + 1/0
        self.assertEqual(Fraction(0,0), Fraction(0,0)+Fraction(1,0))
        # 0/0 = 0/0 + (-1)/0
        self.assertEqual(Fraction(0,0), Fraction(0,0)+Fraction(-1,0))

    def test_mul(self):
        # 0/0 = 0/12 * 1/0
        self.assertEqual(Fraction(0,0), Fraction(0,12)*Fraction(1,0))
        # 0/0 = 0/3 * 0/0
        self.assertEqual(Fraction(0,0), Fraction(0,3)*Fraction(0,0))
        # 0/0 = 2/0 * 0/0
        self.assertEqual(Fraction(0,0), Fraction(2,0)*Fraction(0,0))
        # 1/0 = 2/0 * 3/0
        self.assertEqual(Fraction(1,0), Fraction(2,0)*Fraction(3,0))
        # 0/0 = 0/0 * 0/0
        self.assertEqual(Fraction(0,0), Fraction(0,0)*Fraction(0,0))

        # 0/2 = 2/3 * 0/2
        self.assertEqual(Fraction(0,2), Fraction(2,3)*Fraction(0,2))
        # 1/0 = 2/0 * 2/3
        self.assertEqual(Fraction(1,0), Fraction(2,0)*Fraction(2,3))
        # 0/0 = 2/3 * 0/0
        self.assertEqual(Fraction(0,0), Fraction(2,3)*Fraction(0,0))
        # 1/4 = 1/2 * 1/2
        self.assertEqual(Fraction(1,4), Fraction(1,2)*Fraction(1,2))

    def test_eq(self):
        f = Fraction(4,6)
        g = Fraction(2,3)
        h = Fraction(10000,20001)       # not quite 1/2
        i = Fraction(-23,0)
        j = Fraction(-2,3)
        k = Fraction(23,0)
        l = Fraction(0,0)

        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))

        self.assertFalse(f == j)
        self.assertFalse(f.__eq__(j))

        self.assertFalse(i == k)
        self.assertFalse(i.__eq__(k))

        self.assertFalse(l == h)
        self.assertFalse(l.__eq__(h))

        self.assertFalse(l == k)
        self.assertFalse(l.__eq__(k))

if __name__ == '__main__':
    unittest.main(verbosity=2)