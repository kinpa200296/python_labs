#!/usr/bin/env python

from mymetaclasses import model_creator
import unittest

__author__ = 'kinpa200296'


class Man:
    __metaclass__ = model_creator.ModelCreator
    name = model_creator.StringField()
    age = model_creator.IntField()


class Student(Man):
    group = model_creator.StringField()
    address = model_creator.StringField()

    def __init__(self):
        self.inited = True


class TestModelCreator(unittest.TestCase):
    def test_empty_fields(self):
        man = Man(age=25)

        self.assertEqual(man.name, None)
        self.assertEqual(man.age, 25)

    def test_invalid_field(self):
        with self.assertRaises(TypeError):
            Man(age=(12, 2))

    def test_fields(self):
        man = Man(name='Pavel', age=19)

        self.assertEqual(man.name, 'Pavel')
        self.assertEqual(man.age, 19)

    def test_inherit(self):
        student = Student(name='Pavel', age=19, group='353505')

        self.assertEqual(student.name, 'Pavel')
        self.assertEqual(student.age, 19)
        self.assertEqual(student.group, '353505')
        self.assertTrue(student.inited)

suite = unittest.TestLoader().loadTestsFromTestCase(TestModelCreator)
unittest.TextTestRunner(verbosity=2).run(suite)
