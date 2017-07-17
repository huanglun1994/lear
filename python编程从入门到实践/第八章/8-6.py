# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数，接受两个参数表示城市和国家
def city_country(city, country):
    message = city.title() + ', ' + country.title()
    return message
#调用函数三次并打印返回值
print(city_country('beijing', 'China'))
print(city_country('london', 'England'))
print(city_country('paris', 'France'))