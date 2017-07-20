# -*- coding: utf-8 -*-
"""管理士兵"""
__author__ = 'Huang Lun'
import pygame


class Soldier:
    """管理士兵的各种行为"""
    def __init__(self, screen):
        """初始化士兵并设置其初始位置"""
        self.screen = screen

        # 加载士兵图像并获取其外接矩形
        self.image = pygame.image.load('soldier.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个新士兵放在屏幕中央
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """在指定位置绘制士兵"""
        self.screen.blit(self.image, self.rect)
