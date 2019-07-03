#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 取出
print(d.get('Bob'))

# 添加
d.update(c=3)
print(d['c'])

d.update(c=3, d=4)
print(d['d'])

d.update({'f': 6, 'g': 7})
print(d)

# 删除
d.pop('Michael')
print(d)

del d['Bob']
print(d)

# 遍历

print('遍历key')
for key in d.keys():
    print(key)

print('遍历value')
for value in d.values():
    print(value)

print('遍历key和value')
for item in d.items():
    print(item)