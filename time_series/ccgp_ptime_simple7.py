import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
"""
思路：直接拿上周同一时间的发布量来预估本周发布量
"""


def seven_weight(num):  # num: <class 'pandas.core.series.Series'>
    # weights = np.array([0.88, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02])
    # num = np.array(num)
    # print(num, np.dot(weights, num))
    # return np.dot(weights, num)  # 向量点乘
    return num[0]


# 1.读取csv格式数据
df = pd.read_csv('../raw_data/OTS_data_count/ccgp_country_ctime_2019_count.csv')

# 2.将数据索引改为日期形式
df['Date'] = pd.to_datetime(df['Date'])
df.set_index("Date", inplace=True)

# 3.按照一定频率重新采样(采样的时候会补全数据，缺失值补为0)
df = df.resample('d', closed='left').sum()
# print(ts.tail(12))

# 4.将datafram数据集转换为series数据
ts = pd.Series(df['Count'].values, index=df.index)

# 5.划分训练集和测试集
seg = int(ts.count() * 0.9) - 7  # 不需要训练，直接测试
test = ts[seg-1:-1]
print(type(test))
predicted = test.rolling(window=8).apply(seven_weight, raw=False)  # 滑动窗口
plt.plot(test, label='test')
plt.plot(predicted, label='predicted')
plt.show()
predicted.dropna(inplace=True)

print(type(test), type(predicted))
print(len(test), len(predicted))
# test, predicted = list(test), list(predicted)
# print(len(test), len(predicted))
# print(type(test), type(predicted))
print(test)
print(predicted)
test = test[7:]
rms = sqrt(mean_squared_error(test, predicted))
print('均方误差：', rms)
