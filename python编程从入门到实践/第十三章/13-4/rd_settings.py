# -*- coding: utf-8 -*-
"""雨滴下落的设置"""
__author__ = 'Huang Lun'


class Settings:
    """存储所有设置的类"""
    def __init__(self):
        """初始化设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 雨滴速度设置
        self.raindrop_speed_factor = 1
