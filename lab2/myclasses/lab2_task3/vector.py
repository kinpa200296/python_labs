#!/usr/bin/env python

from numbers import Number
from math import sqrt

__author__ = 'kinpa200296'


class Vector(object):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            data = args[0]
        else:
            data = args

        if any([not isinstance(value, Number) for value in data]):
            raise TypeError('You can only pass values of numeric types or 1 list of numeric values')

        self._values = [value for value in data]

    def __str__(self):
        return str(tuple(self._values))

    def __repr__(self):
        return "'{0}'".format(self.__str__())

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors sizes don\'t match')
        return Vector([x + y for x, y in zip(self._values, other._values)])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('Vectors sizes don\'t match')
        return Vector([x - y for x, y in zip(self._values, other._values)])

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('Vectors sizes don\'t match')
            return sum([x*y for x, y in zip(self._values, other._values)])
        else:
            return Vector([x*other for x in self._values])

    def __eq__(self, other):
        return all([x == y for x, y in zip(self._values, other._values)])

    def __abs__(self):
        return sqrt(sum([x*x for x in self._values]))

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values[item]

    def __setitem__(self, key, value):
        self._values[key] = value
