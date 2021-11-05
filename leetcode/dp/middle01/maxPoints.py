from functools import lru_cache
from typing import List


# 1937. 扣分后的最大得分
# https://leetcode-cn.com/problems/maximum-number-of-points-with-cost/
class Solution:
    #
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            dp[0][i] = points[0][i]

        for r in range(1, m):
            for c1 in range(n):  # 当前列
                point1 = points[r][c1]
                goal = 0
                for c2 in range(n):  # 上一层节点选择
                    point2 = points[r][c2]
                    temp = point1 + point2 - abs(c1 - c2)
                    goal = max(goal, temp)
                dp[r][c1] = goal

        return 0

    # 递归 + 记忆化搜索
    # 超时
    def maxPoints2(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        max_value = 0

        @lru_cache(None)
        def dfs(pos_info) -> int:
            val = 0  # 最大值
            row, y = pos_info
            if row >= m:
                return 0
            for Y in range(n):
                cur = points[row][Y]
                next_info = row + 1, Y
                back_sum = dfs(next_info) + cur - abs(y - Y)
                val = max(val, back_sum)
            return val

        for i in range(n):
            info = (1, i)
            max_value = max(max_value, dfs(info) + points[0][i])

        return max_value
