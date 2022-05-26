from collections import defaultdict
from typing import List
from functools import lru_cache


# 103. 最少的硬币数目
class Solution:

    # 动态规划: 01背包
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [int(1e9)] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j, c in enumerate(coins):
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] < int(1e9) else -1

    def coinChange4(self, coins: List[int], amount: int) -> int:
        @lru_cache(amount)
        def dfs(retain) -> int:
            if retain < 0: return -1
            if retain == 0: return 0
            ans = int(1e9)
            for c in coins:
                cnt = dfs(retain - c)
                if cnt >= 0 and cnt < ans:
                    ans = cnt + 1
            return ans if ans < int(1e9) else -1

        if amount < 0: return 0
        return dfs(amount)

    # TODO 递归必须使用记忆化搜索
    def coinChange5(self, coins: List[int], amount: int) -> int:
        # FIXME 没有使用上记忆化搜素
        @lru_cache(None)
        def dfs(retain, count=0) -> int:
            if retain < 0: return -1
            if retain == 0: return count

            cnt = float("inf")
            for c in coins:
                tmp = dfs(retain - c, count + 1)
                if tmp > 0:
                    cnt = min(cnt, tmp)
            return cnt

        ans = dfs(amount, 0)
        return ans


# 剑指 Offer II 093. 最长斐波那契数列
class Solution1:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # unique 并没有删除任何元素，此处，只是为了提升判断速度
        unique = set(arr)

        dp = defaultdict(lambda: 2)

        for l in range(n):
            for r in range(l + 1, n):
                two, three = arr[l], arr[r]
                one = three - two
                # TODO 前一个值one必须存在原数组中；且 one 不能等于two
                # if one in unique and one != two:
                if one in unique and one < two:
                    # 确保三个值在同一个斐波那契数列中
                    dp[(two, three)] = dp[(one, two)] + 1
        # FIXME 必须考虑dp为空的情况
        ans = 0
        for _, v in dp.items():
            ans = max(ans, v)
        return ans if ans >= 3 else 0

    # 暴力方法
    def lenLongestFibSubseq2(self, A):
        uniqueEle = set(A)
        ans = 0

        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                x, y = A[i], A[j] + A[i]
                length = 2
                while y in uniqueEle:
                    x, y = y, y + x
                    length += 1
                ans = max(length, ans)
        return ans if ans >= 3 else 0


