# -*- coding: utf-8 -*-
"""响应并打印按键事件的属性"""
__author__ = 'Huang Lun'
import sys
import pygame


def run():
    """程序主体"""
    # 初始化并创建一个屏幕对象
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Key Event")
    bg_color = (255, 255, 255)

    # 开始主循环
    while True:

        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        # 每次循环时都重绘屏幕
        screen.fill(bg_color)

        # 让最近绘制的屏幕可见
        pygame.display.flip()

run()
