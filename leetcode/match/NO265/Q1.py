
from typing import List


# 5914. 值相等的最小索引
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        n = len(nums)
        for i, val in enumerate(nums):
            if i % 10 == val:
                return i
        return -1

