import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

ChinaBank = pd.read_csv('../raw_data/ChinaBank.csv', index_col='Date', parse_dates=['Date'])
print(ChinaBank)

# ChinaBank.index = pd.to_datetime(ChinaBank.index)
# print(ChinaBank)

sub = ChinaBank['2014-01':'2014-06']['Close']
# print(sub)

train = sub.ix['2014-01':'2014-03']
# print(train)

test = sub.ix['2014-04':'2014-06']
plt.figure(figsize=(10, 10))
# print(train)
plt.plot(train)
plt.savefig('../output/ChinaBank_raw', dpi=600)
plt.show()

ChinaBank['Close_diff_1'] = ChinaBank['Close'].diff(1)
ChinaBank['Close_diff_2'] = ChinaBank['Close_diff_1'].diff(1)
fig = plt.figure(figsize=(20, 6))
ax1 = fig.add_subplot(131)
ax1.plot(ChinaBank['Close'])
ax2 = fig.add_subplot(132)
ax2.plot(ChinaBank['Close_diff_1'])
ax3 = fig.add_subplot(133)
ax3.plot(ChinaBank['Close_diff_2'])
plt.savefig('../output/ChinaBank', dpi=600)
plt.show()
