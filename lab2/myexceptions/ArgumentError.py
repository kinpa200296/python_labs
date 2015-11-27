#!/usr/bin/env python

__author__ = 'kinpa200296'


class ArgumentError(Exception):
    def __init__(self, expected, actual, comment=None):
        self._expected = expected
        self._actual = actual
        self._comment = comment

    def __str__(self):
        prefix = 'Too {0} arguments.'.format('many' if (self._expected < self._actual) else 'few')
        middle = 'Got {actual} arguments, expected {expected}.'.format(actual=self._actual, expected=self._expected)
        if self._comment is None:
            return '{prefix} {middle}'.format(prefix=prefix, middle=middle)
        else:
            return '{prefix} {middle}\n{comment}'.format(prefix=prefix, middle=middle, comment=self._comment)
