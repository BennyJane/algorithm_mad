from typing import List


class DetectSquares:

    def __init__(self):
        self.cMap = {}
        self.map = {}
        self.resMap = {}

    def set_pos_name(self, x, y):
        return f"{x}_{y}"

    def add(self, point: List[int]) -> None:
        self.resMap.clear()  # 每次添加数据后，清空答案缓存
        x = point[0]
        y = point[1]
        key = self.set_pos_name(x, y)
        if not self.cMap.get(key):
            self.cMap[key] = 1
        else:
            self.cMap[key] = self.cMap.get(key) + 1

        if not self.map.get(x):
            self.map[x] = []
            self.map[x].append(point)
        else:
            self.map[x].append(point)

    def count(self, point: List[int]) -> int:
        ans = 0
        x = point[0]
        y = point[1]
        key = self.set_pos_name(x, y)
        if self.resMap.get(key) is not None:
            return self.resMap.get(key)
        xPoints = self.map.get(x)
        if xPoints is None:
            return ans
        isUsed = []
        for i in range(len(xPoints)):
            otherPoint = xPoints[i]
            s_y = otherPoint[1]
            if y == s_y:
                continue
            width = abs(s_y - y)
            if width in isUsed:
                continue
            else:
                isUsed.append(width)
            ans += self.check(x, y, width)
        self.resMap[key] = ans
        return ans

    def check(self, x, y, width):
        point2 = f"{x + width}_{y}"

        point1 = f"{x}_{y - width}"
        point3 = f"{x + width}_{y - width}"
        res1 = self.cMap.get(point1, 0) * self.cMap.get(point2, 0) * self.cMap.get(point3, 0)

        point1 = f"{x}_{y + width}"
        point3 = f"{x + width}_{y + width}"
        res2 = self.cMap.get(point1, 0) * self.cMap.get(point2, 0) * self.cMap.get(point3, 0)

        point2 = f"{x - width}_{y}"

        point1 = f"{x}_{y - width}"
        point3 = f"{x - width}_{y - width}"
        res3 = self.cMap.get(point1, 0) * self.cMap.get(point2, 0) * self.cMap.get(point3, 0)

        point1 = f"{x}_{y + width}"
        point3 = f"{x - width}_{y + width}"
        res4 = self.cMap.get(point1, 0) * self.cMap.get(point2, 0) * self.cMap.get(point3, 0)
        ans = res1 + res2 + res3 + res4
        return ans
