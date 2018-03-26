# 导入Tensorflow库以进行后续操作
import tensorflow as tf
import numpy as np
# from .Bases import ClassifierBase

# # 定义常亮，同时把数据类型定义为能够进行GPU计算的tf.float32类型
# x = tf.constant(1, dtype=tf.float32)
# # 定义可训练的变量
# y = tf.Variable(2, dtype=tf.float32)
# # 定义不可训练的变量
# z = tf.Variable(3, dtype=tf.float32, trainable=False)
# x_add_y = x + y
# print(x_add_y)
# y_sub_z = y - z
# print(y_sub_z)
# x_times_z = x * z
# print(x_times_z)
# z_div_x = z / x
# print(z_div_x)
# # 用Numpy数组进行Tensorflow的初始化
# x = tf.constant(np.array([[1, 2], [3, 4]]))
# # Tensorflow中对应于np.sum的方法
# axis0 = tf.reduce_sum(x, axis=0)  # 将会得到值为[4,6]的tensor
# axis1 = tf.reduce_sum(x, axis=1)  # 将会得到值为[3,7]的tensor
# print(axis0, axis1)
# x = tf.constant(1)
# y = x + 1
# z = y + 1
# print(tf.Session().run(y))  # 将会输出2
# print(tf.Session().run([y, z]))  # 将会输出[2,3]
# """x = tf.Variable(1)
# print(tf.Session().run(x))  # 报错！"""
# x = tf.Variable(1)
# with tf.Session().as_default() as sess:
#     sess.run(tf.global_variables_initializer())  # 初始化所有Variable
#     print(sess.run(x))
# class TFLinearSVM(ClassifierBase):
#     def __init__(self):
#         super(TFLinearSVM, self).__init__()
#         self._w = self._b = None
#         # 使用self._sess属性来存储一个Session以方便调用
#         self._sess = tf.Session()
#
#     def fit(self, x, y, sample_weight=None, lr=0.001, epoch=10 ** 4, tol=1e-3):
#         # 将sample_weight转换 为constant Tensor
#         if sample_weight is None:
#             sample_weight = tf.constant(np.ones(len(y)), dtype=tf.float32, name='sample_weight')
#         else:
#             sample_weight = tf.constant(np.array(sample_weight) * len(y), dtype=tf.float32, name='sample_weight')
#         # 将输入数据转换为constant Tensor
#         x, y = tf.constant(x, dtype=tf.float32), tf.constant(y, dtype=tf.float32)
#         # 将需要训练的w、b定义为可训练Variable
#         self._w = tf.Variable(np.zeros(x.shape[1]), dtype=tf.float32, name='w')
#         self._b = tf.Variable(0., dtype=tf.float32, name='b')
#         # 调用相应方法获得当前模型预测值
#         y_pred = self.predict(x, True, False)
#         # 利用相应函数计算出总损失
#         cost = tf.reduce_sum(tf.maximum(1 - y * y_pred, 0) * sample_weight) + tf.nn.l2_loss(self._w)
#         # 利用Tensorflow封装好的优化器，定义更新参数步骤
#         # 该步骤会调用相应算法，以减少上述总损失为目的来进行参数的更新
#         train_step = tf.train.AdamOptimizer(learning_rate=lr).minimize(cost)
#         # 初始化所有Variable
#         self._sess.run(tf.global_variables_initializer())
#         # 不断调用更新参数步骤，如果期间发现误差小于阈值的话就提前终止迭代
#         for _ in range(epoch):
#             if self._sess.run([cost, train_step])[0] < tol:
#                 break
#
#     # 定义获取模型预测值的方法
#     def predict(self, x, get_raw_results=False, out_of_sess=True):
#         # 利用reduce_sum方法算出预测向量
#         rs = tf.reduce_sum(self._w * x, axis=1) + self._b
#         if not get_raw_results:
#             rs = tf.sign(rs)
#         # 如果out_of_sess参数为True，就要利用Session吧具体数值算出来
#         if out_of_sess:
#             rs = self._sess.run(rs)
#         # 否则直接把Tensor返回即可
#         return rs
# 定义一个数据类型weitf.float32，长未知，宽为2的矩阵Placeholder
x = tf.placeholder(tf.float32, [None, 2])
# 定义一个numpy数组：[[1,2],[3,4],[5,6]]
y = np.array([[1, 2], [3, 4], [5, 6]])
# 定义x+1对应的Tensor
z = x + 1
# 利用Session及其feed_dict参数，将y的值赋予x，同时输出z的值
print(tf.Session().run(z, feed_dict={x: y}))  # 将会输出[[2,3],[4,5],[6,7]]
