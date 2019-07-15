#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
迭代器
"""

# 创建一个
g = (x * x for x in range(10))

print(g)

for n in g:
    print(n)

print("-----------")

# 打印斐波拉契数列

def fib(n):
    i, a, b = 0, 0 ,1
    while i < n:
        yield b
        t = (b, a + b)
        a = t[0]
        b = t[1]
        i += 1
    return "done"


gg = fib(6)
for n in gg:
    print(n)

# 捕获异常，获取返回值
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
         print('Generator return value:', e.value)
         break

# 输出奇数
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()

print(next(o))
print(next(o))
print(next(o))

print("---------杨辉三角-------")
# 杨辉三角
# C(n+1,i)=C(n,i)+C(n,i−1)

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

