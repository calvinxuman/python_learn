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
    name = name[0].upper()+name[1:].lower()
    return name
    #return name.capitalize()
#print(list(map(normalize,['adam', 'LISA', 'barT'])))


#请编写一个prod()函数，可以接受一个list并利用reduce()求积
def prod(L):
    def multiply(x,y):
        return x*y
    return reduce(multiply,L)
#print(prod([3, 5, 7, 9]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    s1 = s.split('.')[0]  #取整数部分
    s2 = s.split('.')[1][::-1]   #取小数部分并倒序排列
    def str2int(st):
        d1 = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        return d1[st]
    i1 = list(map(str2int,s1))  #生成整数部分（整形），并转化为列表
    i2 = list(map(str2int,s2))  #生成小数部分（整形），并转化为列表
    def f1(a,b):
        return a*10 + b
    def f2(a,b):
        return a*0.1 + b
    return reduce(f1,i1)+reduce(f2,i2)*0.1
print(str2float('123.45600'))

