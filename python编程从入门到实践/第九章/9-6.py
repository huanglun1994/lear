# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'


class Restaurant:
    """一次饭店的简单模拟"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descripe_restaurant(self):
        """定义描述属性方法"""
        print("\nThe restaurant's name is " + self.restaurant_name.title() + '.')
        print("\nThe restaurant's cuisine type is " + self.cuisine_type + '.')

    def open_restaurant(self):
        """定义描述是否在营业的方法"""
        print('\nThe restaurant ' + self.restaurant_name.title() + ' is open.')


class IceCreamStand(Restaurant):
    """模拟冰淇淋店，继承自饭店类"""
    def __init__(self, restaurant_name, cuisine_type):
        """继承父类属性，初始特有属性"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['cookie dough', 'chocolate fudge brownie', 'phish food', 'strawberry cheesecake',
                        'cherry garcia', 'chunky monkey', 'clever cookies', 'baked alaska']

    def show_icecream_type(self):
        """定义一个方法显示有哪些口味的冰淇淋"""
        print('\nThe following are the icecream kinds of ' + self.restaurant_name.title() + "'s Shop:")
        for icecream_kind in self.flavors:
            print('- ' + icecream_kind.title())
        print('\nWelcome to taste!')

# 实例化一个冰淇淋店对象
icecream_shop = IceCreamStand('huang lun', 'cream')
# 调用显示冰淇淋种类方法
icecream_shop.show_icecream_type()