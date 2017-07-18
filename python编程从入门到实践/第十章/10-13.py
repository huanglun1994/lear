# -*- coding: utf-8 -*-
"""记录并问候用户"""
__author__ = 'Huang Lun'
import json


def input_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    return username


def save_username():
    """存储用户名"""
    filename = 'username.json'
    username = input('Please enter your name: ')
    print("We'll remember you when you come back, " + username + '!')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def get_latest_name():
    """获取最后一次的用户名"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            latest_mame = json.load(f_obj)
    except FileNotFoundError:
        latest_mame = save_username()
        return latest_mame
    else:
        return latest_mame


def greet_user():
    """问候用户，并指出其名字"""
    latest_name = get_latest_name()
    username = input_new_username()
    # 如果用户名不正确则重新输入
    while username == latest_name:
        print("Welcome back, " + username + "!")
        break
    else:
        print('The name is wrong, please enter again.')
        return greet_user()
# 调用函数
greet_user()
