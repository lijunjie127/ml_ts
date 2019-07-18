import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def seven_weight(num):  # num: <class 'pandas.core.series.Series'>
    weights = np.array([0.88, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2])
    num = np.array(num)
    return np.dot(weights, num)  # <class 'numpy.float64'>


v = np.random.randn(20)
tx = pd.Series(v)
tx.index = pd.date_range('2018-12-01', periods=20, freq="d")
# rm = tx.rolling(window=5, center=False).mean()
rm = tx.rolling(window=7).apply(seven_weight, raw=False)
rm.plot(color='blue', label='rm')
tx.plot(color='orange', label='tx')
plt.legend(loc='best')
plt.title('rm_and_tx')
plt.show()



