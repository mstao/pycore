#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
定制类

__getattr__

"""

class Student(object):
    def __init__(self):
        self._name = 'Walker'

    def __getattr__(self, item):
        if item == 'score':
            return 99
        raise AttributeError('Student object has no attribute %s' % item)

s = Student()

print(s.score)