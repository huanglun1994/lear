# -*- coding: utf-8 -*-
"""保存用户名字"""
__author__ = 'Huang Lun'
# 提示用户输入名字
name = input('Please enter your name: ')
# 将用户名字保存到文件中
with open('guest.txt', 'w') as f:
    f.write(name + '\n')
