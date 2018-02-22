#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/22  15:25
# @Author  : calvin

#生成器
L = [x * x for x in range(10)]
g = (x * x for x in range(10))
'''通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。
创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：'''
print(next(g))
print(next(g))
print(next(g))

'''generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误'''

'''如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：'''

def fab(max):
    n,a,b =0,0,1
    while n < max:
        print(b)
        a,b = b,a+b
        n = n+1
    return 'done'
'''仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，

可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了

这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generato'''


#杨辉三角
def triangles():
    L = [1]
    while  True:
        yield L
        L.append(0)
        L=[L[i-1] + L[i] for i in range(len(L))]

print(next(L))
print(next(triangles()))
print(next(triangles()))
print(next(triangles()))
print(next(triangles()))
