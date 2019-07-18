import datetime

# 1.生成时间格式的数据
cur = datetime.datetime(2019, 7, 18, 13, 9)
print(cur, type(cur))

d = datetime.date(2019, 7, 21)
print(d)

t = datetime.datetime(2018, 8, 8).now()
print(t)
print('='*100)

# 2.修改时间格式的数据，加减时间间隔
cur0 = datetime.datetime(2018, 12, 30, 15, 30, 59)
print(cur0)
cur1 = cur0 + datetime.timedelta(days=1)
print(cur1)
cur2 = cur1 + datetime.timedelta(minutes=1)
print(cur2)
cur3 = cur2 + datetime.timedelta(minutes=29, seconds=1)
print(cur3)
cur4 = cur3 - datetime.timedelta(weeks=1, minutes=29, seconds=1)
print(cur4)
print('='*100)

# 生成一组满足正太分布的时间序列
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
b = datetime(2018, 12, 16, 17, 30, 55)
vi = np.random.randn(60)  # 一维正太分布的60个数据
ind = []                  # 时间戳index
for x in range(60):
    bi = b + timedelta(minutes=x)
    ind.append(bi)

ts = pd.Series(vi, index=ind)

plt.plot(ts, label='ts')
plt.legend(loc='best')
plt.show()
print(ts.count())
print(ts.head())
