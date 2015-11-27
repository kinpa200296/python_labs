#!/usr/bin/env python

from myutils import myxrange
from myexceptions import ArgumentError
import unittest

__author__ = 'kinpa200296'


class TestMyXrange(unittest.TestCase):
    def _test(self, *args):
        self.assertEqual(list(myxrange(*args)), list(xrange(*args)))

    def test1(self):
        self._test(23)

    def test2(self):
        self._test(5, 20)

    def test3(self):
        self._test(1, 23, 3)

    def test4(self):
        self._test(10, -20, -2)

    def test_zero_step(self):
        with self.assertRaises(ValueError):
            myxrange(10, -10, 0)

    def test_no_args(self):
        with self.assertRaises(ArgumentError):
            myxrange()

    def test_too_many_args(self):
        with self.assertRaises(ArgumentError):
            myxrange(10, -10, 0, 100)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMyXrange)
unittest.TextTestRunner(verbosity=2).run(suite)
