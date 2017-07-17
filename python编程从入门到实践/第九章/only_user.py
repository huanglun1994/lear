# -*- coding: utf-8 -*-
"""创建用户类"""
__author__ = 'Huang Lun'


class User:
    """一个用户类的简单模拟"""
    def __init__(self, first_name, last_name, **profiles):
        """初始化类属性"""
        self.info = {'first name': first_name.title(), 'last name': last_name.title(), 'login_attempts': 0}
        for key, value in profiles.items():
            self.info[key] = value.title()

    def describe_user(self):
        """定义描述类属性的方法"""
        for key, value in self.info.items():
            print(key.title() + ': ' + value)

    def greet_user(self):
        """定义问候用户的方法"""
        print('\nHi, ' + self.info['first name'] + ' ' + self.info['last name'] + '!')

    def increment_login_attempts(self):
        """定义一个方法使尝试登录次数加1"""
        self.info['login_attempts'] += 1

    def reset_login_attempts(self):
        """定义一个方法将尝试登录次数重置为0"""
        self.info['login_attempts'] = 0
