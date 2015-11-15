__author__ = 'kinpa200296'


def generator(n):
    prev, cur = 0, 1
    for i in xrange(n):
        yield cur
        prev, cur = cur, prev + cur
