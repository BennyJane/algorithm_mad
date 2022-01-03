from collections import defaultdict, deque
from typing import List


class Solution1:
    def checkString(self, s: str) -> bool:
        ACnt = 0
        BCnt = 0
        for i, c in enumerate(s):
            if c == 'a':
                if BCnt > 0:
                    return False
                ACnt += 1
            else:
                BCnt += 1

        return True


class Solution2:
    def numberOfBeams(self, bank: List[str]) -> int:
        stack = []

        ans = 0
        for i, s in enumerate(bank):
            cnt = 0
            for c in s:
                if c == '1':
                    cnt += 1
            if stack:
                ans += stack[-1] * ans
            if cnt > 0:
                stack.append(cnt)

        return ans


class Solution3:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for c in asteroids:
            if mass >= c:
                mass += c
            else:
                return False

        return True


# 图： 求最长环
class Solution4:
    """
    题目分析：
    每个节点(员工)只能有一个出度，但可以有多个入度，即只有一个父节点，可以有多个子节点
    如果存在环，需要分两种情况讨论：
        - 长度等于2，需要考虑以两个节点为结尾的 单链表长度的最大值之和
        - 长度大于3，只有环中的节点满足条件
    """

    def maximumInvitations(self, g: List[int]) -> int:
        n = len(g)
        # 记录每个节点的直系子节点
        rg = [[] for _ in range(n)]  # g 的反图
        deg = [0] * n  # g 上每个节点的入度
        for v, w in enumerate(g):
            rg[w].append(v)
            deg[w] += 1

        # 拓扑排序，剪掉 g 上的所有树枝
        # 初始值：选择所有叶子节点，即入度为0
        q = deque(i for i, d in enumerate(deg) if d == 0)
        # 删除所有非环内的节点，即最终，只有环中的节点的入度不为0
        while q:
            v = q.popleft()
            w = g[v]  # v 只有一条出边
            deg[w] -= 1
            if deg[w] == 0:
                q.append(w)

        # 通过反图 rg 寻找树枝上最深的链
        def rdfs(v: int) -> int:
            max_depth = 1
            for w in rg[v]:
                # FIXME 只考虑树枝上的节点，避免重复访问环中的节点
                if deg[w] == 0:  # 树枝上的点在拓扑排序后，入度均为 0
                    max_depth = max(max_depth, rdfs(w) + 1)
            return max_depth

        max_ring_size, sum_chain_size = 0, 0
        for i, d in enumerate(deg):
            if d <= 0:
                continue
            # 遍历基环上的点（拓扑排序后入度大于 0）
            deg[i] = -1
            ring_size = 1
            v = g[i]
            while v != i:
                deg[v] = -1  # 将基环上的点的入度标记为 -1，避免重复访问
                ring_size += 1
                v = g[v]
            if ring_size == 2:  # 基环大小为 2
                sum_chain_size += rdfs(i) + rdfs(g[i])  # 累加两条最长链的长度
            else:
                max_ring_size = max(max_ring_size, ring_size)  # 取所有基环的最大值
        return max(max_ring_size, sum_chain_size)

    def maximumInvitations3(self, g: List[int]) -> int:
        n = len(g)
        # 统计每个节点的入度, 即统计子节点数量
        deg = [0] * n
        for b in g:
            deg[b] += 1

        # 记录每个节点到叶子节点的深度
        maxDepth = [0] * n
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:  # 拓扑排序，减掉g上的所有树枝
            v = q.popleft()
            parent = g[v]

            # 计算当前节点的深度
            maxDepth[v] += 1
            # 父节点，存在多个子节点，即多个入度来源，所以取最大值
            # 计算环上节点的树枝长度，不包含 环上节点的长度
            maxDepth[parent] = max(maxDepth[parent], maxDepth[v])

            # 更新节点的入度
            deg[parent] -= 1
            if deg[parent] == 0:  # 下一层叶子节点
                q.append(parent)

        max_ring_size = sum_chain_size = 0
        for i, d in enumerate(deg):
            if d == 0:
                continue
            # 遍历所有环上的点，即拓扑排序后入度大于0的节点
            deg[i] = 0
            step = 1
            # 遍历整个环，并将环上节点的入度更新为0，避免重复访问
            parent = g[i]
            while parent != i:
                # FIXME 避免重复访问的关键
                deg[parent] = 0
                step += 1
                parent = g[parent]
            if step == 2:
                # FIXME maxDepth[g[i]] 不能使用maxDepth[parent], 此时 parent 等于 i，错误
                # 所有长度2的环，可以连接起来，依然满足题目条件
                sum_chain_size += (maxDepth[i] + maxDepth[g[i]] + 2)
            else:
                max_ring_size = max(max_ring_size, step)
        return max(sum_chain_size, max_ring_size)

    def maximumInvitations2(self, favorite: List[int]) -> int:
        n = len(favorite)

        d = defaultdict(list)
        for i, c in enumerate(favorite):
            d[c].append(i)

        visited = [False] * n
        ans = 1
        for i in range(n):
            if visited[i]:
                continue
            start = i
            visited[i] = True
            nxt = favorite[i]
            temp = set()
            lastIndex = i
            temp.add(i)
            step = 1

            # 是否首尾相接
            isEnd = False
            while nxt not in temp and (
                    favorite[nxt] not in temp or lastIndex == favorite[nxt] or favorite[nxt] == start):
                if favorite[nxt] == start:
                    isEnd = True
                visited[nxt] = True
                temp.add(nxt)
                lastIndex = nxt

                nxt = favorite[nxt]
                step += 1
            if not isEnd:
                pass
            ans = max(ans, step)

        return ans


