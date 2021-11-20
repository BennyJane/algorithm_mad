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
        ans = []
        for i in range(n):
            temp = s[i] + self.permutation(s[:i]) + self.permutation(s[i:])
        return list(ans)


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
