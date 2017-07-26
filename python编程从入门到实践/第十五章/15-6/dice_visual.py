# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
import pygal
from die_class import Die

# 创建两个D6
die_1 = Die()
die_2 = Die()

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 1000 times.'
hist.x_labels = [str(i) for i in range(2, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
