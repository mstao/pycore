#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 初始化list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# 取第一个元素
print(classmates[0])

# 取最后一个元素
print(classmates[-1])

# 追加元素到末尾
classmates.append("Mary")
print(classmates)

# 把元素插入到指定的位置
classmates.insert(1, "Walker")
print(classmates)

# 删除最后一个元素
classmates.pop()
print(classmates)

# 删除指定位置的元素
classmates.pop(3)
print(classmates)

# 替换指定位置元素
classmates[0] = "OK"
print(classmates)

# 获取长度
print(len(classmates))
