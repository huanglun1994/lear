# -*- coding: utf-8 -*-
"""游戏主体"""
__author__ = 'Huang Lun'
import pygame
from settings_class import Settings
from ship_class import Ship
import gf
from pygame.sprite import Group


def run_game():
    """运行游戏"""
    # 初始化游戏设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, ai_settings)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
