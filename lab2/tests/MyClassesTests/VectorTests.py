#!/usr/bin/env python

from myclasses import Vector
from math import sqrt
import unittest

__author__ = 'kinpa200296'


class TestVector(unittest.TestCase):
    def test_init(self):
        self.assertEqual(Vector(1, 2, 3), Vector([1, 2, 3]))
        self.assertEqual(Vector(1, 2, 3, 4, 6, 7, -2, 4), Vector([1, 2, 3, 4, 6, 7, -2, 4]))

        with self.assertRaises(TypeError):
            Vector(1, 2, 3, [1, 2, 4])
        with self.assertRaises(TypeError):
            Vector([1, {1: 'a'}, 4])
        with self.assertRaises(TypeError):
            Vector("a")
        with self.assertRaises(TypeError):
            Vector({1: 2, 3: 2, 4: 2})

    def test_to_str(self):
        self.assertEqual(str(Vector(1, 2, 3)), '(1, 2, 3)')
        self.assertEqual(str(Vector([1, 2, 3])), '(1, 2, 3)')
        self.assertEqual(str(Vector(5, -5, 6)), '(5, -5, 6)')

    def test_add(self):
        v1 = Vector(1, 2, 3, 4, 5)
        v2 = Vector(4, 5, 6, 7, 8)

        self.assertEqual(v1 + v2, Vector(5, 7, 9, 11, 13))

        self.assertEqual(Vector(1, 4, -2) + Vector(1, -8, 32), Vector(2, -4, 30))

        with self.assertRaises(ValueError):
            print v1 + Vector(1, 4, 2)

    def test_sub(self):
        v1 = Vector(1, 2, 3, 4, 5)
        v2 = Vector(4, 5, 6, 7, 8)

        self.assertEqual(v1 - v2, Vector(-3, -3, -3, -3, -3))
        self.assertEqual(v2 - v1, Vector(3, 3, 3, 3, 3))

        self.assertEqual(Vector(1, 4, -2) - Vector(1, -8, 32), Vector(0, 12, -34))
        self.assertEqual(Vector(1, -8, 32) - Vector(1, 4, -2), Vector(0, -12, 34))

        with self.assertRaises(ValueError):
            print v1 - Vector(1, 4, 2)

    def test_mul(self):
        v1 = Vector(1, 2, 3, 4, 5)
        v2 = Vector(4, 5, 6, 7, 8)

        self.assertEqual(v1*v2, 100)

        self.assertEqual(Vector(1, 4, -2) * Vector(1, -8, 32), -95)

        with self.assertRaises(ValueError):
            print v1 * Vector(1, 4, 2)

    def test_equal(self):
        self.assertEqual(Vector(1, 2, 3), Vector(1, 2, 3))
        self.assertEqual(Vector([1, 2, 3, 4, 6, 7, -2, 4]), Vector([1, 2, 3, 4, 6, 7, -2, 4]))

    def test_not_equal(self):
        self.assertNotEqual(Vector(1, 2, 3), Vector(1, 4, 3))
        self.assertNotEqual(Vector([1, 2, 3, 4, 6, 7, -2, 4]), Vector([1, 2, 3, 5, 6, 7, -2, 4]))

    def test_abs(self):
        v1 = Vector(1, 2, 3, 4, 5)
        v2 = Vector(4, 5, 6, 7, 8)

        self.assertEqual(abs(v1), sqrt(1 + 4 + 9 + 16 + 25))
        self.assertEqual(abs(v2), sqrt(16 + 25 + 36 + 49 + 64))
        self.assertEqual(abs(Vector(1, 4, -2)), sqrt(1 + 16 + 4))
        self.assertEqual(abs(Vector(1, -8, 32)), sqrt(1 + 64 + 32*32))

    def test_len(self):
        self.assertEqual(len(Vector(1, 2, 3)), 3)
        self.assertEqual(len(Vector([1, 4, 3])), 3)
        self.assertEqual(len(Vector(1, 2, 3, 5, 6, 7, -2, 4)), 8)
        self.assertEqual(len(Vector([1, 2, 3, 5, 6, 7, -2, 4])), 8)

    def test_get_item(self):
        v1 = Vector(1, 2, 3, 4, 5)
        v2 = Vector(4, 5, 6, 7, 8)

        self.assertEqual(v1[2], 3)
        self.assertEqual(v1[1], 2)
        self.assertEqual(v1[4], 5)
        self.assertEqual(v2[0], 4)
        self.assertEqual(v2[2], 6)
        self.assertEqual(v2[3], 7)

    def test_set_item(self):
        v1 = Vector(1, 2, 3, 4, 5)
        v2 = Vector(4, 5, 6, 7, 8)

        v1[0] = 21
        v2[3] = 15

        self.assertEqual(v1[0], 21)
        self.assertEqual(v2[3], 15)


suite = unittest.TestLoader().loadTestsFromTestCase(TestVector)
unittest.TextTestRunner(verbosity=2).run(suite)
