# 导入需要用到的库
import numpy as np
import matplotlib.pyplot as plt

# 定义存储输入数据（x）和目标数据（y）的数组
x, y = [], []
# 遍历数据集，变量sample对应的正是一个个样本
for sample in open('MachineLearning-master\\_Data\\prices.txt', 'r'):
    # 由于数据是用逗号隔开的，所以调用python中的split方法并将逗号作为参数传入
    _x, _y = sample.split(',')
    # 将字符串数据转换为浮点数数据
    x.append(float(_x))
    y.append(float(_y))
# 读取完数据后，将它们转换为numpy数组以方便进一步的处理
x, y = np.array(x), np.array(y)
# 标准化
x = (x - x.mean()) / x.std()
# 将原始数据以散点图的形式画出
plt.figure()
plt.scatter(x, y, c='g', s=6)
plt.show()
