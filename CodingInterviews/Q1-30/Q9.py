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

#
def Solution(self, nums: list) -> int:
    _max = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i] + nums[i - 1])
        _max = max(_max, nums[i])
    return _max


if __name__ == '__main__':
    s1 = "2,5,6,7,9,5,7"
    s2 = "1,7,4,3,4"
    ori_list = [s1.split(","), s2.split(",")]
    r = Solution(ori_list, num=3)
    print(r)
