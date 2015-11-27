#!/usr/bin/env python

from ModelField import ModelField

__author__ = 'kinpa200296'


class StringField(ModelField):
    @classmethod
    def convert(cls, value):
        try:
            return str(value)
        except TypeError:
            return None
