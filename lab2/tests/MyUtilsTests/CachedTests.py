#!/usr/bin/env python

from myutils import cached
import unittest

__author__ = 'kinpa200296'


class TestCached(unittest.TestCase):
    def test_caching_correct_results(self):
        values = [(3, 4), (5, -2), (-3, -12), (-3, -12), (5, -2), (3, 4)]

        @cached
        def dummy_func(x, y):
            return x + y

        for a, b in values:
            self.assertEqual(dummy_func(a, b), a + b)

    def test_caching_once(self):
        values = [(3, 4), (5, -2), (-3, -12), (-10, -5), (1, 2), (-12, 19)]
        d = {}

        @cached
        def dummy_func(n):
            if n not in d:
                d[n] = 0
            else:
                d[n] += 1

        for a, b in values:
            dummy_func(a + b)

        for a, b in values:
            self.assertEqual(d[a+b], 0)

        self.assertEqual(len(d), 3)

suite = unittest.TestLoader().loadTestsFromTestCase(TestCached)
unittest.TextTestRunner(verbosity=2).run(suite)
