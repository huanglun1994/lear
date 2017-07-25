# -*- coding: utf-8 -*-
"""管理程序功能的函数模块"""
__author__ = 'Huang Lun'
import sys
import pygame
from star import Star


def create_group(ai_settings, screen, stars):
    """创建星星群"""
    # 创建一个星星，并计算一行可容纳多少个星星
    star = Star(ai_settings, screen)
    number_stars_x = get_number_stars_x(ai_settings, star.rect.width)
    number_rows = get_number_rows(ai_settings, star.rect.height)

    # 创建星星群
    for row_number in range(number_rows):
        for star_number in range(number_stars_x):
            create_star(ai_settings, screen, stars, star_number, row_number)


def get_number_stars_x(ai_settings, star_width):
    """计算每行可容纳多少个星星"""
    separation_distance_rank = get_space_rank(ai_settings, star_width)
    number_stars_x = int(ai_settings.screen_width / (star_width + separation_distance_rank))
    return number_stars_x


def create_star(ai_settings, screen, stars, star_number, row_number):
    """创建一个星星并将其放在当前行"""
    star = Star(ai_settings, screen)
    separation_distance_rank = get_space_rank(ai_settings, star.rect.width)
    separation_distance_row = get_space_row(ai_settings, star.rect.height)
    star.rect.x = (star.rect.width + separation_distance_rank) * star_number
    star.rect.y = (star.rect.height + separation_distance_row) * row_number
    stars.add(star)


def get_number_rows(ai_settings, star_height):
    """计算屏幕可容纳多少行星星"""
    separation_distance_row = get_space_row(ai_settings, star_height)
    number_rows = int(ai_settings.screen_height / (star_height + separation_distance_row))
    return number_rows


def check_events():
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, stars):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def get_space_rank(ai_settings, star_width):
    """获取每列星星的间距"""
    number_stars_x_around = int(ai_settings.screen_width / (star_width + 5))
    separation_distance_rank = ai_settings.screen_width / number_stars_x_around - star_width
    return separation_distance_rank


def get_space_row(ai_settings, star_height):
    """获取每行星星的间距"""
    number_rows_around = int(ai_settings.screen_height / (star_height + 5))
    separation_distance_row = ai_settings.screen_height / number_rows_around - star_height
    return separation_distance_row
