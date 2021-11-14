from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        from heapq import heappop
        from heapq import heapify

        heapify(items)
        n = len(queries)
        ans = [0] * n

        array = [i for i in range(n)]
        array.sort(key=lambda x: queries[x])

        preMax = 0
        for i, oriIndex in enumerate(array):
            q = queries[oriIndex]
            while items and items[0][0] <= q:
                price, beauty = heappop(items)
                preMax = max(preMax, beauty)
            ans[oriIndex] = preMax

        return ans
