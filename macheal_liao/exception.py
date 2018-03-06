#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5  14:49
# @Author  : calvin

# def div(a,b):
#     try:
#         return int(a)/int(b)
#     except ValueError:
#         print('数据类型错误！')
#     except ZeroDivisionError:
#         print('被除数不能为零！')
#     finally:
#         print('计算完成')
#
# A1 = input('请输入除数a:')
# A2 = input('请输入被除数b:')
#
# print(div(A1,A2))


from functools import reduce

def str2num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    try:
        return reduce(lambda acc, x: acc + x, ns)
    except TypeError:
        print('33333')

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

