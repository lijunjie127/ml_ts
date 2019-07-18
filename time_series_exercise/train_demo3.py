import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt

# Subsetting the dataset
# Index 11856 marks the end of year 2013
df = pd.read_csv('../raw_data/train.csv', nrows=11856)

# Creating train and test set
# Index 10392 marks the end of October 2013
train = df[0:10392]
test = df[10392:]

y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = train['Count'].rolling(60).mean().iloc[-1]
plt.figure(figsize=(16, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast')
plt.legend(loc='best')
plt.savefig('train_demo3_moving_avg')
plt.show()


rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['moving_avg_forecast']))
print(rms)



