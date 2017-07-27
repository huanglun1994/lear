# -*- coding: utf-8 -*-
"""绘制全球各国2016年的GDP图表"""
__author__ = 'Huang Lun'
import json
from pygal_maps_world.maps import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS
from country_codes_full import get_country_code as gcd

# 将数据加载到一个列表中
filename = 'gdp.json'
with open(filename) as f:
    gdp_data = json.load(f)

# 创建一个包含GDP值的字典
cc_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2016':
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = gcd(country_name)
        if code:
            cc_gdp[code] = gdp

wm_style = RS('#336699', base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World GDP in 2016, by Country'
wm.add('GDP', cc_gdp)

wm.render_to_file('world_gdp.svg')
