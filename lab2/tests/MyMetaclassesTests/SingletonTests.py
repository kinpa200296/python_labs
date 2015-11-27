#!/usr/bin/env python

from mymetaclasses import Singleton
import unittest

__author__ = 'kinpa200296'


class TestSingleton(unittest.TestCase):
    def test_instance_equal(self):
        class Dummy(object):
            __metaclass__ = Singleton

        a1 = Dummy()
        a2 = Dummy()

        self.assertTrue(a1 is a2)

    def test_two_different_classes(self):
        class Dummy1(object):
            __metaclass__ = Singleton

        class Dummy2(object):
            __metaclass__ = Singleton

        a = Dummy1()
        b = Dummy2()

        self.assertFalse(a is b)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSingleton)
unittest.TextTestRunner(verbosity=2).run(suite)
