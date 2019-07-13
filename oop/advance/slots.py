#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

"""
使用__slots__

希望一个对象限制其属性，使用__slots__

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
"""

class Student(object):
    pass


s = Student();


# 动态给实例绑定一个属性
s.name = '11'
print(s.name)


# 动态给实例绑定一个方法
def set_name(self, name):
    self.name = name


s.set_name = MethodType(set_name, s)
s.set_name('9999')
print(s.name)

# 给类绑定一个
def set_score(self, score):
    self.score = score

Student.set_score = set_score

s.set_score(66)
print(s.score)


class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

