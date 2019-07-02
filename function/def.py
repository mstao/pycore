#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def nop():
    pass


x, y = move(100, 100, 60, math.pi / 6)

print(x, y)
