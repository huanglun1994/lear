# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'


class User:
    """一个用户类的简单模拟"""
    # 初始化类属性
    def __init__(self, first_name, last_name, **profiles):
        self.info = {'first name': first_name.title(), 'last name': last_name.title(), 'login_attempts': 0}
        for key, value in profiles.items():
            self.info[key] = value.title()

    # 定义描述类属性的方法
    def describe_user(self):
        for key, value in self.info.items():
            print(key.title() + ': ' + value)

    # 定义问候用户的方法
    def greet_user(self):
        print('\nHi, ' + self.info['first name'] + ' ' + self.info['last name'] + '!\n')

    # 定义一个方法使尝试登录次数加1
    def increment_login_attempts(self):
        self.info['login_attempts'] += 1

    # 定义一个方法将尝试登录次数重置为0
    def reset_login_attempts(self):
        self.info['login_attempts'] = 0

# 实例化一个用户对象
user = User('huang', 'lun', city='chengdu')
# 利用for循环调用增加尝试登录次数方法多次，并打印最终的次数值
for i in range(5):
    user.increment_login_attempts()
print(user.info['login_attempts'])
# 调用重置次数方法并打印值以确认
user.reset_login_attempts()
print(user.info['login_attempts'])
