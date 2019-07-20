import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import acf, pacf, plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARMA

# 初始化数据
time_series = pd.Series(
    [151.0, 188.46, 199.38, 219.75, 241.55, 262.58, 328.22, 396.26, 442.04, 517.77, 626.52, 717.08, 824.38, 913.38,
     1088.39, 1325.83, 1700.92, 2109.38, 2499.77, 2856.47, 3114.02, 3229.29, 3545.39, 3880.53, 4212.82, 4757.45,
     5633.24, 6590.19, 7617.47, 9333.4, 11328.92, 12961.1, 15967.61])
time_series.index = pd.Index(sm.tsa.datetools.dates_from_range('1978', '2010'))
time_series.plot(figsize=(12, 8))  # 1200 * 800 像素
plt.show()

# 指数变线性，取对数
time_series = np.log(time_series)
time_series.plot(figsize=(8, 6))  # 800 * 600 像素
plt.show()

# 平稳化，取一阶差分
time_series = time_series.diff(1)
time_series = time_series.dropna(how=any)
time_series.dropna(inplace=True)
time_series.plot(figsize=(8, 6))  # 800 * 600 像素
plt.show()

#  adf 检验
t = sm.tsa.stattools.adfuller(time_series)
# output = pd.DataFrame(
#     index=['Test Statistic Value', "p-value", "Lags Used", "Number of Observations Used", "Critical Value(1%)",
#            "Critical Value(5%)", "Critical Value(10%)"], columns=['value']
#     )
# output['value']['Test Statistic Value'] = t[0]
# output['value']['p-value'] = t[1]
# output['value']['Lags Used'] = t[2]
# output['value']['Number of Observations Used'] = t[3]
# output['value']['Critical Value(1%)'] = t[4]['1%']
# output['value']['Critical Value(5%)'] = t[4]['5%']
# output['value']['Critical Value(10%)'] = t[4]['10%']
# print(output)
print(t)
if float(t[1]) < 0.05:
    print('{}:通过平稳性检验'.format(t[1]))
else:
    print('未通过')

# 确定自相关系数和平均移动系数（p,q）
plot_acf(time_series)
plot_pacf(time_series)
plt.show()

r, rac, Q = sm.tsa.acf(time_series, qstat=True)
prac = pacf(time_series, method='ywmle')
table_data = np.c_[range(1, len(r)), r[1:], rac, prac[1:len(rac) + 1], Q]
table = pd.DataFrame(table_data, columns=['lag', "AC", "Q", "PAC", "Prob(>Q)"])

print(table)

d = 1
(p, q) = (sm.tsa.arma_order_select_ic(time_series, max_ar=3, max_ma=3, ic='aic')['aic_min_order'])
print('p q:', p, q)
arma_mod = ARMA(time_series, (p, d, q)).fit(disp=-1, method='mle')
summary = (arma_mod.summary2(alpha=.05, float_format="%.8f"))
print(summary)

# 残差和白噪声检验
# arma_mod = ARMA(time_series, (0, 1, 1)).fit(disp=-1, method='mle')
resid = arma_mod.resid
resid.plot()
plt.title('resid')
plt.show()
t = sm.tsa.stattools.adfuller(resid)
print(t)
