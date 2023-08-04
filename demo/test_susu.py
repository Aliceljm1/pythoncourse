
#打印n之前每个数字，如果输入5，则打印1，2，3，4，5
#如果输入3则打印 ，1，2，3
def show_nums(n):
    for i in range(1,n+1):
        print(i)

show_nums(5)
show_nums(3)

#请修改上述代码，从2开始打印，且不打印n本身，如输入5，则打印2，3，4

#百分号是取模运算，也就是做除法之后的余数作为结果。5除2余数是1，所以5%2=1
print(5%2)
print(5%3)
print(5%4)
print(5%5)


#-------------------------------------------------------------------
#判断某个数字是否能够被另外一个数字整除
def isok(num1,num2):
    if(num1%num2==0):
        print("数字{0}可以被数字{1}整除".format(num1,num2))
    else:
        print("数字{0}不可以被数字{1}整除*****".format(num1,num2))

isok(6,3)
isok(6,5)

# 定义is_prime函数来检查一个数是否是素数
def is_prime(n):
    if n <= 1:
        return False

    # 对于每个小于n的数字，我们都检查n能否被这个数字整除
    for i in range(2, n):
        if n % i == 0:  # 如果n能被i整除，那么n就不是素数
            return False

    # 如果n不能被任何小于n的数字整除，那么n就是素数
    return True


# 打印出1-100以内的素数
prime_numbers = []
for i in range(1, 101):
    if is_prime(i):
        prime_numbers.append(i)

print(prime_numbers)
