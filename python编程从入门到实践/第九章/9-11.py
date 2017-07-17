# -*- coding: utf-8 -*-
"""导入用户模块，实例一个管理员对象并调用方法验证导入是否正确"""
__author__ = 'Huang Lun'
# 导入用户模块，并实例管理员对象
import user
admin = user.Admin('huang', 'lun', city='chengdu')
# 调用显示特权方法验证导入是否正确
admin.privilege.show_privileges()
