import collections
from collections import deque
from collections import Counter
from itertools import chain
from typing import List
from collections import defaultdict


class Solution1:
    # 1034. 边界着色 MIDDLE
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]

        target = grid[row][col]
        factors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            if dp[x][y] == -1 or grid[x][y] != target:
                return
            dp[x][y] = -1
            for xMov, yMov in factors:
                nxtX, nxtY = x + xMov, y + yMov
                if nxtX < 0 or nxtX >= m or nxtY < 0 or nxtY >= n or (
                        dp[nxtX][nxtY] == 0 and grid[nxtX][nxtY] != target):
                    grid[x][y] = color
                else:
                    dfs(nxtX, nxtY)

        dfs(row, col)
        return grid

    def colorBorder2(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        # 记录是否位置是否已经访问
        visited = [[False] * n for _ in range(m)]
        borders = list()  # FIXME 记录边界位置，最后更新原数组颜色
        oriColor = grid[row][col]
        visited[row][col] = True

        def dfs(x, y):
            isBorder = False  # 只要相邻四个方向有一个不是岛屿，当前位置就是边界位置
            # 移动的四个可能性
            factors = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for dx, dy in factors:
                nx, ny = x + dx, y + dy
                # 优先考虑正面情况：下一步位置是岛屿 ==》 然后取反，获得非岛屿的情况
                if not (0 <= nx < m and 0 <= y < n and grid[nx][ny] == oriColor):
                    isBorder = True
                elif not visited[nx][ny]:
                    # 下一步为岛屿的情况：只需要考虑未访问过的情况
                    visited[nx][ny] = True
                    dfs(nx, ny)
            if isBorder:
                borders.append((x, y))

        dfs(row, col)
        for x, y in borders:
            grid[x][y] = color
        return grid

    # 广度优先
    def colorBorder3(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        oriColor = grid[row][col]
        # 移动的四个可能性
        factors = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # 已访问位置记录
        visited = [[0] * n for _ in range(m)]

        borders = list()
        # FIXME 初始节点处理
        stack = [(row, col)]
        visited[row][col] = 1

        while stack:
            # TODO 每次处理一批节点
            size = len(stack)
            temp = list()  # FIXME 记录下一批节点
            for _ in range(size):
                x, y = stack.pop()
                isBorder = False
                for dx, dy in factors:
                    nX, nY = x + dx, y + dy
                    if 0 <= nX < m and 0 <= nY < n and grid[nX][nY] == oriColor:
                        if visited[nX][nY] == 0:
                            # FIXME 这个位置更新已访问记录
                            visited[nX][nY] = 1
                            temp.append((nX, nY))
                    else:
                        isBorder = True
                if isBorder:
                    borders.append((x, y))
            # 更新stack
            stack = temp
        # 边界着色
        for x, y in borders:
            grid[x][y] = color
        return grid

    def colorBorder4(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        originalColor = grid[row][col]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        borders = []
        direc = ((-1, 0), (1, 0), (0, -1), (0, 1))

        # 使用双端队列
        q = deque([(row, col)])
        visited[row][col] = True
        while q:
            # 每次只处理一个节点
            x, y = q.popleft()
            isBorder = False
            for dx, dy in direc:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == originalColor):
                    isBorder = True
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
            if isBorder:
                borders.append((x, y))
        for x, y in borders:
            grid[x][y] = color
        return grid


# 463. 岛屿的周长 SIMPLE
class Solution2:
    """
    先找到边界方块： 然后计算边界长度，即不与陆地(1)相邻的边的数量
    """

    # 暴力求解： 直接遍历所有方块，逐个判断，并累加
    # 每个位置的边界情况是确定的，且不会重复计算
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moveDir = ((1, 0), (-1, 0), (0, 1), (0, -1))
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                temp = 0
                for dx, dy in moveDir:
                    nx, ny = i + dx, j + dy
                    if not (0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1):
                        temp += 1
                ans += temp
        return ans

    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        moveDir = ((1, 0), (-1, 0), (0, -1), (0, 1))

        visited = [[False] * n for _ in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited[i][j] = True
                    break

        ans = 0
        while queue:
            # 先进先出
            x, y = queue.popleft()
            temp = 0  # 计算边界长度
            for dx, dy in moveDir:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                else:
                    # FIXME 核心，统计边界长度
                    temp += 1
            ans += temp
        return ans


# 695.岛屿的最大面积
class Solution3:
    # 只有在水平于垂直方向上的相邻才是相邻
    # 没有给出岛屿位置
    """
    优化： 不适用数组记录已访问位置，直接将已经访问的位置修改为0
    """

    # 广度优先：
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """ 关键点：
        记录已经访问过的位置
        统计相邻陆地的数量，即岛屿面积
        """
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        moveDir = ((1, 0), (-1, 0), (0, -1), (0, 1))

        def stats(X, Y) -> int:
            res = 1
            queue = deque()
            queue.append((X, Y))
            visited[X, Y] = True

            while queue:
                x, y = queue.popleft()
                for dx, dy in moveDir:
                    nx, ny = x + dx, y + dy
                    # 只处理岛屿部分
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        if not visited[nx][ny]:
                            visited[nx][ny] = True
                            res += 1
                            queue.append((nx, ny))
            return res

        ans = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    continue
                area = stats(x, y)
                ans = max(ans, area)
        return ans

    # 递归： 深度优先
    def maxAreaOfIsland2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        moveDir = ((1, 0), (-1, 0), (0, -1), (0, 1))

        def dfs(x, y):
            cnt = 1
            for dx, dy in moveDir:
                nx, ny = x + dx, y + dy
                # 只处理岛屿部分
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        cnt += dfs(nx, ny)
            return cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                visited[i][j] = True
                res = dfs(i, j)
                ans = max(ans, res)

        return ans

    def maxAreaOfIsland3(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0  # 记录当前岛屿面积
                q = collections.deque([(i, j)])
                while q:
                    cur_i, cur_j = q.popleft()
                    # 判断是否为岛屿
                    # FIXME 修改判断逻辑的位置
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    # 如果是岛屿，面积加1
                    cur += 1
                    # FIXME 将当前位置修改为0，表示已经访问过
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        # 相邻位置直接放入队列不筛选
                        q.append((next_i, next_j))
                ans = max(ans, cur)
        return ans

    # 深度优先搜索 + 栈
    def maxAreaOfIsland4(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                cur = 0
                stack = [(i, j)]
                while stack:
                    cur_i, cur_j = stack.pop()
                    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
                        continue
                    cur += 1
                    grid[cur_i][cur_j] = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = cur_i + di, cur_j + dj
                        stack.append((next_i, next_j))
                ans = max(ans, cur)
        return ans


# 200.岛屿数量 MIDDLE
class Solution4:
    """
    参考 695.岛屿最大面积,统计维度修改为岛屿数量
    """

    # FIXME 注意是字符串 1-0; 而不是数字1-0
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0":
                    continue
                ans += 1
                # 将当前岛屿的所有位置修改为0
                stack = [(row, col)]
                grid[row][col] = "0"
                while stack:
                    x, y = stack.pop()
                    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                            grid[nx][ny] = "0"
                            stack.append((nx, ny))
        return ans

    # 递归
    def numIslands1(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            # 核心目标: 将相连道路的值修改为0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1":
                    grid[nx][ny] = "0"
                    dfs(nx, ny)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                ans += 1
                grid[i][j] = "0"
                dfs(i, j)
        return ans


# 305. 岛屿数量II
class Solution5:
    # 思路1: 当新增岛屿四周不与岛屿相连时,岛屿数据 +1 FIXME 错误:没有考虑岛屿数量减少的情况
    def numIslands(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(n)]

        ans = []
        cnt = 0
        for x, y in positions:
            add = 1  # 默认新增一个岛屿
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                # 判断是否相邻岛屿
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                    add = 0
                    break
            grid[x][y] = 1
            cnt += add
            ans.append(cnt)
        return ans

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0] * n for _ in range(m)]

        index = 1  # 独立岛屿编号
        visited = list()  # 记录连同的岛屿的编号
        ans = []
        for x, y in positions:
            if grid[x][y] != 0:  # FIXME 填充相同位置,直接返回
                ans.append(len(visited))
                continue
            indexArr = list()  # 统计当前填充位置,连通的岛屿索引
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                # 判断是否相邻岛屿: TODO 当连同岛屿后,需要减少岛屿数量
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 0:
                    indexArr.append(grid[nx][ny])
            if len(indexArr) == 0:
                # 没有相邻岛屿时,就新增一个岛屿
                index += 1
                visited.append([index])
                grid[x][y] = index
            elif len(indexArr) == 1:
                # 只有一个连同岛屿
                grid[x][y] = indexArr[0]
            else:
                grid[x][y] = indexArr[0]
                temp = list()
                indexSet = set(indexArr)
                for t in visited:
                    tSet = set(t)
                    if len(tSet.intersection(indexSet)) > 0:
                        indexSet.update(tSet)
                    else:
                        temp.append(t)
                temp.append(list(indexSet))
                visited = temp  # 更新连同岛屿编号
            ans.append(len(visited))
        return ans


# 323. 无向图中连通分量的数目 MIDDLE
class Solution6:
    # 利用集合特性
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [1] * n

        res = list()
        for item in edges:
            t = set(item)
            temp = list()
            for s in res:
                if t.intersection(set(s)):
                    t.update(set(s))
                else:
                    temp.append(s)
            temp.append(t)
            res = temp
        cnt = len(res)
        # FIXME 需要使用 * 传入
        for i in chain(*res):
            visited[i] = 0
        cnt += sum(visited)
        return cnt

    # 利用图论基础知识
    # 使用map记录相邻关系,然后使用广度优先 or 深度优先,遍历连同分量,并记录以访问的值
    # 参考: 岛屿题目
    def countComponents2(self, n: int, edges: List[List[int]]) -> int:
        dic = defaultdict(list)
        res = 0

        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        visited = set()

        for i in range(n):
            if i in visited:
                continue
            res += 1
            visited.add(i)
            # bfs: 搜索所有连同分量
            queue = deque()
            queue.append(i)
            while queue:
                nx = queue.popleft()
                for j in dic[nx]:
                    if visited[j]:
                        continue
                    visited.add(j)
                    queue.append(j)
        return res


# 547 省份数量 MIDDLE
class Solution7:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        d = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    d[i].append(j)
                    d[j].append(i)

        visited = [0] * n
        ans = 0

        for i in range(n):
            if visited[i] == 1:
                continue
            ans += 1
            # 遍历所有相邻城市,并更新visited状态
            queue = deque()
            queue.append(i)
            visited[i] = 1
            while queue:
                nx = queue.popleft()
                for j in d[nx]:
                    if visited[j] == 1:
                        continue
                    visited[j] = 1
                    queue.append(j)
        return ans


# 1101. 彼此熟识的最早时间  MIDDLE
class Solution8:
    # 所有人熟识,即 连同分量为1
    # 考虑二分法
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        res = list()
        logs.sort(key=lambda x: x[0])
        for time, x, y in logs:
            edge = {x, y}

            temp = list()
            for s in res:
                if edge.intersection(set(s)):
                    edge.update(set(s))
                else:
                    temp.append(s)
            temp.append(edge)
            res = temp
            if len(res[0]) == n:
                return time
        return -1


# 261.以图判树
class Solution9:
    # 合法树条件: 连同分量为1; 且不存在环
    # 判断方式:从任意节点出发,可以访问所有节点
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        flag = n == len(edges) + 1
        if not flag:
            return flag
        res = list()
        res.append([0])  # 解决 n = 1的情况,edges长度为0
        for x, y in edges:
            cur = {x, y}
            temp = list()
            for old in res:
                if cur.intersection(set(old)):
                    cur.update(set(old))
                else:
                    temp.append(old)
            temp.append(cur)
            res = temp
        return len(res[0]) == n

    # FIXME 这个解法,没有排除环的情况吧?
    def validTree2(self, n: int, edges: List[List[int]]) -> bool:
        # 树的边数 与 节点 个数的关系
        # FIXME 此处的判断,排除环的存在
        flag = n == len(edges) + 1
        if not flag:
            return flag
        mark = [0 for _ in range(n)]
        grid = [[] for _ in range(n)]
        for x, y in edges:
            grid[x].append(y)
            grid[y].append(x)

        # 广度优先搜索
        # 从任意一个节点出发,可以访问到所有节点
        def bfs(root):
            que = [root]
            while que:
                node = que.pop(0)
                for ns in grid[node]:
                    if not mark[ns]:
                        que.append(ns)
                        mark[ns] = 1

        mark[0] = 1
        bfs(0)
        return sum(mark) == n


# 286. 墙与门 MIDDLE
class Solution10:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        pass

    def wallsAndGates2(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        row = len(rooms)
        if row == 0:
            return
        col = len(rooms[0])

        def bfs(grip: List[List[int]], x, y, path: int):
            for r, c in ([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]):
                if r < 0 or r >= row or c < 0 or c >= col:
                    continue
                if grip[r][c] == -1 or grip[r][c] == 0:
                    continue
                cur = grip[r][c]
                if path + 1 >= cur:
                    continue
                grip[r][c] = path + 1
                bfs(grip, r, c, path + 1)

        for i in range(row):
            for j in range(col):
                if rooms[i][j] == 0:
                    bfs(rooms, i, j, 0)


# 207.课程表
class Solution11:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 记录节点关系：每个节点保存相邻节点的数据
        edges = collections.defaultdict(list)
        # 记录是否已经访问过： 0 未访问 1 访问中 2 已经访问
        visited = [0] * numCourses
        result = list()
        # 判断拓扑排序是否有效 ==》 是否为无环图
        valid = True

        for child, parent in prerequisites:
            edges[parent] = child

        def dfs(p: int):
            # TODO 允许修改闭包外部变量
            nonlocal valid
            # 设置改
            visited[p] = 1
            for c in edges[p]:
                if visited[c] == 0:
                    dfs(c)
                    if not valid:  # 存在循环
                        return
                elif visited[c] == 1:
                    valid = False
                    return
            visited[p] = 2
            result.append(p)

        # 遍历处理每个节点的情况
        for i in range(numCourses):
            if valid and visited[i] == 0:
                dfs(i)

        return valid


# 684. 冗余连接
class Solution12:
    # 效率更高
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # 记录各个连通分量,每个连通分量使用数组存储
        queue = deque()
        for x, y in edges:
            cur = {x, y}
            size = len(queue)
            for _ in range(size):
                s = queue.popleft()
                if x in s and y in s:
                    return [x, y]
                elif x in s or y in s:
                    cur.update(s)
                else:
                    queue.append(s)
            queue.append(cur)
        return []

    def findRedundantConnection2(self, edges: List[List[int]]) -> List[int]:
        # 记录各个连通分量,每个连通分量使用数组存储
        res = list()
        for item in edges:
            cur = set(item)
            x, y = item
            temp = list()  # 数组重复创建于删除
            for s in res:
                if x in s and y in s:
                    return [x, y]
                elif x in s or y in s:
                    cur.update(set(s))
                else:
                    temp.append(s)
            temp.append(cur)
            res = temp
        return []


# 找到小镇的法官 DIMPLE
# 寻找个节点的入度是 n-1, 出度是 0
class Solution13:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegrees = Counter(y for _, y in trust)
        outDegrees = Counter(x for x, _ in trust)
        return next((i for i in range(1, n + 1) if inDegrees[i] == n - 1 and outDegrees[i] == 0), -1)

    def findJudge2(self, n: int, trust: List[List[int]]) -> int:
        # FIXME 需要特别处理N为1的情况
        if n == 1:
            return 1
        d = dict()  # 记录信任某人的其他人列表，使用集合存储
        visited = [False] * n  # 记录是否信任过其他人，法官为False
        for x, y in trust:
            visited[x - 1] = True
            if y not in d:
                d[y] = set()
                d[y].add(x)
            else:
                d[y].add(x)
        # FIXME 必须先统计完所有数据，才判断，不能中途直接判断
        for k, v in d.items():
            if len(v) == n - 1 and not visited[k - 1]:
                return k
        return -1

    # 转化为 寻找名人的题目
    def findJudge3(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        d = defaultdict(set)
        for x, y in trust:
            d[x].add(y)
        ans = 1
        # 利用法官不信任任何人的条件,中断查询
        for i in range(2, n + 1):
            if ans in d and i in d[ans]:
                ans = i
        # ans 信任别人，直接返回-1
        if ans in d:
            return -1
        for i in range(1, n + 1):
            if i == ans:
                continue
            # i 不信任法官
            if i not in d:
                return -1
            if ans not in d[i]:
                return -1
        return ans


# 277. 搜寻名人 MIDDLE
class Solution14:

    def findCelebrity(self, n: int) -> int:
        def knows(a: int, b: int) -> bool:
            return True

        # 筛选候选人
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        # 检查候选人
        for i in range(n):
            if i == candidate:
                continue
            if not knows(i, candidate):
                return -1
            if knows(candidate, i):
                return -1
        return candidate

    # 超时
    def findCelebrity2(self, n: int) -> int:
        def knows(a: int, b: int) -> bool:
            return True

        inDeg = [0] * n
        outDeg = [0] * n
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    inDeg[j] += 1
                    outDeg[i] += 1
        for i in range(n):
            if inDeg[i] == n - 1 and outDeg[i] == 0:
                return i
        return -1


# 317. 离建筑物最近的距离
class Solution15:
    """
    简单问题：如何统计从单个建筑出发，可以到达的位置以及距离？ 存在不可达到的位置；
    在计算出每个建筑可到到的位置以及距离后，统计全部建筑可以到达的位置，并计算距离和，取最小值
    """

    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        sum_dist = [[0 for _ in range(n)] for _ in range(m)]
        can_reach = [[0 for _ in range(n)] for _ in range(m)]

        def startOne(x, y):
            # 需要使用额外空间记录已访问位置，原数组需要重复使用，不能被修改
            visited = [[False for _ in range(n)] for _ in range(m)]
            visited[x][y] = True
            queue = [(x, y)]
            step = 0
            while queue:
                nxtQueue = list()
                step += 1
                for X, Y in queue:
                    for nx, ny in [[X + 1, Y], [X - 1, Y], [X, Y + 1], [X, Y - 1]]:
                        # 只处理可以到达的空地
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                            if visited[nx][ny]:
                                continue
                            nxtQueue.append((nx, ny))
                            sum_dist[nx][ny] += step
                            can_reach[nx][ny] += 1
                            visited[nx][ny] = True
                # FIXME 重置queue
                queue = nxtQueue

        total = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    total += 1
                    startOne(i, j)

        ans = float("inf")
        for i in range(m):
            for j in range(n):
                if can_reach[i][j] == total:
                    ans = min(ans, sum_dist[i][j])

        return ans if ans != float("inf") else -1


# 296. 最佳的碰头地点
"""
有一队人（两人或以上）想要在一个地方碰面，他们希望能够最小化他们的总行走距离。

给你一个 2D 网格，其中各个格子内的值要么是 0，要么是 1。

1 表示某个人的家所处的位置。这里，我们将使用 曼哈顿距离 来计算，其中 distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|。

示例：

输入: 

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

输出: 6 

解析: 给定的三个人分别住在(0,0)，(0,4) 和 (2,2):
     (0,2) 是一个最佳的碰面点，其总行走距离为 2 + 2 + 2 = 6，最小，因此返回 6。

"""


class Solution16:

    # 中位数： 即聚会点
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rows, cols = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        # rows 自然升序
        cols.sort()  # 需要重新排序

        def calDist(array):
            total = 0
            l, r = 0, len(array) - 1
            while l < r:
                total += abs(array[r] - array[l])
                l += 1
                r -= 1
            return total

        return calDist(rows) + calDist(cols)

    # FIXME 超时
    def minTotalDistance3(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        sum_dist = [[0 for _ in range(n)] for _ in range(m)]

        def startOne(x, y):
            # 需要使用额外空间记录已访问位置，原数组需要重复使用，不能被修改
            visited = [[False for _ in range(n)] for _ in range(m)]
            visited[x][y] = True
            queue = [(x, y)]
            step = 0
            while queue:
                nxtQueue = list()
                step += 1
                for X, Y in queue:
                    for nx, ny in [[X + 1, Y], [X - 1, Y], [X, Y + 1], [X, Y - 1]]:
                        # 只处理可以到达的空地
                        if 0 <= nx < m and 0 <= ny < n:
                            if visited[nx][ny]:
                                continue
                            nxtQueue.append((nx, ny))
                            sum_dist[nx][ny] += step
                            visited[nx][ny] = True
                queue = nxtQueue

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    startOne(i, j)

        ans = float("inf")
        for arr in sum_dist:
            ans = min(ans, min(arr))
        return ans if ans != float("inf") else -1

    # FIXME 超时
    def minTotalDistance2(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 先统计所有人位置
        array = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    array.append((i, j))

        ans = float("inf")
        # 每个人位置作为起点，计算到达其余点的距离
        for i in range(m):
            for j in range(n):
                SUM = 0
                for x, y in array:
                    # 计算每个位置到所有人的距离
                    SUM += abs(x - i) + abs(y - j)
                ans = min(ans, SUM)

        return ans


if __name__ == '__main__':
    pass
