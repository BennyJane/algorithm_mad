# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【找朋友】 ： 双指针
=================================================================================
"""


def Solution(ori: list):
    length = len(ori)
    if len(ori) < 2:
        return [0]
    res = [0 for _ in ori]  # 不在原数据上修改
    for i in range(0, length - 1):
        left = ori[i]
        j = i + 1  # 第二个指针
        while j < length:
            right = ori[j]
            if right > left:
                res[i] = j
                break  # FIXME 及时终止
            else:
                j += 1
    return res


def Solution2(ori: list):
    _len = len(ori)
    res = [0] * _len
    if _len < 2:
        return res
    for i in range(_len):
        cur_height = ori[i]
        for j in range(i + 1, _len):
            height = ori[j]
            if height > cur_height:
                res[i] = j
                break  # FIXME 只需要找到一个满足条件的对象
    return res


if __name__ == '__main__':
    s = [100, 95]
    print(Solution(s), "[02]:", Solution2(s))

    s = [100, 9, 100, 110, 52, 250]
    print(Solution(s), "[02]:", Solution2(s))
