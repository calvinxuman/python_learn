#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13  15:44
# @Author  : calvin



#题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
list1 = [x * x for x in range(100)]
for i in range(-100,2000):
    n = i + 100
    m = i + 268
    if n in list1 and m in list1:
        print(i)