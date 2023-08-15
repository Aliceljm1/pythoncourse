#集合的学习

# 集合（set）是一个无序的不重复元素序列。
# 集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
# 可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
# 创建格式：
# 
# parame = {value01,value02,...}
# 或者
# set(value)
# 以下是一个简单实例：

set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合
set2 = set([4, 5, 6, 7])      # 使用 set() 函数从列表创建集合


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 这里演示的是去重功能
{'orange', 'banana', 'pear', 'apple'}
'orange' in basket                 # 快速判断元素是否在集合内

'crabgrass' in basket
False

# 打印结果，分析集合之间的运算法则
...
a = set('abc')
b = set('ab123')
print(a)

print(a - b)                              # 集合a中包含而集合b中不包含的元素

print(a | b)                              # 集合a或b中包含的所有元素

print(a & b)                              # 集合a和b中都包含了的元素

print(a ^ b)                             # 不同时包含于a和b的元素

#参考文档；
# https://mp.weixin.qq.com/s?__biz=MzI0MDE1NTE5MA==&mid=2650878716&idx=3&sn=6dd121a3043b3dc3fd89685d8f178866&chksm=f2eabda5c59d34b32076d34ebd356fa48e6dc29f2c31f1c514672144b8be8e4fce7ec27b7538&scene=27


# 1、添加元素
# 语法格式如下：
# s.add( x )
# 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。

thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)
{'Taobao', 'Facebook', 'Google', 'Runoob'}

# 2、移除元素
# 语法格式如下：
# s.remove( x )
# 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。

thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)


# 3、计算集合元素个数
# 语法格式如下：
# len(s)
# 计算集合 s 元素个数。

thisset = set(("Google", "Runoob", "Taobao"))
len(thisset)

# 4、清空集合
# 语法格式如下：
# s.clear()
#
# 5、判断元素是否在集合中存在
# 语法格式如下：
# x in s
# 判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。

thisset = set(("Google", "Runoob", "Taobao"))
"Runoob" in thisset

#TODO， 1.存在一个集合 s1={1,2,3},s2={1,2,5,6}
# 1.1 求s1和s2的交集
# 1.2 求s1和s2的并集
# 2.对于集合s1添加元素，元素的值为最后数字*2，如s1={1,2,3}，添加后s1={1,2,3,6}。用计算的方式实现，不要直接添加数字6
# 3.对于集合s2删除倒数第二个元素
# 4.对于集合s1，判断元素4是否存在
# 5.使用for循环遍历集合s1，创造一个新集合s3，新集合的元素为s1中每个元素的平方
# 6.使用for循环遍历集合s2，创造一个新集合s4，新集合的元素为s2中每个元素的平方，如果元素的值大于10，
# 则强制修改这个元素的值为10

