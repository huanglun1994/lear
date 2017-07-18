# -*- coding: utf-8 -*-
"""统计单词出现次数"""
__author__ = 'Huang Lun'
# 读取文件中的内容
with open('The Zen of Python.txt') as f:
    count = 0
    for line in f:
        count += line.lower().count('is')
# 输出统计总数
print(count)
