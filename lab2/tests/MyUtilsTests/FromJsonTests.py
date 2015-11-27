#!/usr/bin/env python

from myutils import from_json
import unittest

__author__ = 'kinpa200296'


class TestToJson(unittest.TestCase):
    def test_1(self):
        json = self.__read_from_file('files/test1.json')
        json_obj = from_json(json)
        self.assertEqual(json_obj["escape_value"], 'line1\nline2')

    def test_2(self):
        json = self.__read_from_file('files/test2.json')
        json_obj = from_json(json)
        self.assertEqual(repr(json_obj),
                         "{'array': ['abc', 3212, None], 'object': {'key2': 'value 2', 'key1': 123}, 'bool': True}")

    def test_raise(self):
        with self.assertRaises(ValueError):
            from_json("{[[asd]")

    def __read_from_file(self, file_name):
        with open(file_name) as f:
            json = f.read()
        return json

suite = unittest.TestLoader().loadTestsFromTestCase(TestToJson)
unittest.TextTestRunner(verbosity=2).run(suite)
