# -*- coding: utf-8 -*-
wang_wang = {'kind': 'Dog', 'master': 'Wang Di'}
miao_miao = {'kind': 'Cat', 'master': 'Huang Lun'}
pets = [wang_wang, miao_miao]
for pet in pets:
    print('\n' + pet['master'] + "'s pet is a " + pet['kind'] + '.')