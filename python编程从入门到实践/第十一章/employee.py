# -*- coding: utf-8 -*-
"""雇员信息"""
__author__ = 'Huang Lun'


class Employee:
    """模拟雇员的信息"""
    def __init__(self, given_name, family_name, annual_salary):
        """初始化雇员的名、姓和年薪"""
        self.given_name = given_name.title()
        self.family_name = family_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, increment=5000):
        """将年薪增加一定额度，默认加5000"""
        self.annual_salary += increment
