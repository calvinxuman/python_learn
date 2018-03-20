#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9  10:00
# @Author  : calvin

import copy

l1 = [[1,2,3],4,5,6]
l2 = l1.copy()
l3 = copy.deepcopy(l1)
l1[0] = [1,2,8]
print(l2)
print(l3)