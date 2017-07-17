# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#将五香烟熏牛肉存在sandwiches_orders列表中
sandwich_orders = ['tea sandwiches', 'classic club sandwiches', 'crilled chess sandwiches', 'ham sandwiches',
                   'pastrami', 'pastrami', 'pastrami', 'pastrami']
print('Sorry, we have sold out of pastrami.\n')
#当列表中存在五香烟熏牛肉时删除它
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
#打印现在的列表
print('Now sandwich_orders:')
print(sandwich_orders)