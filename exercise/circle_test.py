#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 0015 10:57
# @Author  : calvin
from circle import *
str1 = input('请输入一组圆的半径：')
l1 = str1.split(',')
for i in l1:
    r = float(i)
    Cl = Circle(r)
    print('%.2f\t%.2f\t%.2f'%(Cl.radius,Cl.length_circle(),Cl.area_circle()))

