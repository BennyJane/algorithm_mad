import math
from typing import List
from bisect import bisect_left, bisect
from collections import defaultdict
from sortedcontainers import SortedList
from math import lcm

# 剑指 Offer II 006. 排序数组中两个数字之和
from leetcode.utils import TreeNode


class Solution1:
    # 确定一个数以后，再使用二分法查找另一个数
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        index = n - 1
        while index > 0:
            if numbers[index] + numbers[0] > target:
                index -= 1
                continue
            retain = target - numbers[index]
            left, right = 0, index - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == retain:
                    return [mid, right]
                elif numbers[mid] < retain:
                    left = mid + 1
                else:
                    right = mid - 1
            index -= 1
        return []

    # 直接使用二分法查找两个值
    # 双指针 + 二分法
    def twoSum_simple(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left, right]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1

    # 超时
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            res = target - num
            if res in numbers[i + 1:]:
                # 注意索引重新计算
                return [i, numbers[i + 1:].index(res) + i + 1]

    #
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            res = target - num
            # 必须重新生成数组，bisect_left 需要操作有序数组
            index = bisect_left(numbers[i + 1:], res)
            # 可以取到1
            if 0 <= index < len(numbers) - i - 1:
                if numbers[index + i + 1] == res:
                    return [i, index + i + 1]
        return []


