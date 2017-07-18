# -*- coding: utf-8 -*-
"""读取喜欢的数字"""
__author__ = 'Huang Lun'
import json


def read_number():
    """读取文件中的数字"""
    file_name = 'favorite_number.json'
    # 若文件存在则读取，若不存在则提示信息
    try:
        with open(file_name) as f:
            number = json.load(f)
    except FileNotFoundError:
        print('There is no such file.')
    else:
        print("I know your favorite number! It's " + number + '.')
# 调用函数
read_number()
