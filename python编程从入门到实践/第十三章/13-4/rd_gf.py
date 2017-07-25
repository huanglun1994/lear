# -*- coding: utf-8 -*-
"""雨滴下落的函数管理"""
__author__ = 'Huang Lun'
import sys
import pygame
from raindrop import Raindrop


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def get_number_raindrops_x(ai_settings, raindrop_width):
    """计算每行可容纳多少个雨滴"""
    separation_distance_rank = get_space_rank(ai_settings, raindrop_width)
    number_raindrops_x = int(ai_settings.screen_width / (raindrop_width + separation_distance_rank))
    return number_raindrops_x


def get_space_rank(ai_settings, raindrop_width):
    """获取每列雨滴的间距"""
    number_raindrops_x_around = int(ai_settings.screen_width / (raindrop_width + 5))
    separation_distance_rank = ai_settings.screen_width / number_raindrops_x_around - raindrop_width
    return separation_distance_rank


def create_raindrop(ai_settings, screen, raindrops, raindrop_number):
    """创建一个雨滴并将其放在当前行"""
    raindrop = Raindrop(ai_settings, screen)
    separation_distance_rank = get_space_rank(ai_settings, raindrop.rect.width)
    raindrop.rect.x = (raindrop.rect.width + separation_distance_rank) * raindrop_number
    raindrops.add(raindrop)


def create_group(ai_settings, screen, raindrops):
    """创建雨滴群"""
    # 创建一个雨滴，并计算一行可容纳多少个雨滴
    raindrop = Raindrop(ai_settings, screen)
    number_raindrops_x = get_number_raindrops_x(ai_settings, raindrop.rect.width)

    # 创建雨滴群
    for raindrop_number in range(number_raindrops_x):
        create_raindrop(ai_settings, screen, raindrops, raindrop_number)


def update_raindrops(raindrops):
    """若雨滴到达屏幕底部则删除雨滴"""
    # 更新雨滴的位置
    raindrops.update()

    # 删除已消失的雨滴
    for raindrop in raindrops.copy():
        if raindrop.check_edges():
            raindrops.empty()


def check_raindrops(ai_settings, screen, raindrops):
    """检查雨滴群是否没有雨滴了，没有雨滴则重新生成雨滴群"""
    if not raindrops:
        create_group(ai_settings, screen, raindrops)


def update_screen(ai_settings, screen, raindrops):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    raindrops.draw(screen)
    pygame.display.flip()
