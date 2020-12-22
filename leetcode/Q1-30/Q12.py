# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : algorithm_mad
# Time       ：2020/12/21 23:25
# Warning    ：The Hard Way Is Easier


# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符
# 串。如果答案不存在，则返回空字符串。
#
#  示例 1:
#
#
# 输入:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# 输出:
# "apple"
#
#
#  示例 2:
#
#
# 输入:
# s = "abpcplea", d = ["a","b","c"]
#
# 输出:
# "a"
#
#
#  说明:
#
#
#  所有输入的字符串只包含小写字母。
#  字典的大小不会超过 1000。
#  所有输入的字符串长度不会超过 1000。
#
#  Related Topics 排序 双指针

"""
1. 题目中字典的条件：指的是同长度，比较字母大小排序
2. 给定字符串删除部分后，可以变化为目标字符串
    ==》 判断条件：字符串长度相同； 顺序一致； 相同字符的个数相同
    ==》 错误：只判断目标字符串单个字符是否在s中，没有判断数量已经位置？
"""

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ""
        for word in d:
            left = 0
            for w in word:
                while left < len(s):
                    if w == s[left]:  # 找到相同字符，跳出循环
                        left += 1
                        break
                    left += 1
                else:
                    # 运行else部分，表示没有匹配到相应的字符串
                    # 如果遍历s的过程中，完全没有找到等于w的字符，则直接退出
                    break
            else:
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):  # 长度相等，取字符串比较中较小的
                    if word < res:
                        res = word
        return res

    def second(self, s: str, d: List[str]) -> str:
        """运行速度不如上面"""
        res = ""
        for word in d:
            l = r = 0
            while l < len(s) and r < len(word):
                if s[l] == word[r]:
                    l += 1
                    r += 1
                else:
                    l += 1
            if r == len(word):  # word 完全匹配
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):  # 长度相等，取字符串比较中较小的
                    if word < res:
                        res = word
        return res

    # https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/solution/524-tong-guo-shan-chu-zi-mu-pi-pei-dao-zi-dian-li-/
    def third(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))

        def _match(word):
            i = 0
            for w in word:
                k = s.find(w, i)  # 匹配到会返回字符索引
                if k == -1:  # 没有匹配到
                    return False
                i = k + 1
            return True

        for c in d:
            if _match(c):  # 验证成功
                return c
        return ""

    def fourth(self, s: str, d: List[str]) -> str:
        """优化代码"""
        d.sort(key=lambda x: (-len(x), x))

        def f(word):
            i = 0
            for w in word:
                k = s.find(w, i)
                if k == -1:
                    return False  # 只要发现未匹配字符， 立即返回
                i = k + 1
            return True

        gen = (c for c in d if f(c))  # 生成器表达式
        return next(gen, "")  # 设置了默认返回值

    def fifth(self, s: str, d: List[str]) -> str:
        def f(word):
            i = 0
            for w in word:
                k = s.find(w, i)
                if k == -1:
                    return False
                i = k + 1
            return True

        gen = filter(f, sorted(d, key=lambda x: (-len(x), x)))
        return next(gen, "")

# leetcode submit region end(Prohibit modification and deletion)
