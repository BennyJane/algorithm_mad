# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【猜数字】【重要】
"""


def Solution(guess_list):
    # 统计所有4位数是否满足条件：1 满足 0 不满足
    nums = [1] * 9999
    one_cnt = 9999

    def getHit(one, other) -> str:
        x = y = 0

        ten1 = [0] * 10
        ten2 = [0] * 10

        for a, b in zip(one, other):
            if a == b:
                x += 1
            else:
                ten1[int(a)] += 1
                ten2[int(b)] += 1
        for i in range(10):
            y += min(ten1[i], ten2[i])
        return f"{x}A{y}B"

    for info in guess_list:
        guess, template = info.split(" ")

        # 筛选和guess可以生成相同xAyB模式的 4位数字
        for index, val in enumerate(nums):
            if val == 0:
                continue
            num_str = str(index)
            width = len(str(num_str))
            num_str = "0" * (4 - width) + num_str
            x_a_y_b = getHit(num_str, guess)
            # 优先排除不匹配的数字
            if x_a_y_b != template:
                nums[index] = 0
                one_cnt -= 1
    print(nums.index(1))
    return one_cnt <= 1


if __name__ == '__main__':
    s1 = [
        "4815 1A1B",
        "5716 0A1B",
        "7842 0A1B",
        "4901 0A0B",
        "8585 3A0B",
        "8555 2A1B",
    ]
    print(Solution(s1))
