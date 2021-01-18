# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier


"""
=================================================================================
【数组拼接】【重要】
=================================================================================
"""


def Solution(ori: list, num: int):
    res = []
    rows = len(ori)
    end_num = 0  # 记录已经去空的数组
    while True:
        for index in range(rows):
            temp = ori[index]
            if len(temp) == 0:
                continue
            elif 0 < len(temp) <= num:
                res.extend(ori[index])
                ori[index] = []
                end_num += 1
            elif len(ori[index]) > num:
                res.extend(ori[index][:num])
                ori[index] = ori[index][num:]
        if end_num >= rows:
            break
    return ",".join(res)


def Solution2(ori: list, num: int) -> list:
    rows = len(ori)
    empty_num = 0

    res = []
    # 跳出循环的条件： 取空内部的数组
    while empty_num < rows:
        # TODO 需要通过索引去获取ori数组内嵌的数组
        for index in range(rows):  # 必须使用索引，需要动态修改数组内部的列表
            row = ori[index]
            # TODO 这里需要考虑长度为零的情况
            if len(row) == 0:
                continue
            elif 0 < len(row) <= num:
                res.extend(row)
                ori[index] = []
                empty_num += 1
            elif len(row) > num:
                res.extend(row[:num])
                ori[index] = row[num:]
    return ",".join(res)


if __name__ == '__main__':
    s1 = "2,5,6,7,9,5,7"
    s2 = "1,7,4,3,4"
    ori_list = [s1.split(","), s2.split(",")]
    print(Solution(ori_list, num=3))

    ori_list = [s1.split(","), s2.split(",")]
    print(Solution2(ori_list, num=3))
