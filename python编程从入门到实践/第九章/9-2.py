# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'


class Restaurant:
    """一次饭店的简单模拟"""
    # 初始化属性
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    # 定义描述属性方法
    def descripe_restaurant(self):
        print("\nThe restaurant's name is " + self.restaurant_name.title() + '.')
        print("The restaurant's cuisine type is " + self.cuisine_type + '.\n')

    # 定义描述是否在营业的方法
    def open_restaurant(self):
        print('The restaurant ' + self.restaurant_name.title() + ' is open.\n')

# 创建三个饭店类的实例对象
restaurant1 = Restaurant('di wang', 'Chinese food')
restaurant2 = Restaurant('yin he', 'French food')
restaurant3 = Restaurant('shi ji', 'Italian food')
# 每个实例对象都调用描述饭店属性方法
restaurant1.descripe_restaurant()
restaurant2.descripe_restaurant()
restaurant3.descripe_restaurant()