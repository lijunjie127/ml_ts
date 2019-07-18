import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from ml_model.util.test_stationarity import test_stationarity

# plt.plot([1,2,4,5,6])
# plt.show()

data = pd.read_csv('raw_data/ChinaBank.csv')
# print(data.head())
# csv_file.to_csv('copy_for_csv.csv')
ts = data['Low']
# print(ts.head(100))
ts_diff_1 = ts.diff(1)
# plt.plot(ts_diff_1, color='red', label='diff_1')
# plt.plot(ts_diff_1.diff(1), color='green', label='diff_2')
plt.plot(ts, color='blue', label='Original')
plt.plot(np.log(ts), color='red', label='Log')

ts_log = np.log(ts)
# print(ts_diff_1)
print(type(ts_diff_1))
print(type(ts))
# print(ts)
test_stationarity(ts)

moving_avg = ts_log.rolling(12).mean()
plt.plot(ts_log)
plt.plot(moving_avg, color='green', label='Avg')

plt.legend(loc='best')
plt.show(block=False)

ts_diff_1.dropna(inplace=True)
ts_diff_2 = ts_diff_1.diff(1)
ts_diff_2.dropna(inplace=True)
test_stationarity(ts_diff_2)

da = [1,1.1,1,1.1,1,1,1.9,1.2,1,1.1,1,1,1,1,1]
test_series = pd.Series(da)
test_stationarity(test_series)

