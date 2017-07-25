# -*- coding: utf-8 -*-
"""一屏幕的星星"""
__author__ = 'Huang Lun'
import pygame
from star_settings import Settings
import gf
from pygame.sprite import Group


def run():
    """运行程序"""
    # 初始化设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Star")

    # 创建一个星星编组
    stars = Group()

    # 创建星星群
    gf.create_group(ai_settings, screen, stars)

    # 开始主循环
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, stars)

run()
