"""
--------------------------------------------------------------------
单串： 单串问题：打家劫舍系列
--------------------------------------------------------------------
"""
from typing import List


class Solution4:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        count = n // 3

        visited = [False] * n

        def dfs(cnt: int) -> int:
            if cnt <= 0:
                return 0
            max_value = 0
            for i in range(n):
                if visited[i]:
                    continue
                cur = slices[i]
                visited[i] = True
                right = i + 1
                while visited[right % n]:
                    right += 1
                visited[right % n] = True
                left = i - 1
                while visited[left % n]:
                    left -= 1
                visited[left % n] = True
                other = dfs(cnt - 1)
                max_value = max(max_value, cur + other)
                visited[i] = False
                visited[left % n] = False
                visited[right % n] = False
            return max_value

        ans = dfs(count)
        return ans

    def maxSizeSlices2(self, slices: List[int]) -> int:
        def calculate(s):
            n = len(s)
            choose = (n + 1) // 3
            dp = [[0] * (choose + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, choose + 1):
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i - 2 >= 0 else 0) + s[i - 1])
            return dp[n][choose]

        ans1 = calculate(slices[1:])
        ans2 = calculate(slices[:-1])
        return max(ans1, ans2)



if __name__ == '__main__':
    sol = Solution4()
    nums = [4, 1, 2, 5, 8, 3, 1, 9, 7]
    nums = [1, 2, 3, 4, 5, 6]
    nums = [6, 3, 1, 2, 6, 2, 4, 3, 10, 4, 1, 4, 6, 5, 5, 3, 4, 7, 6, 5, 8, 7, 3, 8, 8, 1, 7, 1, 7, 8]
    sol.maxSizeSlices(nums)
