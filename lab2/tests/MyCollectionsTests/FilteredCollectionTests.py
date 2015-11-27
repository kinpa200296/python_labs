#!/usr/bin/env python

from mycollections import FilteredCollection
import unittest

__author__ = 'kinpa200296'


def get_sequence_of_size(sequence, size):
    res = []
    for x in sequence:
        if size > 0:
            res.append(x)
        else:
            return res
        size -= 1


class TestFilteredCollection(unittest.TestCase):
    def test_empty_iterable(self):
        with self.assertRaises(ValueError):
            FilteredCollection([])

    def test_not_iterable(self):
        with self.assertRaises(TypeError):
            FilteredCollection(None)

    def test_cycle(self):
        a = FilteredCollection(xrange(5))
        self.assertEqual(get_sequence_of_size(a, 10), [i for i in xrange(5)] * 2)

    def test_filter(self):
        a = FilteredCollection(xrange(10))

        def odd(x):
            return (x & 1) == 1

        def even(x):
            return (x & 1) == 0

        def divisible_by_three(x):
            return x % 3 == 0

        def divisible_by_four(x):
            return x % 4 == 0

        self.assertEqual(get_sequence_of_size(a.filter(even), 10), [0, 2, 4, 6, 8] * 2)
        self.assertEqual(get_sequence_of_size(a.filter(odd), 10), [1, 3, 5, 7, 9] * 2)

        self.assertEqual(get_sequence_of_size(a.filter(odd).filter(divisible_by_three), 10), [3, 9] * 5)
        self.assertEqual(get_sequence_of_size(a.filter(even).filter(divisible_by_four), 9), [0, 4, 8] * 3)


suite = unittest.TestLoader().loadTestsFromTestCase(TestFilteredCollection)
unittest.TextTestRunner(verbosity=2).run(suite)
