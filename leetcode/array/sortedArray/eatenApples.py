import heapq
from typing import List
from heapq import heappush
from heapq import heappop


# 1705. 吃苹果的最大数目
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(days)
        array = list()

        # 起始索引不为0
        today = 1
        ans = 0

        # 进入循环的条件：队列不为空；仍在长出苹果
        while array or today <= n:
            # 每天先添加新生成的苹果，并删除已经过期的苹果

            # 记录过期时间，以及数量
            # 有序队列中保存：[过期时间，苹果数量]
            if today <= n and apples[today - 1] != 0:
                heappush(array, [today + days[today - 1], apples[today - 1]])
            # 寻找到最先过期的苹果：过期日期最早
            while array and array[0][0] <= today:
                heappop(array)
            # 队列不为空，可以吃一个苹果
            if array:
                if array[0][1] == 1:
                    heappop(array)
                else:
                    array[0][1] -= 1
                ans += 1
            today += 1
        return ans

    def eatenApples2(self, apples: List[int], days: List[int]) -> int:
        pq, i, ans = [], 0, 0
        while i < len(apples):
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if apples[i]:
                heapq.heappush(pq, [i + days[i], apples[i]])
            if pq:
                pq[0][1] -= 1
                if not pq[0][1]:
                    heapq.heappop(pq)
                ans += 1
            i += 1
        while pq:
            cur = heapq.heappop(pq)
            # 可以连续吃苹果的天数：过期前的天数，苹果树
            d = min(cur[0] - i, cur[1])
            i += d
            ans += d
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
        return ans


if __name__ == '__main__':
    sol = Solution()
    arr1 = [2, 1, 10]
    arr2 = [2, 10, 1]
    sol.eatenApples(arr1, arr2)
