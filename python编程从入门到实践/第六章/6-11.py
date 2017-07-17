# -*- coding: utf-8 -*-
cities = {
    'Beijing': {
        'country': 'China',
        'population': '21730 thousand',
        'fact': 'This city is the capital of China.',
    },
    'Washington': {
        'country': 'America',
        'population': '650 thousand',
        'fact': 'This city is the capital of America.',
    },
    'London': {
        'country': 'England',
        'population': '8000 thousand',
        'fact': 'This city is the capital of England.',
    },
}
for city, infos in cities.items():
    print('\n' + city.title() + "'s infomation is:")
    for info, content in infos.items():
        print('\t' + info.title() + ": " + content)
