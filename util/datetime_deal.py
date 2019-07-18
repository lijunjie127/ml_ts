
def traverse(year):                 # 遍历一整年的日期
    """
    imput: 2020
    output:
    2020-01-01
    2020-01-02
    2020-01-03
    2020-01-04
    2020-01-05
    2020-01-06
    2020-01-07
    ...
    2020-12-30
    2020-12-31
    :param year:
    :return:
    """
    for month in range(1, 13):
        days = 31                   # 1, 3, 5, 7, 8, 10, 12
        if month in [4, 6, 9, 11]:
            days = 30
        if month == 2:
            if year % 4:            # 不用考虑满100或者满400的情况
                days = 28
            else:
                days = 29
        for day in range(1, days + 1):
            print('{}-{:0>2}-{:0>2}'.format(year, month, day))


traverse(2020)
