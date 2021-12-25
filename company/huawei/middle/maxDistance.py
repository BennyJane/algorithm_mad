from collections import deque
from typing import List


class Solution:
    # 1162.地图分析
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        if len(queue) == 0 or len(queue) == m * n:
            return -1

        step = 0
        while queue:
            size = len(queue)
            isExist = False
            for i in range(size):
                x, y = queue.popleft()
                for nx, ny in ([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]):
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 0:
                        isExist = True
                        queue.append((nx, ny))
                        # FIXME 访问过的路径必须标注
                        grid[nx][ny] = 1
            step += isExist
        return step


# 317.离建筑物最近的距离
class Solution2:

    def shortestDistance(self, grid: List[List[int]]) -> int:
        return 0
