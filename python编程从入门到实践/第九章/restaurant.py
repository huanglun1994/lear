# -*- coding: utf-8 -*-
"""一次饭店的简单模拟"""
__author__ = 'Huang Lun'


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descripe_restaurant(self):
        """定义描述属性方法"""
        print("\nThe restaurant's name is " + self.restaurant_name.title() + ' Restaurant.')
        print("\nThe restaurant's cuisine type is " + self.cuisine_type + '.')

    def open_restaurant(self):
        """定义描述是否在营业的方法"""
        print('\nThe restaurant ' + self.restaurant_name.title() + ' is open.')
