# -*- coding: utf-8 -*-
"""猫和狗"""
__author__ = 'Huang Lun'
# 读取存储猫和狗的文件并打印，处理文件不存在时的异常
files = ['cats.txt', 'dogs.txt']
for file in files:
    try:
        with open(file) as f:
            print(f.read())
        print('----------------')
    except FileNotFoundError:
        pass
