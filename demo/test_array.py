# 创建一个二维数组
array_2d = [
    ['a00', 'a01', 'a02', 'a03'],
    ['a10', 'a11', 'a12', 'a13'],
    ['a20', 'a21', 'a22', 'a23']
]
print(array_2d[0][1])

# 循环访问二维数组的每个元素
for i in range(3):
    for j in range(4):
        print(array_2d[i][j], end=' ')
    print()  # 每行打印完后换行

def printRight(row,column):
    print(array_2d[row][column+1])

printRight(0,0)


#存在一个二维数组，3行4列，值从1开始，计算最后一列的数字之和

# 定义二维数组
array = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
#TODO 编写双重for循环打印二维数组的每个数字


# 使用for循环计算最后一列的和
sum = 0
for i in range(3):
    for j in range(4):
        if j==3:
            sum=sum+array[i][j]
print(sum)
print("----------------------------------------------")

sum=0
# 遍历每一行
for row in array:
    # 加上该行的最后一个数字
    sum =sum+ row[-1]
print(sum)
print("----------------------------------------------")

#TODO 计算上述二维数组对角线数据之和

