# -*- coding: utf-8 -*-
"""创建一个管理员实例，并调用方法显示特权"""
__author__ = 'Huang Lun'
# 导入管理员和特权模块
import admin_privileges
# 实例管理员对象并调用方法
admin = admin_privileges.Admin('huang', 'lun', city='chengdu')
admin.privilege.show_privileges()
