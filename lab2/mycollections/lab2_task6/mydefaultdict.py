#!/usr/bin/env python

__author__ = 'kinpa200296'


class mydefaultdict(object):
    def __init__(self):
        self._dict = dict()

    def __getitem__(self, item):
        if item not in self._dict:
            self._dict[item] = mydefaultdict()
        return self._dict[item]

    def __setitem__(self, key, value):
        self._dict[key] = value

    def __str__(self):
        return str(self._dict)

    def __repr__(self):
        return repr(self._dict)
