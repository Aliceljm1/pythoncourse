#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 例2：elif用法

#1.编写代码判断 数字num 是否在 9到5之间,如果是打印 ok
#2.判断num是否在 -2到4 或者 9到3之间 ，如果是打印ok2
#3. 判断字符串 "abc123" 是否长度为3，如果不是打印 no len =3.
num1 = -1
if num1 >=5 and  num1 <=9:
    print('ok')
num2 = -1
if (num2 >=-2 and  num2 <=4 ) or (num2 >=3 and  num2 <=9):
    print('ok2')
word = 'abc123'
# if word len == 3
