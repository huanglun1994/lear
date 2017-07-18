# -*- coding: utf-8 -*-
"""两个数相加"""
__author__ = 'Huang Lun'
# 提示用户输入信息及退出操作
print("Give me two numbers, and I'll add them.\nEnter 'q' to quit.")
while True:
    # 输入第一个数字，判断是否需要退出程序
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    # 输入第二个数字，判断是否需要退出程序
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    # 异常处理，若输入的不是‘q’之外的非数字，则给出提示
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, you must enter two numbers.")
    # 没有错误时的运行结果
    else:
        print(result)
