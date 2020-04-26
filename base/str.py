#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符串
print(ord('A'))
print(ord('中'))
print(chr(66))

# 编码
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 占位符
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 数字转字符串
print("azxvc" + str(1111))


print(max(80, 100, 1000))
