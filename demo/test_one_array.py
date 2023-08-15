#一维数组教程

array=[1,2,3,4,5]

#打印数组的长度
print(len(array))
#打印数组的最后一个数
print(array[4]) #思考为什么是4，而不是3或者2？

array_length=len(array)
#读取数组长度存储变量，用这个变量 打印最后一个元素
print(array[array_length-1])

#使用for 循环打印数组的每一个元素
for element in array:
    print(element)

#使用下标访问数组的每个元素
for index in range(len(array)):
    print(array[index])

#使用while循环打印数组的每一个元素
index=0
while index < len(array):
    print(array[index])
    index+=1

#编写代码 测试range函数1个参数
for index in range(10):
    print(index)

#编写代码 测试range函数三个参数， 修改三个参数的值，观察输出结果，参考文档：https://www.runoob.com/python/python-func-range.html
for index in range(0,10,2):
    print(index)


#使用for循环从后往前挨个打印数组元素
for index in range(len(array)-1,0,-1):
    print(array[index])


#1.编写代码，打印数组[1,2,3,4,5]中第2个开始的元素，
#2.编写代码，打印数组[1,2,3,4,5]中第2个到第4个元素，
#3.使用range打印数字，从2到10，步长为2，
#4.使用range打印数字，从10到2，步长为-2，