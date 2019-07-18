import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

from sklearn.metrics import mean_squared_error
from math import sqrt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1.读取csv格式数据
df = pd.read_csv('../raw_data/OTS_data_count/ccgp_country_ctime_2019_count.csv')


# 2.将数据索引改为日期形式
df['Date'] = pd.to_datetime(df['Date'])
df.set_index("Date", inplace=True)

# 3.按照一定频率重新采样(采样的时候会补全数据，缺失值补为0)
df = df.resample('d', closed='left').sum()

# 4.将datafram数据集转换为series数据
ts = pd.Series(df['Count'].values, index=df.index)

# 5.检验数据的平稳性并平稳化数据集
# test_stationarity(ts)
# ts_diff_1 = ts.diff(1)			# 对ts求一阶差分
# ts_diff_1.dropna(inplace=True)  # 对一阶差分进行缺失值处理
# test_stationarity(ts_diff_1)
# plt.plot(ts, color='red', label='origin')
# plt.plot(ts_diff_1, color='blue', label='diff1')
# plt.legend(loc='best')
# plt.show()

# 6.划分训练集和测试集(7:3的比例)
seg = int(ts.count() * 0.9)
train = ts[:seg]  # 六月之前为训练集
test = ts[seg:-1]   # 七月开始为测试集

# 6.1 可视化输出训练数据和测试数据
# plt.plot(train, label='data_train')
# plt.plot(test, label='data_test')
# plt.title('Original')
# plt.legend(loc='best')
# plt.show()

# 7.通过ARIMA差分自回归移动平均模型对数据进行训练
fit1 = sm.tsa.statespace.SARIMAX(train, order=(2, 1, 4), seasonal_order=(0, 1, 1, 7)).fit()
# fit1.save()
predict_series = fit1.predict(start="2019-06-26", end="2019-7-14", dynamic=True)

plt.figure(figsize=(16, 8))
plt.plot(train, label='Train')
plt.plot(test, label='True')
plt.plot(predict_series, label='Predict')
plt.title('2019_ccgp_country_crawl_time_d1')
plt.legend(loc='best')
plt.show()

# print('实际值：', test)
# print('预测值：', predict_series)

# print(len(test), len(predict_series))
print(type(test), type(predict_series))
# <class 'pandas.core.series.Series'> <class 'pandas.core.series.Series'>

rms = sqrt(mean_squared_error(test, predict_series))
print('均方误差：', rms)
