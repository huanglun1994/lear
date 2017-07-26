# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
import pygal
from die import Die

# 创建两个D6
die_1 = Die()
die_2 = Die()

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# 分析结果
results_value = set()
for a in range(1, die_1.num_sides+1):
    for b in range(1, die_2.num_sides+1):
        results_value.add(a * b)
results_list = sorted(list(results_value))
frequencies = [results.count(value) for value in results_list]

# 对结果进行可视化
hist = pygal.Bar()

hist.title = 'Results of rolling two D6 1000 times.'
hist.x_labels = [str(i) for i in results_list]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 * D6', frequencies)
hist.render_to_file('dice_visual.svg')
