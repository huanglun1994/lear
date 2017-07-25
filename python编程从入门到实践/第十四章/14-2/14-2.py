# -*- coding: utf-8 -*-
"""游戏主体"""
__author__ = 'Huang Lun'
import pygame
from settings_class import Settings
from ship_class import Ship
from gs import GameStats
from button_class import Button
from rect import Rect
import gf
from pygame.sprite import Group


def run_game():
    """运行游戏"""
    # 初始化游戏设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Hit Rect")

    # 创建Play按钮
    play_button = Button(screen, 'Play')

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个矩形块一个子弹编组
    ship = Ship(ai_settings, screen)
    rect = Rect(ai_settings, screen)
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button, rect)

        # 游戏处于活动状态时运行以下代码
        if stats.game_active:
            ship.update()
            gf.update_rect(ai_settings, rect)
            gf.update_bullets(ai_settings, bullets, rect, stats)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, stats, play_button, rect)

run_game()
