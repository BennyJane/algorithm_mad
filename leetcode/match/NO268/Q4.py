import math
from functools import lru_cache


# 5933. k 镜像数字的和
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        ans = 0
        count = 0
        length = 1
        while count < n:
            temp = self.find(length, k)
            for num in temp:
                ans += int(num)
                count += 1
                if count >= n:
                    break
            length += 1

        return ans

    # 找到k 进制下前n个回文组合
    def find(self, length: int, k):
        nums = [str(i) for i in range(k)]
        if length == 1:
            return nums[1:]
        half = 1
        if length % 2 == 0:
            half = length // 2
        else:
            half = length // 2 + 1
        res = []

        # 检测对应10进制是否为回文

        def check(target: str):
            _len = len(target)
            ori = int(target, k)
            oriStr = str(int(ori))
            if oriStr == oriStr[::-1]:
                return int(ori)
            return None

        # 找到所有回文组合
        @lru_cache(None)
        def dfs(index: int, s):
            if index >= half:
                if length & 1:
                    pre = s[:-1]
                    temp = pre + s[-1] + pre[::-1]
                else:
                    temp = s + s[::-1]
                oriNum = check(temp)
                if oriNum is not None:
                    res.append(oriNum)
                return
            if index == 0:
                for c in nums[1:]:
                    dfs(index + 1, s + c)
            else:
                for c in nums:
                    dfs(index + 1, s + c)

        dfs(0, "")
        return res


class Solution1:
    def kMirror(self, k: int, n: int) -> int:
        def nxt_rev(cur):   # 10进制中：符合回文特征的下一个值
            s = str(cur)
            # 先分奇偶数讨论
            if len(s) % 2:
                l = r = len(s) // 2
            else:
                r = len(s) // 2
                l = r - 1
            while l >= 0 and s[l] == '9':
                l -= 1
                r += 1
            if l == -1:
                return 10 ** len(s) + 1
            elif l == r:
                return int(s[:l] + str((int(s[l]) + 1)) + s[r + 1:])
            return int(s[:l] + str((int(s[l]) + 1)) + '0' * (r - 1 - l) + str((int(s[r]) + 1)) + s[r + 1:])

        # 十进制转换为base进制
        def convert_to_base(num, base):
            ans = []
            while num:  # 连续取余数，直到为0
                ans.append(str(num % base))
                num //= base
            return "".join(ans[::-1])   # 余数反向重排，得到k进制数值

        def is_rev(s):  # 判断是否为回文
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        ans = 1
        cur = 1
        n -= 1
        while n:
            cur = nxt_rev(cur)
            if is_rev(convert_to_base(cur, k)):
                ans += cur
                n -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # sol.kMirror(3, 7)
    # sol.kMirror(7, 17)
    print(int("21212", 3))
