# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数接受一个列表，并遍历这个列表
def show_magicians(magicians):
    for magician in magicians:
        print(magician)
#定义一个函数接受一个列表并对列表中的元素进行修改
def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'the Great ' + magicians[i].title()
    return magicians
#创建一个列表包含各位魔术师的名字
magicians = ['david copperfield', 'david blaine', 'liu qian', 'hiro sakai', 'peter marvey']
#分别调用两个函数
make_great(magicians)
show_magicians(magicians)