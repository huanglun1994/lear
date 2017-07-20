# -*- coding: utf-8 -*-
"""显示鬼脸"""
__author__ = 'Huang Lun'
import sys
import pygame
from photos import Photo
import time


def run():
    """程序主体"""
    # 初始化并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Poke Face")
    bg_color = (255, 255, 255)
    pfs = [Photo(screen, 'pf_1.bmp'), Photo(screen, 'pf_2.bmp'), Photo(screen, 'pf_3.bmp'), Photo(screen, 'pf_4.bmp')]

    # 开始主循环
    while True:

        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环时都重绘屏幕
        for pf in pfs:
            screen.fill(bg_color)
            pf.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()
            time.sleep(0.5)

run()
