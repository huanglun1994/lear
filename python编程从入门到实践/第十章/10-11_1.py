# -*- coding: utf-8 -*-
"""存储喜欢的数字"""
__author__ = 'Huang Lun'
import json


def get_number():
    """提示用户输入喜欢的数字"""
    favorite_number = input('Please enter your favorite number: ')
    return favorite_number


def save_number():
    """存储用户输入的数字"""
    file_name = 'favorite_number.json'
    # 获取用户输入的数字
    favorite_number = get_number()
    # 若得到的是数字则存为json数据，若不是则重新获取
    try:
        if type(int(favorite_number)) is int:
            with open(file_name, 'w') as f:
                json.dump(favorite_number, f)
    except ValueError:
        return save_number()
# 调用函数
save_number()
