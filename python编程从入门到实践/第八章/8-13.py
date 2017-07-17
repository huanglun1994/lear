# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数接受两个位置形参和一个任意数量形参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value.title()
    return profile
#使用自己的一些消息调用函数
user_profile = build_profile('haung', 'lun', city='chengdu', field='python', girlfriend='wang di')
print(user_profile)