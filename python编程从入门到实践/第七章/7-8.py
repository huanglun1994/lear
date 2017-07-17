# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#创建一个列表存储所有的三明治，创建一个空列表存储完成的三明治
sandwich_orders = ['tea sandwiches', 'classic club sandwiches', 'crilled chess sandwiches', 'ham sandwiches']
finished_sandwiches = []
#将orders列表中的三明治移到空列表中
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made you ' + sandwich.title() + '.')
    finished_sandwiches.append(sandwich)
#打印新列表中的所有三明治
print('\n-------- New Sandwiches -------')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())