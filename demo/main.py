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




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
