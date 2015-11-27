#!/usr/bin/env python

__author__ = 'kinpa200296'


def generator(iterable, func):
    while True:
        for val in iterable:
            if func(val):
                yield val


class FilteredCollection(object):
    def __init__(self, iterable):
        try:
            self._iterable = iterable
            self._iter = iter(self._iterable)
        except TypeError:
            raise TypeError('first argument must be iterable')
        if not isinstance(self._iterable, type(generator([], lambda x: x))):
            if len(self._iterable) == 0:
                raise ValueError('Cannot make infinitive source out of empty collection')

    def __iter__(self):
        return self

    def next(self):
        try:
            return self._iter.next()
        except StopIteration:
            self._iter = iter(self._iterable)
            return self._iter.next()

    def filter(self, func):
        return FilteredCollection(generator(self._iterable, func))
