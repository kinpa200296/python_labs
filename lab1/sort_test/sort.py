__author__ = 'kinpa200296'


import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", help="specify input file")
parser.add_argument("-o", "--output", help="specify output file")
args = parser.parse_args()

arr = []

if args.input is None:
    nums = raw_input("enter array: ").split()
    arr.extend([int(x) for x in nums])
else:
    with open(args.input, "r") as f:
        nums = f.readline().split()
        arr.extend([int(x) for x in nums])

arr.sort()

if args.output is None:
    print " ".join([str(x) for x in arr])
else:
    with open(args.output, "w") as f:
        f.write(" ".join([str(x) for x in arr]))
