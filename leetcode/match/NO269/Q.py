from bisect import bisect_right
from typing import List


class Solution1:
    def firstPalindrome(self, words: List[str]) -> str:
        ans = ""
        for w in words:
            reverseWord = w[::-1]
            if w == reverseWord:
                return w
        return ans


class Solution2:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index = 0
        n = len(spaces)
        ans = ""
        for i, c in enumerate(s):
            if index < n and i == spaces[index]:
                ans = ans + " " + c
                index += 1
            else:
                ans += c
        return ans


class Solution3:
    # 滑动窗口
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        cnt = 0
        l, r = 0, 0
        while l < n:
            r = l
            while r + 1 < n and prices[r] - prices[r + 1] == 1:
                r += 1
            for t in range(1, r - l + 1):
                cnt += t
            l += 1

        return cnt

    def getDescentPeriods2(self, prices: List[int]) -> int:
        n = len(prices)
        cnt = 0
        l, r = 0, 0
        while l < n:
            r = l
            while r + 1 < n and prices[r] - prices[r + 1] == 1:
                r += 1
            cnt += (r - l + 1)
            l += 1

        return cnt


class Solution4:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(k):
            f = list()
            j, length = i, 0
            while j < n:
                length += 1
                it = bisect_right(f, arr[j])
                if it == len(f):
                    f.append(arr[j])
                else:
                    f[it] = arr[j]
                j += k
            ans += length - len(f)
        return ans


"""
[5,4,3,2,1]
1
[4,1,5,2,6,2]
2
[4,1,5,2,6,2]
3


[12,6,12,6,14,2,13,17,3,8,11,7,4,11,18,8,8,3]
1
输出：
8
预期：
12

"""
if __name__ == '__main__':
    sol = Solution4()
    # arr = [12, 6, 12, 6, 14, 2, 13, 17, 3, 8, 11, 7, 4, 11, 18, 8, 8, 3]
    # k = 1
    arr = [4, 1, 5, 2, 6, 2]
    k = 3
    sol.kIncreasing(arr, k)
