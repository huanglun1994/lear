# -*- coding: utf-8 -*-
"""创建用户类、特权类和管理员类"""
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


class Privileges:
    """模拟管理员的特权"""
    def __init__(self):
        """初始化类属性"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """定义一个方法显示特权"""
        print('\nThe admin can do the following things:')
        for privilege in self.privileges:
            print('- ' + privilege.capitalize() + '.')


class Admin(User):
    """模拟管理员"""
    def __init__(self, first_name, last_name, **profiles):
        """继承父类属性，并用特权类实例来增加特权属性"""
        super().__init__(first_name, last_name, **profiles)
        self.privilege = Privileges()
