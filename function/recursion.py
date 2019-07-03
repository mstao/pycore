#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归
def recursion(i):
    if i == 1:
        return 1
    return i*recursion(i-1)


print(recursion(5))

