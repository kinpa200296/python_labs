#!/usr/bin/env python

from myexceptions import ArgumentError

__author__ = 'kinpa200296'


class myxrange(object):
    def __init__(self, *args):
        args_count = len(args)

        if args_count not in [1, 2, 3]:
            raise ArgumentError('1, 2 or 3', args_count)

        self._start = 0
        self._step = 1
        if args_count == 1:
            self._stop = args[0]
        elif args_count >= 2:
            self._start = args[0]
            self._stop = args[1]
            if args_count == 3:
                self._step = args[2]

        if self._step == 0:
            raise ValueError('myxrange: step(argument 3) must not be zero')

    def __iter__(self):
        self._current = self._start
        return self

    def next(self):
        if self._step > 0:
            if self._current >= self._stop:
                raise StopIteration
        else:
            if self._current <= self._stop:
                raise StopIteration

        value = self._current
        self._current += self._step
        return value
