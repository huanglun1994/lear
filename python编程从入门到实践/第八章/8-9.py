# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数接受一个列表，并遍历这个列表
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
#创建一个列表包含各位魔术师的名字
magicians = ['david copperfield', 'david blaine', 'liu qian', 'hiro sakai', 'peter marvey']
show_magicians(magicians)