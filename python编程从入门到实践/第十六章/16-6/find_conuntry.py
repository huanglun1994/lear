# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
import json
from country_codes import get_country_code as gcd

# 将数据加载到一个列表中
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# 找出不能识别国别码的国家
error_country = []
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2016':
        country_name = gdp_dict['Country Name']
        code = gcd(country_name)
        if not code:
            error_country.append(country_name)
