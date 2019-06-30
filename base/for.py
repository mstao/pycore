#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break
n2 = 1
while n2 <= 100:
    if n2 > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n2)
    n2 = n2 + 1
print('END')

# continue
n3 = 0
while n3 < 10:
    n3 = n3 + 1
    if n3 % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n3)
