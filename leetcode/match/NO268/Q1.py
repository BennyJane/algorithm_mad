from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        n = len(colors)
        for i in range(1, n):
            for j in range(i):
                if colors[i] != colors[j]:
                    ans = max(ans, i - j)

        return ans
