from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        _len = len(rides)
        take_dp = [0] * (n + 1)
        # 按照end位置升序排列
        rides = sorted(rides, key=lambda x: x[1])
        index = 0
        for i in range(1, n + 1):
            # 出租车不载人的收益
            take_dp[i] = take_dp[i - 1]
            while index < _len and rides[index][1] <= i:
                start, end, tip = rides[index]
                take_dp[i] = max(take_dp[i], take_dp[start] + end + tip - start)
                index += 1
        return take_dp[n]

    def maxTaxiEarnings2(self, n: int, rides: List[List[int]]) -> int:
        _len = len(rides)
        take_dp = [0] * (n + 1)
        rides = sorted(rides, key=lambda x: x[1])
        ans = 0
        for i in range(1, _len + 1):
            start, end, tip = rides[i - 1]
            money_base = end - start + tip
            # 找出start之前的利润最大值
            # TODO 超时了
            pre_take = take_dp[:start + 1]
            money_pre_max = max(pre_take)

            take_dp[end] = max(take_dp[end], money_base + money_pre_max)
            ans = max(ans, take_dp[end])
        return ans


if __name__ == '__main__':
    sol = Solution()
    n = 10
    nums = [[9, 10, 2], [4, 5, 6], [6, 8, 1], [1, 5, 5], [4, 9, 5], [1, 6, 5], [4, 8, 3], [4, 7, 10], [1, 9, 8],
            [2, 3, 5]]
    sol.maxTaxiEarnings(n, nums)
