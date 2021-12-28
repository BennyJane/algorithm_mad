# from functools import cache
from functools import reduce, lru_cache
from linecache import cache
from typing import List
from collections import defaultdict


# 472.连接词
class Solution1:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = defaultdict(list)

        def dfs(W, index):
            if len(W) == index:
                return True
            for l in d.keys():
                if W[index: index + l] in d[l]:
                    if dfs(W, index + l):
                        return True
            return False

        ans = []
        for w in sorted(words, key=len):
            L = len(w)
            # 空字符串一定不能满足由两个子字符串组合而成
            # 不存在重复字符串，也就不存在 空字符串 + 相等字符串 = 相等字符串 的情况
            if L == 0:
                continue
            if dfs(w, 0):
                ans.append(w)
            else:
                d[L].append(w)
        return ans

    def findAllConcatenatedWordsInADict4(self, words: List[str]) -> List[str]:
        # 虽然题目保证了不重复，使用set并不会减少数据量；但在判断某个字符是否存在时，使用set效率明显高于list
        d = defaultdict(set)

        def dfs(word, index):
            if len(word) == index:
                return True
            # 只需要考虑已有单词长度，必须先排除空字符串（即长度为0 的情况），避免死循环
            for l in d.keys():
                # 此处判断使用set效率更高
                if word[index: index + l] in d[l]:
                    if dfs(word, index + l):
                        return True
            return False

        ans = []
        filter(lambda x: len(x) != 0, words)
        for w in sorted(words, key=len):
            L = len(w)
            # 空字符串一定不能满足由两个子字符串组合而成
            # 不存在重复字符串，也就不存在 空字符串 + 相等字符串 = 相等字符串 的情况
            if L == 0:
                continue
            if dfs(w, 0):
                ans.append(w)
            else:
                d[L].add(w)
        return ans

    def findAllConcatenatedWordsInADict2(self, words: List[str]) -> List[str]:
        @cache
        def check(w, p): return (p and w[p:] in book) or p == len(w) or any(
            w[p: i + 1] in book and check(w, i + 1) for i in range(p, len(w) - 1))

        book = set(words)
        return [w for w in words if w and check(w, 0)]

    def findAllConcatenatedWordsInADict3(self, words: List[str]) -> List[str]:
        book, res = set(), []

        def check(w, p):
            if len(w) == p:
                return True
            for i in range(p, len(w)):
                if w[p: i + 1] in book and check(w, i + 1):
                    return True
            return False

        for w in sorted(words, key=len):
            if w and check(w, 0):
                res.append(w)
            else:
                book.add(w)
        return res


Trie, END = lambda : defaultdict(Trie), '#'
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words: reduce(dict.__getitem__, word, trie)[END] = None
        @cache
        def check(w, p = 0):
            t = trie
            for i in range(p, len(w)):
                if w[i] not in t:
                    return False
                # := PY3.8新增语法：在表达式内部为变量赋值
                # if END in (t := t[w[i]]) and i + 1 < len(w) and check(w, i + 1):
                t = t[w[i]]
                if END in t and i + 1 < len(w) and check(w, i + 1):
                    return True
            return p != 0 and END in t
        return [w for w in words if check(w)]


# 140. 单词拆分 II
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        ans = list()

        # FIXME 索引判断
        def dfs(index, arr: List[str]):
            if index == len(s):
                ans.append(" ".join(arr))
                return
            for i in range(index, len(s)):
                if s[index: i + 1] in wordSet:
                    arr.append(s[index:i + 1])
                    dfs(i + 1, arr)
                    arr.pop()

        dfs(0, list())
        return ans

    # 效率非常高，近似使用缓存
    def wordBreak3(self, s: str, wordDict: List[str]) -> List[str]:
        d = defaultdict(set)
        # wordDict中不包含重复字符串，且不包含空字符串
        for w in wordDict:
            d[len(w)].add(w)

        ans = list()

        def dfs(index, arr: List[str]):
            if index == len(s):
                ans.add(" ".join(arr))
                return
            for l in d.keys():
                if s[index: index + l] in d[l]:
                    arr.append(s[index:index + l])
                    dfs(index + l, arr)
                    arr.pop()

        dfs(0, list())
        return ans

    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def backtrack(index: int) -> List[List[str]]:
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans

        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]


if __name__ == '__main__':
    sol = Solution1()
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    # sol.findAllConcatenatedWordsInADict(words)
