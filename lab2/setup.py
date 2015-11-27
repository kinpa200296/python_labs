#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='lab2',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'readme.txt')).read(),
    scripts=['myutils/lab2_task1/checker.py', 'myutils/lab2_task1/gen.py', 'myutils/lab2_task1/mergesort.py'],
    entry_points={
        'console_scripts': [
            'lab2_sort = myutils.lab2_task1.mergesort:execute_from_command_line',
            'lab2_gen = myutils.lab2_task1.gen:execute_from_command_line',
            'lab2_check = myutils.lab2_task1.checker:execute_from_command_line'
        ]
        },
    install_requires=[
    ]
)
