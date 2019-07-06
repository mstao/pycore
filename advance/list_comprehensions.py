#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

"""
列表生成式
"""

L = []
for x in range(1, 11):
    L.append(x * x)

# 使用列表生成式
print([x * x for x in range(1, 11)])

# 过滤数据
print([x * x for x in range(1, 11) if x % 2 != 0])

# 列出当前目录下的所有文件和目录名
print([d for d in os.listdir('.')])
