# -*- coding: utf-8 -*-
"""雨滴类"""
__author__ = 'Huang Lun'
import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """表示单个雨滴的类"""
    def __init__(self, ai_settings, screen):
        """初始化雨滴并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载雨滴图像，并设置其rect属性
        self.image = pygame.image.load('raindrop.bmp')
        self.rect = self.image.get_rect()

        # 每个雨滴最初都在屏幕左上角，原点处
        self.rect.x = 0
        self.rect.y = 0

        # 存储雨滴的位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制雨滴"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向下移动雨滴"""
        self.y += self.ai_settings.raindrop_speed_factor
        self.rect.y = self.y

    def check_edges(self):
        """如果雨滴位于屏幕底部边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom:
            return True
