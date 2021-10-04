from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        up_sum = sum(grid[0])
        down_sum = 0

        ans = 1000000000
        for i in range(n):
            up_sum -= grid[0][i]
            if i > 0:
                down_sum += grid[1][i - 1]
            temp = max(up_sum, down_sum)
            ans = min(ans, temp)
        return ans
