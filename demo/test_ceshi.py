
#1.打印出1到100之间的所有质数  -错误，
#存在一个list1=[4,2,5,1,3]
#2.编写代码，删除最后一个元素 -正确
#3.编写代码在最后插入元素1 -正确
#4.编写乘法口诀表- 正确

#2023年8月3日编程小测试 总分75分 (全程向日葵桌面监控，没有查询百度)


def print_hollow_triangle(n):
    for i in range(n):
        # 打印空格,个数从n每行依次递减
        for j in range(n - i - 1):
            print(' ', end='')

        # 打印星号，星号个数是第1行1个，第2行3个，5，7,9...显然有规律，
        # 但如果不是第一行和最后一行，且不是一行的首尾，则打印空格
        for k in range(2 * i + 1):
            if i == 0 or i == n-1 or k == 0 or k == 2 * i:
                print('*', end='')
            else:
                print(' ', end='')

        # 换行
        print()

# 示例：打印一个5行的镂空三角形
print_hollow_triangle(5)