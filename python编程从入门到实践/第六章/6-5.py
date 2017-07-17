# -*- coding: utf-8 -*-
river_countrys = {
    'nile': 'egypt',
    'chang jiang': 'china',
    'huang he': 'china',
}
for river, country in river_countrys.items():
    print('The '+ river.title() + ' runs through ' + country.title() + '.')
for river in river_countrys.keys():
    print(river.title())
for country in set(river_countrys.values()):
    print(country.title())