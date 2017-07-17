# -*- coding: utf-8 -*-
favorite_numbers = {
    'huanglun': [1, 2, 3],
    'wangdi': [4, 5, 6],
    'yandong': [7, 8, 9],
    'ranming': [10, 11, 12],
    'maning': [13, 14, 15],
}
for people, numbers in favorite_numbers.items():
    print('\n' + people.title() + "'s favorite numbers are:")
    for number in numbers:
        print('\t' + str(number))