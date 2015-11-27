#!/usr/bin/env python

from myexceptions import ArgumentError

__author__ = 'kinpa200296'


class LinearFunc(object):
    def __init__(self, k, b):
        self._k = k
        self._b = b

    def __str__(self):
        str_format = ''

        if self._k != 0:
            str_format += '{k}x'
            if self._b != 0:
                str_format += ' {sign} {b}'
        else:
            if self._b < 0:
                str_format += '{sign}{b}'
            else:
                str_format += '{b}'

        return str_format.format(k=self._k, b=abs(self._b), sign='+' if self._b > 0 else '-')

    def __repr__(self):
        return repr(self.__str__())

    def __call__(self, *args):
        if len(args) != 1:
            raise ArgumentError(1, len(args), 'Only 1 argument is expected.')

        if isinstance(args[0], LinearFunc):
            return self._composition(args[0])

        return self._k*args[0] + self._b

    def __add__(self, other):
        return LinearFunc(self._k + other._k, self._b + other._b)

    def __mul__(self, other):
        if isinstance(other, LinearFunc):
            return self._composition(other)

        return LinearFunc(self._k*other, self._b*other)

    def __eq__(self, other):
        if isinstance(other, LinearFunc):
            return self._k == other._k and self._b == other._b
        else:
            return False

    def _composition(self, other):
        if not isinstance(other, LinearFunc):
            raise TypeError('an instance of LinearFunc expected, but got {0}'.format(str(other.__class__)))

        return LinearFunc(self._k*other._k, self._k*other._b + self._b)
