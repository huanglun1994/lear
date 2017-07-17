# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数，接受尺码及字样两个参数
def make_shirt(size, words):
    print('The T-shirt is a ' + size + ' size.')
    print("There is a word on this T-shirt, it's content is " + '"' + words + '".\n')
#使用位置参数调用函数
make_shirt('small', 'I love you!')
#使用关键字参数调用函数
make_shirt(size='small', words='I love you!')