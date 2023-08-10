
#循环遍历打印一个二维数组

a1=[1,2,5,7]

# 初始化二维数组
array = [
    ["a00", "a01"],
    ["a10", "a11"]
]

print(array[0][0])

print(array[0][1])

print(array[1][1])

# 使用嵌套循环遍历二维数组
for hang_hao in range(2): # 外层循环遍历行
    for lie_hao in range(2): # 内层循环遍历列
        print(array[hang_hao][lie_hao]) # 打印当前元素



#使用代码构建一个二维数组，1.三行四列，数字从a00到a19

# 初始化一个空的二维列表来存储结果
array = []
# 使用一个外层循环来迭代每一行
for hang_hao in range(3):
    # 创建一个空的列表来存储当前行的元素
    row = []
    # 使用一个内层循环来迭代每一列
    for lie_hao in range(4):
        # 为每个元素创建一个字符串，形如 "aXY"，其中 X 是行号，Y 是列号
        element = "a" + str(hang_hao) + str(lie_hao)
        # 将元素添加到当前行中
        row.append(element)
    # 将当前行添加到二维数组中
    array.append(row)

# 打印二维数组
for row in array:
    print(row)


print("----------------------------------------------------------------------")

# TODO 1.构造一个二维数组，存放5行4列数字， 数字从1开始。依次存放。

array = []
# 用一个计数器记录当前的数字，从1开始
number = 1

# 使用一个外层循环来迭代每一行
for row_index in range(5):
    # 创建一个空的列表来存储当前行的元素
    row = []
    # 使用一个内层循环来迭代每一列
    for column_index in range(4):
        # 将当前数字添加到当前行中
        row.append(number)
        # 数字加一，以便下一个元素
        number += 1
    # 将当前行添加到二维数组中
    array.append(row)

# 打印二维数组
for row in array:
    print(row)

print("----------------------------------------------------------------------")

# 计算array[2][1]和前后两个个数字的和()
sum_of_neighbors = array[2][0] + array[2][1] + array[2][2]
print(f"array[2][1] 和前后数字之和: {sum_of_neighbors}")
# 观察分析前后数字的特点
print("----------------------------------------------------------------------")

# 计算array[2][1]和上下两个个数字的和()
array[1][1] +array[2][1]+array[3][1]

print("----------------------------------------------------------------------")

# 计算array[2][1]和左上角，右上角两个个数字的和()
array[2-1][1-1] +array[2][1]+array[2-1][1+1]

print("----------------------------------------------------------------------")

#将上述过程抽象，支持输出任意行列的数据

def makeArray(rows, columns, array):
    # 使用一个外层循环来迭代每一行
    for i in range(rows):
        # 创建一个空的列表来存储当前行的元素
        row = []
        # 使用一个内层循环来迭代每一列
        for j in range(columns):
            # 为每个元素创建一个字符串，形如 "aXY"，其中 X 是行号，Y 是列号
            element = "a" + str(i) + str(j)
            # 将元素添加到当前行中
            row.append(element)
        # 将当前行添加到二维数组中
        array.append(row)


# 定义行数和列数
rows = 3
columns = 4
# 初始化一个空的二维列表来存储结果
array = []

# 调用函数来创建数组
makeArray(rows, columns, array)

# 打印二维数组
for row in array:
    print(row)


print("----------------------------------------------------------------------")

# 定义杨辉三角的行数
n = 10

# 初始化一个二维列表，用来存储杨辉三角
triangle = []

# 使用循环，从第一行到第n行
for hang in range(n):
    # 创建当前行的列表
    row = []

    # 通过循环添加每一行的数字
    for lie in range(hang + 1):
        # 如果是第一列或者最后一列，数字都是1
        if lie == 0 or lie == hang:
            row.append(1)
        else:
            # 否则，某数字等于上一行的同一列的前一个数字和后一个数字之和
            # previous_row = triangle[hang - 1]
            # number = previous_row[lie - 1] + previous_row[lie]

            number =  triangle[hang - 1][lie - 1] +  triangle[hang - 1][lie]

            row.append(number)

    # 将当前行添加到三角形的列表中
    triangle.append(row)

for row in triangle:
    #简单打印
    print(row)
print("----------------------------------------------------------------------")

#map 函数介绍：将列表中的所有数字乘以 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(lambda x: x * 2, numbers)
print(list(doubled_numbers)) # 输出: [2, 4, 6, 8, 10]

#字母转大写
words = ["a", "d", "e"]
upper_words = map(lambda word: word.upper(), words)
print(list(upper_words)) # 输出: A D E

# 打印杨辉三角
for row in triangle:
    #美观打印每一行，并使用空格隔开,看上去更容易懂
    print(' '.join(map(str, row)).center(n * 4))















test=[]
m=7
for i in range(m):
        test.append(2*(i+1)-1)



test.append(1)
test.append(3)
test.append(5)


#测试，请请示如下代码
ar=[]
for i in range(n):
    row = []
    for j in range(i+1):
        if j==0 or j==i+1-1:
            row.append(1)
        else:
            num=ar[i-1][j-1]+ar[i-1][j]
            row.append(num)
    ar.append(row)

print(ar)
print("--------------ar-----------------")