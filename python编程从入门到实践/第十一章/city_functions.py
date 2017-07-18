# -*- coding: utf-8 -*-
"""城市，国家"""
__author__ = 'Huang Lun'


def city_country(city, country):
    """返回“城市，国家”样式的字符串"""
    message = city.title() + ', ' + country.title()
    return message
