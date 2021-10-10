import logging
from typing import List
from collections import defaultdict

logging.getLogger().setLevel(logging.DEBUG)

"""
--------------------------------------
长度为n的数组所有子序列
--------------------------------------
"""


def children(nums: List[int]) -> List[int]:
    n = len(nums)

    # 所有子序列
    ans = []
    # 对不同长度子序列的分组情况
    d = defaultdict(list)
    for i in range(1 << n):
        # 计算子序列长度
        cnt = bin(i).count("1")
        temp = []
        for j in range(n):
            if (1 << j) & i:
                temp.append(nums[j])
        ans.append(temp)
        d[cnt].append(temp)
    print(d)
    print(ans)
    return ans


children([1, 2, 3])

"""
--------------------------------------
两个有序数组，每个数组取一个值，求和为target的两个值
两个数组为升序
--------------------------------------
"""


def findTwoNum(nums1: List[int], nums2: List[int], target: int):
    left = 0
    right = len(nums2) - 1

    while left < len(nums1) and right >= 0:
        temp = nums1[left] + nums2[right]
        if temp == target:
            return [left, right]
        elif temp > target:
            right -= 1
        else:
            left += 1

    return [-1, -1]


res = findTwoNum([1, 2, 4, 3, ], [1, 4, 5, 3], 6)
logging.info(res)
