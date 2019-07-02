#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 默认参数
# 默认参数必须指向不变对象！

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 2))


def add_end(s=None):
    if s is None:
        s = []
    s.append('END')
    return s


# 可变参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple

def calcu(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calcu(1, 2, 3))

nums = [1, 2, 3]
print(calcu(*nums))


# 关键字参数
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Walker', 20)
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数

def person(name, age, *, city, job):
    print(name, age, city, job)


person('Walker', 20, city='2222', job='zzz')

def product(*numbers):
    sum = 1
    for n in numbers:
        sum *= n
    return sum


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试成功!')
    except TypeError:
        print('测试失败!')

