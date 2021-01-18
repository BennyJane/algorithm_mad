# !/usr/bin/env python
# -*-coding:utf-8 -*-
# Warning    ：The Hard Way Is Easier
"""
=================================================================================
【第k个排列】
https://leetcode-cn.com/problems/permutation-sequence/solution/jian-dan-si-lu-zhao-dao-wei-shu-gui-lu-onjie-fa-by/

暴力枚举法
https://my.oschina.net/u/4328928/blog/3315408
=================================================================================
"""


def Solution(n: int, k: int):
    from math import factorial
    # nums 修改为降序，可以取得相反效果
    nums = [i for i in range(1, n + 1)]  # 升序，决定了转成字符串后的排列顺序
    ans = []
    """
    假设n=4, k=6:
    3!=6 , k / 6 = 1 余数为0，但实际上，第一个ids应该对应nums中索引0对应的值
    """
    k -= 1  # nums列表从0开始编号，k减一，实现将商转化为正确的列表索引
    while len(nums) > 1:
        ids = k // factorial(len(nums) - 1)  # 开头的数字
        ans.append(nums[ids])
        # 等效： k -= ids * factorial(len(nums) - 1)
        k = k % factorial(len(nums) - 1)
        nums.pop(ids)
    ans += list(nums)  # 将剩余数字放到末尾
    return ''.join(list(map(str, ans)))


def Solution2(n, k):
    from math import factorial
    nums = [i for i in range(1, n + 1)]
    ans = []

    k -= 1
    while len(nums) > 0:
        index = k // factorial(len(nums) - 1)
        ans.append(nums[index])
        k = k % factorial(len(nums) - 1)
        nums.pop(index)
    print(nums, "ans", ans)
    return ''.join(list(map(str, ans)))


if __name__ == '__main__':
    s, k = 4, 10
    print(Solution(s, k))

    s, k = 3, 1
    print(Solution(s, k))

    s, k = 3, 5
    print(Solution(s, k))

    s, k = 3, 5
    print(Solution2(s, k))

    s, k = 3, 2
    print(Solution2(s, k))
