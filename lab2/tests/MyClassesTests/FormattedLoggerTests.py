#!/usr/bin/env python

from myclasses import FormattedLogger
import unittest

__author__ = 'kinpa200296'

test_res1 = '''say_hello() = Hello, world!
say_hello(name=Bob) = Hello, Bob!
calc_sum(10, 20) = 30
calc_sum(3, 4) = 7
say_age(18) = John is 18.
say_age(18, name=Bob) = Bob is 18.'''

test_res2 = '''say_hello() = Hello, world!
say_hello() = Hello, Bob!
calc_sum() = 30
calc_sum() = 7
say_age() = John is 18.
say_age() = Bob is 18.'''

test_res3 = '''say_hello: (),() -> Hello, world!
say_hello: (),(name=Bob) -> Hello, Bob!
calc_sum: (10, 20),() -> 30
calc_sum: (3, 4),() -> 7
say_age: (18),() -> John is 18.
say_age: (18),(name=Bob) -> Bob is 18.'''

test_res4 = '''say_hello: () -> Hello, world!
say_hello: (name=Bob) -> Hello, Bob!
calc_sum: (10, 20) -> 30
calc_sum: (3, 4) -> 7
say_age: (18) -> John is 18.
say_age: (18, name=Bob) -> Bob is 18.'''


class Dummy(FormattedLogger):
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


class BadDummy(FormattedLogger):
    def __init__(self):
        pass


class TestFormattedLogger(unittest.TestCase):
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

        self.assertEqual(str(dummy), test_res1)

    def test_formatting(self):
        dummy = Dummy(format='{func_name}() = {res}')
        dummy.say_hello()
        dummy.say_hello(name='Bob')
        dummy.calc_sum(10, 20)
        dummy.calc_sum(3, 4)
        dummy.say_age(18)
        dummy.say_age(18, name='Bob')

        self.assertEqual(str(dummy), test_res2)

        dummy = Dummy(format='{func_name}: ({args}),({kwargs}) -> {res}')
        dummy.say_hello()
        dummy.say_hello(name='Bob')
        dummy.calc_sum(10, 20)
        dummy.calc_sum(3, 4)
        dummy.say_age(18)
        dummy.say_age(18, name='Bob')

        self.assertEqual(str(dummy), test_res3)

        dummy = Dummy(format='{func_name}: ({arguments}) -> {res}')
        dummy.say_hello()
        dummy.say_hello(name='Bob')
        dummy.calc_sum(10, 20)
        dummy.calc_sum(3, 4)
        dummy.say_age(18)
        dummy.say_age(18, name='Bob')

        self.assertEqual(str(dummy), test_res4)

    def test_bad_format_string(self):
        with self.assertRaises(ValueError):
            Dummy(format='{dummy}')

suite = unittest.TestLoader().loadTestsFromTestCase(TestFormattedLogger)
unittest.TextTestRunner(verbosity=2).run(suite)
