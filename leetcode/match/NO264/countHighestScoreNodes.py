from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    # 求每个节点在子节点个数，使用哈希表存储
    # 只需要找到左右子树的长度即可： left * right * (n - left - right - 1)

    ori_parents = None

    # FIXME 超时
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        self.ori_parents = parents
        ans = 0  # 必然可以取到
        d = defaultdict(list)

        res = {}

        # TODO 耗时操作
        def findChild(p: int):
            res = []
            if p in d:
                res = d[p]
            else:
                for index, v in enumerate(parents):
                    if v == p:
                        res.append(index)
                d[p] = res
            if len(res) == 0:
                return None, None
            elif len(res) == 1:
                return res[0], None
            else:
                return res[0], res[1]

        for i in range(0, n):
            left, right = findChild(i)
            l_c, r_c = 0, 0
            if left:
                l_c = self.dfs(left)
            if right:
                r_c = self.dfs(right)
            retain = max(1, n - l_c - r_c - 1)
            l_c = max(1, l_c)
            r_c = max(1, r_c)
            temp = l_c * r_c * retain
            if temp not in res:
                res[temp] = 1
            else:
                res[temp] += 1
            ans = max(ans, temp)

        return res[ans]

    @lru_cache(None)
    def dfs(self, p: int):
        """计算的是每个节点到叶子节点的节点数量"""
        count = 1
        # FIXME 耗时操作
        for index, v in enumerate(self.ori_parents):
            if v == p:
                count += self.dfs(index)
        return count

    """
    -----------------------------------------------------------------
    递归函数设计
    -----------------------------------------------------------------
    """

    def countHighestScoreNodes2(self, parents: List[int]) -> int:
        n = len(parents)
        # 计算每个节点在子节点，最多两个
        # FIXME 预先处理，找到子节点
        son = [[] for _ in range(n)]
        for i in range(1, n):
            p = parents[i]
            son[p].append(i)

        d = dict()  # 记录每个根节点下在节点数量

        @lru_cache(None)
        def calNodeCount(p: int):
            """计算每个子树的节点个数"""
            if not son[p]:  # 没有子节点
                d[p] = 1
                return 1
            c = 1
            for child_index in son[p]:
                c += calNodeCount(child_index)
            d[p] = c
            return c

        calNodeCount(0)

        # TODO 注意题目要求，统计的是最大值出现的次数
        ans = 0
        max_value = 0
        for i in range(n):
            cnt = 1
            for child in son[i]:
                cnt = cnt * d[child]
            if i != 0:
                cnt = cnt * (d[0] - d[i])
            if cnt == max_value:
                ans += 1
            elif cnt > max_value:
                max_value = cnt
                ans = 1

        return ans


class Solution1:
    # 求每个节点在子节点个数，使用哈希表存储
    # 只需要找到左右子树的长度即可： left * right * (n - left - right - 1)

    # FIXME 超时
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)

        son = [[] for _ in range(n)]
        for i in range(1, n):
            p = parents[i]
            son[p].append(i)

        d = dict()

        def dfs(p: int):
            if p in d:
                return d[p]
            m = 1
            for index in son[p]:
                m += dfs(index)
            d[p] = m
            return m

        dfs(0)

        ans = 0
        max_value = 0

        for i in range(0, n):
            cnt = 1
            child_count = 0
            for c in son[i]:
                count = d[c]
                cnt *= count
                child_count += count
            retain = max(1, n - child_count - 1)
            temp = cnt * retain
            if temp == max_value:
                ans += 1
            elif temp > max_value:
                max_value = temp
                ans = 1

        return ans


if __name__ == '__main__':
    sol = Solution1()
    # nums = [-1, 2, 0, 2, 0]
    nums = [-1, 2, 0]
    # nums = [-1, 2, 0, 2, 0]
    # nums = [-1, 0]
    sol.countHighestScoreNodes(nums)
