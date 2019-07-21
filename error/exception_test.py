#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
try
catch
finally

https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')