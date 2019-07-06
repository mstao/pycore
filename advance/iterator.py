#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

# 迭代

# 判是否为可迭代对象

# str是否可迭代
print(isinstance('abc', Iterable))

# list是否可迭代
print(isinstance([1, 2, 3], Iterable))

# 整数是否可迭代
print(isinstance(123, Iterable))

# 输出下标和值
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 输出两个值
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(data):
    if len(data) == 0:
        return None, None
    min = max = data[0]
    for x in data:
        if x < min:
            min = x
        elif x > max:
            max = x
    return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
