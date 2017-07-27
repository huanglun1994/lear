# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
import json
from country_codes import get_country_code as gcd

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 找出不能识别国别码的国家
error_country = []
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        code = gcd(country_name)
        if not code:
            error_country.append(country_name)
