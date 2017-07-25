# -*- coding: utf-8 -*-
"""模拟雨滴下落"""
__author__ = 'Huang Lun'
import pygame
from rd_settings import Settings
import rd_gf as gf
from pygame.sprite import Group


def run():
    """运行程序"""
    # 初始化设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Raindrops")

    # 创建一个雨滴编组
    raindrops = Group()

    # 创建雨滴群
    gf.create_group(ai_settings, screen, raindrops)

    # 开始游戏的主循环
    while True:
        gf.check_events()
        gf.update_raindrops(raindrops)
        gf.update_screen(ai_settings, screen, raindrops)

run()
