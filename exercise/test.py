#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9  10:00
# @Author  : calvin

import re
key = r"<html><body><h1>hello world<h1></body></html>"
regs = r'(?<=<h1>).+?(?=<h1>)'
reg = re.compile(regs)
list1= re.search(reg,key)
print(list1.group(1))

