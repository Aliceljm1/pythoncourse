# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 ,格式如下所示：
# d = {key1 : value1, key2 : value2, key3 : value3 }

# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
# 一个简单的字典实例：
# testdict = {'name': 'Jack', 'age': 123, 'web': 'www.baidu.com'}

# 使用大括号 {} 来创建空字典
emptyDict = {}

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

# 使用内建函数 dict() 创建字典：
emptyDict = dict()

# 打印字典
print(emptyDict)

# 查看字典的数量
print("Length:", len(emptyDict))

# 查看类型
print(type(emptyDict))

# 访问字典里的值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

#注意访问方式和数组很想，但是是用字符串来作为访问的条件(类似查字典)
print("tinydict['Name']: ", tinydict['Name'])
print("tinydict['Age']: ", tinydict['Age'])

# 如果用字典里没有的键访问数据，会输出错误
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print("tinydict['Alice']: ", tinydict['Alice'])

# 修改字典
# 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

tinydict['Age'] = 8  # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])


# 删除字典元素
# 能删单一的元素也能清空字典，清空只需一项操作。
# 显式删除一个字典用del命令，如下实例：
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典

print("tinydict['Age']: ", tinydict['Age'])
print("tinydict['School']: ", tinydict['School'])
#但这会引发一个异常，因为用执行 del 操作后字典不再存在：

# 字典键的特性
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

tinydict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print("tinydict['Name']: ", tinydict['Name'])

# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
tinydict = {['Name']: 'Runoob', 'Age': 7}
print("tinydict['Name']: ", tinydict['Name'])



#TODO,1.自己编写一个字典，元神某个角色，包含名字，攻击力，属性，等级，输出，打印出来。
#2. 直接打印出攻击力的值， 之后打印出所有的键值对的值，格式是 “属性:xx=aa”
#3. 添加一个属性，如血量
#4. 删除一个属性，等级
#5. 打印一个不存在属性值，查看报错情况
#6. 判断这个字典中是否存在属性 “情绪”,如果不存在，就添加一个情绪属性，值为”开心“
#7.编写代码把字典中的所有健保存到一个数组当中去。