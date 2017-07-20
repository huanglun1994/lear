# -*- coding: utf-8 -*-
"""屏幕中间的士兵"""
__author__ = 'Huang Lun'
import sys
import pygame
from soldier import Soldier


def create_screen():
    """创建一个白色的窗口，中央有个士兵"""
    # 初始化并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Soldier')

    # 设置屏幕的颜色
    bg_color = (255, 255, 255)

    # 创建一个士兵对象
    soldier = Soldier(screen)

    # 开始主循环
    while True:

        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕
        screen.fill(bg_color)
        soldier.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

create_screen()
