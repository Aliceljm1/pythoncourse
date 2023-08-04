#存在一个list1=[4,2,5,1,3]
#1.编写代码，删除最后一个元素
#2.编写代码在最后插入元素1
#3.打印列表中数字1出现的次数
#4.扩充列表的元素，添加list2=[8,3,5]
#5.排序整个大列表，打印出所有数据



#1.有四个数字，分别是：1、2、3、4，提问：能组成多少个互不相同且无重复数字的三位数？打印出来。
#2. 用程序求解方程，7=3*x+1


count=0
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != k and i != j and j != k:    # 判断三个数是否互不相同
                count += 1
                print("%d%d%d  " %(i,j,k), end=" ")
                if count % 8 == 0:
                    print()
print("三位互不相同的数，一共有：{} 个。" .format(count))

print("第一种")#两个for循环直接做乘法，计算结果
for i in range(1,10):
    for j in range(1,10):
        print("{0}*{1}={2}".format(i,j,i*j),end=" ")

print("\n第二种")#第一种方法不好看，每隔9个换行
for i in range(1,10):
    for j in range(1,10):
        print("{0}*{1}={2}".format(i,j,i*j),end="\t ")
    print()

print("\n第三种")#打印规范乘法口诀表，解决重复数据问题，核心是解决第二重循环的循环次数问题，依次+1
for i in range(1,10):
    for j in range(1,i+1):
        print("{0}*{1}={2}".format(i,j,i*j),end="\t ")
    print()


for i in range(1,10):
    if 7==3*i+1:
        print("7=3*x+1的解是：",i)