# 1099. 小于 K 的两数之和
class Solution2:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        from sortedcontainers import SortedList
        array = SortedList(nums)

        ans = -1
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if array[i] >= k or array[i] + array[0] >= k:
                continue
            res = k - array[i]
            if res < 0:  # 题目要求最下值 >= 1
                continue
            # 查找
            left = array.bisect_left(res)
            if 0 < left - 1 < n and left - 1 != i:
                ans = max(ans, array[i] + array[left - 1])
        return ans

    def twoSumLessThanK1(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        nums.sort()
        l, r = 0, n - 1
        ans = float("-inf")
        while l < r:
            if nums[l] + nums[r] >= k:
                r -= 1
            else:
                ans = max(ans, nums[l] + nums[r])
                l += 1

        return ans if ans != float("-inf") else ans

    # 暴力求解
    def twoSumLessThanK2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float("-inf")
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < k:
                    ans = max(nums[i] + nums[j], ans)
        return -1 if ans == float("-inf") else ans


# 1. 两数之和
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pass


# 167. 两数之和 II - 输入有序数组
class Solution4:
    # 数据不重复，答案唯一

    # 使用map记录已访问数据的索引
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        for i, v in enumerate(numbers):
            res = target - v
            if res in d:
                return [d[res] + 1, i + 1]
            else:
                d[v] = i

    # 二分法
    # 固定一个位置，寻找另一个数字
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            low, high = i + 1, n - 1
            while low <= high:
                mid = (low + high) // 2
                if numbers[mid] == target - numbers[i]:
                    return [i + 1, mid + 1]
                elif numbers[mid] > target - numbers[i]:
                    high = mid - 1
                else:
                    low = mid + 1

        return [-1, -1]

    # 双指针
    def twoSum3(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left, right]
            elif s > target:
                right -= 1
            else:
                left += 1
        return 0


# 170. 两数之和 III - 数据结构设计
class TwoSum:
    """
    设计一个接收整数流的数据结构，该数据结构支持检查是否存在两数之和等于特定值。

    实现 TwoSum 类：

    TwoSum() 使用空数组初始化 TwoSum 对象
    void add(int number) 向数据结构添加一个数 number
    boolean find(int value) 寻找数据结构中是否存在一对整数，使得两数之和与给定的值相等。如果存在，返回 true ；否则，返回 false 。
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_counts = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.num_counts.keys():
            comple = value - num
            if num != comple:
                if comple in self.num_counts:
                    return True
            elif self.num_counts[num] > 1:
                return True

        return False


# 653. 两数之和 IV - 输入 BST 树结构
class Solution5:
    # map | HashSet 记录已访问节点，一边遍历一边判断
    def findTarget(self, root: TreeNode, k: int) -> bool:
        return True
    # 广度优先搜索： 使用队列逐层遍历树节点，使用HashSet记录已经访问节点值
    # 中序遍历(树 =》 有序数组)，再结合二分搜索


# 259. 较小的三数之和
class Solution20:
    """
    给定一个长度为 n 的整数数组和一个目标值 target，
    寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。
    """

    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        if n == 0:
            return ans

        for i in range(n - 2):
            first = nums[i]
            # FIXME 优化，快速计算重复数字对应的重复结果
            if nums[i + 1] + nums[i + 2] + first >= target:
                break
            for j in range(i + 1, n - 1):
                second = nums[j]
                if nums[j + 1] + second + first >= target:
                    break
                left, right = j + 1, n - 1
                res = target - first - second
                while left < right:
                    # FIXME ?? 中间点的计算规则总结
                    mid = (left + right) // 2 + 1
                    if nums[mid] < res:
                        left = mid
                    else:
                        right = mid - 1
                ans += (left - j)
        return ans

    # 先固定一个变量，使用归并排序的框架
    # 同理： 1099.小于K的两数之和
    def threeSumSmaller2(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = 0

        def func(left, T):
            cnt = 0
            right = n - 1
            while left < right:
                # 两个端点范围内的数据全部满足条件： 左端点不变，右端点切换
                if nums[left] + nums[right] < T:
                    cnt += right - left
                    left += 1
                else:
                    right -= 1
            return cnt

        for i in range(n - 2):
            ans += func(i + 1, target - nums[i])
        return ans


# 713. 乘积小于K的子数组
class Solution21:
    # 统计数量； 前缀和思想
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 0:
            return 0
        n = len(nums)
        pre = [1]
        for i in range(n):
            pre.append(pre[i] * nums[i])
        ans = 0
        for i in range(1, n + 1):
            if nums[i] >= k:
                continue
            l, r = 0, i
            while l <= r:
                # FIXME 乘积过大，转float类型，两种类型计算除法会报错
                cur = pre[r] // pre[l]
                if cur < k:
                    ans += r - l
                    break
                else:
                    l += 1
        return ans

    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        ans = 0
        for i in range(n):
            if nums[i] >= k:
                continue
            res = nums[i]
            cnt = 1
            for j in range(i + 1, n):
                if res * nums[j] < k:
                    res *= nums[j]
                    cnt += 1
            ans += cnt
        return ans

    # 滑动窗口： 维护乘积小于k的左右端点
    def numSubarrayProductLessThanK3(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        pre = 1
        ans = 0
        left = right = 0
        while right < len(nums):
            pre *= nums[right]
            while pre >= k:
                pre /= nums[left]
                left += 1
            # 统计窗口内满足条件的连续子数组数量
            ans += (right - left + 1)
            right += 1
        return ans

    # 二分查找：固定一个端点，二分查找最大的右端点满足: 左右端点范围的数据乘积 < k
    # TODO 乘积数字非常大，使用取对数的方法，将乘法转化为加法
    def numSubarrayProductLessThanK4(self, nums: List[int], k: int) -> int:
        if k <= 0: return 0
        k = math.log(k)

        # 前缀乘积序列： 一定是升序数组
        pre = [0]
        for n in nums:
            pre.append(pre[-1] + math.log(n))

        ans = 0
        for i, x in enumerate(pre):
            # FIXME bisect 就是 bisect_right 查找满足条件的最右侧索引
            j = bisect(pre, x + k - 1e-9, i + 1)
            ans += j - i - 1
        return ans



# 560.和为K的子数组 TODO 错误多次
class Solution22:
    # 取值范围：有正有负; 子数组连续

    # 暴力方法：计算所有连续子数组的情况
    # FIXME 超时
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1] + num)

        ans = 0
        n = len(nums)
        for i in range(1, n + 1):
            for j in range(i):
                if pre[i] - pre[j] == k:
                    ans += 1
        return ans

    # TODO 前缀和 + 哈希表优化
    # pre[i] - pre[j] = k ==> pre[j] = pre[i] - k ,统计前缀和pre[j]的数量
    def subarraySum2(self, nums: List[int], k: int) -> int:
        ans, pre = 0, 0
        d = defaultdict(int)
        d[0] = 1
        for num in nums:
            pre += num
            if pre - k in d.keys():
                ans += d[pre - k]
            d[pre] += 1
        return ans


# 523. 连续的子数组和 TODO 错误
class Solution23:
    # 连续子数组； 和为k的整数倍[0:]
    # 不能排序，需要保证原数组顺序

    # TODO 核心思路： 转化为当前前缀和与已访问前缀和的关系

    # 560.参考和为k的子数组
    # pre % k = x --》 x * k = pre
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(n):
            preSum[i + 1] = nums[i] + preSum[i]

        # 使用map记录次数，可用于解答数量统计问题；子数组长度统计最值问题；
        seen = set()
        for i in range(2, len(preSum)):
            # i -2 处的前缀和可以加到可选择选项中
            modVal = preSum[i - 2] % k
            seen.add(modVal)
            # 找到前缀和的余数恰好等于当前余数的索引位置，最终结果区间两个余数相等的索引之间
            if preSum[i] % k in seen:
                return True
        return False

    # 参考文章： https://leetcode-cn.com/problems/continuous-subarray-sum/solution/gong-shui-san-xie-tuo-zhan-wei-qiu-fang-1juse/
    def checkSubarraySum2(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        d = defaultdict(int)  # 记录余数出现的索引位置
        remainder = 0  # 记录余数
        for i, c in enumerate(nums):
            remainder = (remainder + nums[i]) % k
            if remainder in d.keys():
                preIndex = d.get(remainder)
                if i - preIndex >= 2:
                    return True
            else:
                # 同余数值，只记录最左侧索引，确保长度最大
                d[remainder] = i
        return False

    # 超时
    def checkSubarraySum3(self, nums: List[int], k: int) -> bool:
        pre = [0]
        for i, c in enumerate(nums):
            pre.append(c + pre[i])

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if j - i < 2:
                    continue
                cur = pre[j] - pre[i]
                if cur == 0:
                    return True
                if cur % k == 0:
                    return True
        return False


# 974.和可被 K 整除的子数组
class Solution24:
    # 参考 523.连续子数组和； 本题目统计数量
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        d[0] = 1  # 表示前缀和恰好为k倍数的情况也满足题目要求

        ans = 0
        remainder = 0
        for i in range(n):
            remainder = (remainder + nums[i]) % k
            if remainder in d.keys():
                ans += d.get(remainder)
            d[remainder] += 1

        return ans

    def subarraysDivByK2(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in nums:
            total += elem
            modulus = total % k
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans

    def subarraysDivByK3(self, nums: List[int], k: int) -> int:
        record = {0: 1}
        total = 0
        for elem in nums:
            total += elem
            modulus = total % k
            record[modulus] = record.get(modulus, 0) + 1

        ans = 0
        # 排列组合方法：计算同余数的情况
        for x, cx in record.items():
            ans += cx * (cx - 1) // 2
        return ans


# 1201. 丑数 III
class Solution25:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        cnt = 0
        for i in range(2 * 10 ** 9):
            if i % a == 0 or i % b == 0 or i % c == 0:
                cnt += 1
            if cnt == n:
                return i
        return -1

    def nthUglyNumber3(self, n: int, a: int, b: int, c: int) -> int:
        lab, lbc, lac, labc = lcm(a, b), lcm(b, c), lcm(a, c), lcm(a, b, c)

        def countugly(x):
            return x // a + x // b + x // c - x // lab - x // lbc - x // lac + x // labc

        l, r = 1, min(min(a, b, c) * n, 2 * pow(10, 9))
        while l < r:
            m = (l + r) // 2
            if countugly(m) < n:
                l = m + 1
            else:
                r = m
        return l

    def nthUglyNumber4(self, n: int, a: int, b: int, c: int) -> int:
        lab, lbc, lac, labc = lcm(a, b), lcm(b, c), lcm(a, c), lcm(a, b, c)

        def countugly(x):
            return x // a + x // b + x // c - x // lab - x // lbc - x // lac + x // labc

        l, r = n // countugly(labc) * labc, (n // countugly(labc) + 1) * labc
        while l < r:
            m = (l + r) // 2
            if countugly(m) < n:
                l = m + 1
            else:
                r = m
        return l

    # 丑数II的思路 错误
    def nthUglyNumber2(self, n: int, a: int, b: int, c: int) -> int:
        array = [a, b, c]
        seen = set(array)
        while n > 0:
            minVal = heappop(array)
            n -= 1
            if minVal * a not in seen:
                heappush(array, minVal * a)
            if minVal * b not in seen:
                heappush(array, minVal * b)
            if minVal * c not in seen:
                heappush(array, minVal * c)
        return array[-1]

