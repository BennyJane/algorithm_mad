from typing import List
from sortedcontainers import SortedList
from math import ceil


# 5920. 分配给商店的最多商品的最小值
class Solution:
    # 二分法：左右端点修改是基于中点
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        # TODO 二分区间：1~商品数量最大值， 两个端点都可以取到
        # 因为商品数量 <= 商店数量，一定可以实现每个商品全部放到一个商店的情况
        left = 1  # FIXME 不能取0：作为除数；不符合实际题目
        right = max(quantities)
        while left < right:  #
            mid = (right + left) // 2  # 计算中点：偏左侧； (right + left) // 2 +1 偏右侧
            # 验证分组(实际需要商店)数量
            count = 0
            for i in range(m):
                # 向上取整 from math import ceil
                # count += quantities[i] // mid if quantities[i] % mid == 0 else quantities[i] // mid +1
                count += ceil(quantities[i] / mid)
            if count <= n:
                right = mid
            else:  # 取值偏小，应该增大
                left = mid + 1
        return left

    # 二分法查找: 超时
    def minimizedMaximum2(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        if m == n:  # 当商品数量与商店数量一致，不存在多于商店进行拆分，直接取最大值
            return max(quantities)
        # 有序数组，默认为升序
        array = SortedList(quantities)
        left = ceil(sum(quantities) / n)
        right = array[-1]
        while left < right:
            mid = (right + left) // 2
            count = 0
            index = array.bisect_right(mid)
            if index < n:
                count += index
                for i in range(index, m):
                    # cur = quantities[i]
                    # count += cur // mid if cur % mid == 0 else cur // mid + 1
                    count += ceil(array[i] / mid)
            if count <= n:
                right = mid
                # right -= 1    # FIXME 二分法，不是增减1
            else:
                left = mid + 1

        return left

    # TODO 验证通过120+例子
    def minimizedMaximum1(self, n: int, quantities: List[int]) -> int:
        # m <= n
        m = len(quantities)
        if m == n:
            return max(quantities)

        total = sum(quantities)
        target = total // n if total % n == 0 else total // n + 1

        # 记录余数与分配的商店数量
        res = list()
        count = 0  # 分配商店数量
        # 升序排列
        quantities.sort()
        for i, val in enumerate(quantities):
            if val <= target:
                count += 1
            else:
                # 所需要的商店数量
                temp = val // target
                count += temp
                if val % target != 0:
                    res.append((val % target, temp))

        if count + len(res) <= n:
            return target

        res.sort(key=lambda x: x[0] / x[1])
        diff = count + len(res) - n
        if diff < len(res):
            x, y = res[diff - 1]
            up = x // y if x % y == 0 else x // y + 1
        else:
            pass
        return target + up


if __name__ == '__main__':
    sol = Solution()
    # n = 22
    # nums = [25, 11, 29, 6, 24, 4, 29, 18, 6, 13, 25, 30]

    # n = 15
    # nums = [16, 24, 18, 26, 18, 28, 11, 8, 22, 26, 21, 23]

    n = 22
    nums = [25, 11, 29, 6, 24, 4, 29, 18, 6, 13, 25, 30]

    # sol.minimizedMaximum(n, nums)
    sol.minimizedMaximum2(n, nums)

    print((3 + 0) // 2)
    print((3 + 0) // 2 + 1)
    print((3 - 0) // 2 + 0 + 1)
    print((2 - 0) // 2 + 0 + 1)
    print((1 - 0) // 2 + 0 + 1)
