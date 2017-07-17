# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'


class Restaurant:
    """一次饭店的简单模拟"""
    # 初始化属性
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    # 定义描述属性方法
    def descripe_restaurant(self):
        print("\nThe restaurant's name is " + self.restaurant_name.title() + '.')
        print("The restaurant's cuisine type is " + self.cuisine_type + '.\n')

    # 定义描述是否在营业的方法
    def open_restaurant(self):
        print('The restaurant ' + self.restaurant_name.title() + ' is open.\n')

    # 定义一个修改用餐人数的方法
    def set_number_served(self, number):
        self.number_served = number

    # 定义一个方法使用餐人数递增
    def increment_number_served(self, max_number):
        self.number_served += max_number

# 实例化一个饭店对象
restaurant = Restaurant('yin he', 'Chinese food')
# 打印初始用餐人数
print('There are ' + str(restaurant.number_served) + ' people having had a dinner in ' +
      restaurant.restaurant_name.title() + ' Restaurant.\n')
# 修改用餐人数为20并打印
restaurant.number_served = 20
print('There are ' + str(restaurant.number_served) + ' people having had a dinner in ' +
      restaurant.restaurant_name.title() + ' Restaurant.\n')
# 调用方法修改用餐人数为30并打印
restaurant.set_number_served(30)
print('There are ' + str(restaurant.number_served) + ' people having had a dinner in ' +
      restaurant.restaurant_name.title() + ' Restaurant.\n')
# 实例化一个饭店对象，并指出每天最多接待用餐人数
another_restaurant = Restaurant('wang chao', 'Chinese food')
another_restaurant.increment_number_served(1000)
print('There can be at most ' + str(another_restaurant.number_served) + ' people having a dinner at the same time' +
      ' in ' + another_restaurant.restaurant_name.title() + ' Restaurant.')