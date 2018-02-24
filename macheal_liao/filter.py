#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/24  13:49
# @Author  : calvin

'''filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，

filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素'''

def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])))


#用filter求素数
def _odd_iter():    #先构造一个从3开始的奇数序列
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):   #然后定义一个筛选函数
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
# 打印100以内的素数:
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break


#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    # s = str(n)
    # m = len(s)//2
    # if len(s)%2 == 0:
    #     s1 = s[:m]
    #     s2 = s[m:][::-1]
    # else:
    #     s1 = s[:m]
    #     s2 = s[m+1:][::-1]
    # return s1 == s2
    return str(n) == str(n)[::-1]
print(list(filter(is_palindrome,range(1, 200))))