class Solution41:
    def maximumInvitations(self, g: List[int]) -> int:  # favorite 就是内向基环森林 g
        n = len(g)
        deg = [0] * n  # g 上每个节点的入度
        for w in g:
            deg[w] += 1

        max_depth = [0] * n
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:  # 拓扑排序，剪掉 g 上的所有树枝
            v = q.popleft()
            max_depth[v] += 1
            w = g[v]  # v 只有一条出边
            max_depth[w] = max(max_depth[w], max_depth[v])
            deg[w] -= 1
            if deg[w] == 0:
                q.append(w)

        max_ring_size, sum_chain_size = 0, 0
        for i, d in enumerate(deg):
            if d == 0:
                continue
            # 遍历基环上的点（拓扑排序后入度大于 0）
            deg[i] = 0
            ring_size = 1
            v = g[i]
            while v != i:
                deg[v] = 0  # 将基环上的点的入度标记为 0，避免重复访问
                ring_size += 1
                v = g[v]
            if ring_size == 2:  # 基环大小为 2
                sum_chain_size += max_depth[i] + max_depth[g[i]] + 2  # 累加两条最长链的长度
            else:
                max_ring_size = max(max_ring_size, ring_size)  # 取所有基环的最大值
        return max(max_ring_size, sum_chain_size)


class Solution42:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        # 统计入度，便于进行拓扑排序
        indeg = [0] * n
        for i in range(n):
            indeg[favorite[i]] += 1

        used = [False] * n
        f = [1] * n
        q = deque(i for i in range(n) if indeg[i] == 0)

        while q:
            u = q.popleft()
            used[u] = True
            v = favorite[u]
            # 状态转移
            f[v] = max(f[v], f[u] + 1)
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

        # ring 表示最大的环的大小
        # total 表示所有环大小为 2 的「基环内向树」上的最长的「双向游走」路径之和
        ring = total = 0
        for i in range(n):
            if not used[i]:
                j = favorite[i]
                # favorite[favorite[i]] = i 说明环的大小为 2
                if favorite[j] == i:
                    total += f[i] + f[j]
                    used[i] = used[j] = True
                # 否则环的大小至少为 3，我们需要找出环
                else:
                    u = i
                    cnt = 0
                    while True:
                        cnt += 1
                        u = favorite[u]
                        used[u] = True
                        if u == i:
                            break
                    ring = max(ring, cnt)

        return max(ring, total)



if __name__ == '__main__':
    sol = Solution4()
    # arr = [2, 2, 1, 2]
    # arr = [1, 2, 0]
    arr = [3, 0, 1, 4, 1]
    arr = [1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8]
    sol.maximumInvitations(arr)
