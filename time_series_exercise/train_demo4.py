import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.api import SimpleExpSmoothing
from math import sqrt
"""
方法4：简单指数平滑法
报错：
from scipy.misc import logsumexp
ImportError: cannot import name 'logsumexp'
解决：重装statsmodels和scipy
"""

# Subsetting the dataset
# Index 11856 marks the end of year 2013
df = pd.read_csv('../raw_data/train.csv', nrows=11856)
# print(df.tail(10))

# Creating train and test set
# Index 10392 marks the end of October 2013
train = df[0:10392]
test = df[10392:]

y_hat_avg = test.copy()
fit = SimpleExpSmoothing(np.asarray(train['Count'])).fit(smoothing_level=0.6, optimized=False)
y_hat_avg['SES'] = fit.forecast(len(test))
plt.figure(figsize=(16, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['SES'], label='SES')
plt.legend(loc='best')
plt.savefig('train_demo4_ses')
plt.show()


rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['SES']))
print(rms)



