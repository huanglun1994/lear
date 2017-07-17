# -*- coding: utf-8 -*-
"""使用有序字典创建词汇表"""
__author__ = 'Huang Lun'
# 导入有序字典类
from collections import OrderedDict
# 实例化有序字典类，并赋值
keys_mean = OrderedDict()
keys_mean['for'] = 'circulation'
keys_mean['if'] = 'condition testing'
keys_mean['print'] = 'output'
keys_mean['int'] = 'integer'
keys_mean['break'] = 'exit a loop'
# 遍历字典的键值对，确认字典按输入的顺序存储信息
for key, mean in keys_mean.items():
    print(key + ': ' + mean)
