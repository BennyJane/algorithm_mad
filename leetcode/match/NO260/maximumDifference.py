from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        min_value = nums[0]
        right = 1
        while right < len(nums):
            if nums[right] <= min_value:
                # 必须在此处处理相等的情况
                min_value = nums[right]
            else:
                ans = max(ans, nums[right] - min_value)
            right += 1
        return ans
