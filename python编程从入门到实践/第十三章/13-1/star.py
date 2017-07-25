# -*- coding: utf-8 -*-
"""管理星星"""
__author__ = 'Huang Lun'
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """表示单个星星的类"""
    def __init__(self, ai_settings, screen):
        """初始化星星并设置其起始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载星星图像，并设置其rect属性
        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        # 每个星星最初都在屏幕原点
        self.rect.x = 0
        self.rect.y = 0

    def blitme(self):
        """在指定位置绘制星星"""
        self.screen.blit(self.image, self.rect)
