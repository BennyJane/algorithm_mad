from typing import List
from functools import lru_cache

"""
包含题目：
638. 大礼包

"""


# 638. 大礼包
# https://leetcode-cn.com/problems/shopping-offers/
# 位运算、记忆化搜索 数组 动态规划 回溯 状态压缩
class Solution638:

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)  # 大礼包前n个数为商品数量，最后一位是总价格(优惠后)

        # 过滤不需要计算的大礼包，只需要保留需要计算的大礼包
        filter_special = []
        for sp in special:
            # 筛选条件：购物清单（商品数量不会空）不能为空；最后价格需要小于单独购买价格
            total = sum(sp[i] * price[i] for i in range(n))
            # 最后一位不是商品数量
            if sum(sp[:n]) > 0 and total > sp[-1]:
                filter_special.append(sp)

        # TODO 使用闭包函数，避免参数传递(price, special)
        @lru_cache(None)  # 记忆化搜索提高效率
        def dfs(cur_needs):
            # 不购买大礼包，原价购买的价格
            min_prices = sum(need * price[i] for i, need in enumerate(cur_needs))
            # 逐个讨论大礼包是否可以购买
            for cur_special in filter_special:
                special_price = cur_special[-1]
                next_needs = []
                for i in range(n):
                    # 大礼包商品数量必须小于当前需求状态
                    if cur_special[i] > cur_needs[i]:
                        break
                    next_needs.append(cur_needs[i] - cur_special[i])
                # else:  # 没有正常遍历完的情况，即该礼包不可购买
                #     continue
                if len(next_needs) == n:
                    min_prices = min(min_prices, dfs(tuple(next_needs)) + special_price)
            return min_prices

        return dfs(tuple(needs))


# 最初版本(自己实现)
class Solution638_1:
    ans = None
    ori_price = None
    ori_special = None

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        # 单独购买的总价
        total = sum(need * price[i] for i, need in enumerate(needs))
        self.ans = total

        self.ori_price = price
        self.ori_special = []
        for sp in special:
            if sum(sp[:n]) > 0 and sum([p * s for p, s in zip(price, sp[:n])]) > sp[-1]:
                self.ori_special.append(sp)

        self.dfs(needs, 0)

        return self.ans

    def dfs(self, cur_needs: List[int], cost):
        if self.isEnd(cur_needs):
            self.ans = min(self.ans, cost)
            return
        # 剪枝
        if cost >= self.ans:
            return

        n = len(self.ori_price)
        # TODO 每次递归：只需要考虑两种情况，要么使用一个礼包，要么不使用礼包
        # 优先考虑使用其中一个大礼包的情况
        for sp in self.ori_special:
            # 先判断是否可以购买
            for i in range(n):
                if sp[i] > cur_needs[i]:
                    break
            else:  # 确保礼包中商品数量均小于当前需求状态中的值
                next_needs = [cur_needs[i] - sp[i] for i in range(n)]
                # 在调用函数时，处理cost，不影响当前作用域中的cost
                self.dfs(next_needs, cost + sp[-1])
        # 考虑不适用礼包的情况
        cur_total = sum(cur_needs[i] * self.ori_price[i] for i in range(n))
        self.ans = min(self.ans, cur_total + cost)

    def isEnd(self, cur_needs: List[int]) -> bool:
        """检测商品是否已经全部购买"""
        for c in cur_needs:
            if c != 0:
                return False
        return True


class Solution39:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return []


if __name__ == '__main__':
    nums = [1, 23, 4, 5, 6, 4, 3, 2]
    for m, n in zip(nums, nums):
        print(m, n)
