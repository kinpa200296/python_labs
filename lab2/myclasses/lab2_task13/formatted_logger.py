#!/usr/bin/env python

import re

__author__ = 'kinpa200296'


class FormattedLogger(object):
    def __init__(self, **kwargs):
        self._logs = []
        if 'format' in kwargs:
            specifiers = [spec[1:-1] for spec in re.findall('{\w*}', kwargs['format'])]
            for spec in specifiers:
                if spec not in ['func_name', 'arguments', 'res', 'args', 'kwargs']:
                    raise ValueError('Specifier "{spec}" is not allowed.'.format(spec=spec))
            self._format = kwargs['format']
        else:
            self._format = '{func_name}({arguments}) = {res}'
        pass

    def __getattribute__(self, item):
        try:
            super(FormattedLogger, self).__getattribute__('_logs')
        except AttributeError:
            raise TypeError('You should call Logger constructor when inheriting from it')

        attr = super(FormattedLogger, self).__getattribute__(item)

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
        args_str = ', '.join(args_strings)
        kwargs_str = ', '.join(kwargs_strings)
        log_str = self._format.format(func_name=item, res=result, arguments=arguments_str,
                                      args=args_str, kwargs=kwargs_str)
        self._logs.append(log_str)
        return log_str

    def __str__(self):
        return '\n'.join(self._logs)

    def __repr__(self):
        return repr(self.__str__())
