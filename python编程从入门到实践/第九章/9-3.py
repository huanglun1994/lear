# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'


class User:
    """一个用户类的简单模拟"""
    # 初始化类属性
    def __init__(self, first_name, last_name, **profiles):
        self.info = {'first name': first_name.title(), 'last name': last_name.title()}
        for key, value in profiles.items():
            self.info[key] = value.title()

    # 定义描述类属性的方法
    def describe_user(self):
        for key, value in self.info.items():
            print(key.title() + ': ' + value)

    # 定义问候用户的方法
    def greet_user(self):
        print('\nHi, ' + self.info['first name'] + ' ' + self.info['last name'] + '!\n')

# 创建两个不同用户的实例，并调用两个类方法
user1 = User('huang', 'lun', city='Chengdu', girlfriend='wang di')
user2 = User('wang', 'di', school='xi nan min da', boyfriend='huang lun')
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
