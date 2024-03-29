import collections
from collections import defaultdict, deque
from typing import List


# 444. 序列重建
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        inDeg = defaultdict(int)  # 统计每个节点的入度
        graph = defaultdict(list)  # 构建图
        # 统计
        num_set = set()
        for seq in sequences:
            # 记录sequences中出现的所有数字
            # 等效于
            num_set |= set(seq)
            # 序列含义: 表达节点的前后关系, 前一个节点 指向 后一个节点, 后一个节点入度增加1
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i + 1])
                inDeg[seq[i + 1]] += 1

        # 若数字集合与org长度不等或不一致，直接返回False
        if len(num_set) != len(nums) or set(nums) != num_set: return False

        # 通过BFS排序
        q = deque([node for node in num_set if node not in inDeg])
        res = []
        while q:
            if len(q) > 1: return False  # 若同一层有不止一个则说明结果不唯一
            tmp = q.popleft()
            res.append(tmp)
            if tmp in graph:
                for node in graph[tmp]:
                    inDeg[node] -= 1
                    if not inDeg[node]:
                        q.append(node)

        return res == nums  # 判断是否生成的唯一顺序res与org一致

    def sequenceReconstruction2(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        relation_nums = set()

        for arr in sequences:
            relation_nums.update(set(arr))
            for i in range(len(arr) - 1):
                graph[arr[i]].append(arr[i + 1])
                in_degree[arr[i + 1]] += 1

        if len(relation_nums) != len(nums):
            return False

        # 初始值：根节点，入度为0的节点
        start = list()
        for c in list(relation_nums):
            if c not in in_degree:
                start.append(c)
        q = deque(start)

        index = 0
        while q:
            # 每批次节点超过1
            if len(q) > 1:
                return False
            cur = q.popleft()
            # 当前值不符合nums的顺序，直接返回False
            if cur != nums[index]:
                return False
            index += 1
            if cur in graph:
                for node in graph[cur]:
                    # FIXME 下一批节点入度 减1；并筛选入度为0的新一批节点
                    in_degree[node] -= 1
                    if in_degree[node] == 0:
                        q.append(node)
        return True

# 210. 课程表 II
class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        # 将所有入度为 0 的节点放入队列中
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            # 从队首取出一个节点
            u = q.popleft()
            # 放入答案中
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                # 如果相邻节点 v 的入度为 0，就可以选 v 对应的课程了
                if indeg[v] == 0:
                    q.append(v)

        if len(result) != numCourses:
            result = list()
        return result

    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        result = list()
        # 判断有向图中是否有环
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    valid = False
                    return
            # 将节点标记为「已完成」
            visited[u] = 2
            # 将节点入栈
            result.append(u)

        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        if not valid:
            return list()

        # 如果没有环，那么就有拓扑排序
        # 注意下标 0 为栈底，因此需要将数组反序输出
        return result[::-1]


# 743. 网络延迟时间
class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # FIXME 索引从1开始
        graph = defaultdict(list)
        # 描述入度: 从入度为0的叶子节点开出遍历
        out_degree = [0] * (n + 1)
        for s, e, w in times:
            graph[s].append((s, e, w))
            out_degree[e] += 1

        # 记录每个节点的最小耗时
        dp = [float("inf")] * (n + 1)
        dp[k] = 0
        q = deque(graph[k])
        while q:
            start, end, time = q.popleft()
            # 剪枝操作：耗时过长，直接跳过
            if dp[start] + time > dp[end]:
                continue
            dp[end] = dp[start] + time
            out_degree[end] -= 1
            for arr in graph[end]:
                nxt = arr[1]
                # FIXME 下个节点出度不会0，存在子节点，就需要继续往后遍历
                if out_degree[nxt] > 0:
                    q.append(arr)
        ans = -1
        for i in range(1, n + 1):
            t = dp[i]
            if t == float("inf") and i != k:
                return -1
            ans = max(ans, t)
        return ans



    # 最短路径算法
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x - 1][y - 1] = time

        dist = [float('inf')] * n
        dist[k - 1] = 0
        # FIXME k -1 位置并没有在此时更新为True
        used = [False] * n
        for _ in range(n):
            # TODO 核心：寻找距离x最近的 未确定 且 距离耗时最短的 节点
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            used[x] = True
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1
