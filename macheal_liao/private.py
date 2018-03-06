#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/1  14:57
# @Author  : calvin


class Student():
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def set_gender(self,name):
        if name == 'female':
            self.__gender = 'female'
        elif name == 'male':
            self.__gender = 'male'
        else:
            print('Invalid gender!')

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

bart = Student('Bart', 'male')
print(bart.get_gender())
bart.set_gender('female')
print(bart.get_gender())
bart.set_gender('null')
print(bart.get_name())



