__author__ = 'kinpa200296'

from qsort import qsort
from mergesort import merge_sort
import wordcounter
import argparse
import fibonacci


def create_parser():
    p = argparse.ArgumentParser()
    p.add_argument("task", help="""choose one of the following tasks:
                                   qsort - sort array with quicksort;
                                   mergesort - sort array with mergesort;
                                   count - count words;
                                   top - print a sentence of top 10 words;
                                   fibonacci - print first N numbers of fibonacci sequence
                                """)
    p.add_argument("-i", "--input", help="specify input file")
    p.add_argument("-o", "--output", help="specify output file")
    p.add_argument("-q", "--quantity", help="specify quantity of fibonacci number to generate (default=10)",
                        type=int, default=10, metavar="N")
    return p


def read_array(filename):
    arr = []
    if filename is None:
        nums = raw_input("enter array: ").split()
        arr.extend([int(x) for x in nums])
    else:
        with open(filename, "r") as f:
            nums = f.readline().split()
            arr.extend([int(x) for x in nums])
    return arr


def print_array(filename, arr):
    if filename is None:
        print " ".join([str(x) for x in arr])
    else:
        with open(filename, "w") as f:
            f.write(" ".join([str(x) for x in arr]))


def do_qsort():
    arr = read_array(args.input)

    qsort(arr, 0, len(arr) - 1)

    print_array(args.output, arr)


def do_mergesort():
    arr = read_array(args.input)

    arr = merge_sort(arr)

    print_array(args.output, arr)


def do_count():
    wordcounter.analyze_file(args.input)
    wordcounter.print_result(args.output)


def do_top():
    wordcounter.analyze_file(args.input)
    with open(args.output, "w") as f:
        str = " ".join([x[0] for x in wordcounter.find_top10_words()])
        f.write(str)


def do_fibonacci():
    if args.output is None:
        for i in fibonacci.generator(args.quantity):
            print i
    else:
        with open(args.output, "w") as f:
            for i in fibonacci.generator(args.quantity):
                f.write(str(i) + "\n")


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    if args.task == "qsort":
        do_qsort()
    elif args.task == "mergesort":
        do_mergesort()
    elif args.task == "count":
        do_count()
    elif args.task == "top":
        do_top()
    elif args.task == "fibonacci":
        do_fibonacci()
    else:
        print "Invalid task parameter '{}'".format(args.task)
        parser.print_help()
