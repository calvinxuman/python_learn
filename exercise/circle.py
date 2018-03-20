#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 10:07
# @Author  : calvin

class Circle():
    PI = 3.141695
    def __init__(self,radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self,r):
        self.__radius = r

    def length_circle(self):
        return 2*Circle.PI*self.__radius

    def area_circle(self):
        return Circle.PI*self.__radius*self.__radius
