# -*- coding: utf-8 -*-
persons = ['ma yun', 'wang jianlin', 'ding lei', 'ma huateng']
print("I'm so sorry that I only can invite two person to join my party.")
for i in range(len(persons) - 2):
    person3 = persons.pop()
    print('Dear ' + person3.title() + ", I'm so sorry that I can't invite you to join my party.")
for person4 in persons:
    print('Dear ' + person4.title() + ", I'll invite you to join my party.")
del persons[1]
del persons[0]
print(persons)