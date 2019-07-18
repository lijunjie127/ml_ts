import matplotlib.pyplot as plt
import pandas as pd
import os
print(os.getcwd())

pdict = {}
cdict = {}
count = 0
"""2019-07-15 18:30:38"""

# 2019年的抓取时间
with open('../raw_data/OTS_year_data/ccgp_country_ctime_2019.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        ptime, ctime = line.split(',')

        # 按天（日期）小时统计发布时间
        p_time = ptime[:10]
        c_time = ctime[:10]

        pdict[p_time] = pdict.get(p_time, 0) + 1
        cdict[c_time] = cdict.get(c_time, 0) + 1

plist = list(pdict.items())          # 时间，发布数的键值对转换为列表，列表中每个元素是元组
clist = list(cdict.items())

plist.sort(key=lambda x: x[0])       # 按照日期进行排序
clist.sort(key=lambda x: x[0])

p_count = [x[1] for x in plist]      # 取出列表中的第二个元素，去掉日期，保留发布量
c_count = [x[1] for x in clist]

p_count_pd = pd.Series(p_count)      # 转成series格式
c_count_pd = pd.Series(c_count)

# plt.plot(p_count_pd)
# plt.plot(p_count_pd.diff(1))
# plt.plot(p_count_pd.diff(1).diff(1))
# plt.plot(p_count_pd.diff(1).diff(1).diff(1))
plt.plot(c_count_pd)
plt.plot(c_count_pd.diff(1))
plt.plot(c_count_pd.diff(1).diff(1))
plt.plot(c_count_pd.diff(1).diff(1).diff(1))

plt.show()

