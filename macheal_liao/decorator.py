#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 0027 13:25
# @Author  : calvin
import functools,time

# def now():
#     print('2015-3-25')
# f = now
# print(f())

'''函数对象有一个__name__属性，可以拿到函数的名字'''
# print(f.__name__)
# print(now.__name__)

'''现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）'''
# def log(func):
#     def wrapper(*args,**kwargs):
#         print('call function %s'%func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# @log
# def now():
#     print('2015-3-25')
# now()

'''由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，

于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。

wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，

首先打印日志，再紧接着调用原始函数'''


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本

# def log(text):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             print('%s %s'%(text,func.__name__))
#             return func(*args,**kwargs)
#         return wrapper
#     return  decorator
#
# @log('execute')
# def now():
#     print('2015-3-25')
# now()

'''以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，

它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的"now"变成了"wrapper"

因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的'''

# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args,**kwargs):
#         print('call %s():' % func.__name__)
#         return func(*args,**kwargs)
#     return wrapper

'''import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可'''

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        start = time.time()
        fn(*args,**kwargs)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end-start)* 1000))
        return fn(*args,**kwargs)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')