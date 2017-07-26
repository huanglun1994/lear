# -*- coding: utf-8 -*-
"""掷骰子可视化"""
__author__ = 'Huang Lun'
import matplotlib.pyplot as plt
from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 设置绘图窗口的尺寸
plt.figure(dpi=128, figsize=(10, 6))

# 绘制折线图并将图形显示出来
plt.plot(list(range(1, die.num_sides+1)), frequencies, 'r-', linewidth=2)

# 设置图表标题，并给坐标轴加上标签
plt.title("Results of rolling one D6 1000 times", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Frequencies', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
