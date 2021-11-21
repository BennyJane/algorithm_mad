import itertools
from functools import lru_cache
from itertools import product
from typing import List
import sys


# 554. 砖墙
# MIDDLE 哈希表 + 前缀和 + 统计
class Solution:
    """
    计算每行缝隙的位置
    统计所有行不同缝隙位置的数量 ==》 哈希表
    找到出现次数最多的缝隙位置，进行划线

    结果 = 总行数 - 相同缝隙位置数量(最大值)

    # 当 Java 发生溢出时，会直接转成负数来处理，对本题没有影响
    """

    def leastBricks(self, wall: List[List[int]]) -> int:
        return 0


# 475. 供暖器
# https://leetcode-cn.com/problems/heaters/
class Solution1:
    """
    遍历所有房间，从每个房间考虑，最接近的两个供暖器中所需半径中的较小值


    MIDDLE: 排序 双指针 贪心 二分法
    https://leetcode-cn.com/problems/heaters/solution/er-fen-suan-fa-ti-xing-2-by-tunsuy-ytt6/
    https://leetcode-cn.com/problems/heaters/solution/shuang-zhi-zhen-by-huichuan-lz51/
    """

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        return 0


# 1109. 航班预订统计
# MIDDLE 差分 前缀和
# 暴力 + TODO 理解差分法
class Solution3:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        for left, right, inc in bookings:
            nums[left - 1] += inc
            if right < n:
                nums[right] -= inc

        for i in range(1, n):
            nums[i] += nums[i - 1]

        return nums


# 547. 省份数量 ==》 323. 无向图中连通分量的数目 ==》 200. 岛屿数量
# https://leetcode-cn.com/problems/number-of-provinces/
# 并查集
class Solution4:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        return 0


# 剑指 Offer 38. 字符串的排列
# https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/
class Solution5:
    """
    字符串全排列
    """

    def permutation(self, s: str) -> List[str]:
        n = len(s)
        visited = [False] * n
        # FIXME 去重
        ans = set()

        def dfs(count, child: str):
            if count >= n:
                ans.add(child)
                return
            for i in range(n):
                if visited[i]:
                    continue
                visited[i] = True
                dfs(count + 1, child + s[i])
                visited[i] = False

        dfs(0, "")
        return list(ans)

    # 递归法：不使用回溯
    def permutation1(self, s: str) -> List[str]:
        if len(s) <= 1:
            return [s]
        ans = set()
        for i in range(len(s)):
            for perm in self.permutation(s[:i] + s[i + 1:]):
                ans.add(s[i] + perm)
        return list(ans)
        # return list(set(s[i] + perm for i in range(len(s)) for perm in self.permutation(s[:i] + s[i + 1:])))

    # 下一个更大值
    def permutation2(self, s: str) -> List[str]:
        ans = list()
        n = len(s)
        char_list = list(s)

        # 确定字典序最小的排列方式
        char_list.sort()
        ans.append("".join(char_list))

        def reversePart(arr: List[str], start):
            left = start
            right = n - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        # 找到下一个字典序更大的排列组合
        def nextPermutation(arr: str):
            # FIXME python传入数组，字典等对象后，修改其内容，会影响外部传入的原始参数的值 ==》 JAVA相似
            # 从右侧开始遍历，找到第一个小于右侧相邻字符的索引位置
            left = n - 2
            while left >= 0 and arr[left] >= arr[left + 1]:
                left -= 1
            if left < 0:  # 不存在
                return False
            # 从右侧开始遍历，找到第一个大于上面确定位置的数值
            right = n - 1
            while right >= 0 and arr[left] >= arr[right]:
                right -= 1
            # 交换上面找到的两个位置的字符
            arr[left], arr[right] = arr[right], arr[left]
            # left索引后字符串，需要逆向排序，降低整个字符的大小
            reversePart(arr, left + 1)
            return True

        while nextPermutation(char_list):
            ans.append("".join(char_list))

        return ans

    # python 内置函数
    def permutation3(self, s: str) -> List[str]:
        return list(set(''.join(st) for st in itertools.permutations(s)))

    def permutation4(self, s: str) -> List[str]:
        n = len(s)
        curr = list(sorted(s))
        end = list(reversed(curr))
        ans = []
        # 生成下一个排列
        while curr != end:
            ans.append(''.join(curr))
            i = n - 2
            # 29631 -> 31269
            while i > 0 and curr[i] >= curr[i + 1]:
                i -= 1
            j = n - 1
            while j > i - 1 and curr[j] <= curr[i]:
                j -= 1
            curr[i], curr[j] = curr[j], curr[i]
            curr = curr[:i + 1] + sorted(curr[i + 1:])
        ans.append(''.join(end))
        return ans


# 面试题 01.07. 旋转矩阵
# https://leetcode-cn.com/problems/rotate-matrix-lcci/
# 不占用额外内存空间能否做到？
class Solution6:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


if __name__ == '__main__':
    sol = Solution5()
    sol.permutation("abc")
