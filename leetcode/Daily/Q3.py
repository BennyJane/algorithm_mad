from collections import Counter
from itertools import permutations


# 5878. 重复 K 次的最长子序列
# https://leetcode-cn.com/problems/longest-subsequence-repeated-k-times/
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # 统计词频
        num = Counter(s)
        # sorted: 排序， 按照字母降序排列
        # 统计满足重复k次的子序列包含的单词，并合并为字符串hot
        # 出现次数非常多的单词，可能会在hot中出现多次
        hot = ''.join(ele * (num[ele] // k) for ele in sorted(num, reverse=True))
        # 子序列最大长度为hot的长度
        for i in range(len(hot), 0, -1):
            # 罗列子序列所有排列方式
            for item in permutations(hot, i):
                word = ''.join(item)
                # TODO 转迭代器，不重复遍历
                ss = iter(s)
                if all(c in ss for c in word * k):
                    return word
        return ''


class Solution2:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        return ""


if __name__ == '__main__':
    sol = Solution()
    sol.longestSubsequenceRepeatedK("letsleetcode", 2)
