#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This is a test moudle
"""

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 私有函数
def _p1():
    print('111111111111')


if __name__ == '__main__':
    test()