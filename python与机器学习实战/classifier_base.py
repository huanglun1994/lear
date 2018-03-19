import numpy as np


class ClassifierBase:
    def __init__(self, *args, **kwargs):
        # 将自己的名字name初始化为类名（self.__class__.__name__）
        self.name = self.__class__.__name__

    # 定义__str__魔术方法
    def __str__(self):
        return self.name

    # 定义__repr__魔术方法，通常会将它定义为和__str__方法保持一致
    def __repr__(self):
        return str(self)

    # 定义__getitem__魔术方法，以使ClassifierBase拥有类似字典查询一般的功能
    def __getitem__(self, item):
        if isinstance(item, str):
            return getattr(self, '_' + item)

    # 定义计算准确率的方法，用到了一些附录B中会介绍的numpy的知识
    @staticmethod
    def acc(y, y_pred):
        y = np.array(y)
        y_pred = np.array(y_pred)
        return np.sum(y == y_pred) / len(y)

    # 定义一个留待子类实现的接口--predict方法
    def predict(self, x, get_raw_results=False):
        pass

    # 根据预测方法（predict），输出在某个数据集上的准确率
    def evaluate(self, s, y):
        y_pred = self.predict(x)
        y = np.array(y)
        print(ClassifierBase.acc(y, y_pred))
