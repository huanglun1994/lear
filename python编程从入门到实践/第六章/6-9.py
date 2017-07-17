# -*- coding: utf-8 -*-
favorite_places = {
    'Huang Lun': ['Chengdu', 'Hainan', 'Hongkong'],
    'Wang Di': ['Beijing', 'Taiwan', 'Shanghai'],
    'Xiao Ming': ['Hangzhou', 'Guangzhou', 'Nanjing'],
}
for people, places in favorite_places.items():
    print('\n' + people + "'s favorite places are:")
    for place in places:
        print('\t' + place)