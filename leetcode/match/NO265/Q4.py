from typing import List
from collections import Counter


class Solution:
    # FIXME 超时
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        arr1 = self.bfs(s1)
        arr2 = self.bfs(s2)
        d = dict()
        for word in arr2:
            length = len(word)
            if length not in d:
                d[length] = [word]
            else:
                d[length].append(word)
        for word in arr1:
            length = len(word)
            if length not in d:
                continue
            for word2 in d.get(length):
                if self.check(word, word2):
                    return True
        return False

    def check(self, word1, word2) -> bool:
        for i, c1 in enumerate(word1):
            if c1 == word2[i] or c1 == "*" or word2[i] == "*":
                continue
            else:
                return False
        return True

    def bfs(self, word: str):
        res = []
        start = 0
        n = len(word)
        while start < n:
            c = word[start]
            if c.isalpha():
                right = start + 1
                while right < n and word[right].isalpha():
                    right += 1
                if not res:
                    res.append(word[start: right])
                else:
                    res = [item + word[start: right] for item in res]
                start = right
            else:
                right = start + 1
                while right < n and word[right].isdigit():
                    right += 1
                mid = self.change(word[start: right])
                if mid and res:
                    temp = []
                    for item in res:
                        for cur in mid:
                            temp.append(item + cur)
                    res = temp
                if not res and mid:
                    res = mid
                start = right

        return res

    def change(self, num: str) -> List[str]:
        n = len(num)
        res = ["*" * int(num)]
        if n == 2:
            res.append("*" * int(num[0]) + "*" * int(num[1]))
        if n == 3:
            res.append("*" * int(num[0]) + "*" * int(num[1]) + "*" * int(num[2]))
            res.append("*" * int(num[:2]) + "*" * int(num[2]))
            res.append("*" * int(num[0]) + "*" * int(num[1:]))
        return res


class Solution1:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(1, n1 + 1):
            up = s1[i - 1]
            for j in range(1, n2 + 1):
                down = s2[j - 1]
                if up.isalpha() and down.isalpha():
                    if up == down:
                        dp[i][j] = dp[i - 1][j - 1]
                elif up.isalpha():
                    # 考虑down中数字个数
                    pass
                elif down.isalpha():
                    pass
                else:
                    pass


if __name__ == '__main__':
    sol = Solution()
    # s1 = "112s"
    # s2 = "g841"

    # s1 = "a5b"
    # s2 = "c5b"

    s1 = "98u8v8v8v89u888u998v88u98v88u9v99u989v8u"
    s2 = "9v898u98v888v89v998u98v9v888u9v899v998u9"
    sol.possiblyEquals(s1, s2)
