__author__ = 'kinpa200296'


def compare(a, b):
    return a < b


def merge_sort(a, comparator = compare):
    if len(a) <= 1:
        return a
    middle = len(a) / 2
    b = merge_sort(a[0:middle])
    c = merge_sort(a[middle:len(a)])
    a = []
    i, j = 0, 0
    while (i < len(b)) and (j < len(c)):
        if not comparator(b[i], c[j]):
            a.append(c[j])
            j += 1
        else:
            a.append(b[i])
            i += 1
    a.extend(b[i:])
    a.extend(c[j:])
    return a
