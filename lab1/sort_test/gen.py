__author__ = 'kinpa200296'


import argparse
from random import randint


parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="specify output file")
parser.add_argument("count", help="number of arguments to generate", type=int)
parser.add_argument("--max", help="max number that can be generated", type=int, default=10 ** 9)
parser.add_argument("--min", help="min number that can be generated", type=int, default=0)
args = parser.parse_args()

res = []
for i in xrange(args.count):
    res.append(randint(args.min, args.max))

if args.output is None:
    print " ".join([str(x) for x in res])
else:
    with open(args.output, "w") as f:
        f.write(" ".join([str(x) for x in res]))
