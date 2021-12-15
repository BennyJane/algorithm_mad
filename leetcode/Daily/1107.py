from typing import List
from collections import Counter, defaultdict


# 598. 范围求和 II
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n

        min_width = float("inf")
        min_height = float("inf")

        for w, h in ops:
            min_width = min(w, min_width)
            min_height = min(h, min_height)

        return min_width * min_height

    def maxCount2(self, m: int, n: int, ops: List[List[int]]) -> int:
        mina, minb = m, n
        for a, b in ops:
            mina = min(mina, a)
            minb = min(minb, b)
        return mina * minb


# 370. 区间加法
class Solution1:
    # 差分法 > 模拟法
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        ans = [0] * (length + 1)
        # TODO 注意索引范围： end 对应索引也是包含在inc范围后，应该从后一个索引开始-inc
        for start, end, inc in updates:
            ans[start] += inc
            ans[end + 1] -= inc

        total = 0
        for i, v in enumerate(ans):
            total += v
            ans[i] = total
        return ans[:-1]


# 520. 检测大写字母
class Solution2:
    def detectCapitalUse(self, word: str) -> bool:
        ori = word
        choices = [word.lower(), word.upper(), word[0].upper() + word[1:].lower()]

        return ori in choices

    def detectCapitalUse1(self, word: str) -> bool:
        # 若第 1 个字母为小写，则需额外判断第 2 个字母是否为小写
        if len(word) >= 2 and word[0].islower() and word[1].isupper():
            return False

        # 无论第 1 个字母是否大写，其他字母必须与第 2 个字母的大小写相同
        return all(word[i].islower() == word[1].islower() for i in range(2, len(word)))


# 677. 键值映射
# 可以使用字典树
# https://leetcode-cn.com/problems/map-sum-pairs/
class MapSum:

    def __init__(self):
        self.cache = dict()

    def insert(self, key: str, val: int) -> None:
        self.cache[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        for key, val in self.cache.items():
            if str(key).startswith(prefix):
                ans += val
        return ans


import math


# 319. 灯泡开关
class Solution3:
    def bulbSwitch(self, n: int) -> int:
        if n <= 1:
            return n
        ans = 1

        def count(num):
            res = 1
            limit = int(math.sqrt(num)) + 1
            for j in range(2, limit):
                if num % j == 0:
                    if j * j == num:
                        res += 1
                    else:
                        res += 2
            return res

        for i in range(2, n):
            if count(i) % 2 == 0:
                ans += 1
        return ans

    def bulbSwitch2(self, n: int) -> int:
        return int(math.sqrt(n + 0.5))


# 594. 最长和谐子序列
class Solution4:
    def findLHS(self, nums: List[int]) -> int:
        d = dict()
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        countList = sorted(d.items(), key=lambda x: x)
        length = len(countList)
        ans = 0
        for i in range(1, length):
            if countList[i][0] - countList[i - 1][0] == 1:
                l = countList[i][1] + countList[i - 1][1]
                ans = max(ans, l)

        return ans

    def findLHS1(self, nums: List[int]) -> int:
        count = Counter(nums)

        sortedNums = sorted(count.items())
        n = len(sortedNums)
        dp = [0] * n
        for i in range(1, n):
            x, c1 = sortedNums[i]
            y, c2 = sortedNums[i - 1]
            if x - y == 1:
                dp[i] = c1 + c2
        return max(dp)

    def findLHS2(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        return max((val + cnt[key + 1] for key, val in cnt.items() if key + 1 in cnt), default=0)

    # 滑动窗口
    def findLHS3(self, nums: List[int]) -> int:
        nums.sort()
        begin = 0
        ans = 0
        for end in range(len(nums)):
            # TODO 维护窗口：保证左右端点差值 <= 1
            while nums[end] - nums[begin] > 1:
                begin += 1

            if nums[end] - nums[begin] == 1:
                ans = max(ans, end - begin + 1)
        return 0


# 851. 喧闹和富有
class Solution5:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        edges = [[] for _ in range(N)]
        for k, v in richer:
            edges[v].append(k)
        memorize = [None] * N

        def dfs(node):
            if memorize[node] is None:
                memorize[node] = node
                for i in edges[node]:
                    cand = dfs(i)
                    if quiet[cand] < quiet[memorize[node]]:
                        memorize[node] = cand
            return memorize[node]

        return map(dfs, range(N))
