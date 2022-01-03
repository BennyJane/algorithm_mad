from collections import deque
from collections import defaultdict
from typing import List


class Solution1:
    # LCP 07. 传递信息
    """
    广度优先遍历：从n-1，逐层往下遍历
    """

    # 深度优先遍历
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        d = defaultdict(list)
        for s, e in relation:
            d[e].append(s)
        ans = 0

        def dfs(p, res):
            nonlocal ans
            # 终止条件：恰好传递K轮，且到达0
            if res == 0:
                if p == 0:
                    ans += 1
                return
            for s in d[p]:
                dfs(s, res - 1)

        for s in d[n - 1]:
            dfs(s, k - 1)

        return ans

    def numWays2(self, n: int, relation: List[List[int]], k: int) -> int:
        d = defaultdict(list)
        for s, e in relation:
            d[e].append(s)
        ans = 0

        def dfs(arr, index, res):
            nonlocal ans
            # 终止条件：恰好传递K轮，且到达0
            if res == 0:
                if index == 0:
                    ans += 1
                return
            for i in arr:
                dfs(d[i], i, res - 1)

        dfs(d[n - 1], n - 1, k)
        return ans
