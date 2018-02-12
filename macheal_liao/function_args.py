#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/11 0011 14:35
# @Author  : calvin


#位置参数

def power(x,n):
    m = 1
    while n > 0:
        m = x*m
        n = n-1
    return m

#power(x, n)函数有两个参数：x和n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数x和n


#默认参数

def power(x,n=2):
    m = 1
    while n > 0:
        m = x*m
        n = n-1
    return m

'''设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

！！！定义默认参数要牢记一点：默认参数必须指向不变对象！！！！'''
#因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
#此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
#我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参数

'''在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来'''

def sum(*list):
    sum = 0
    for i in list:
        sum = sum + i*i
    return sum

print(sum(1,2,3,4,5,6))
#  *list表示把list这个列表中的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

list1 = [1,2,3]
print(sum(*list1))


#关键字参数
'''关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict'''
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Adam', 22, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#命名关键字参数
'''对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
这种方式定义的函数如下：'''

def person(name, age, *, city, job):
    print(name, age, city, job)

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


#命名关键字参数可以有缺省值，从而简化调用：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


#参数组合

'''在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。

但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

比如定义一个函数，包含上述若干种参数：'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


def product(*args):
    r = 1
    for i in args:
        r = r*i
    return r
print(product(5, 6, 7))









