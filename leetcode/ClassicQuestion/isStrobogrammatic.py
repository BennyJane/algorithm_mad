# 246. 中心对称数
from functools import lru_cache
from typing import List


class Solution1:
    def isStrobogrammatic(self, num: str) -> bool:
        # 满足旋转后还是数字的数字
        # 2 5 不是
        reverseDict = {'6': '9', '9': '6', '8': '8', '0': '0', '1': '1'}
        l, r = 0, len(num) - 1
        while l <= r:
            if num[l] not in reverseDict \
                    or reverseDict[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution2:
    def findStrobogrammatic2(self, n: int) -> List[str]:
        if n == 0:
            return []

        d = [["0", "0"], ["1", "1"], ["8", "8"], ["9", "6"], ["6", "9"]]

        stack = list()
        if n & 1 == 1:
            n -= 1
            stack.extend(["0", "1", "8"])
        else:
            stack.append("")
        n //= 2
        while n > 0:
            temp = list()
            while stack:
                cur = stack.pop()
                for x, y in d:
                    # 避免以0开头
                    if n == 1 and x == "0":
                        continue
                    temp.append(x + cur + y)
            stack = temp
            n -= 1
        return stack

    def findStrobogrammatic(self, n: int) -> List[str]:

        pairs = [['1', '1'], ['8', '8'], ['6', '9'], ['9', '6']]

        def fun(x):
            if x == 0:
                return [""]
            elif x == 1:
                return ["0", "1", "8"]
            res = []
            for num in fun(x - 2):
                for a, b in pairs:
                    res.append(a + num + b)

                if x != n:
                    res.append("0" + num + "0")
            return res

        # print(fun(n))
        return fun(n)


class Solution3:
    def func(self, n: int) -> List[str]:
        self.pairs = [['1', '1'], ['8', '8'], ['6', '9'], ['9', '6']]

        def dfs(x: int) -> List[str]:
            if x == 0:
                return [""]
            if x == 1:
                return ["0", "1", "8"]
            ans = []
            for s in dfs(x - 2):
                for a, b in self.pairs:
                    ans.append(a + s + b)
                if x != n:
                    ans.append('0' + s + '0')
            return ans

        return dfs(n)

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        n1, n2 = len(low), len(high)
        min_len = min(n1, n2)
        max_len = max(n1, n2)
        res = []
        for n in range(min_len, max_len + 1):
            for s in self.func(n):
                if int(low) <= int(s) <= int(high):
                    res.append(s)
        return len(res)
