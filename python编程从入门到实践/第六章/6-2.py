# -*- coding: utf-8 -*-
favorite_numbers = {
    'huanglun': 1,
    'wangdi': 2,
    'yandong': 3,
    'ranming': 4,
    'maning': 5,
}
for name, favorite_number in favorite_numbers.items():
    print(name.title() + "'s favorite number is " + str(favorite_number) + '.')
