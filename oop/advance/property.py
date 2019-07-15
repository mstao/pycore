#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用@property
"""


class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be int')
        if value < 0 or value > 100:
            raise ValueError('Score must be between 0 and 100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


s = Student()
s.score = 100
print(s.score)
