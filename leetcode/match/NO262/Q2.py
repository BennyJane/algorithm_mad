from typing import List

from leetcode.match.NO262 import arr, x


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        n = len(grid)
        m = len(grid[0])
        l = []
        start = grid[0][0]
        for i in range(n):
            for j in range(m):
                cur = grid[i][j]
                if (cur - start) % x != 0:
                    return -1
                l.append(cur)
        arr = sorted(l)
        total = sum(arr)
        ans = 100000000000000000
        pre = 0
        _len = len(arr)
        for i in range(len(arr)):
            c = arr[i]
            count = abs((c * i - pre) / x) + abs((c * (_len - i) - total + pre) / x)
            ans = min(count, ans)
            pre += c

        return int(ans)


if __name__ == '__main__':
    sol = Solution()
    sol.minOperations(arr, x)
