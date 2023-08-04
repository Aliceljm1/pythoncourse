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
