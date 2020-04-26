#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

"""
fork
"""

name = input("请输入你的名字：")
print("welcome to my python world！",name)
weight1 = input("请输入你现在的体重：")
weight2 = input("请输入你的目标体重：")
print(name,"你还需要减重",int(weight1) - int(weight2),"斤呢~")
slogan = input("请输入你的口号：")
print(name,"朝着你的目标努力吧！",slogan,"你会成功的！")