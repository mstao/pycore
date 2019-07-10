#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
实例属性和类属性
"""

class Student(object):
    name = 'Walker' # 类属性


s = Student()
print(Student.name)
print(s.name)

s.name = 2222

print(s.name)
print(Student.name)

del s.name
print(s.name)

