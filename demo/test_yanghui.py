
#循环遍历打印一个二维数组

# 初始化二维数组
array = [
    ["a00", "a01"],
    ["a10", "a11"]
]

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
            previous_row = triangle[hang - 1]
            number = previous_row[lie - 1] + previous_row[lie]
            row.append(number)

    # 将当前行添加到三角形的列表中
    triangle.append(row)

for row in triangle:
    #简单打印
    print(row)
print("----------------------------------------------------------------------")

# 打印杨辉三角
for row in triangle:
    #美观打印每一行，并使用空格隔开,看上去更容易懂
    print(' '.join(map(str, row)).center(n * 3))
