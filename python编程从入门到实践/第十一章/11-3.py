# -*- coding: utf-8 -*-
"""测试雇员类是否正常"""
__author__ = 'Huang Lun'
# 导入需要的模块
from employee import Employee
import unittest


class TestEmployee(unittest.TestCase):
    """针对Employee类的测试"""

    def setUp(self):
        """创建一个雇员实例对象"""
        self.employee = Employee('xiao', 'hong', 50000)

    def test_give_default_raise(self):
        """测试默认涨工资的方法是否正确"""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """测试指定增幅工资量后年薪是否正确"""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()
    