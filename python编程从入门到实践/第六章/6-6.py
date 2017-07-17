# -*- coding: utf-8 -*-
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
persons = ['jen', 'phil', 'huang lun', 'wang di']
for person in persons:
    if person in favorite_languages.keys():
        print('Thank you for taking your poll.')
    else:
        print('Please take your poll.')
