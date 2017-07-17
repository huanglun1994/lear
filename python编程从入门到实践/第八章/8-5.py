# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数，接受两个参数分别表示城市名及所属国
def describe_city(city, country='China'):
    print(city + ' is in ' + country + '.\n')
#调用三次这个函数
describe_city('Beijing')
describe_city('Chengdu')
describe_city('London', 'England')
