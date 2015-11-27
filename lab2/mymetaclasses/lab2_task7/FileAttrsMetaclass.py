#!/usr/bin/env python

__author__ = 'kinpa200296'


def FileAttrsMetaclassFactory(filename):
    class FileAttrsMetaclass(type):

        __filename = filename

        def __new__(mcs, name, bases, attrs):
            with open(mcs.__filename, 'r') as f:
                for line in f.read().splitlines():
                    try:
                        key, separator, value = line.split('"')[1:-1]
                    except:
                        raise ValueError(
                            'line {line} in file {filename} is incorrect. Only "name":"value" is correct'.format(
                                line=line, filename=mcs.__filename))
                    if key in attrs:
                        raise KeyError('Class {name} already has key = {key}', name=name, key=key)
                    else:
                        attrs[key] = value

            return super(FileAttrsMetaclass, mcs).__new__(mcs, name, bases, attrs)

    return FileAttrsMetaclass
