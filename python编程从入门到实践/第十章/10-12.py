# -*- coding: utf-8 -*-
"""存储并读取喜欢的数字"""
__author__ = 'Huang Lun'
import json


def get_number():
    """提示用户输入喜欢的数字"""
    favorite_number = input('Please enter your favorite number: ')
    return favorite_number


def save_number():
    """存储用户输入的数字"""
    # 获取用户输入的数字
    favorite_number = get_number()
    # 若得到的是数字则存为json数据，若不是则重新获取
    try:
        if type(int(favorite_number)) is int:
            with open(file_name, 'w') as f:
                json.dump(favorite_number, f)
    except ValueError:
        return save_number()


def read_number():
    """读取文件中的数字"""
    # 若文件存在则读取，若不存在则提示信息
    try:
        with open(file_name) as f:
            number = json.load(f)
    except FileNotFoundError:
        return save_number()
    else:
        print("I know your favorite number! It's " + number + '.')
file_name = 'favorite_number.json'
# 调用两次函数读取数字，默认为文件不存在
read_number()
print('-----------------')
read_number()
