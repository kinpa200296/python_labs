__author__ = 'kinpa200296'

from random import choice


def compare(a, b):
    return a < b


def qsort(a, l, r, comparator = compare):
    i, j = l, r
    pivot = a[choice(range(l, r))]
    while (i < j):
        while comparator(a[i], pivot):
            i += 1
        while comparator(pivot, a[j]):
            j -= 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
    if l < j:
        qsort(a, l, j)
    if i < r:
        qsort(a, i, r)
