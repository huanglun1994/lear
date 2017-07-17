# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数接受一个列表，并遍历这个列表
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
#定义一个函数接受一个列表并对列表中的元素进行修改
def make_great(magicians):
    magicians_copy = magicians[:]
    for i in range(len(magicians_copy)):
        magicians_copy[i] = 'the Great ' + magicians_copy[i]
    return magicians_copy
#创建一个列表包含各位魔术师的名字
magicians = ['david copperfield', 'david blaine', 'liu qian', 'hiro sakai', 'peter marvey']
#调用函数修改列表
magicians_copy = make_great(magicians)
#调用函数显示魔术师名字
show_magicians(magicians)
show_magicians(magicians_copy)
