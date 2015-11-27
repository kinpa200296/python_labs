#!/usr/bin/env python

from myutils import sort_utility
import unittest

__author__ = 'kinpa200296'


input_file = 'files/input.txt'
output_file = 'files/output.txt'
max_num = 1000000


def _test_correct_sort(count):
    sort_utility.generate(count, input_file, max_num)

    sort_utility.sort(input_file, output_file)

    return sort_utility.check_if_sorted(output_file)


class TestMergesort(unittest.TestCase):
    def test_correct_sort_0(self):
        self.assertTrue(_test_correct_sort(0))

    def test_correct_sort_1000(self):
        self.assertTrue(_test_correct_sort(1000))

    def test_big_sort(self):
        self.assertTrue(_test_correct_sort(100000))

suite = unittest.TestLoader().loadTestsFromTestCase(TestMergesort)
unittest.TextTestRunner(verbosity=2).run(suite)
