# 1036.逃离大迷宫
class Solution12:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        """
        BLOCKED: 在包围圈中
        VALID: 不在包围圈中
        FOUND: 无论是否在包围圈中,在n(n-1)/2步搜索过程中到达target
        """
        BLOCKED, VALID, FOUND = -1, 0, 1
        WIDTH = 10 ** 6
        bCount = len(blocked)

        # 1个障碍物,无法构成包围圈
        if bCount < 2:
            return True
        # 利用集合判断元素包含关系,效率高于list
        hash_blocked = set(tuple(pos) for pos in blocked)

        def check(startPos: tuple, endPos: tuple) -> int:
            # 包围圈内最大非障碍数量
            countdown = bCount * (bCount - 1) // 2

            q = deque([startPos])
            visited = {startPos}

            while q and countdown > 0:
                x, y = q.popleft()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < WIDTH and 0 <= ny < WIDTH \
                            and (nx, ny) not in hash_blocked \
                            and (nx, ny) not in visited:
                        if (nx, ny) == endPos:
                            return FOUND
                        countdown -= 1
                        q.append((nx, ny))
                        visited.add((nx, ny))
            # 广度优先搜索提前结束: 表示startPos位于包围圈内,且另一个点不再包围圈内
            if countdown > 0:
                return BLOCKED
            # 另一个点不在指定范围内
            return VALID

        firstSearch = check(tuple(source), tuple(target))
        if firstSearch == FOUND:
            return True
        if firstSearch == BLOCKED:
            return False
        # 检索终点指定范围是否可以发现起始点
        secondSearch = check(tuple(target), tuple(source))
        if secondSearch == BLOCKED:
            return False
        return True
    def isEscapePossible2(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        WIDTH = int(1e6)  # 矩阵长宽
        MAX_POINTS = int(1e5)  # 从起始点 或 终点 广度搜索点的范围, 直接使用估值
        BASE = 131  # 计算坐标的辅助参数
        DIR = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # lambda:表达式, 降低运算速度
        lineFunc = lambda p: p[0] * BASE + p[1]
        # 计算每个坐标的哈希值
        blocked_hash = {lineFunc(pos) for pos in blocked}

        def check(startPos, endPos):
            visited = {lineFunc(startPos)}

            q = deque()
            q.append(startPos)

            while q and len(visited) <= MAX_POINTS:
                x, y = q.popleft()
                for mx, my in DIR:
                    nx, ny = x + mx, y + my
                    projectPos = lineFunc((nx, ny))
                    if (0 > nx or nx >= WIDTH) or (
                            0 > ny or ny >= WIDTH) or projectPos in blocked_hash or projectPos in visited:
                        continue
                    if (nx, ny) == endPos:
                        return True
                    q.append((nx, ny))
                    visited.add(projectPos)

            return len(visited) > MAX_POINTS

        return check(tuple(source), tuple(target)) and check(tuple(target), tuple(source))