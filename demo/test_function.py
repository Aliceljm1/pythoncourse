# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 定义函数
def print_info(str):
    "打印任何传入的字符串"
    print("日志:"+str)
    return


# 调用函数
print_info("我要调用用户自定义函数!")
print_info("再次调用同一函数")


def ChangeInt(a):
    a = 10


b = 2
ChangeInt(b)
print(b)
# 结果是 2

# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo(name="miki") # 这里的年纪默认就是多少呢？


#1.编写函数 addTwoNum, 两个数相加，把结果打印出来
#2.编写函数 getStringLength 返回字符串的长度
#3.编写函数 addNum() ，把两个数a,b相加，其b中默认值是10， 给出两种调用方法。

