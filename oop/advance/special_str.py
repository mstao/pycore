#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
定制类

__str__

"""

class Student(object):
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return 'Student object(name: %s)' % self._name
    __repr__ = __str__


s = Student('Walker')
print(s)
