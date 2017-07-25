# -*- coding: utf-8 -*-
"""游戏设置"""
__author__ = 'Huang Lun'


class Settings:
    """存储游戏中的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # 人的速度设置
        self.person_speed_factor = 1.5

        # 球设置
        self.ball_drop_speed = 1
