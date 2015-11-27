#!/usr/bin/env python

import re

__author__ = 'kinpa200296'


def from_json(json):
    return json_parser(json).parse()


class json_parser:
    def __init__(self, json):
        self._tr = text_reader(json)

    def parse(self):
        return self.__read_struct()

    def __read_struct(self):
        if self._tr.starts_with('{'):
            return self.__read_obj()
        elif self._tr.starts_with('['):
            return self.__read_arr()
        else:
            return self.__read_value()

    def __read_obj(self):
        tr = self._tr
        obj = dict()

        tr.read('{')
        while True:
            key_value = self.__read_key_value()
            obj[key_value[0]] = key_value[1]
            if tr.starts_with(','):
                tr.read(',')
            else:
                break
        tr.read('}')

        return obj

    def __read_key_value(self):
        key = self._tr.try_read_quoted_str()
        self._tr.read(':')
        value = self.__read_struct()
        return key, value

    def __read_arr(self):
        tr = self._tr
        obj = []

        tr.read('[')
        while True:
            struct = self.__read_struct()
            obj.append(struct)
            if tr.starts_with(','):
                tr.read(',')
            else:
                break
        tr.read(']')

        return obj

    def __read_value(self):
        number = self._tr.try_read_number()
        if number is not None:
            return number

        string = self._tr.try_read_quoted_str()
        if string:
            return string

        name = self._tr.try_read_str()
        if name == 'null':
            return None
        elif name == 'true':
            return True
        elif name == 'false':
            return False

        raise ValueError('Could not read value from json')


class text_reader:
    def __init__(self, text):
        self._text = text
        self._pos = 0

    def starts_with(self, value):
        self.__skip_blank()
        return self._text[self._pos:][:len(value)] == value

    def read(self, value):
        if self.starts_with(value):
            self._pos += len(value)
            return value
        raise ValueError('Could not read {0} from position {1} in text'.format(value, self._pos))

    def try_read_number(self):
        self.__skip_blank()
        s = self.__read_regex(r'^([0-9]+)')
        if s:
            return int(s)
        return None

    def try_read_str(self):
        self.__skip_blank()
        return self.__read_regex(r'^(\w+)')

    def try_read_quoted_str(self):
        self.__skip_blank()
        s = self.__read_regex(r'^\"(([\w,\s]|\\\S)+)\"')
        if s:
            return s[1:-1].decode('string_escape')
        return None

    def __skip_blank(self):
        self.__read_regex(r'^\s+')

    def __read_regex(self, regex):
        m = re.search(regex, self._text[self._pos:])
        if m:
            res = m.group(0)
            self._pos += len(res)
            return res
        return None
