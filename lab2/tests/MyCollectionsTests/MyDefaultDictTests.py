#!/usr/bin/env python

from mycollections import mydefaultdict
import unittest

__author__ = 'kinpa200296'


class TestMyDefaultDict(unittest.TestCase):
    def test1(self):
        d = mydefaultdict()
        d['abc']['def']['hij'] = 'klm'
        d['abc']['def']['543'] = 9.0
        d[5][2] = 3
        d[5][10] = 10
        d[0] = 1
        self.assertEqual(str(d), "{0: 1, 'abc': {'def': {'543': 9.0, 'hij': 'klm'}}, 5: {2: 3, 10: 10}}")

    def test_empty(self):
        d = mydefaultdict()
        self.assertEqual(str(d), '{}')

suite = unittest.TestLoader().loadTestsFromTestCase(TestMyDefaultDict)
unittest.TextTestRunner(verbosity=2).run(suite)
