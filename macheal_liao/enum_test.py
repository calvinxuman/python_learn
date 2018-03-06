#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/5  13:42
# @Author  : calvin

from enum import Enum,unique

'''当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份:'''
JAN = 1
FEB = 2
MAR = 3

'''好处是简单，缺点是类型是int，并且仍然是变量。

更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：'''

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

'''value属性则是自动赋给成员的int常量，默认从1开始计数。

如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：'''
@unique
class Week(Enum):
    Sunday = 0 # Sun的value被设定为0
    Monday = 1
    Tuesday = 2
    Wedsday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6

'''@unique装饰器可以帮助我们检查保证没有重复值。

访问这些枚举类型可以有若干种方法：

既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。'''
print(Week.Sunday)
print(Week(1))
print(Week['Tuesday'])

#把Student的gender属性改造为枚举类型，可以避免使用字符串：

# class Gender(Enum):
#     Male = 0
#     Female = 1
#
# class Student():
#     def __init__(self,name,gender):
#         self.__name = name
#         self.__gender = gender
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def gender(self):
#         return self.__gender
#
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('测试通过!')
# else:
#     print('测试失败!')
# print(bart.gender)
