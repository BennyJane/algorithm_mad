# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier

"""
=================================================================================
【最大矩阵和】 动态规划
最大子序和
https://leetcode-cn.com/problems/max-submatrix-lcci/solution/er-wei-zhuan-yi-wei-by-yyy-108/

=================================================================================
"""


# 处理一维数组： 最大子序列和
def Solution(nums: list) -> int:
    _max = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
        _max = max(_max, nums[i])
    print(nums)
    return _max


def Solution2(l):
    import copy
    res = copy.deepcopy(l)
    for i in range(1, len(l)):
        if res[i - 1] < 0:
            res[i] = l[i]
        else:
            res[i] = l[i] + res[i - 1]
    print(res)
    return max(res)


def Solution3(l):
    for i in range(1, len(l)):
        # TODO 只需要处理前缀和大于等于0的数据
        if l[i - 1] >= 0:
            l[i] = l[i] + l[i - 1]
    print(l)
    return max(l)


def Solution4(l):
    _max = l[0]
    for i in range(1, len(l)):
        if l[i - 1] < 0:
            before_sum = l[i]
        else:
            before_sum = l[i] + l[i - 1]
        if before_sum > _max:
            _max = before_sum
    return _max


if __name__ == '__main__':
    t = [1, 2, 3, 24, 65, 142, -12, -2563, 125]
    print(Solution(t))

    t = [1, 2, 3, 24, 65, 142, -12, -2563, 125]
    print(Solution2(t))

    t = [1, 2, 3, 24, 65, 142, -12, -2563, 125]
    print(Solution3(t))

    t = [1, 2, 3, 24, 65, 142, -12, -2563, 125]
    print(Solution3(t))
