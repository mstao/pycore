#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
定义一个类

1.
用 __name 表示一个私有成员变量，外部不可直接访问

2. __init__ 表示类初始化函数，当创建一个对象的时候，需要调用此方法
"""

class Person(object):

    def __init__(self, name: str, age: int) -> None:
        self.__name = name
        self.__age = age

    def print(self):
        print('name=%s, age=%s' % (self.__name, self.__age))


p1 = Person('Walker', 20)
p1.age = 21

p1.print()
