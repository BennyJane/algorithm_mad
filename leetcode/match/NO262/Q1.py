from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d = set(nums1)
        ans = set()

        for n in set(nums2):
            if n in d:
                ans.add(n)
            else:
                d.add(n)
        for n in set(nums3):
            if n in d:
                ans.add(n)

        return list(ans)
