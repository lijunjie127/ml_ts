import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.api import Holt
from math import sqrt
"""
方法5：霍尔特(Holt)线性趋势法
"""
df = pd.read_csv('../raw_data/train.csv', nrows=11856)
# df['Datetime'] = pd.to_datetime(df['Datetime'])
# df.set_index("Datetime", inplace=True)
# df.index = pd.DatetimeIndex(df.index)
train = df[0:10392]
test = df[10392:]

# Aggregating the dataset at daily level
df['Timestamp'] = pd.to_datetime(df['Datetime'], format='%d-%m-%Y %H:%M')
df.index = df['Timestamp']
df = df.resample('D').mean()

train['Timestamp'] = pd.to_datetime(train['Datetime'], format='%d-%m-%Y %H:%M')
train.index = train['Timestamp']
train = train.resample('D').mean()

test['Timestamp'] = pd.to_datetime(test['Datetime'], format='%d-%m-%Y %H:%M')
test.index = test['Timestamp']
test = test.resample('D').mean()

# print(df.head())
# print('-'*100)

# print(df.head())
# print('-'*100)
print(train.head())
# print(train['Count'].axes)

# print(train.iloc['Count'])

sm.tsa.seasonal_decompose(train['Count']).plot()
result = sm.tsa.stattools.adfuller(train['Count'])
plt.show()

# from statsmodels.tsa.api import Holt
#
# y_hat_avg = test.copy()
#
# fit = Holt(np.asarray(train['Count'])).fit(smoothing_level=0.3, smoothing_slope=0.1)
# y_hat_avg['Holt_linear'] = fit.forecast(len(test))
#
# plt.figure(figsize=(16, 8))
# plt.plot(train['Count'], label='Train')
# plt.plot(test['Count'], label='Test')
# plt.plot(y_hat_avg['Holt_linear'], label='Holt_linear')
# plt.legend(loc='best')
# plt.show()


# rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['SES']))
# print(rms)
