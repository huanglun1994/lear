# -*- coding: utf-8 -*-
"""矩形块"""
__author__ = 'Huang Lun'
import pygame


class Rect:
    """管理矩形块的各种行为"""

    def __init__(self, ai_settings, screen):
        """初始化矩形块并设置其初始位置"""
        self.reset_rect(screen, ai_settings)

    def update(self):
        """调整矩形块的位置"""
        # 更新表示矩形块位置的小数值
        self.y += (self.ai_settings.rect_speed_factor * self.ai_settings.rect_direction)

        # 更新表示矩形块的rect的位置
        self.rect.centery = self.y

    def biltme(self):
        """在屏幕上绘制矩形块"""
        pygame.draw.rect(self.screen, self.rect_color, self.rect)

    def check_edges(self):
        """如果矩形块位于屏幕边缘，就返回True"""
        if self.rect.bottom >= self.screen_rect.bottom:
            return True
        elif self.rect.top <= 0:
            return True

    def reset_rect(self, screen, ai_settings):
        """让矩形块复位"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()

        # 设置矩形块的尺寸
        self.width, self.height = 50, 200
        self.rect_color = (0, 255, 0)

        # 创建矩形块的rect对象，并使其在屏幕右侧边缘居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.ai_settings.screen_width - (self.width / 2)

        # 在矩形块的属性center中存储小数值
        self.y = float(self.rect.centery)
