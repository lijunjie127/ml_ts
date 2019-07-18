import matplotlib.pyplot as plt
import subprocess
from collections import Counter
"""
统计每天信息的发布量
"""


def file2list(file_path_and_name, ptime_for_0_and_ctime_for_1):
    """要求文件每一行以逗号分开，左边是发布时间，右边是抓取时间"""
    # total_line = os.system('cat {} | wc -l'.format(file_path_and_name))
    (status, output) = subprocess.getstatusoutput('cat {} | wc -l'.format(file_path_and_name))
    print('总共:{}条记录'.format(output))

    day_count_dict = {}  # 临时字典存储，例如：{'2017-07-20': 4620, '2017-09-04': 4707, ...}
    day_count_list = []  # 最终数据,例如：[4620, 4707, ...]
    with open(file_path_and_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            ctime = line.split(',')[ptime_for_0_and_ctime_for_1]  # 获取发布时间或者抓取时间，例如：2019-07-11 11:13:14
            dtime = ctime[:10]                          # 获取到天的日期，例如：2019-07-11
            day_count_dict[dtime] = day_count_dict.get(dtime, 0) + 1  # 统计

    day_count_dict_list = list(day_count_dict.items())  # 字典转列表
    day_count_dict_list.sort(key=lambda a: a[0])        # 按照时间进行排序
    for i in day_count_dict_list:                       # 提取发布数量
        day_count_list.append(i[1])

    return day_count_list


if __name__ == '__main__':
    import os
    print(os.getcwd())
    file_path = '../raw_data/OTS_data/'  # raw_data/OTS_data/ots_ccgp_country_ccgp_gov_cn_store_all.txt
    file_name = 'ots_ccgp_country_ccgp_gov_cn_store_all.txt'
    day_list = file2list(file_path + file_name, 0)  # 0是发布时间
    # print(day_list[:100])
    plt.plot(day_list)
    plt.savefig(file_name[:-4], dpi=600)

    plt.show()
