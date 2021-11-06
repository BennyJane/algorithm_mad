from functools import lru_cache
from math import inf
from typing import List


# 1937. 扣分后的最大得分
# https://leetcode-cn.com/problems/maximum-number-of-points-with-cost/
class Solution:
    """
    某个位置(不是第一行)上取值：
    pos_max = 当前行某点(i)得分 + 上一行(row - 1)某列(j)出得分  - 两个点坐标差的绝对值abs(i - j)
    绝对值分情况讨论：
    点j位于i左侧，则 pos_max = goal_i + pre_goal_j + j - i = (goal_i - i)每个位置为确定值  + pre_goal_j + j
    点j位于i右侧，则 pos_max = goal_i + pre_goal_j - j + i = goal_i + i + pre_goal - j
    """

    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])

        dp = [0] * n  # 记录上一行数据
        for i in range(m):
            # 临时存储当前行数据
            temp = [0] * n

            left_max = float("-inf")
            # 计算每个位置的最大值： 上一行得分 + 索引j
            for j in range(n):
                left_max = max(left_max, dp[j] + j)
                # 先统计每个位置，可能的最大值
                temp[j] = max(temp[j], left_max + points[i][j] - j)

            right_max = float("-inf")
            for j in range(n):
                right_max = max(right_max, dp[j] - j)
                temp[j] = max(temp[j], right_max + points[i][j] + j)
            dp = temp
        return max(dp)

    def maxPoints3(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = points[0]
        for i in range(1, m):
            new_dp = list(dp)
            left_max = -inf
            right_max = -inf
            for j in range(n):
                left_max = max(left_max, dp[j] + j)
                right_max = max(right_max, dp[n - 1 - j] - (n - 1 - j))
                new_dp[j] = max(left_max - j + points[i][j], new_dp[j])
                new_dp[n - 1 - j] = max((n - 1 - j) + right_max + points[i][n - 1 - j], new_dp[n - 1 - j])
            dp = new_dp
        return max(dp)

    # 暴力迭代法
    def maxPoints1(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[0][i] = points[0][i]

        for r in range(1, m):
            for c1 in range(n):  # 当前列
                point1 = points[r][c1]
                goal = 0
                # 每个节点：都需要考虑上一行的所有位置  ==》 n * n 次遍历
                for c2 in range(n):  # 上一层节点选择
                    temp = point1 + dp[r - 1][c2] - abs(c1 - c2)
                    goal = max(goal, temp)
                dp[r][c1] = goal
                # fixme 不能在这儿通过i == m-1, 记录最大值，当m=1时，不会进入该循环
        ans = 0  # 在最后一行的寻找最大值
        for i in range(n):
            ans = max(ans, dp[m - 1][i])
        return ans

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


if __name__ == '__main__':
    sol = Solution()
    nums = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    sol.maxPoints(nums)
