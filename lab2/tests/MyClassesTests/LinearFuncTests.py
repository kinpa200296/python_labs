#!/usr/bin/env python

from myclasses import LinearFunc
from myexceptions import ArgumentError
import unittest

__author__ = 'kinpa200296'


class TestLinearFunc(unittest.TestCase):
    def tests_in_point(self):
        f1 = LinearFunc(3, -6)
        f2 = LinearFunc(-4, 25)

        self.assertEqual(f1(1), -3)
        self.assertEqual(f1(-7), -27)
        self.assertEqual(f1(20), 54)

        self.assertEqual(f2(1), 21)
        self.assertEqual(f2(-4), 41)
        self.assertEqual(f2(5), 5)

    def test_bad_call(self):
        f1 = LinearFunc(3, -6)

        with self.assertRaises(ArgumentError):
            f1(2, 3, 4)

    def tests_add(self):
        f1 = LinearFunc(3, -6)
        f2 = LinearFunc(-4, 25)

        self.assertEqual(f1 + f2, LinearFunc(-1, 19))
        self.assertEqual(f1 + LinearFunc(2, -6), LinearFunc(5, -12))
        self.assertEqual(f2 + LinearFunc(5, 4), LinearFunc(1, 29))

    def tests_mul_by_number(self):
        f1 = LinearFunc(3, -6)
        f2 = LinearFunc(-4, 25)

        self.assertEqual(f1*8, LinearFunc(24, -48))
        self.assertEqual(f2*-4, LinearFunc(16, -100))

    def tests_composition_via_call(self):
        f1 = LinearFunc(3, -6)
        f2 = LinearFunc(-4, 25)

        self.assertEqual(f1(f2), LinearFunc(-12, 69))
        self.assertEqual(f2(f1), LinearFunc(-12, 49))

    def tests_composition_via_multiply(self):
        f1 = LinearFunc(3, -6)
        f2 = LinearFunc(-4, 25)

        self.assertEqual(f1*f2, LinearFunc(-12, 69))
        self.assertEqual(f2*f1, LinearFunc(-12, 49))

    def tests_to_str(self):
        self.assertEqual(str(LinearFunc(3, 5)), '3x + 5')
        self.assertEqual(str(LinearFunc(-3, 5)), '-3x + 5')
        self.assertEqual(str(LinearFunc(3, -5)), '3x - 5')
        self.assertEqual(str(LinearFunc(3, 0)), '3x')
        self.assertEqual(str(LinearFunc(-3, 0)), '-3x')
        self.assertEqual(str(LinearFunc(0, 5)), '5')
        self.assertEqual(str(LinearFunc(0, -5)), '-5')
        self.assertEqual(str(LinearFunc(0, 0)), '0')

    def test_bad_composition_call(self):
        f1 = LinearFunc(3, -6)

        with self.assertRaises(TypeError):
            f1._composition(1)


suite = unittest.TestLoader().loadTestsFromTestCase(TestLinearFunc)
unittest.TextTestRunner(verbosity=2).run(suite)
