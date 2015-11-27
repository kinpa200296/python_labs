#!/usr/bin/env python

import tempfile
import argparse

__author__ = 'kinpa200296'


max_elem_in_memory = 100


def merge(n1, n2, f1, f2, fout):
    i = 0
    j = 0
    a1 = int(f1.readline())
    a2 = int(f2.readline())
    while i < n1 or j < n2:
        if i == n1 or (j != n2 and a2 < a1):
            fout.write('{0}\n'.format(a2))
            j += 1
            if j < n2:
                a2 = int(f2.readline())

        else:
            fout.write('{0}\n'.format(a1))
            i += 1
            if i < n1:
                a1 = int(f1.readline())


def merge_sort(n, fin, fout):
    if n <= max_elem_in_memory:
        data = [int(fin.readline()) for _ in xrange(n)]
        data.sort()
        for val in data:
            fout.write('{0}\n'.format(val))
        return

    f1 = tempfile.TemporaryFile()
    f2 = tempfile.TemporaryFile()

    n1 = n/2
    n2 = n - n1
    merge_sort(n1, fin, f1)
    merge_sort(n2, fin, f2)

    f1.seek(0)
    f2.seek(0)

    merge(n1, n2, f1, f2, fout)

    f1.close()
    f2.close()


def sort(input_file, output_file):
    with open(input_file, 'r') as file_in:
        n = sum(1 for _ in file_in)
        file_in.seek(0)

        with open(output_file, 'w') as file_out:
            merge_sort(n, file_in, file_out)


def execute_from_command_line():
    p = argparse.ArgumentParser()
    p.description = 'sorts large files of numbers separated by line feed using mergesort'
    p.add_argument('input_file', help='specify input file')
    p.add_argument('output_file', help='specify output file')
    p.add_argument('-m', '--mem_size', help='specify quantity of numbers which can fit into memory (default=100)',
                   type=int, default=100, metavar='M')
    args = p.parse_args()

    print 'Starting sorting file {}...'.format(args.input_file)
    global max_elem_in_memory
    max_elem_in_memory = args.mem_size
    sort(args.input_file, args.output_file)
    print 'Done...'

if __name__ == '__main__':
    execute_from_command_line()
