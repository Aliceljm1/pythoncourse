# 请编写python代码，实现如下功能：1.格式化字符串
# 存在字典{"name":"李白","age":24}
# 找到各种方法格式化字符串   ”姓名:李白,年纪24“



data = {"name": "李白", "age": 24}
formatted_string = "姓名:" + data['name'] + ",年纪" + str(data['age'])
print(formatted_string)

# 或者

formatted_string = "姓名:", data['name'], ",年纪", str(data['age'])
print(''.join(formatted_string))


data = {"name": "李白", "age": 24}
formatted_string = f"姓名:{data['name']},年纪{data['age']}"
print(formatted_string)


#字典的解包操作 **data 将这个字典转换成了两个单独的命名参数，即 name="李白" 和 age=24, **data就是语法糖
data = {"name": "李白", "age": 24}
formatted_string = "姓名:{name},年纪{age}".format(**data)
print(formatted_string)
