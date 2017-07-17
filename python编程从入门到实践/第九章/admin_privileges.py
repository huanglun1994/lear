# -*- coding: utf-8 -*-
"""创建管理员类和特权类"""
__author__ = 'Huang Lun'

# 导入用户类
from only_user import User
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
