# -*- coding: utf-8 -*-
__authour__ = 'Huang Lun'
#建立一个空列表，存储用户想去度假的地方
responses = []
#设置一个标志，指出调查是否继续
active = True
prompt = 'If you could visit one place in the world, where would you go? '
while active:
    #提示被调查者输入想去的地方
    place = input(prompt)
    #将答案存入列表
    responses.append(place)
    #询问是否继续调查
    repeat = input('Would you like to let another person respond? (yes / no) ')
    if repeat == 'no':
        active = False
#打印调查结果
print('\n--- Poll Results ---')
for desired_place in responses:
    print(desired_place.title())
