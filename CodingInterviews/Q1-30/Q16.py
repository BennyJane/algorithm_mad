# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【手机类型】
- 从库存量最大的类型开始 去库存操作
=================================================================================
"""


# FIXME 输入方式理解错误
def Solution(ori: list, k: int):
    d = {}
    for n in ori:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    type_num = len(d.keys())  # 手机种类
    type_count = [value for value in d.values()]
    type_count.sort(reverse=True)
    for _count in type_count:
        k -= _count
        if k >= 0:
            type_num -= 1
        else:
            break
    return type_num


def Solution2():
    # 读取输入内容
    import sys
    n = int(input())
    d = {}
    for _ in range(n):
        phone = sys.stdin.readline()
        if phone in d:
            d[phone] += 1
        else:
            d[phone] = 1
    k = int(input())
    print("n d k", n, d, k)
    # 获取每种类型手机的数量，并降序排列
    _count = sorted(list(d.values()), reverse=True)
    print("_count", _count)
    type_nums = len(_count)
    for c in _count:
        k -= c
        if k <= 0:
            type_nums -= 1
    return type_nums


if __name__ == '__main__':
    s = [5, 1, 1, 2, 2, 2]
    print(Solution(s, k=2))

    s = [5, 1, 1, 2, 2, 2, 4, 4, 5, 5, 1, 2, ]
    print(Solution(s, 7))

    print("[第二个方法]: ", Solution2())
