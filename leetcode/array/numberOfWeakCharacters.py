from typing import List


# 1996. 游戏中弱角色的数量
# https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/
class Solution1:
    # 暴力求解：嵌套遍历,超时
    """
    图形化展示：寻找完全位于另一个矩形内部的小的矩形， 利用矩形前缀和，判断矩形内是否存在其他点？


    """

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], -x[1]))
        ans = max_defense = i = 0
        n = len(properties)
        while i < n:
            j, cur_max, max_defense = i, max_defense, max(max_defense, properties[i][1])
            while j < n and properties[j][0] == properties[i][0]:
                if cur_max > properties[j][1]:
                    ans += 1
                j += 1
            i = j
        return ans

    # TODO 特别处理：第一个维度相等的情况
    # 任选一个维度，降序排列，另一个维度在前一个维度相等时，升序排列，
    # 从最大值往后遍历(可以从第二个位置往后遍历)，
    # 对于当前位置来说，左侧一定存在在该维度上大于等于自己的对象，只要前面存在另一个维度也大于自己对象，
    # 那么当前位置，必然是弱对象； 因此，遍历过程中，只需要保留另一个维度的最大值。
    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        # 任选一个维度降序排列 FIXME 当前维度相等时，按照另一个维度升序排列
        properties.sort(key=lambda x: (-x[0], x[1]))
        # 另一个维度的最大值
        yMax = properties[0][1]
        n = len(properties)
        ans = 0
        for i in range(1, n):
            y = properties[i][1]
            # 当 yMax 大于 y 时，yMax对应的x维度的值，一定与当前索引处的x值不等。
            # 按照排序规则，x值等于当前索引的位置，对应的y值均小于等于当前位置的y
            if yMax > y:
                ans += 1
            else:
                # 当更新y值时，本应该同时更新x维度的值
                yMax = y
        return ans

    # 只针对一个维度,进行排序
    def numberOfWeakCharacters3(self, properties: List[List[int]]) -> int:
        # 任选一个维度降序排列
        properties.sort(key=lambda x: -x[0])

        y_max = properties[0][1]
        n = len(properties)
        ans = 0

        left = 0
        while left + 1 < n:
            # 比较当前值与下一个值的关系
            if properties[left + 1][0] == properties[left][0]:
                # 处理连续相等的情况
                y_max = max(y_max, properties[left + 1][1])
            else:
                if y_max > properties[left + 1][1]:
                    ans += 1
                y_max = max(y_max, properties[left + 1][1])
            left += 1
        return ans
