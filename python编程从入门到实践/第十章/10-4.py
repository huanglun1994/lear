# -*- coding: utf-8 -*-
"""问候用户并保存记录"""
__author__ = 'Huang Lun'
# 循环提示用户输入名字
while True:
    name = input("Please enter your name(enter 'q' to exit): ")
    if name == 'q':
        break
    else:
        # 问候用户
        print('Hi, ' + name + '!\n')
        # 保存用户访问记录
        with open('guest_book.txt', 'a') as f:
            f.write(name.title() + ' has visited.\n')
