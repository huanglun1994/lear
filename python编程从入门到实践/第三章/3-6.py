# -*- coding: utf-8 -*-
persons = ['ma yun', 'wang jianlin', 'ding lei', 'ma huateng']
print('I find a bigger dining-table, so I want to invite another three people to my party.')
persons.insert(0, 'li yanhong')
persons.insert(2, 'liu qiangdong')
persons.append('dong mingzhu')
for person2 in persons:
    print('I will invite ' + person2.title() + ' to join my party!')