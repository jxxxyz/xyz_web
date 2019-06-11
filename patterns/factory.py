# -*- encoding: utf-8 -*-
"""
@author: jiaxinxin
@license: (C) Copyright 2015-2019, Palmax Corporation Limited.
@contact:jiaxinxin@palmax.cn
@software: PyCharm
@file: factory.py
@time: 2019-06-11 11:08
@desc:
"""
from __future__ import unicode_literals
from __future__ import print_function


class GreekLocalizer(object):

    def __init__(self):
        self.translations = {"dog": "σκύλος", "cat": "γάτα"}

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer(object):

    def localize(self, msg):
        return msg


def get_localizer(language="English"):
    localizers = {
        "English": EnglishLocalizer,
        "Greek": GreekLocalizer,
    }
    return localizers[language]()


def main():
    """
    # Create our localizers
    >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")
    # Localize some text
    >>> for msg in "dog parrot cat bear".split():
    ...     print(e.localize(msg), g.localize(msg))
    dog σκύλος
    parrot parrot
    cat γάτα
    bear bear
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
