#!/usr/bin/env python

__author__ = 'kinpa200296'


class Logger(object):
    def __init__(self):
        self._logs = []
        pass

    def __getattribute__(self, item):
        try:
            super(Logger, self).__getattribute__('_logs')
        except AttributeError:
            raise TypeError('You should call Logger constructor when inheriting from it')

        attr = super(Logger, self).__getattribute__(item)

        if item not in ['_log', '_logs', '__str__'] and hasattr(attr, '__call__'):
            def wrapper(*args, **kwargs):
                result = attr(*args, **kwargs)
                self._log(item, result, *args, **kwargs)
                return result

            return wrapper
        else:
            return attr

    def _log(self, item, result, *args, **kwargs):
        kwargs_strings = ['{key}={value}'.format(key=key, value=value) for key, value in kwargs.iteritems()]
        args_strings = [str(x) for x in args]
        arguments_str = ', '.join(args_strings + kwargs_strings)
        log_str = '{func_name}({arguments}) = {res}'.format(func_name=item, res=result, arguments=arguments_str)
        self._logs.append(log_str)
        return log_str

    def __str__(self):
        return '\n'.join(self._logs)

    def __repr__(self):
        return repr(self.__str__())
