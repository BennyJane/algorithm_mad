from random import randrange, random


class Solution1:
    # 686. 重复叠加字符串匹配
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        res = ""
        ans = 0
        while len(res) < n:
            res += a
            ans += 1
        res += a  # 首尾需要考虑多一个a

        if b not in res:
            return -1
        idx = res.index(b)
        if idx + n > m * ans:
            return ans + 1
        return ans


# 方法一：Rabin-Karp 算法
class Solution12:
    def strstr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        k1 = 10 ** 9 + 7
        k2 = 1337
        mod1 = randrange(k1) + k1
        mod2 = randrange(k2) + k2

        hash_needle = 0
        for c in needle:
            hash_needle = (hash_needle * mod2 + ord(c)) % mod1
        hash_haystack = 0
        for i in range(m - 1):
            hash_haystack = (hash_haystack * mod2 + ord(haystack[i % n])) % mod1
        extra = pow(mod2, m - 1, mod1)
        for i in range(m - 1, n + m - 1):
            hash_haystack = (hash_haystack * mod2 + ord(haystack[i % n])) % mod1
            if hash_haystack == hash_needle:
                return i - m + 1
            hash_haystack = (hash_haystack - extra * ord(haystack[(i - m + 1) % n])) % mod1
            hash_haystack = (hash_haystack + mod1) % mod1
        return -1

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        index = self.strstr(a, b)
        if index == -1:
            return -1
        if n - index >= m:
            return 1
        return (m + index - n - 1) // n + 2


# 方法二：Knuth-Morris-Pratt 算法
class Solution13:
    def strstr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        pi = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and needle[i] != needle[j]:
                j = pi[j - 1]
            if needle[i] == needle[j]:
                j += 1
            pi[i] = j

        i, j = 0, 0
        while i - j < n:
            while j > 0 and haystack[i % n] != needle[j]:
                j = pi[j - 1]
            if haystack[i % n] == needle[j]:
                j += 1
            if j == m:
                return i - m + 1
            i += 1
        return -1

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        index = self.strstr(a, b)
        if index == -1:
            return -1
        if n - index >= m:
            return 1
        return (m + index - n - 1) // n + 2


# 1044.最长重复子串
class Solution2:
    """
    从最长的可能新开始遍历，只要存在重复，即可终止返回

    重复特征：
    假设从i开始存在长度为k的字符串，那么另一个字符串的起始索引一定在索引i之后；
    如果已经确认存在长度为k的解，那么其他索引的讨论，可以直接从长度k+1考虑 ==》 剪枝

    """

    # 广度优先思想
    def longestDupSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            while s[i:i + len(ans) + 1] in s[i + 1:]:
                ans = s[i:i + len(ans) + 1]
        return ans

    # 递归
    def longestDupSubstring2(self, s: str) -> str:
        n = len(s)
        length = 0

        def dfs(index):
            nonlocal length
            nxtL = length + 1
            # TODO 核心： 将判断是否存在重复字符串的方法，交给内置方法
            while s[index: index + nxtL] in s[index + 1:]:
                length = max(length, nxtL)
                nxtL += 1

        ans = ""
        for i in range(n - 1):
            dfs(i)
            if length > len(ans):
                ans = s[i: s + length + 1]
        return ans


class Solution22:
    # 二分查找 + Rabin-Karp 字符串编码
    # https://leetcode-cn.com/problems/longest-duplicate-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode-0i9rd/
    def longestDupSubstring(self, s: str) -> str:
        # 生成两个进制
        a1, a2 = random.randint(26, 100), random.randint(26, 100)
        # 生成两个模
        mod1, mod2 = random.randint(10 ** 9 + 7, 2 ** 31 - 1), random.randint(10 ** 9 + 7, 2 ** 31 - 1)
        n = len(s)
        # 先对所有字符进行编码
        arr = [ord(c) - ord('a') for c in s]
        # 二分查找的范围是[1, n-1]
        l, r = 1, n - 1
        length, start = 0, -1
        while l <= r:
            m = l + (r - l + 1) // 2
            idx = self.check(arr, m, a1, a2, mod1, mod2)
            # 有重复子串，移动左边界
            if idx != -1:
                l = m + 1
                length = m
                start = idx
            # 无重复子串，移动右边界
            else:
                r = m - 1
        return s[start:start + length] if start != -1 else ""

    def check(self, arr, m, a1, a2, mod1, mod2):
        n = len(arr)
        aL1, aL2 = pow(a1, m, mod1), pow(a2, m, mod2)
        h1, h2 = 0, 0
        for i in range(m):
            h1 = (h1 * a1 + arr[i]) % mod1
            h2 = (h2 * a2 + arr[i]) % mod2
        # 存储一个编码组合是否出现过
        seen = {(h1, h2)}
        for start in range(1, n - m + 1):
            h1 = (h1 * a1 - arr[start - 1] * aL1 + arr[start + m - 1]) % mod1
            h2 = (h2 * a2 - arr[start - 1] * aL2 + arr[start + m - 1]) % mod2
            # 如果重复，则返回重复串的起点
            if (h1, h2) in seen:
                return start
            seen.add((h1, h2))
        # 没有重复，则返回-1
        return -1


class Solution23:
    # 字典树
    def longestDupSubstring(self, s: str) -> str:
        return ""
