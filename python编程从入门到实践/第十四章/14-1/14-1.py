# -*- coding: utf-8 -*-
"""游戏主体"""
__author__ = 'Huang Lun'
import pygame
import gf
from settings_class import Settings
from gs import GameStats
from button_class import Button
from ship_class import Ship
from pygame.sprite import Group


def run_game():
    """运行游戏"""
    # 初始化游戏设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        # 游戏处于活动状态时运行以下代码
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()
