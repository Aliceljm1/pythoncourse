
print("----------------------------------------------------------------")

#打印5行星号， 第1行打印4个空格，1个星号，第2行打印3个空格1个星号，第3行打印2个空格1个星号，依次类推

for i in range(5):
    # 打印空格
    for j in range(4-i):
        print(' ', end='')

    # 打印一个星号
    print('*')


print("----------------------------------------------------------------")

#打印5行星号， 第1行打印4个空格，1个星号，第2行打印3个空格2个星号，第3行打印2个空格3个星号，依次类推
#和上一题的区别是每行打印的星号个数改变了，且等于行号
for i in range(5):
    # 打印空格
    for j in range(4-i):
        print(' ', end='')

    for k in range(i):
        print('*', end='')
    print()
print("----------------------------------------------------------------")

#请把上述题目抽成函数，能够打印n行星号，注意每行1个星号
def print_right_triangle(n):
    for i in range(n):
        # 打印空格
        for j in range(n - 1- i ):
            print(' ', end='')

        # 打印一个星号
        print('*')

print_right_triangle(8)

print("-------------------------88888---------------------------------------")


#请打印n以内所有的奇数，分行打印， 输出内容为 第i行 奇数=x
#核心是x需要用i的数学表达式来表示，注意i从0开始
n=10
for i in range(n):
    print("第",i,"行 奇数=",2*i+1)

print("-------------------------奇数---------------------------------------")

#打印出n行等边三角形,星号组成
def print_triangle(n):
    for i in range(n):
        # 打印空格,个数从n每行依次递减
        for j in range(n - i - 1):
            print(' ', end='')

        # 打印星号，星号个数是第1行1个，第2行3个，5，7,9...显然有规律，
        for k in range(2 * i + 1):
            print('*', end='')

        # 换行
        print()

# 示例：打印一个5行的三角形
print_triangle(5)

print("----------------------------------------------------------------")

#打印出镂空等边三角形，也就是要求三角形内部是镂空的，只需要轮廓的星号
#1.镂空三角形有什么特点？2.镂空三角形中每行空格数有什么特点，能否用行号，或者列号来来计算表示？

def print_hollow_triangle(n):
    for i in range(n):
        # 打印空格,个数从n每行依次递减
        for j in range(n - i - 1):
            print(' ', end='')

        # 打印星号，星号数目规律是:第1行，最后1行都是 2 * i + 1 个(参考上面一个函数)，
        # 其他行都是两个星号，中间空格，且空格个数是(2*i+1)-2个 ，-2是减去首尾的星号
        if i == 0 or i == n - 1:  # 第一行和最后一行打印星号
            for k in range(2 * i + 1):
                print('*', end='')
        else:  # 其他行打印两个星号，中间打印空格
            print('*', end='')
            for k in range((2 * i + 1) - 2):
                print(' ', end='')
            print('*', end='')

        # 换行
        print()

# 示例：打印一个5行的镂空三角形
print_hollow_triangle(5)

print("--------------------------打印镂空三角形--------------------------------------")

def print_hollow_triangle2(n):
    for i in range(n):
        # 打印空格,个数从n每行依次递减
        for j in range(n - i - 1):
            print(' ', end='')
        stars=2*i+1
        # 打印星号，星号数目规律是:第1行，最后1行是 2 * i + 1 个，其他行都是两个星号，中间空格，且空格个数是(2*i+1)-2个
        if i == 0 or i == n - 1:  # 第一行和最后一行打印星号
            for k in range(stars):
                print('*', end='')
        else:  # 其他行打印两个星号，中间打印空格
            print('*', end='')
            for k in range(stars - 2):
                print(' ', end='')
            print('*', end='')

        # 换行
        print()

# 示例：打印一个5行的镂空三角形
print_hollow_triangle2(5)

print("--------------------------打印镂空三角形2--------------------------------------")


def print_hollow_triangle3(n):
    for i in range(n):
        # 打印空格,个数从n每行依次递减
        for j in range(n - i - 1):
            print(' ', end='')

        # 如果是第一行和最后一行,直接打印星号
        # 如果k==0那么说明是第一个星号，打印它，如果k==2*i说明是最后一个星号也打印，否则打印空格，完成三角形除去首位的中间部分星号打印
        for k in range(2 * i + 1):
            if i == 0 or i == n-1:
                print('*', end='')
            elif  k == 0 or k == 2 * i:
                print('*', end='')
            else:
                print(' ', end='')

        # 换行
        print()

# 示例：打印一个5行的镂空三角形
print_hollow_triangle3(5)

print("--------------------------打印镂空三角形3--------------------------------------")


def print_hollow_triangle3(n):
    for i in range(n):
        # 打印空格,个数从n每行依次递减
        for j in range(n - i - 1):
            print(' ', end='')

        #和上一个函数相比，可以化简逻辑，直接写一行判定，前提是虽然两个判定的条件不一样，但是判定成功执行的操作是一样的就可以合并
        for k in range(2 * i + 1):
            if i == 0 or i == n-1 or k == 0 or k == 2 * i:
                print('*', end='')
            else:
                print(' ', end='')

        # 换行
        print()

# 示例：打印一个5行的镂空三角形
print_hollow_triangle3(5)

print("--------------------------打印镂空三角形4--------------------------------------")
