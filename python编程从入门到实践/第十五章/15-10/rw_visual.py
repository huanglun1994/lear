# -*- coding: utf-8 -*-
"""绘制随机漫步点图"""
__author__ = 'Huang Lun'
import pygal
from random_walk import RandomWalk

# 创建一个RandomWalk实例，并将其包含的所有点都绘制出来
rw = RandomWalk()
rw.fill_walk()

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Random Walk'
hist.x_labels = [str(i) for i in rw.x_values]
hist.x_title = 'X'
hist.y_title = 'Y'

hist.add('X + Y', rw.y_values)
hist.render_to_file('random_walk_visual.svg')
