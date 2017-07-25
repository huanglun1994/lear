# -*- coding: utf-8 -*-
"""球"""
__author__ = 'Huang Lun'
import pygame
from random import randint
from pygame.sprite import Sprite


class Ball(Sprite):
    """管理球的各种行为"""
    def __init__(self, ai_settings, screen):
        """初始化球并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载球图像并获取其外接矩形
        self.image = pygame.image.load('ball.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将球放在屏幕顶部随机位置
        self.rect.centerx = randint(self.rect.width / 2, self.ai_settings.screen_width - (self.rect.width / 2))
        self.rect.centery = 0

        # 在球的属性center中存储小数值
        self.center = float(self.rect.centery)

    def update(self):
        """更新球下落后的位置"""
        self.center += self.ai_settings.ball_drop_speed

        # 根据self.center更新rect对象
        self.rect.centery = self.center

    def blitme(self):
        """在指定位置绘制球"""
        self.screen.blit(self.image, self.rect)
