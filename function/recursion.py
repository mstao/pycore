#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 递归
def recursion(i):
    if i == 1:
        return 1
    return i * recursion(i-1)


print(recursion(5))

# 斐波那契数列
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


for n in range(5):
    print(fib(n + 1))
