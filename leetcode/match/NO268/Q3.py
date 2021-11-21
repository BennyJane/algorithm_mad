from bisect import bisect_left, bisect_right
from typing import List
from functools import lru_cache
from collections import defaultdict


class RangeFreqQuery:

    # FIXME 耗时发生在这一步: 需要创建大量字典数据结构
    def __init__(self, arr: List[int]):
        n = len(arr)
        self.cache = [defaultdict(int)]
        lastDict = defaultdict(int)
        for i in range(n):
            cur = arr[i]
            temp = defaultdict(int)
            temp.update(lastDict)
            temp[cur] += 1
            self.cache.append(temp)

    @lru_cache(None)
    def query(self, left: int, right: int, value: int) -> int:
        leftDict = self.cache[left]
        rightDict = self.cache[right + 1]
        res = rightDict.get(value, 0) - leftDict.get(value, 0)
        return 0 if res < 0 else res


class RangeFreqQuery1:

    def __init__(self, arr: List[int]):
        self.cache = arr

    @lru_cache(None)  # FIXME 必须使用记忆化搜索，否则会超时
    def query(self, left: int, right: int, value: int) -> int:
        temp = self.cache[left:right + 1]
        temp.count(value)
        return temp.count(value)


class RangeFreqQuery2:

    def __init__(self, arr: List[int]):
        self.num_idxs = defaultdict(list)
        for i, x in enumerate(arr):
            self.num_idxs[x].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.num_idxs.keys():
            return 0
        idxs = self.num_idxs[value]
        L = bisect_left(idxs, left)
        R = bisect_right(idxs, right)
        return R - L


if __name__ == '__main__':
    nums = [2, 2, 1, 2, 2]
    sol = RangeFreqQuery(nums)
    sol.query(2, 4, 1)
