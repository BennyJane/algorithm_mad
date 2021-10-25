import heapq
from typing import List
from collections import Counter


# TODO 考察内容：堆 有序队列，将复杂度降低到nlog(k), 由于排序方式

# 692. 前K个高频单词

# 尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。 ==> 优先队列
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        n = len(words)
        # FIXME 直接取k不能保证顺序
        topK = count.most_common(n)
        arr = sorted(topK, key=lambda x: (-1 * x[1], x[0]))
        ans = [item[0] for item in arr[:k]]
        return ans


# 347. 前 K 个高频元素
# https://leetcode-cn.com/problems/top-k-frequent-elements/
class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        ans = map.most_common(k)
        return [item[0] for item in ans]


# 295. 数据流的中位数
# https://leetcode-cn.com/problems/find-median-from-data-stream/

# 优先队列 || 大小堆
class MedianFinder:

    def __init__(self):
        self.queMin = list()
        self.queMax = list()

    def addNum(self, num: int) -> None:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if not queMin_ or num <= -queMin_[0]:
            heapq.heappush(queMin_, -num)
            if len(queMax_) + 1 < len(queMin_):
                heapq.heappush(queMax_, -heapq.heappop(queMin_))
        else:
            heapq.heappush(queMax_, num)
            if len(queMax_) > len(queMin_):
                heapq.heappush(queMin_, -heapq.heappop(queMax_))

    def findMedian(self) -> float:
        queMin_ = self.queMin
        queMax_ = self.queMax

        if len(queMin_) > len(queMax_):
            return -queMin_[0]
        return (-queMin_[0] + queMax_[0]) / 2


from sortedcontainers import SortedList


# 有序集合 + 双指针
class MedianFinder1:

    def __init__(self):
        self.nums = SortedList()
        self.left = self.right = None
        self.left_value = self.right_value = None

    def addNum(self, num: int) -> None:
        nums_ = self.nums

        n = len(nums_)
        nums_.add(num)

        if n == 0:
            self.left = self.right = 0
        else:
            # 模拟双指针，当 num 小于 self.left 或 self.right 指向的元素时，num 的加入会导致对应指针向右移动一个位置
            if num < self.left_value:
                self.left += 1
            if num < self.right_value:
                self.right += 1

            if n & 1:
                if num < self.left_value:
                    self.left -= 1
                else:
                    self.right += 1
            else:
                if self.left_value < num < self.right_value:
                    self.left += 1
                    self.right -= 1
                elif num >= self.right_value:
                    self.left += 1
                else:
                    self.right -= 1
                    self.left = self.right

        self.left_value = nums_[self.left]
        self.right_value = nums_[self.right]

    def findMedian(self) -> float:
        return (self.left_value + self.right_value) / 2


# 387. 字符串中的第一个唯一字符（Simple）
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        for i, v in enumerate(s):
            if s.count(v) == 1:
                return i

        return -1

    def firstUniqChar2(self, s: str) -> int:
        for i, v in enumerate(s):
            if s.count(v) == 1:
                return i

        return -1


if __name__ == '__main__':
    sol = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    sol.topKFrequent(words, 3)
