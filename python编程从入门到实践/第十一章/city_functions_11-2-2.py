# -*- coding: utf-8 -*-
"""城市，国家"""
__author__ = 'Huang Lun'


def city_country(city, country, population=''):
    """返回“城市，国家”样式的字符串"""
    # 如果给定了人口数
    if population:
        message = city.title() + ', ' + country.title() + ' - population ' + str(population)
        return message
    else:
        message = city.title() + ', ' + country.title()
        return message
