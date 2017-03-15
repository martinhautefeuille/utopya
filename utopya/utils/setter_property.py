#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Martin Hautefeuille
# Utopya Project
# Copyright (c) 2017 Martin Hautefeuille & Adrián Rosolen


class SetterProperty:
    """Setter decorator that does not need the @property getter decorator

    Please see discussion:
        http://stackoverflow.com/questions/17576009/python-class-property-use-setter-but-evade-getter
    """
    def __init__(self, func, doc=None):
        self.func = func
        self.__doc__ = doc if doc is not None else func.__doc__

    def __set__(self, obj, value):
        return self.func(obj, value)


# end of file
