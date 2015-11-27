#!/usr/bin/env python

from ModelField import ModelField

__author__ = 'kinpa200296'


class ModelCreator(type):
    def __new__(mcs, name, bases, attrs):
        old_init = attrs.get('__init__', None)

        def new_init(self, *args, **kwargs):
            fields_found = []
            for key in kwargs:
                if hasattr(self, key) and _fill_field(self, key, kwargs[key]):
                    fields_found.append(key)
            for field in fields_found:
                del kwargs[field]

            for attr in dir(self):
                if isinstance(getattr(self, attr), ModelField):
                    setattr(self, attr, None)

            if old_init is not None:
                old_init(self, *args, **kwargs)

        attrs['__init__'] = new_init

        return super(ModelCreator, mcs).__new__(mcs, name, bases, attrs)


def _fill_field(inst, key, value):
    attr = getattr(inst, key)
    if isinstance(attr, ModelField):
        converted_value = attr.convert(value)
        if converted_value is None:
            raise TypeError('Cannot convert {value} to {field}'.format(value=value, field=attr.__class__.__name__))
        setattr(inst, key, converted_value)
        return True
    return False
