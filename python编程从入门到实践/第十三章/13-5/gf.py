# -*- coding: utf-8 -*-
"""管理游戏的函数模块"""
__author__ = 'Huang Lun'
import sys
import pygame
from ball import Ball


def check_events(person):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, person)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, person)
            

def update_screen(ai_settings, screen, person, balls):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    person.blitme()
    for ball in balls:
        ball.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
    

def check_keydown_events(event, person):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        person.moving_right = True
    elif event.key == pygame.K_LEFT:
        person.moving_left = True


def check_keyup_events(event, person):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        person.moving_right = False
    elif event.key == pygame.K_LEFT:
        person.moving_left = False


def update_ball(ai_settings, screen, persons, balls):
    """更新球的位置，并检测球和人的碰撞"""
    # 更新球的位置
    balls.update()

    # 检查球和人是否碰撞以及是否超出了屏幕底部
    check_ball_person_collisions(balls, persons, ai_settings, screen)
    check_ball_bottom(balls, ai_settings, screen)


def check_ball_person_collisions(balls, persons, ai_settings, screen):
    """响应球和人的碰撞"""
    # 删除发生碰撞的球
    collisions = pygame.sprite.groupcollide(balls, persons, True, False)

    # 如果球与人发生碰撞则重新创建一个球
    if not balls:
        create_ball(ai_settings, screen, balls)


def create_ball(ai_settings, screen, balls):
    """创建一个球"""
    ball = Ball(ai_settings, screen)
    balls.add(ball)


def check_ball_bottom(balls, ai_settings, screen):
    """检测球是否超出屏幕底部，若超出则重新生成一个球"""
    for ball in balls.copy():
        if ball.rect.bottom >= ai_settings.screen_height:
            balls.remove(ball)
            create_ball(ai_settings, screen, balls)
