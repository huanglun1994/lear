# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取日期、最高气温和最低气温
filename1 = 'death_valley_2014.csv'
filename2 = 'sitka_weather_2014.csv'


def read_csv(filename):
    """读取文件"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    return dates, highs, lows

data1 = read_csv(filename1)
data2 = read_csv(filename2)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(data1[0], data1[1], c='red', alpha=0.5)
plt.plot(data1[0], data1[2], c='blue', alpha=0.5)
plt.fill_between(data1[0], data1[1], data1[2], facecolor='blue', alpha=0.1)

plt.plot(data2[0], data2[1], c='green', alpha=0.5)
plt.plot(data2[0], data2[2], c='black', alpha=0.5)
plt.fill_between(data2[0], data2[1], data2[2], facecolor='black', alpha=0.1)

# 设置图形的格式
plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA and Sitka', fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
