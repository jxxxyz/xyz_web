# -*- encoding: utf-8 -*-
"""
@author: jiaxinxin
@license: (C) Copyright 2015-2019, Palmax Corporation Limited.
@contact:jiaxinxin@palmax.cn
@software: PyCharm
@file: lazy_evaluation.py
@time: 2019-06-11 11:21
@desc:
"""
from __future__ import print_function
import functools


class lazy_property(object):

    def __init__(self, function):
        self.function = function
        functools.update_wrapper(self, function)

    def __get__(self, obj, type_):
        if obj is None:
            return self
        val = self.function(obj)
        obj.__dict__[self.function.__name__] = val
        return val


def lazy_property2(fn):
    atrr = '__lazy__' + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, atrr):
            setattr(self, atrr, fn(self))
        return getattr(self, atrr)

    return _lazy_property


class Person(object):

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.call_count2 = 0

    @lazy_property
    def relatives(self):
        relatives = 'Many relatives'
        return relatives

    @lazy_property2
    def parents(self):
        self.call_count2 += 1
        return 'Father and mother'


def main():
    """
    >>> Jhon = Person('Jhon', 'Coder')
    >>> Jhon.name
    'Jhon'
    >>> Jhon.occupation
    'Coder'
    # Before we access `relatives`
    >>> sorted(Jhon.__dict__.items())
    [('call_count2', 0), ('name', 'Jhon'), ('occupation', 'Coder')]
    >>> Jhon.relatives
    'Many relatives.'
    # After we've accessed `relatives`
    >>> sorted(Jhon.__dict__.items())
    [('call_count2', 0), ..., ('relatives', 'Many relatives.')]
    >>> Jhon.parents
    'Father and mother'
    >>> sorted(Jhon.__dict__.items())
    [('_lazy__parents', 'Father and mother'), ('call_count2', 1), ..., ('relatives', 'Many relatives.')]
    >>> Jhon.parents
    'Father and mother'
    >>> Jhon.call_count2
    1
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)

