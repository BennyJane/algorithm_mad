import itertools
from typing import List


# 616. 给字符串添加加粗标签
# https://leetcode-cn.com/problems/add-bold-tag-in-string/
class Solution:
    # S: 字典树、动态规划
    # G: 字典树、数组、哈希表、字符串、字符串匹配

    # TODO 长度为1000，考虑暴力求解
    # TODO 仿照合并区间的思路
    def addBoldTag(self, s: str, words: List[str]) -> str:
        if not words:
            return s

        # 记录重点字符的索引范围
        stack = []

        n = len(s)
        for i in range(n):
            for j in range(n, i, -1):
                prefix = s[i:j]
                if prefix in words:
                    temp = [i, j]
                    if stack:
                        pre = stack.pop()
                        pre, temp = self.merge(pre, temp)
                        if temp is None:
                            stack.append(pre)
                        else:
                            stack.append(pre)
                            stack.append(temp)
                    else:
                        stack.append(temp)
        ans = ""
        left = 0
        for pos in stack:
            x, y = pos
            ans += s[left:x]
            ans += "<b>{}</b>".format(s[x:y])
            left = y
        ans += s[left: n]
        return ans

    def merge(self, pre, cur):
        if pre[1] < cur[0]:
            return pre, cur
        arr = [min(pre[0], cur[0]), max(pre[1], cur[1])]
        return arr, None


# FIXME 减少额外空间的使用
class Solution1(object):
    def boldWords(self, S, words):
        N = len(S)
        mask = [False] * N
        # 标注所有重点索引位置
        for i in range(N):
            prefix = S[i:]
            for word in words:
                if prefix.startswith(word):
                    for j in range(i, min(i + len(word), N)):
                        mask[j] = True

        ans = []
        for incl, grp in itertools.groupby(zip(S, mask), lambda z: z[1]):
            if incl:
                ans.append("<b>")
            ans.append("".join(z[0] for z in grp))
            if incl:
                ans.append("</b>")
        return "".join(ans)


if __name__ == '__main__':
    sol = Solution()
    s = "aaabbcc"
    words = ["aaa", "aab", "bc"]
    sol.addBoldTag(s, words)
