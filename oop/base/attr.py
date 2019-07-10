#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 属性

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
print(setattr(obj, 'y', 19))
print(getattr(obj, 'y'))
print(obj.x)

print('-------')
fn = getattr(obj, 'power')
print(fn)
print(fn())
