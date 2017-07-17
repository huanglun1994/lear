# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数接受尺码和字样两个参数，且都有默认值
def make_shirt(size='large', words='I love Python'):
    print('The T-shirt is a ' + size + ' size.')
    print("There is a word on this T-shirt, it's content is " + '"' + words + '".\n')
#调用函数使用默认参数
make_shirt()
#调用函数传递尺码参数
make_shirt(size='middle')
#调用函数传递字样参数
make_shirt(words='I love you')