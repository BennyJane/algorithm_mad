from typing import List


# 275. H 指数 II
class Solution:
    # 关键点：右侧长度决定了h的下限
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        count = 0  # 记录已经遍历数组长度
        ans = 0
        for i in range(n - 1, -1, -1):
            count += 1
            cur = citations[i]
            if cur >= count:
                ans = max(ans, count)

        return ans

    def hIndex2(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        ans = 0
        while left <= right:
            mid = int((left + right + 1) / 2)
            right_len = n - mid
            if citations[mid] >= right_len:
                ans = max(ans, right_len)
                right -= 1
            else:
                left += 1

        return ans

    def hIndex3(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if citations[mid] >= n - mid:
                right = mid - 1
            else:
                left = mid + 1
        return n - left
