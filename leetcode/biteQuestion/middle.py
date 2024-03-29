from typing import List


class Solution1:
    # 29. 两数相除
    # https://leetcode-cn.com/problems/divide-two-integers/
    """
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，
    要求不使用乘法、除法和 mod 运算符。
    """

    # TODO 允许使用加法
    def divide(self, dividend: int, divisor: int) -> int:
        def divide(self, dividend: int, divisor: int) -> int:
            INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

            # 考虑被除数为最小值的情况
            if dividend == INT_MIN:
                if divisor == 1:
                    return INT_MIN
                if divisor == -1:
                    return INT_MAX

            # 考虑除数为最小值的情况
            if divisor == INT_MIN:
                return 1 if dividend == INT_MIN else 0
            # 考虑被除数为 0 的情况
            if dividend == 0:
                return 0

            # 一般情况，使用二分查找
            # 将所有的正数取相反数，这样就只需要考虑一种情况
            rev = False
            if dividend > 0:
                dividend = -dividend
                rev = not rev
            if divisor > 0:
                divisor = -divisor
                rev = not rev

            # 快速乘
            def quickAdd(y: int, z: int, x: int) -> bool:
                # x 和 y 是负数，z 是正数
                # 需要判断 z * y >= x 是否成立
                result, add = 0, y
                while z > 0:
                    if (z & 1) == 1:
                        # 需要保证 result + add >= x
                        if result < x - add:
                            return False
                        result += add
                    if z != 1:
                        # 需要保证 add + add >= x
                        if add < x - add:
                            return False
                        add += add
                    # 不能使用除法
                    z >>= 1
                return True

            left, right, ans = 1, INT_MAX, 0
            while left <= right:
                # 注意溢出，并且不能使用除法
                mid = left + ((right - left) >> 1)
                check = quickAdd(divisor, mid, dividend)
                if check:
                    ans = mid
                    # 注意溢出
                    if mid == INT_MAX:
                        break
                    left = mid + 1
                else:
                    right = mid - 1

            return -ans if rev else ans


# 89. 格雷编码
class Solution2:
    # 对称生成
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            size = len(ans)
            for j in range(size - 1, -1, -1):
                ans.append(ans[j] | (1 << (i - 1)))
        return ans

    # 公式法： 第n个格雷码 G(n) = n xor (n>>1)
    def grayCode2(self, n: int) -> List[int]:
        ans = [0] * (1 << n)
        for i in range(1 << n):
            ans[i] = (i >> 1) ^ i
        return ans
