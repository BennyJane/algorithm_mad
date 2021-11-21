from typing import List


class Solution:
    # 模拟法
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        count = 0
        n = len(plants)
        visited = [False] * n
        while count < n:
            temp = 0
            end = 0
            for i in range(n):
                if visited[i]:
                    continue
                if temp + plants[i] > capacity:
                    break
                else:
                    temp += plants[i]
                    visited[i] = True
                    end = i
                    count += 1
            if end == i:
                ans += end + 1
            else:
                ans += (end + 1) * 2

        return ans

    # 模拟法
    def wateringPlants3(self, plants: List[int], capacity: int) -> int:
        n = len(plants)
        res = 0
        i = 0
        cur = capacity
        while i < n:
            if cur >= plants[i]:
                res += 1
                cur -= plants[i]
            else:
                res += (i + i + 1)
                cur = capacity - plants[i]
            i += 1
        return res

    # 贪心
    def wateringPlants2(self, plants: List[int], capacity: int) -> int:
        ans = len(plants)
        water = capacity
        for i, need in enumerate(plants):
            if water < need:
                ans += 2 * i
                water = capacity
            water -= need
        return ans
