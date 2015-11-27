#!/usr/bin/env python

__author__ = 'kinpa200296'


def cached(func):

    cache = dict()

    def wrapper(*args, **kwargs):
        key = (func, args, tuple(kwargs.keys()), tuple(kwargs.values()))

        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        else:
            return cache[key]

    return wrapper
