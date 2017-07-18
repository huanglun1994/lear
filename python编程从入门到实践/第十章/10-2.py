# -*- coding: utf-8 -*-
"""读取learning_python.txt文件并替换其中的Python为C"""
__author__ = 'Huang Lun'
# 读取文件，使用replace替换指定字符串
with open('learning_python.txt') as f:
    for line in f:
        print(line.replace('Python', 'C').rstrip())
