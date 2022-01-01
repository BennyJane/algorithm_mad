from typing import List
from collections import defaultdict


# 1248. 统计「优美子数组」
class Solution1:
    """
    Template: 统计满足数量条件子数组的个数
    """

    def numberOfSubarrays4(self, nums: List[int], k: int) -> int:
        # 记录某个数量出现的次数
        d = defaultdict(int)
        # 0出现次数为1
        d[0] = 1

        pre = ans = 0
        for c in nums:
            # 先统计当前奇数个数
            if c & 1 == 1:
                pre += 1
                d[pre] += 1
            else:
                d[pre] += 1
            # 计算满足K个奇数的连续子数组的数量
            if pre - k in d.keys():
                ans += d[pre - k]
        return ans

    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        # 使用数组记录奇数的前缀和
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num % 2 == 1:
                odd += 1
            if odd >= k:
                ans += cnt[odd - k]
            cnt[odd] += 1
        return ans

    # 数学 + 滑动窗口
    def numberOfSubarrays3(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # 只统计奇数索引位置
        odd = [-1]
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)

        # 使用滑动窗口，维持奇数个数为K
        oddL = len(odd)
        # 初始化边界索引与窗口属性
        l = r = 1
        ans = 0
        win = 0
        while r < oddL - 1:
            win += 1
            # 窗口超出条件：移动左边界
            while win > k:
                win -= 1
                l += 1
            # 窗口满足条件
            if win == k:
                # 左右端点奇数外部长度 的乘积
                ans += (odd[i] - odd[i - 1]) * (odd[r + 1] - odd[r])
            # 移动右边界
            r += 1

        return ans

    def numberOfSubarrays2(self, nums: List[int], k: int) -> int:
        odd = [-1]
        for i, c in enumerate(nums):
            if c & 1 == 1:
                odd.append(i)
        odd.append(len(nums))

        n = len(odd)
        ans = 0
        for i in range(1, n):
            if i + k < n:
                ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans


class ProductOfNumbers:
    """
     最后 K 个数的乘积

    题目不会查询历史数据：只需要保留最后K个元素即可；
    在add时并不知道K的值，而且整个查询过程中K值不断变化，
    所以无法在add时直接删除多余元素
    """

    def __init__(self):
        self.cache = list()
        self.pre = [1]
        self.size = 0

    def add(self, num: int) -> None:
        self.cache.append(num)
        # FIXME 处理出现的0值
        if self.pre[-1] == 0:
            # 前面有0，重新计算
            self.pre.append(num)
        else:
            self.pre.append(self.pre[-1] * num)
        self.size += 1

    def getProduct(self, k: int) -> int:
        arr = self.cache[self.size - k:]
        # 判断最后K的元素中，是否有0
        if 0 in set(arr):
            return 0
        dev = self.pre[-1 * k - 1]
        # 判断最后k+1的元素是否为0
        if dev == 0:
            return self.pre[-1]
        return self.pre[-1] // dev


class ProductOfNumbers1:

    def __init__(self):
        self.pre = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.pre = [1]
            self.size = 0
        else:
            self.pre.append(self.pre[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if self.size >= k:
            return self.pre[-1] // self.pre[- k - 1]
        else:
            return 0


class ProductOfNumbers2:
    """
    题目数据保证：任何时候，任一连续数字序列的乘积都在 32-bit 整数范围内，
    不会溢出，这其实告诉了我们如果只乘大于 11 的数话，
    数字序列长度最多不会超过 3232，
    因为大于 11 最小的数 22 的连着 3232 个乘起来已经达到题目乘积的上界，所以我们只需要忽略 00 和 11，在查询的时候暴力乘复杂度就能得到保证。
    """

    def __init__(self):
        # FIXME 还是需要使用前缀积来优化
        self.cache = []
        # 统计每个索引处，0出现的数量
        self.cnt = [0]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.cnt.append(self.cnt[-1] + 1)
        else:
            self.cnt.append(self.cnt[-1])
        self.cache.append(num)
        self.size += 1

    # FIXME 超时
    def getProduct(self, k: int) -> int:
        # 先判断是否存在0
        if self.cnt[-1] - self.cnt[-k - 1] > 0:
            return 0
        ans = 1
        for i in range(k):
            ans *= self.cache[self.size - 1 - i]
        return ans


# 1371. 每个元音包含偶数次的最长子字符串
class Solution3:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        dp = [[True for _ in range(5)] for _ in range(n + 1)]

        return 0

    # FIXME 超时
    def findTheLongestSubstring2(self, s: str) -> int:
        n = len(s)
        d = {
            "a": 0,
            "e": 1,
            "i": 2,
            "o": 3,
            "u": 4
        }

        ans = 0
        for i in range(n):
            array = [True for _ in range(5)]
            for j in range(i, n):
                c = s[j]
                if c in d.keys():
                    index = d[c]
                    array[index] = not array[index]
                if all(array):
                    ans = max(ans, j - i + 1)
        return ans

    def findTheLongestSubstring3(self, s: str) -> int:
        d = {
            "a": 0,
            "e": 1,
            "i": 2,
            "o": 3,
            "u": 4
        }

        ans = 0
        # 状态压缩：5个元音字符状态(奇、偶)的排列组合
        status = [-1 for _ in range(1 << 5)]
        status[0] = 0

        curStatus = 0
        for i, c in enumerate(s):
            if c in d.keys():
                curStatus ^= (1 << d[c])
            if status[curStatus] >= 0:
                ans = max(ans, i + 1 - status[curStatus])
            else:
                status[curStatus] = i + 1

        return ans
