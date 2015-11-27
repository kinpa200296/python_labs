#!/usr/bin/env python

import random
import argparse

__author__ = 'kinpa200296'


def generate(count, filename, max_num):
    with open(filename, 'w') as f:
        for _ in xrange(count):
            f.write('{0}\n'.format(random.randint(-max_num, max_num)))


def execute_from_command_line():
    p = argparse.ArgumentParser()
    p.description = 'generates file of numbers separated by line feed'
    p.add_argument('output_file', help='specify output file')
    p.add_argument('-q', '--quantity', help='specify quantity of numbers to generate (default=100)',
                   type=int, default=100, metavar='Q')
    p.add_argument('-m', '--max_num', help='specify range in which to generate numbers (default=1000000)',
                   type=int, default=1000000, metavar='M')
    args = p.parse_args()

    print 'Starting generating {0} numbers in range[-{1}, {1}]...'.format(args.quantity, args.max_num)
    generate(args.quantity, args.output_file, args.max_num)
    print 'Done...'

if __name__ == '__main__':
    execute_from_command_line()
