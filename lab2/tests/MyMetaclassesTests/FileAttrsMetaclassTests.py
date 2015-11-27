#!/usr/bin/env python

from mymetaclasses import FileAttrsMetaclassFactory
import unittest
import os.path

__author__ = 'kinpa200296'

filename = 'attributes.txt'
data = {
    'attr1': 'value1',
    'attr2': 'value2',
    'attr3': 'value3'
}


def write_to_file(d, file_name):
    with open(file_name, 'w') as f:
        for key, value in d.iteritems():
            f.write('"{key}":"{value}"\n'.format(key=key, value=value))


class TestFileAttrsMetaclass(unittest.TestCase):
    def test_no_attributes_file(self):
        if os.path.isfile(filename):
            os.remove(filename)

        with self.assertRaises(IOError):
            class Dummy(object):
                __metaclass__ = FileAttrsMetaclassFactory(filename)

                hello_str = 'Hello world'

            d = Dummy()
            for key, value in data.iteritems():
                self.assertEqual(value, getattr(d, key))
            self.assertEqual('Hello world', getattr(d, 'hello_str'))

    def test_empty_attributes(self):
        data = {}
        write_to_file(data, filename)

        class Dummy(object):
            __metaclass__ = FileAttrsMetaclassFactory(filename)

            hello_str = 'Hello world'

        d = Dummy()
        for key, value in data.iteritems():
            self.assertEqual(value, getattr(d, key))
        self.assertEqual('Hello world', getattr(d, 'hello_str'))

    def test_add_some_attributes(self):
        write_to_file(data, filename)

        class Dummy(object):
            __metaclass__ = FileAttrsMetaclassFactory(filename)

            hello_str = 'Hello world'

        d = Dummy()
        for key, value in data.iteritems():
            self.assertEqual(value, getattr(d, key))
        self.assertEqual('Hello world', getattr(d, 'hello_str'))

    def test_bad_file_data(self):
        data = {
            'attr1': '"value1"',
            'attr2': 'value2',
            'attr3': 'value3'
        }
        write_to_file(data, filename)

        with self.assertRaises(ValueError):
            class Dummy(object):
                __metaclass__ = FileAttrsMetaclassFactory(filename)

                hello_str = 'Hello world'

            d = Dummy()
            for key, value in data.iteritems():
                self.assertEqual(value, getattr(d, key))
            self.assertEqual('Hello world', getattr(d, 'hello_str'))

suite = unittest.TestLoader().loadTestsFromTestCase(TestFileAttrsMetaclass)
unittest.TextTestRunner(verbosity=2).run(suite)
