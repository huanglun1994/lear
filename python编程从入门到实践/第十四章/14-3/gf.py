# -*- coding: utf-8 -*-
"""管理游戏功能的函数模块"""
__author__ = 'Huang Lun'
import sys
import pygame
from bullet_class import Bullet


def check_events(ai_settings, screen, ship, bullets, stats, play_button, rect):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, ship, bullets, mouse_x, mouse_y, rect, screen, ai_settings)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(stats, play_button, ship, bullets, mouse_x, mouse_y, rect, screen, ai_settings):
    """在玩家单击Play按钮时开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 清空子弹列表
        bullets.empty()

        # 让飞船和矩形块居中，让矩形块重新向下运动
        ship.center_ship()
        rect.reset_rect(screen, ai_settings)


def update_screen(ai_settings, screen, ship, bullets, stats, play_button, rect):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕、飞船、子弹和矩形块
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    rect.biltme()

    # 如果游戏处于非活动状态时，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
        pygame.mouse.set_visible(True)

    # 如果没有剩余射击次数了也绘制Play按钮
    check_bullets_left(stats, play_button)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_rect(ai_settings, rect):
    """检查矩形块是否位于屏幕边缘，并更新矩形块的位置"""
    check_rect_edges(ai_settings, rect)
    rect.update()


def check_rect_edges(ai_settings, rect):
    """矩形块到达边缘时采取相应的措施"""
    if rect.check_edges():
        change_rect_direction(ai_settings)


def change_rect_direction(ai_settings):
    """改变矩形块的方向"""
    ai_settings.rect_direction *= -1


def check_keydown_events(event, ai_settings, screen, ship, bullets, stats):
    """响应按键"""
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, stats, bullets)


def fire_bullet(ai_settings, screen, ship, stats, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) == 0:
        if stats.bullets_left > 0:
            bullet = Bullet(ai_settings, screen, ship)
            bullets.add(bullet)
        else:
            stats.game_active = False
            pygame.mouse.set_visible(True)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_bullets(ai_settings, bullets, rect, stats):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    check_bullet_bottom(ai_settings, bullets, stats)

    # 检查子弹和矩形块的碰撞
    check_bullet_rect_collisions(bullets, rect, ai_settings)


def check_bullet_rect_collisions(bullets, rect, ai_settings):
    """响应子弹和矩形块的碰撞"""
    # 检测子弹和矩形块之间的碰撞
    if pygame.sprite.spritecollideany(rect, bullets):
        bullets.empty()

        # 加快游戏节奏
        ai_settings.increase_speed()


def check_bullet_bottom(ai_settings, bullets, stats):
    """检查是否有子弹到达了屏幕右侧"""
    for bullet in bullets:
        if bullet.rect.right >= ai_settings.screen_width:
            bullets.empty()
            stats.bullets_left -= 1


def check_bullets_left(stats, play_button):
    """检测是否还有剩余射击次数"""
    if stats.bullets_left == 0:
        stats.game_active = False
        play_button.draw_button()
        pygame.mouse.set_visible(True)
