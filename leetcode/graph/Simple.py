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


# 1971. 寻找图中是否存在路径
class Solution2:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        p = [i for i in range(n)]

        def get_root(node):
            if p[node] == node:
                return p[node]
            p[node] = get_root(p[node])
            return p[node]

        def merge(a, b):
            root_a, root_b = get_root(a), get_root(b)
            if root_a != root_b:
                p[root_a] = root_b

        for a, b in edges:
            merge(a, b)
        return get_root(start) == get_root(end)

    def validPath2(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True
        d = defaultdict(list)
        for s, e in edges:
            d[s].append(e)
            d[e].append(s)

        q = list(d[start])
        visited = [False] * n
        while q:
            size = len(q)
            temp = list()
            for i in range(size):
                cur = q[i]
                visited[cur] = True
                if cur == end:
                    return True
                for nxt in d[cur]:
                    if not visited[nxt]:
                        temp.append(nxt)
            q = temp
        return False


# 1791. 找出星型图的中心节点
class Solution3:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = defaultdict(int)
        n = len(edges) + 1
        for s, e in edges:
            d[s] += 1
            d[e] += 1
            if d[s] == n - 1:
                return s
            if d[e] == n - 1:
                return e

        return 0
