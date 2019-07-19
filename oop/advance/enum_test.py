#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用枚举
"""

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday.Fri)

print(Weekday['Fri'])

print(Weekday.Fri.value)

print(Weekday['Fri'].value)

print(Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)