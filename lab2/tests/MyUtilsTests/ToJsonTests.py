#!/usr/bin/env python

from myutils import to_json
import unittest
import json

__author__ = 'kinpa200296'


class TestToJson(unittest.TestCase):
    def test1(self):
        obj = None
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test2(self):
        obj = {"id": 100500, "name": "ahaha", "marks": [5, 7, 5, 8],  "is_valid": True}
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test3(self):
        obj = {None: 1}
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test4(self):
        obj = '\'\"'
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test5(self):
        obj = '\n'
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test6(self):
        obj = {True: 1}
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test7(self):
        obj = '\\'
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test8(self):
        obj = None
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test9(self):
        obj = [None, {1: ["1", {"2": 2}]}, False, 3, "3"]
        self.assertEqual(to_json(obj), json.dumps(obj))

    def test10(self):
        obj = {'None': 1}
        self.assertEqual(to_json(obj), json.dumps(obj))


suite = unittest.TestLoader().loadTestsFromTestCase(TestToJson)
unittest.TextTestRunner(verbosity=2).run(suite)
