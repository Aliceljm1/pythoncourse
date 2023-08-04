# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #1.新增数组cars，包含”Ford”, “Volvo”, “BMW” 循环打印数组中的元素
    #2.循环打印数组中的元素，当元素为Volvo时，退出循环，当元素为BMW时，跳过本次循环
    #3.从后往前打印数组中的元素
    cars=['ford','volvo','BMW']
    for car in cars:
        print(car)

    for  car in cars:
        if car==('volvo'):
            break
        elif car==('BMW'):
            continue
        print(car)

    #2023-7-18,7-19
    #打印字符串 "abc123我爱中国" "123" 两个字符串的长度之和。 如果能用一行代码编写最好
    #打印出第2个，第3个，第8个文字的内容。可用for循环
    #使用for循环打印 "abc123我爱中国" 字符串中的文字，如果文字是数字则 打印 “当前是数字”。判断某字符是否为数字自己百度

    #打印10以内所有偶数，包含10，使用range函数for循环
    #打印从5到20的数，并求和


    #读取用户输入的数字，如果是偶数则打印 偶数，如果是<10则打印 小于10 如果小于10 且 >5 显示 在5-10之间
    #如果是>10 则打印 大于10，如果等于10 则打印 等于10

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
