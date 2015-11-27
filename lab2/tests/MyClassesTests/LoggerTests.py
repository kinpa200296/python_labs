#!/usr/bin/env python

from myclasses import Logger
import unittest

__author__ = 'kinpa200296'

test_res = '''say_hello() = Hello, world!
say_hello(name=Bob) = Hello, Bob!
calc_sum(10, 20) = 30
calc_sum(3, 4) = 7
say_age(18) = John is 18.
say_age(18, name=Bob) = Bob is 18.'''


class Dummy(Logger):
    @staticmethod
    def say_hello(name=None):
        if name is None:
            return 'Hello, world!'
        else:
            return 'Hello, {name}!'.format(name=name)

    @staticmethod
    def calc_sum(a, b):
        return a + b

    @staticmethod
    def say_age(age, name='John'):
        return '{name} is {age}.'.format(name=name, age=age)


class BadDummy(Logger):
    def __init__(self):
        pass


class TestLogger(unittest.TestCase):
    def test_wrong_inheritance(self):
        with self.assertRaises(TypeError):
            bad_dummy = BadDummy()
            bad_dummy.func()

    def test_empty_log(self):
        dummy = Dummy()
        self.assertEqual(str(dummy), '')

    def test_logs(self):
        dummy = Dummy()
        dummy.say_hello()
        dummy.say_hello(name='Bob')
        dummy.calc_sum(10, 20)
        dummy.calc_sum(3, 4)
        dummy.say_age(18)
        dummy.say_age(18, name='Bob')

        self.assertEqual(str(dummy), test_res)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLogger)
unittest.TextTestRunner(verbosity=2).run(suite)
