__author__ = 'kinpa200296'


import re


result = {}


def reset():
    result.clear()


def analyze_string(string):
    for word in re.findall("\w+", string):
        if len(word) > 0:
            result[word] = result.get(word, 0) + 1


def analyze_file(filename):
    with open(filename, "r") as f:
        for line in f.readlines():
            analyze_string(line)


def print_result(filename=None):
    if filename is None:
        for item in result.items():
            print "'{}' counted {} times".format(item[0], item[1])
    else:
        with open(filename, "w") as f:
            for item in result.items():
                f.write("'{}' counted {} times\n".format(item[0], item[1]))


def find_top10_words():
    items = result.items()
    items.sort(key=lambda elem: elem[1], reverse=True)
    return items[0:10]
