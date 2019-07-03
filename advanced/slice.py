#!/usr/bin/env python3
# -*- coding: utf-8 -*-

data = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 切片 data[x:y] 从索引x开始取，直到索引y为止，不包括y
print(data[0:3])

# 如果从0开始取第一个参数可以省略
print(data[:3])

# 取倒数第二个
print(data[-2:-1])

# 取前三个
print('ABCDEFG'[:3])

# 取后三个
print('ABCDEFG'[-3:])
