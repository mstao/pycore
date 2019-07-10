#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

import types
from Person import Person

# type()

print(type(123))
print(type('222'))

print(type(123) == int)
print(type('222') == str)


# types

def fn():
    pass


print(type(fn) == types.FunctionType)
print(isinstance(fn, types.FunctionType))

print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

"""
dir:

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
"""


print(dir('123'))

print(dir(Person))