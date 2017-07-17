# -*- coding: utf-8 -*-
"""掷骰子"""
__author__ = 'Huang Lun'
# 导入随机模块
from random import randint


class Die:
    """模拟一个多面的骰子"""
    def __init__(self, sides=6):
        """初始化骰子属性，默认为六面的骰子"""
        self.sides = sides

    def roll_die(self):
        """掷骰子"""
        print(randint(1, self.sides))

# 实例化一个6面的骰子对象，并掷10次
die_6 = Die(6)
for test_1 in range(10):
    die_6.roll_die()
print('-------------------')
# 实例化一个10面骰子并掷10次
die_10 = Die(10)
for test_2 in range(10):
    die_10.roll_die()
print('-------------------')
# 实例化一个20面骰子并掷10次
die_20 = Die(20)
for test_3 in range(10):
    die_20.roll_die()
