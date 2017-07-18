# -*- coding: utf-8 -*-
"""两个数相加"""
__author__ = 'Huang Lun'
# 提示用户输入信息
print("Give me two numbers, and I'll add them.")
# 输入第一个数字
first_number = input('\nFirst number: ')
# 输入第二个数字
second_number = input('Second number: ')
# 异常处理，若输入的不是非数字，则给出提示
try:
    result = int(first_number) + int(second_number)
except ValueError or TypeError:
    print("Sorry, you must enter two numbers.")
# 没有错误时的运行结果
else:
    print(result)
