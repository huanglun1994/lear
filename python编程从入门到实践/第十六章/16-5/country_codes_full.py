# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
from pygal_maps_world.i18n import COUNTRIES
from find_conuntry import error_country


def get_country_code(country_namme):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        for error_country_name in error_country:
            if name == error_country_name:
                return code
            elif name == country_namme:
                return code
