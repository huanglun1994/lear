# -*- coding: utf-8 -*-
"""抓球游戏"""
__author__ = 'Huang Lun'
import pygame
from game_settings import Settings
from person import Person
import gf
from pygame.sprite import Group


def run_game():
    """运行游戏"""
    # 初始化游戏设置、屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Person And Ball")

    # 创建一个人和一个球编组，人编组
    persons = Group()
    person = Person(ai_settings, screen)
    persons.add(person)
    balls = Group()

    # 创建一个球
    gf.create_ball(ai_settings, screen, balls)

    # 开始游戏的主循环
    while True:
        gf.check_events(person)
        person.update()
        gf.update_ball(ai_settings, screen, persons, balls)
        gf.update_screen(ai_settings, screen, person, balls)

run_game()
