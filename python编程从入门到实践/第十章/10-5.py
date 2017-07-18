# -*- coding: utf-8 -*-
"""询问并保存用户喜欢编程的原因"""
__author__ = 'Huang Lun'
# 循环询问用户喜欢编程的原因
while True:
    reason = input("Please enter your reason for enjoying programing(enter 'q' to exit): ")
    if reason == 'q':
        break
    else:
        with open('reason.txt', 'a') as f:
            f.write(reason + '\n')
