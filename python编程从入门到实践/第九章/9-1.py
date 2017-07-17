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

# 实例化一个饭店对象
restaurant = Restaurant('di wang', 'Chinese food')
# 调用类的属性并打印，调用类的方法
print(restaurant.restaurant_name.title())
print(restaurant.cuisine_type)
restaurant.descripe_restaurant()
restaurant.open_restaurant()