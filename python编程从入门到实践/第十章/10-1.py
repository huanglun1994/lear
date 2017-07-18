# -*- coding: utf-8 -*-
"""打开文件并打印文件内容"""
__author__ = 'Huang Lun'
# 方案一：读取全部内容并打印
with open('learning_python.txt') as f:
    contents = f.read()
    print(contents.rstrip())
print('-------------------')
# 方案二：遍历文件并打印
with open('learning_python.txt') as f:
    for line in f:
        print(line.rstrip())
print('-------------------')
# 方案三：读取文件内容至一个列表中，遍历列表打印
with open('learning_python.txt') as f:
    lines = f.readlines()
for line in lines:
    print(line.rstrip())
