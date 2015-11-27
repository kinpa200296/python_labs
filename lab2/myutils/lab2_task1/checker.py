#!/usr/bin/env python

import argparse

__author__ = 'kinpa200296'


def check_if_sorted(filename, ascending=True):
    with open(filename, 'r') as f:
        s = f.readline()

        if s == '':
            return True

        prev = int(s)
        s = f.readline()
        while s != '':
            cur = int(s)
            if ascending:
                if cur >= prev:
                    prev = cur
                else:
                    return False
            else:
                if cur <= prev:
                    prev = cur
                else:
                    return False
            s = f.readline()
        return True


def execute_from_command_line():
    p = argparse.ArgumentParser()
    p.description = 'checks if number in specified file are sorted in ascending order'
    p.add_argument('input_file', help='specify input file')
    args = p.parse_args()

    print 'Starting check of file {}...'.format(args.input_file)

    if check_if_sorted(args.input_file):
        print 'Numbers are sorted ascending'
    else:
        print 'Numbers are not sorted ascending'

if __name__ == '__main__':
    execute_from_command_line()
