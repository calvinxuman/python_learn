#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12  10:48
# @Author  : calvin

import re

'''
[0-9]	0123456789任意之一
[a-z]	小写字母任意之一
[A-Z]	大写字母任意之一
\d	    等同于[0-9]
\D	    等同于[^0-9]匹配非数字
\w	    等同于[a-z0-9A-Z_]匹配大小写字母、数字和下划线
\W	    等同于[^a-z0-9A-Z_]等同于上一条取非
.       可以匹配任意字符
*       表示任意个字符（包括0个）
+       表示至少一个字符
?       表示0个或1个字符
{n,m}   表示n-m个字符
\s      匹配一个空格（也包括Tab等空白符）
A|B     可以匹配A或B
^       表示行的开头
$       表示行的结束
'''

# def is_valid_email(s):
#     re_s = re.compile(r'[0-9a-zA-Z][0-9a-zA-Z\_\.]+\@[0-9a-zA-Z][0-9a-zA-Z\_]+\.[com|cn|org]')
#     if re_s.match(s):
#         return True
#     else:
#         return False
#
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')

import base64

def safe_base64_decode(s):
    if len(s)%4 == 0:
        return base64.b64decode(s)
    elif len(s)%4 == 3:
        s = s + b'='
        return base64.b64decode(s)
    elif len(s)%4 == 2:
        s = s + b'=='
        return base64.b64decode(s)
    elif len(s)%4 == 1:
        s = s + b'='
        return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
# print(safe_base64_decode(b'YWJjZA'))
print('ok')
