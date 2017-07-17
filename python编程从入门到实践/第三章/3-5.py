# -*- coding: utf-8 -*-
persons = ['ma yun', 'wang jianlin', 'ding lei', 'ma huateng']
print("It's a pity that " + persons[0].title() + " can't be present.")
persons[0] = 'lei jun'
for person1 in persons:
    print('I will invite ' + person1.title() + ' to join my party!')