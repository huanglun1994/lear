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
"""学习笔记：
数据标准化的几种方法：
方法一：规范化方法
也叫离差标准化，是对原始数据的线性变换，使结果映射到[0,1]区间。
方法二：正规化方法
这种方法基于原始数据的均值（mean）和标准差（standard deviation）进行数据的标准化。
将A的原始值x使用z-score标准化到x’。
z-score标准化方法适用于属性A的最大值和最小值未知的情况，或有超出取值范围的离群数据的情况。
spss默认的标准化方法就是z-score标准化。
用Excel进行z-score标准化的方法：在Excel中没有现成的函数，需要自己分步计算，其实标准化的公式很简单。
步骤如下：
1.求出各变量（指标）的算术平均值（数学期望）xi和标准差si ；
2.进行标准化处理：
zij=（xij－xi）/si
其中：zij为标准化后的变量值；xij为实际变量值。
3.将逆指标前的正负号对调。
标准化后的变量值围绕0上下波动，大于0说明高于平均水平，小于0说明低于平均水平。
方差：
（variance)是在概率论和统计方差衡量随机变量或一组数据时离散程度的度量。
概率论中方差用来度量随机变量和其数学期望（即均值）之间的偏离程度。
统计中的方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数。
在许多实际问题中，研究方差即偏离程度有着重要意义。
方差是衡量源数据和期望值相差的度量值。
标准差：
标准差（Standard Deviation） ，中文环境中又常称均方差，是离均差平方的算术平均数的平方根，用σ表示。
标准差是方差的算术平方根。标准差能反映一个数据集的离散程度。平均数相同的两组数据，标准差未必相同。"""
x = (x - x.mean()) / x.std()
# 将原始数据以散点图的形式画出
plt.figure()
plt.scatter(x, y, c='g', s=6)
plt.show()
# 在（-2,4）这个区间上取100个点作为画图的基础
x0 = np.linspace(-2, 4, 100)


# 利用numpy的函数定义训练并返回多项式回归模型的函数
# deg参数代表着模型参数中的n，亦即模型中多项式的次数
# 返回的模型能够根据输入的x（默认是x0），返回相对应的预测的y
def get_model(deg):
    return lambda input_x=x0: np.polyval(np.polyfit(x, y, deg), input_x)


# 根据参数n、输入的x、y返回相对应的损失
def get_cost(deg, input_x, input_y):
    return 0.5 * ((get_model(deg)(input_x) - input_y) ** 2).sum()


# 定义测试参数集并根据它进行各种实验
test_set = (1, 4, 10)
for d in test_set:
    # 输出相应的损失
    print(get_cost(d, x, y))
# 画出相应的图像
plt.scatter(x, y, c='g', s=20)
for d in test_set:
    plt.plot(x0, get_model(d)(), label='degree = {}'.format(d))
# 将横轴、纵轴的范围分别限制在（-2,4）、（10^5,8*10^5）
plt.xlim(-2, 4)
plt.ylim(1e5, 8e5)
# 调用legend方法使曲线对应的label正确显示
plt.legend()
plt.show()
