# -*- coding: utf-8 -*-
"""照片"""
__author__ = 'Huang Lun'
import pygame


class Photo:
    """管理照片的各种行为"""
    def __init__(self, screen, photo_name):
        """初始化照片并设置其初始位置"""
        self.screen = screen

        # 加载照片图像并获取其外接矩形
        self.image = pygame.image.load(photo_name)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每张新照片放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """在指定位置绘制照片"""
        self.screen.blit(self.image, self.rect)
