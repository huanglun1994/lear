# -*- coding: utf-8 -*-
"""测试城市函数是否正确"""
__author__ = 'Huang Lun'
# 导入函数和测试模块
from city_functions_11-2-2 import city_country
import unittest


class CityTestCase(unittest.TestCase):
    """测试city_conuntry函数"""

    def test_city_county(self):
        """函数能正确处理类似beijing，china的输入吗"""
        message = city_country('santiago', 'chile')
        self.assertEqual(message, 'Santiago, Chile')

# 开始测试
if __name__ == '__main__':
    unittest.main()
