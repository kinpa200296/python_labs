#!/usr/bin/env python

__author__ = 'kinpa200296'


class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instance
