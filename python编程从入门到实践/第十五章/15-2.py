# -*- coding: utf-8 -*-
"""数的立方散点图"""
__author__ = 'Huang Lun'
import matplotlib.pyplot as plt

x_5 = list(range(1, 6))
y_5 = [x ** 3 for x in x_5]
x_5000 = list(range(1, 5001))
y_5000 = [x ** 3 for x in x_5000]

# plt.scatter(x_5, y_5, c=y_5, cmap=plt.cm.Greens, edgecolors='none', s=40)
plt.scatter(x_5000, y_5000, c=y_5000, cmap=plt.cm.Reds, edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title('Cube Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()
