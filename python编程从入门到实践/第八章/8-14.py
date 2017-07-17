# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#定义一个函数接受两个位置形参和一个任意数量的关键字形参
def make_car(manufacturer, model, **others_info):
    car_profile = {}
    #将位置实参加入字典
    car_profile['manufacturer'] = manufacturer.title()
    car_profile['model'] = model.title()
    #将关键字实参加入字典
    for key, value in others_info.items():
        car_profile[key] = value
    return car_profile
#调用函数
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
