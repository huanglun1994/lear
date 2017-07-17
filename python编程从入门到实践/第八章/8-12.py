# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数接受任意数量的实参
def make_sandwich(*ingredients):
    """概述要制作的三明治"""
    print('\nMaking a sandwich with the following ingredients:')
    for ingredient in ingredients:
        print('- ' + ingredient)
#分别用不同数量的食材调用函数三次
make_sandwich('carrot')
make_sandwich('ham', 'eggs')
make_sandwich('pork', 'lettuce', 'cheese')