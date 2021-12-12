from typing import List
from functools import lru_cache
from heapq import heappop
from heapq import heappush
from sortedcontainers import SortedList


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = [i for i in range(n)]
        arr.sort(key=lambda x: -1 * nums[x])

        res = []
        target = arr[:k]
        target.sort()
        for index in target:
            res.append(nums[index])

        return res


class Solution2:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time == 0:
            return [i for i in range(n)]
        left = [0] * n

        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1

        right = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1
        res = []
        for i in range(1, n):
            if left[i - 1] >= time and right[i + 1] >= time:
                res.append(i)
        return res


class Solution3:
    # 长度优先，记忆化搜索
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        if n == 0:
            return 0
        visited = [False] * n

        # @lru_cache(None)
        def dfs(index, seen):
            cnt = 0
            x1, y1, r1 = bombs[index]
            nxtArr = list()
            for j in range(n):
                if seen[j]:
                    continue
                x2, y2, r2 = bombs[j]
                if pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2) <= pow(r1, 2):
                    nxtArr.append(j)
                    seen[j] = True
            cnt += len(nxtArr)

            for nxt in nxtArr:
                cnt += dfs(nxt, seen)
            for nxt in nxtArr:
                seen[nxt] = False
            return cnt

        ans = 0
        for i in range(n):
            visited[i] = True
            ans = max(ans, 1 + dfs(i, visited))
            visited[i] = False

        return ans

    def maximumDetonation2(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        if n == 0:
            return 0
        visited = [False] * n

        @lru_cache(None)
        def dfs(index, seen):
            cnt = 0
            x1, y1, r1 = bombs[index]
            nxtArr = list()
            for j in range(n):
                if seen[j]:
                    continue
                x2, y2, r2 = bombs[j]
                if pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2) <= pow(r1, 2):
                    nxtArr.append(j)
                    seen[j] = True
            cnt += len(nxtArr)

            for nxt in nxtArr:
                cnt += dfs(nxt, seen)
            return cnt

        ans = 0
        for i in range(n):
            visited[i] = True
            ans = max(ans, 1 + dfs(i, list(visited)))
            visited[i] = False

        return ans


"""
[[855,82,158],[17,719,430],[90,756,164],[376,17,340],[691,636,152],[565,776,5],[464,154,271],[53,361,162],[278,609,82],[202,927,219],[542,865,377],[330,402,270],[720,199,10],[986,697,443],[471,296,69],[393,81,404],[127,405,177]]
6 - 9


[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]
[null,null,null,"branford",null,"alps",null,"bradford",null,"bradford",null,"bradford","orland"]

"""


class SORTracker:

    def __init__(self):
        self.queryCnt = 0
        self.cache = SortedList(key=lambda x: (-1 * x[0], x[1]))

    def add(self, name: str, score: int) -> None:
        self.cache.add((score, name))

    def get(self) -> str:
        self.queryCnt += 1
        return self.cache[self.queryCnt][0]
