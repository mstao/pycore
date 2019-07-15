#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
定制类

__call__

"""

class Student(object):
    def __init__(self, name):
        self._name = name

    def __call__(self):
        print('My name is %s.' % self._name)


s = Student('Walker')

s()