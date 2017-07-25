# -*- coding: utf-8 -*-
"""游戏中的设置"""
__author__ = 'Huang Lun'


class Settings:
    """存储游戏中的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 子弹设置
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullets_limit = 3

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 飞船的速度设置
        self.ship_speed_factor = 1.5

        # 子弹速度设置
        self.bullet_speed_factor = 5

        # 矩形块设置，rect_direction为1表示向下运动，-1表示向上运动
        self.rect_speed_factor = 1
        self.rect_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.rect_speed_factor *= self.speedup_scale
