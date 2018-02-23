#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/23  14:38
# @Author  : calvin

from functools import reduce

'''map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回'''

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


'''reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算'''

def fn(x, y):
    return x * 10 + y
#print(reduce(fn, [1, 3, 5, 7, 9]))


#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name.capitalize()
print(list(map(normalize,['adam', 'LISA', 'barT'])))