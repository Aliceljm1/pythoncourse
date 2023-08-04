#!/usr/bin/python
# -*- coding: UTF-8 -*-

#存在这样一个字符串 "this is China 中国 "，编写如下代码
#1.打印这个字符串的大写字符串
#2.把这个字符串转换为首字母大写的字符串，存放到新的变量newstr中，打印出来
#3.把这个字符串的后空格删除

a="this is China 中国"
b=a.upper()
print(b)

newstr=a
print(a.title())

print(a.rstrip())