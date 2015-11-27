#!/usr/bin/env python

from ModelField import ModelField

__author__ = 'kinpa200296'


class IntField(ModelField):
    @classmethod
    def convert(cls, value):
        try:
            return int(value)
        except TypeError:
            return None
