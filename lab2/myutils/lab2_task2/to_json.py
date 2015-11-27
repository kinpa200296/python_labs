#!/usr/bin/env python

__author__ = 'kipna200296'


def _process_string(val):
    res = str(repr(val))[1:-1]
    res = res.replace('\\\'', '\'')
    res = res.replace('"', '\\"')
    return res


def _process_key(key):
    if key is None:
        return 'null'
    else:
        return key


def _to_json(obj, level):
    if isinstance(obj, bool):
        if obj:
            result = 'true'
        else:
            result = 'false'
    elif obj is None:
        result = 'null'
    elif isinstance(obj, str):
        result = '"{data}"'.format(data=_process_string(obj))
    elif isinstance(obj, int) or isinstance(obj, float):
        result = str(obj)
    elif isinstance(obj, dict):
        result = '{{{data}}}'.format(
            data=', '.join('"{key}": {value}'.format(key=_process_key(key), value=_to_json(value, level + 1))
                           for key, value in obj.iteritems()))
    else:
        try:
            result = '[{data}]'.format(data=', '.join('{value}'.format(value=_to_json(value, level + 1))
                                                      for value in obj))
        except TypeError:
            result = '"{data}"'.format(data=obj)

    return result


def to_json(obj):
    return _to_json(obj, 0)
