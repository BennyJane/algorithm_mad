from typing import List
from functools import lru_cache


# 300. 最长递增子序列
class Solution1:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        # 子问题：寻找每个索引位置的最长子序列
        def dfs(index: int) -> int:
            ans = 1
            for i in range(index):
                if nums[i] < nums[index]:
                    ans = max(ans, dfs(i) + 1)
            print(ans)
            return ans

        n = len(nums)
        res = 1
        for i in range(n):
            res = max(res, dfs(i))

        return res

    def lengthOfLIS2(self, nums: List[int]) -> int:
        # 子问题：寻找每个索引位置的最长子序列
        @lru_cache(None)
        def dfs(index: int) -> int:
            ans = 1
            for i in range(index):
                if nums[i] < nums[index]:
                    ans = max(ans, dfs(i) + 1)
            return ans

        n = len(nums)
        res = 1
        for i in range(n):
            res = max(res, dfs(i))

        return res

    # FIXME 该方式没有lru_cache 速度快
    def lengthOfLIS3(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n

        # 子问题：寻找每个索引位置的最长子序列
        def dfs(index: int) -> int:
            if cache[index] != -1:
                return cache[index]

            ans = 1
            for i in range(index):
                if nums[i] < nums[index]:
                    ans = max(ans, dfs(i) + 1)
            cache[index] = ans
            return ans

        res = 1
        for i in range(n):
            res = max(res, dfs(i))

        return res

    def lengthOfLIS4(self, nums: List[int]) -> int:
        n = len(nums)
        # TODO 初始值全部设为1 ==》 每个索引位置处，最小递增子序列长度为1 即处理所有值相同的情况
        # FIXME 只设置dp[0] = 1 计算错误
        dp = [1] * n

        for i, val in enumerate(nums):
            for j in range(i, -1, -1):
                # TODO 纠错：寻找i左侧，最长子序列且确保 nums[j] < nums[i]
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


# 最长递增子序列的个数
class Solution2:
    # FIXME 错误：1. 没有考虑长度为1的情况 2. 计算数量时，没有考虑同一个长度可能存在多种满足条件的选择
    # TODO 错误
    def findNumberOfLIS_error(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        count = 0
        max_length = 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = dp[j] + 1
                    # FIXME 错误！！！！
                    if temp == max_length:
                        count += 1
                    if temp > max_length:
                        count = 1
                        max_length = temp
                    dp[i] = max(temp, dp[i])
        return n if max_length == 1 else count

    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # TODO 初始值为1 ==》 初始化所有子序列长度为1的特殊情况
        # FIXME 初始值设置0，计算错误
        dp = [1] * n  # 记录索引i处，以nums[i]为结尾的递增子序列的最大长度
        count = [1] * n  # 记录索引i处，最大长度子序列的数量

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    temp = dp[j] + 1
                    # 先判断相等情况，再判断大于情况（扩展最大值）
                    if temp == dp[i]:  # 最大长度相同，则修改出现的数量
                        count[i] += count[j]
                    if temp > dp[i]:  # 最大长度扩大，则重置出现的次数
                        dp[i] = temp
                        count[i] = count[j]

        max_length = max(dp)
        total = 0
        for i, c in enumerate(count):
            if dp[i] == max_length:
                total += c
        return total

    def findNumberOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i]：使用(length, count) 记录索引i处，最长递增子序列的长度，以及出现的次数
        # 默认值：表示不存在前驱子序列，和当前值构成递增子序列
        dp = [[0, 0] for _ in range(n)]
        # dp = [[1, 1] for _ in range(n)]

        max_length = 1
        for right in range(n):
            dp[right] = [1, 1]  # 在考虑前驱子序列前，进行初始化
            for left in range(right):
                if nums[left] < nums[right]:
                    length = dp[left][0] + 1
                    if length == dp[right][0]:
                        dp[right][1] += dp[left][1]
                        # dp[right][1] += 1
                    if length > dp[right][0]:
                        dp[right][0] = length
                        dp[right][1] = dp[left][1]
                        # FIXME 错误： 当前长度数量 == 前驱子序列长度对应的数量
                        # dp[right][1] = 1
                    max_length = max(max_length, length)
        return sum(c[1] for i, c in enumerate[dp] if c[0] == max_length)


# 俄罗斯套娃信封问题
class Solution3:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)

        f = [1] * n
        envelopes.sort()
        for right in range(n):
            temp_max = 1
            for left in range(right):
                if envelopes[left][1] < envelopes[right][1] and envelopes[left][0] < envelopes[right][0]:
                    temp_max = max(temp_max, f[left] + 1)
            f[right] = temp_max

        return max(f)


if __name__ == '__main__':
    sol = Solution1()
    nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    # sol.lengthOfLIS(nums)
    sol2 = Solution2()
    nums = [1, 2, 4, 3, 5, 4, 7, 2]
    nums = [2, 2, 2, 2, 2]
    sol2.findNumberOfLIS(nums)
