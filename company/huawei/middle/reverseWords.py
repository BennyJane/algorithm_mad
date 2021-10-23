from typing import List


# 186. 翻转字符串里的单词 II
class Solution:
    # 栈结构
    # 嵌套数组
    def reverseWords2(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = []
        n = len(s)
        start = 0
        while start < n:
            temp = []
            while start < n and s[start] != " ":
                temp.append(s[start])
                start += 1
            res.append(temp)
        ans = []
        for t in res[::-1]:
            ans.extend(t)
            ans.append(" ")
        # TODO 必须修改s变量，此处为浅拷贝，不能直接重新赋值s=ans（ans需要先ans.pop()）
        for i in range(n):
            s[i] = ans[i]

    def reverseWords1(self, s: List[str]) -> None:
        # 先拼合单词，再切割为序列，最后逆序
        arr = "".join(s).split(" ")[::-1]
        # 重新添加空格
        res = " ".join(arr)
        for i, c in enumerate(res):
            s[i] = c


# TODO 进阶：使用 O(1) 额外空间复杂度的原地解法。
# 核心思路：定义区间反转函数，而不是单点交换函数
class Solution1:
    # 方法1： 第一次反转整个数组，后续，逐个反转每个单词 ==》 也可以：先反转单个单词，然后再反转整个数组
    def reverseWords(self, s: List[str]) -> None:
        n = len(s)
        self.swapArr(s, 0, n - 1)

        left = 0
        for i in range(n):
            cur = s[i]
            if cur == " ":
                self.swapArr(s, left, i - 1)
                left = i + 1
        # 需要反转最后一个单词
        self.swapArr(s, left, n - 1)

    def swapArr(self, arr: List[str], start: int, end: int):
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1


class Solution3:
    # TODO ~num 按位取反，计算补码
    # 折半交换；末尾单独处理
    def reverseWords(self, s: List[str]) -> None:
        k = len(s)
        half = k // 2
        # 实现整体反转的算法
        for i in range(half):
            s[i], s[~i] = s[~i], s[i]

        slow = 0
        for f in range(k):
            if s[f] == ' ':
                s[slow:f] = s[slow:f][::-1]
                slow = f + 1
        s[slow:f + 1] = s[slow:f + 1][::-1]


if __name__ == '__main__':
    print(1, ~1)
    print(0, ~0)
    print(2, ~2)
